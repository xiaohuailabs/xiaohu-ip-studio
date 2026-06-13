# 小互 IP Studio · 开源中文配图技能

把「中文深度文配图方法论」+「可扩展 IP 角色库」打包的开源 [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills)。自带 **19 个手绘线稿风 IP 角色**,配图时按文章调性选一个出演。**方法论恒定,角色与画风是参数。**

> 脱胎于小黑 / 宝玉 / 卷卷 / illo 几个开源配图技能,学原理不抄外观。血统/致谢见 [CREDITS.md](CREDITS.md)。

## 这是什么

为中文深度文 / 方法拆解生成**由固定角色出演**的正文配图——不是通用插画、不是 PPT 信息图。把文章里一个关键判断 / 流程 / 状态,变成一张有记忆点、一眼怪但一秒懂的解释图。

## 角色库(19 个)

打开 `ip-library.html` 看全家福:

- **职场态 ×12**:小互(主角) / 棱角(杠精) / 团团(躺平) / 方方(KPI古板) / 泡泡(画饼) / 阿冲(内卷) / 小星(邀功) / 电量(能量条) / 续命(咖啡) / 丁零(催命) / 贴贴(健忘) / 双子(反应组)
- **当代情绪态 ×7**:淡淡(淡人) / 破防君(玻璃心) / 疯崽(发疯) / 牛马(打工人) / 缩缩(i人) / 木鱼(电子木鱼) / 替替(AI焦虑)

## 装

任何认 `SKILL.md`(Agent Skills 格式)的 agent 都能用(Claude Code / Codex / 等)——把本目录放进 agent 的 skills 目录即可。依赖只有 `python3`(纯标准库,零第三方)。

## 配置生图(一次)

**不内置任何密钥,填你自己的**:

```bash
python3 scripts/illo.py init     # 填图像 API base_url / model / key
python3 scripts/illo.py doctor   # 自检
```

支持任何 OpenAI 兼容图像端点,详见 [references/backends.md](references/backends.md)。

## 用

跟 agent 说「给这篇配图,用替替」之类,技能会走:选角色 → 消化正文逐节枚举 → 挑认知锚点 → 深层提炼 → 现编隐喻 → 生图 → 反 PPT 自检。

手动生单张:

```bash
python3 scripts/generate.py --prompt-file p.md \
  --reference characters/titi/refs/titi-锚点.png --out out.png
```

## 扩展

- **建自己的角色**:照 [references/character-spec.md](references/character-spec.md),在 `characters/<名>/` 建个目录就进库。
- **加画风**:见 [references/style-spec.md](references/style-spec.md)(但建议守住单一招牌风,辨识度来自统一)。

## 方法论(为什么配出来的图不一样)

核心在 `references/`:逐节枚举防漏配、双向第一性(防凑数 + 防漏配难懂机制)、深层提炼三问(真意/张力/灵魂话)+ 必现内容锁定、三轨分流(情绪锚点 / 解释图 / 四格漫画)、文体→hero、source-fit 选点复检、反 PPT 自检。

## License

MIT。角色形象与画风如需商用,请自行确认生成图的版权合规。
