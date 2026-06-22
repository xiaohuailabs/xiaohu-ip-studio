#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""xiaohu-ip-studio CLI:init(填 key) / doctor(自检)。纯标准库。"""
from __future__ import annotations
import getpass, os, pathlib, sys

CONFIG_DIR = pathlib.Path(os.environ.get("XDG_CONFIG_HOME", str(pathlib.Path.home() / ".config"))) / "xiaohu-ip-studio"
CONFIG_PATH = CONFIG_DIR / "config.yaml"
SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent


def cmd_init():
    print("=== xiaohu-ip-studio 配置生图 ===")
    print(f"配置将写到: {CONFIG_PATH}\n支持任何 OpenAI 兼容图像端点;key 只存本地、永不上传。\n")
    base = input("图像 API base_url [https://api.openai.com/v1]: ").strip() or "https://api.openai.com/v1"
    model = input("图像模型 model [gpt-image-2]: ").strip() or "gpt-image-2"
    key = getpass.getpass("API key (输入时不回显): ").strip()
    if not key:
        print("[中止] 没输入 key。"); sys.exit(2)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(
        f'base_url: "{base}"\nmodel: "{model}"\napi_key: "{key}"\nimage_size: "1024"\n',
        encoding="utf-8",
    )
    os.chmod(CONFIG_PATH, 0o600)
    print(f"\n✅ 已写入 {CONFIG_PATH} (mode 600)\n  自检: python3 scripts/illo.py doctor")


def cmd_doctor():
    ok = True
    print("=== doctor 自检 ===")
    print(f"[*] python: {sys.version.split()[0]}")
    if CONFIG_PATH.exists():
        txt = CONFIG_PATH.read_text(encoding="utf-8")
        has_key = ("api_key" in txt) and ('api_key: "<' not in txt) and ('api_key: ""' not in txt)
        print(f"[{'OK' if has_key else '!!'}] config: {CONFIG_PATH} {'(key 已填)' if has_key else '(缺 key → 跑 init)'}")
        ok = ok and has_key
    else:
        print(f"[!!] config 不存在: {CONFIG_PATH}  → 跑 init")
        ok = False
    # 施工5(2026-06-15):报 resolved backend(配图会走哪条后端)
    if CONFIG_PATH.exists():
        be = None
        for line in CONFIG_PATH.read_text(encoding="utf-8").splitlines():
            ls = line.strip()
            if ls.startswith("backend:"):
                be = ls.split(":", 1)[1].split("#")[0].strip()
            elif ls.startswith("base_url:") and not be:
                bu = ls.split(":", 1)[1].split("#")[0].strip()
                be = "apimart-task" if "apimart" in bu else "openai-sync"
        if be:
            print(f"[*] resolved backend: {be}")
    chars = SKILL_DIR / "characters"
    food = SKILL_DIR / "food-mascots"
    char_dirs = [d for d in chars.iterdir() if d.is_dir()] if chars.exists() else []
    food_dirs = [d for d in food.iterdir() if d.is_dir()] if food.exists() else []
    all_dirs = char_dirs + food_dirs
    n = len(all_dirs)
    print(f"[{'OK' if n > 0 else '!!'}] 角色库: {n} 个角色(手绘线稿 {len(char_dirs)} + 谐音梗 meme {len(food_dirs)})")
    # 施工5:扫每个角色锚点图缺失(开源后别人少了图能一眼看到)
    if all_dirs:
        missing = [d.name for d in sorted(all_dirs, key=lambda d: d.name)
                   if not ((d / "refs").exists() and list((d / "refs").glob("*.png")))]
        if missing:
            print(f"[!!] 锚点图缺失 ({len(missing)}): {', '.join(missing)}")
            ok = False
        else:
            print(f"[OK] 锚点图: {n} 个角色全部齐全")
    gen = SKILL_DIR / "scripts" / "generate.py"
    print(f"[{'OK' if gen.exists() else '!!'}] 生图脚本: {'在' if gen.exists() else '缺'}")
    print("=== " + ("✅ 就绪,可以配图了" if ok else "❌ 有问题,见上") + " ===")
    sys.exit(0 if ok else 1)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "doctor"
    if cmd == "init":
        cmd_init()
    elif cmd == "doctor":
        cmd_doctor()
    else:
        print("用法: python3 scripts/illo.py [init|doctor]")
        sys.exit(2)


if __name__ == "__main__":
    main()
