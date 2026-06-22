#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""xiaohu-ip-studio 生图脚本(开源版)

走 OpenAI 兼容图像端点,自带两种后端(config.yaml 的 backend 字段,缺省自动判断):
  - apimart-task : 异步任务模式(提交 /images/generations → 拿 task_id → 轮询 /tasks/{id} → 下载),
                   适配 apimart 等网关的 GPT-image-2;图生图用 image_urls(base64 data URI)。
  - openai-sync  : 标准同步(/images/generations 直返 b64/url;图生图走 /images/edits multipart)。

读 ~/.config/xiaohu-ip-studio/config.yaml(用 illo.py init 写入,不内置任何密钥)。

  文生图:       python3 generate.py --prompt-file p.md --out out.png
  图生图(锁角色): python3 generate.py --prompt-file p.md --reference <锚点图> --out out.png

prompt 文件 = YAML 头(aspect_ratio 必填) + 正文 prompt。纯标准库,无第三方依赖。
"""
from __future__ import annotations
import argparse, base64, json, os, pathlib, sys, time, urllib.error, urllib.request, uuid

CONFIG_PATH = pathlib.Path(os.environ.get("XDG_CONFIG_HOME", str(pathlib.Path.home() / ".config"))) / "xiaohu-ip-studio" / "config.yaml"

TERMINAL_OK = ("completed", "success", "succeeded", "done", "finished")
TERMINAL_FAIL = ("failed", "error", "cancelled", "canceled", "timeout")


def eprint(*a):
    print(*a, file=sys.stderr)


def parse_simple_yaml(text: str) -> dict:
    """极简扁平 yaml:key: value,忽略注释/空行。够读 config。"""
    cfg = {}
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or ":" not in s:
            continue
        k, v = s.split(":", 1)
        v = v.split("#", 1)[0].strip().strip('"').strip("'")
        cfg[k.strip()] = v
    return cfg


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        eprint(f"[错误] 没找到配置: {CONFIG_PATH}\n  先运行: python3 scripts/illo.py init")
        sys.exit(2)
    cfg = parse_simple_yaml(CONFIG_PATH.read_text(encoding="utf-8"))
    if not cfg.get("api_key") or cfg["api_key"].startswith("<"):
        eprint("[错误] config 里没有有效 api_key,跑 `python3 scripts/illo.py init`")
        sys.exit(2)
    return cfg


def read_prompt_file(p: str):
    text = pathlib.Path(p).read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            for line in text[3:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
            body = text[end + 3:].strip()
    if "aspect_ratio" not in meta:
        eprint("[错误] prompt 文件缺 YAML 头的 aspect_ratio(如 aspect_ratio: \"4:3\")")
        sys.exit(2)
    return meta, body


def aspect_to_size(aspect: str) -> str:
    """openai-sync 用:映射到 gpt-image 合法尺寸档(横/竖/方)。"""
    try:
        w, h = aspect.split(":")
        w, h = int(w), int(h)
    except Exception:
        return "1024x1024"
    if w > h:
        return "1536x1024"
    if h > w:
        return "1024x1536"
    return "1024x1024"


def _guess_mime(path: pathlib.Path) -> str:
    s = path.suffix.lower()
    return {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".webp": "image/webp", ".gif": "image/gif"}.get(s, "image/png")


def _data_uri(path: pathlib.Path) -> str:
    return f"data:{_guess_mime(path)};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def _post_json(url, headers, payload, timeout=300) -> dict:
    body = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={**headers, "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def _post_multipart(url, headers, fields, files, timeout=300) -> dict:
    boundary = "----xipstudio" + uuid.uuid4().hex
    parts = []
    for k, v in fields.items():
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode())
    for k, (fn, data, ct) in files.items():
        parts.append(
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"; filename=\"{fn}\"\r\nContent-Type: {ct}\r\n\r\n".encode()
            + data + b"\r\n"
        )
    parts.append(f"--{boundary}--\r\n".encode())
    body = b"".join(parts)
    req = urllib.request.Request(url, data=body, method="POST",
                                 headers={**headers, "Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def _download(url, timeout=120) -> bytes:
    req = urllib.request.Request(url, method="GET", headers={"Accept": "*/*", "User-Agent": "curl/8.4.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


# ---------- apimart 异步 task 模式 ----------

def _extract_task_id(submit_json: dict):
    if not isinstance(submit_json, dict):
        return None
    data = submit_json.get("data")
    if isinstance(data, list) and data and isinstance(data[0], dict):
        tid = data[0].get("task_id") or data[0].get("id")
        if isinstance(tid, str) and tid:
            return tid
    if isinstance(data, dict):
        tid = data.get("task_id") or data.get("id")
        if isinstance(tid, str) and tid:
            return tid
    tid = submit_json.get("task_id") or submit_json.get("id")
    return tid if isinstance(tid, str) and tid else None


def _poll_task(base_url, api_key, task_id, max_wait_s=300, interval=3.0):
    url = base_url.rstrip("/") + f"/tasks/{task_id}"
    headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json", "User-Agent": "curl/8.4.0"}
    deadline = time.time() + max(int(max_wait_s), 30)
    last = None
    while time.time() < deadline:
        try:
            req = urllib.request.Request(url, method="GET", headers=headers)
            with urllib.request.urlopen(req, timeout=min(60, max_wait_s)) as resp:
                j = json.loads(resp.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            eprint(f"[轮询] HTTP {getattr(e,'code',None)}: {(e.read() if hasattr(e,'read') else b'').decode('utf-8','replace')[:200]}")
            time.sleep(interval); continue
        except Exception as e:
            eprint(f"[轮询] 异常: {e}"); time.sleep(interval); continue
        if not isinstance(j, dict):
            time.sleep(interval); continue
        d = j.get("data") if isinstance(j.get("data"), dict) else j
        s = str(d.get("status") or "").lower()
        if s != last:
            eprint(f"[轮询] task={task_id} status={s} progress={d.get('progress')}"); last = s
        if s in TERMINAL_OK:
            return {"ok": True, "result": d.get("result") if isinstance(d.get("result"), dict) else d}
        if s in TERMINAL_FAIL:
            return {"ok": False, "error": d.get("error") or d.get("message") or "task failed"}
        time.sleep(interval)
    return {"ok": False, "error": f"轮询超过 {max_wait_s}s 仍未完成"}


def _images_from_result(result: dict) -> list:
    """apimart 终态 result.images[*].url(url 可能是 str 或 list[str])→ 下载 bytes。"""
    if not isinstance(result, dict):
        return []
    images = result.get("images")
    if not isinstance(images, list):
        # 有的网关把 url 放在 result.data[].url
        data = result.get("data")
        images = data if isinstance(data, list) else []
    out = []
    for item in images:
        if not isinstance(item, dict):
            continue
        if item.get("b64_json"):
            out.append(base64.b64decode(item["b64_json"])); continue
        uf = item.get("url") or item.get("urls")
        urls = [uf] if isinstance(uf, str) else ([u for u in uf if isinstance(u, str)] if isinstance(uf, list) else [])
        for u in urls:
            try:
                out.append(_download(u))
            except Exception as e:
                eprint(f"[下载] 失败 url={u} err={e}")
    return out


def _image_dims(data: bytes):
    """纯标准库读 PNG / JPEG 宽高,读不出返回 None。(施工5,2026-06-15)"""
    import struct
    if len(data) < 24:
        return None
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        try:
            w, h = struct.unpack(">II", data[16:24]); return (w, h)
        except Exception:
            return None
    if data[:2] == b"\xff\xd8":
        i, n = 2, len(data)
        while i < n - 9:
            if data[i] != 0xFF:
                i += 1; continue
            m = data[i + 1]
            if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                try:
                    h, w = struct.unpack(">HH", data[i + 5:i + 9]); return (w, h)
                except Exception:
                    return None
            i += 2 + ((data[i + 2] << 8) + data[i + 3])
        return None
    return None


def sniff_ext(data: bytes) -> str:
    """按 magic bytes 判真实图片类型,纠正后缀错配。(施工5)"""
    if data[:8] == b"\x89PNG\r\n\x1a\n": return "png"
    if data[:2] == b"\xff\xd8": return "jpg"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP": return "webp"
    if data[:6] in (b"GIF87a", b"GIF89a"): return "gif"
    return ""


def _save_bytes(img: bytes, out: str) -> str:
    p = pathlib.Path(out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(img)
    return str(p.resolve())


def _save_sync(resp: dict, out: str) -> str:
    """openai-sync:从 data[0].b64_json / url 取图。"""
    items = resp.get("data") or []
    if not items:
        eprint("[错误] 返回里没有 data/图片:\n" + json.dumps(resp)[:600]); sys.exit(1)
    d = items[0]
    if d.get("b64_json"):
        img = base64.b64decode(d["b64_json"])
    elif d.get("url"):
        img = _download(d["url"])
    else:
        eprint("[错误] data 里既无 b64_json 也无 url:\n" + json.dumps(d)[:600]); sys.exit(1)
    return _save_bytes(img, out)


def run_apimart(base_url, model, api_key, body, aspect, image_size, refs, out, timeout, task_retries):
    headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json", "User-Agent": "curl/8.4.0"}
    payload = {"model": model, "prompt": body, "n": 1, "size": aspect}
    if image_size:
        payload["resolution"] = image_size.lower()
    if refs:
        payload["image_urls"] = [_data_uri(pathlib.Path(r)) for r in refs[:16]]
    last_err = None
    for attempt in range(1, task_retries + 1):
        try:
            submit = _post_json(f"{base_url}/images/generations", headers, payload, timeout=timeout)
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:300]}"
            eprint(f"[提交 {attempt}/{task_retries}] {last_err}"); time.sleep(2 ** (attempt - 1)); continue
        except Exception as e:
            last_err = str(e); eprint(f"[提交 {attempt}/{task_retries}] {last_err}"); time.sleep(2 ** (attempt - 1)); continue
        task_id = _extract_task_id(submit)
        if not task_id:
            # 也许网关同步直返了图
            try:
                return _save_sync(submit, out)
            except SystemExit:
                last_err = "提交成功但既无 task_id 也无同步图: " + json.dumps(submit)[:300]
                eprint(f"[提交 {attempt}/{task_retries}] {last_err}"); time.sleep(2 ** (attempt - 1)); continue
        eprint(f"[提交] task_id={task_id},开始轮询...")
        poll = _poll_task(base_url, api_key, task_id, max_wait_s=timeout)
        if poll.get("ok"):
            imgs = _images_from_result(poll.get("result") or {})
            if imgs:
                return _save_bytes(imgs[0], out)
            last_err = "任务完成但 result 里没解析到图片 url"
        else:
            last_err = f"任务失败/超时: {poll.get('error')}"
        eprint(f"[提交 {attempt}/{task_retries}] {last_err}"); time.sleep(2 ** (attempt - 1))
    eprint(f"[失败] {task_retries} 次都没成: {last_err}"); sys.exit(1)


def run_sync(base_url, model, api_key, body, aspect, refs, out):
    headers = {"Authorization": f"Bearer {api_key}"}
    size = aspect_to_size(aspect)
    if len(refs) > 1:
        eprint(
            f"[警告] openai-sync 后端的 /images/edits 只吃 1 张参考图,已用第 1 张"
            f"({pathlib.Path(refs[0]).name}),其余 {len(refs) - 1} 张(含双图法的演技锚)被忽略。\n"
            f"  要多图锁角色+表情,把 config.yaml 的 backend 设为 apimart-task(用 image_urls 支持多图)。"
        )
    last_err = None
    for attempt in (1, 2):
        try:
            if refs:
                ref = refs[0]
                files = {"image": (pathlib.Path(ref).name, pathlib.Path(ref).read_bytes(), _guess_mime(pathlib.Path(ref)))}
                fields = {"model": model, "prompt": body, "size": size, "n": "1"}
                resp = _post_multipart(f"{base_url}/images/edits", headers, fields, files)
            else:
                resp = _post_json(f"{base_url}/images/generations", headers, {"model": model, "prompt": body, "size": size, "n": 1})
            return _save_sync(resp, out)
        except urllib.error.HTTPError as e:
            last_err = f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:300]}"
        except Exception as e:
            last_err = str(e)
        eprint(f"[重试 {attempt}/2] {last_err}")
    eprint(f"[失败] 两次都没成: {last_err}"); sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--reference", nargs="*", default=[])
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=None)
    args = ap.parse_args()

    cfg = load_config()
    base_url = cfg.get("base_url", "https://api.openai.com/v1").rstrip("/")
    model = args.model or cfg.get("model", "gpt-image-2")
    image_size = cfg.get("image_size")
    timeout = int(cfg.get("timeout_s", 300))
    task_retries = int(cfg.get("task_retries", 3))
    backend = cfg.get("backend") or ("apimart-task" if "apimart" in base_url else "openai-sync")

    meta, body = read_prompt_file(args.prompt_file)
    aspect = meta.get("aspect_ratio", "1:1")
    eprint(f"[生图] backend={backend} model={model} aspect={aspect} reference={len(args.reference)} 张")

    if backend == "apimart-task":
        out = run_apimart(base_url, model, cfg["api_key"], body, aspect, image_size, args.reference, args.out, timeout, task_retries)
    else:
        out = run_sync(base_url, model, cfg["api_key"], body, aspect, args.reference, args.out)
    # 施工5(2026-06-15):测真实尺寸 + 按 magic bytes 纠正后缀。上游看到 width/height,发现 GPT 返回方图/尺寸跑偏可据此重生。
    result = {"path": out, "backend": backend, "model": model, "aspect": aspect}
    try:
        raw = pathlib.Path(out).read_bytes()
        ext = sniff_ext(raw)
        cur = pathlib.Path(out).suffix.lower().lstrip(".")
        if ext and cur != ext and not (ext == "jpg" and cur == "jpeg"):
            newp = str(pathlib.Path(out).with_suffix("." + ext))
            pathlib.Path(out).rename(newp); out = newp; result["path"] = out
        wh = _image_dims(raw)
        if wh:
            result["width"], result["height"] = wh
    except Exception:
        pass
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
