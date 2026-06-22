#!/usr/bin/env bash
# 小互 IP Studio · 一键安装 / 自检
# 用法:在仓库目录里跑 `bash install.sh`
set -euo pipefail
cd "$(dirname "$0")"

echo "▶ 小互 IP Studio 安装"
echo

# 1. 检查 python3(唯一依赖,纯标准库)
if ! command -v python3 >/dev/null 2>&1; then
  echo "✗ 没找到 python3——请先安装 Python 3 再回来跑。"
  exit 1
fi
echo "✓ python3: $(python3 --version 2>&1)"
echo

# 2. 引导填图像 API key(不内置任何密钥,填你自己的)
echo "▶ 第一步:配置图像 API key"
python3 scripts/illo.py init
echo

# 3. 自检:key / 依赖 / 角色库 / 锚点
echo "▶ 第二步:自检"
python3 scripts/illo.py doctor
echo

echo "✓ 装好了。跟你的 agent 说一句「给这篇文章配图,用替替」就能开始。"
echo "  没 API 也能玩:让它只出提示词、不生图,你贴到 ChatGPT / Gemini 网页版手动生。"
