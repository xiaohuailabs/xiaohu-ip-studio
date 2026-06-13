#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""xiaohu-ip-studio 生图脚本(开源版)

走任何 OpenAI 兼容的图像生成端点。不内置任何密钥——读
~/.config/xiaohu-ip-studio/config.yaml 里你自己填的 key(用 illo.py init 写入)。

  文生图:     python3 generate.py --prompt-file p.md --out out.png
  图生图(锁角色): python3 generate.py --prompt-file p.md --reference <锚点图> --out out.png

prompt 文件 = YAML 头(aspect_ratio 必填) + 正文 prompt。纯标准库,无第三方依赖。
"""
from __future__ import annotations
import argparse, base64, json, os, pathlib, sys, urllib.error, urllib.request, uuid

CONFIG_PATH = pathlib.Path(os.environ.get("XDG_CONFIG_HOME", str(pathlib.Path.home() / ".config"))) / "xiaohu-ip-studio" / "config.yaml"


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
    """映射到 gpt-image 合法尺寸档(横/竖/方)。"""
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


def _post_json(url, headers, payload, timeout=300):
    body = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, method="POST", headers={**headers, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def _post_multipart(url, headers, fields, files, timeout=300):
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


def save_image(resp: dict, out: str) -> str:
    items = resp.get("data") or []
    if not items:
        eprint("[错误] 返回里没有 data/图片:\n" + json.dumps(resp)[:600]); sys.exit(1)
    d = items[0]
    if d.get("b64_json"):
        img = base64.b64decode(d["b64_json"])
    elif d.get("url"):
        with urllib.request.urlopen(d["url"], timeout=120) as r:
            img = r.read()
    else:
        eprint("[错误] data 里既无 b64_json 也无 url:\n" + json.dumps(d)[:600]); sys.exit(1)
    p = pathlib.Path(out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(img)
    return str(p.resolve())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--reference", nargs="*", default=[])
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default=None)
    args = ap.parse_args()

    cfg = load_config()
    base_url = cfg.get("base_url", "https://api.openai.com/v1").rstrip("/")
    model = args.model or cfg.get("model", "gpt-image-1")
    headers = {"Authorization": f"Bearer {cfg['api_key']}"}

    meta, body = read_prompt_file(args.prompt_file)
    size = aspect_to_size(meta.get("aspect_ratio", "1:1"))
    eprint(f"[生图] model={model} size={size} reference={len(args.reference)} 张")

    last_err = None
    for attempt in (1, 2):  # 失败最多重试 2 次
        try:
            if args.reference:
                ref = args.reference[0]
                files = {"image": (pathlib.Path(ref).name, pathlib.Path(ref).read_bytes(), "image/png")}
                fields = {"model": model, "prompt": body, "size": size, "n": "1"}
                resp = _post_multipart(f"{base_url}/images/edits", headers, fields, files)
            else:
                payload = {"model": model, "prompt": body, "size": size, "n": 1}
                resp = _post_json(f"{base_url}/images/generations", headers, payload)
            out = save_image(resp, args.out)
            print(json.dumps({"path": out, "model": model, "size": size}, ensure_ascii=False))
            return
        except urllib.error.HTTPError as e:  # type: ignore
            last_err = f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:300]}"
        except Exception as e:
            last_err = str(e)
        eprint(f"[重试 {attempt}/2] {last_err}")
    eprint(f"[失败] 两次都没成: {last_err}")
    sys.exit(1)


if __name__ == "__main__":
    main()
