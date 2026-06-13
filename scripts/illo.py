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
    model = input("图像模型 model [gpt-image-1]: ").strip() or "gpt-image-1"
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
    chars = SKILL_DIR / "characters"
    n = len([d for d in chars.iterdir() if d.is_dir()]) if chars.exists() else 0
    print(f"[{'OK' if n > 0 else '!!'}] 角色库: {n} 个角色")
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
