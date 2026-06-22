# 生图后端

本技能自带 `scripts/generate.py`,走**任何 OpenAI 兼容的图像生成端点**——**不内置任何密钥,你填自己的**。

## 一次性配置

```bash
python3 scripts/illo.py init     # 引导填 base_url / model / key
python3 scripts/illo.py doctor   # 自检:key / 角色库 / 脚本是否就绪
```

配置写到 `~/.config/xiaohu-ip-studio/config.yaml`(mode 600,只存本地):

| 字段 | 说明 |
|---|---|
| `base_url` | 图像 API 端点。OpenAI 官方 `https://api.openai.com/v1`,或任何兼容网关 |
| `model` | 图像模型名(默认 `gpt-image-2`——本技能的文字铁律按它的中文 ~99% 准确率写;也可填任何兼容模型,但换更弱的模型要回退 prompt-template 的「文字层方案」兜底) |
| `api_key` | 你自己的 key,永不上传 |

## 调用

```bash
# 文生图
python3 scripts/generate.py --prompt-file p.md --out out.png

# 图生图(锁角色,传角色锚点图,走 /images/edits)
python3 scripts/generate.py --prompt-file p.md \
  --reference characters/<名>/refs/<名>-锚点.png --out out.png
```

prompt 文件格式(YAML 头 `aspect_ratio` 必填 + 正文):

```
---
aspect_ratio: "4:3"
---
正文 prompt……
```

## 说明

- 文生图走 `/images/generations`,图生图走 `/images/edits`(gpt-image 系列)。
- `aspect_ratio` 自动映射到合法尺寸档:横 `1536x1024` / 竖 `1024x1536` / 方 `1024x1024`。
- 失败最多重试 2 次,不在挂掉的 API 上死磕。
- 单文件、纯标准库、零第三方依赖。若你的网关是 task 异步模式或字段不同,直接改 `generate.py` 适配即可(代码很短)。
