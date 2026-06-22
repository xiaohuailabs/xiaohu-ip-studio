# 展示模式:角色戏 vs 极简场景

> 2026-06-16 加。角色有复杂度差异,展示方式不该一刀切。**复杂角色(小互)**适合"占 C 位演表情";**符号角色(其余 18 个)**塞进那套反而像表情包——它们天生适合"人极小物极大 + 留白"或"符号角色 + 真实物件"的极简场景。本档定义两种模式 + 按角色自动路由。
>
> **血统**:模式 B 的两种子风格,**方法**借自 [orange-line](https://github.com/orange2ai/orange-line-illustration)(人小物大 / 单点色 / 留白)和 [小黑 2.0 scenes](https://github.com/helloianneo/ian-xiaohei-scenes)(真实物件现场)。⛔ **学的是方法,演员是本库自己的角色**——不照抄它们的"小橙 / 小黑"外观,不复刻它们的具体构图。这样既避开它们的商用授权线(orange-line 闭源商用需授权),又保住本库"自己 19 角色"的识别护城河。

## 两种模式

| | **模式 A · 角色戏** | **模式 B · 极简场景** |
|---|---|---|
| 谁主演 | 角色占画面大、演表情 / 处境 | 物件 / 场景是主体,角色是其中的小符号 |
| 角色占比 | ~40-60% | ~1/12–1/6,物极大顶天 |
| 渲染 | 彩色精致(皮肤 A–K) | 极简:纯黑线 + 单点色 / 黑角色 + 真实物件 |
| 情绪从哪来 | 角色脸 + 处境 | 尺度对比 / 物理重量(**不靠脸**) |
| 默认配谁 | **小互**(唯一复杂角色) | **阿冲等 18 个符号角色** |
| 适合内容 | 产品 / 封面 / 强 IP 感 | 处境 / 情绪 / 金句 / 方法拆解 |

## ⛔ 路由规则(选完角色自动定,不每次问)

- 选了**符号角色**(阿冲 / 团团 / 棱角 / 淡淡 / 疯崽 / 缩缩 / 牛马…)→ 默认**模式 B**。它们本来就是符号级,缩小天然不糊;塞进模式 A 的"占 C 位演表情"会变表情包(2026-06-16 阿冲 A/B 实测坐实)。
- 选了**小互**→ 默认**模式 A**;要"人小物大"时下放模式 B,传极简形态锚点 `refs/xiaohu-极简形态.png`(完整版细节多、缩小会糊)。
- 用户显式覆盖优先(说"走极简场景 / 走角色戏",或 `--mode A/B`)。
- 解释图(三轨之二)**不分 A/B 模式**:无论谁主演,解释图照走 `explanatory-diagrams.md`(角色小而有戏 ~15-18% 嵌入当行动者 + 同墨同线)。模式只切**情绪锚点图**那一轨的演法(模式 A 演处境占位 / 模式 B 人小物大留白)。
- **符号角色可进解释图**(2026-06-19 实测:疯崽钻框 / 团团爬阶 / 方方守分隔线都成立):它们本身简单,缩小嵌入比小互更服帖、更不抢戏。⛔ 但先过 explanatory-diagrams.md 的**选角双适配闸**——团块无肢角色(团团 / 木鱼)只能演被动 / 静态动作,锁定后遇到做不了的图按那里的**三档适配**改动作,不换角色。

## 模式 B 两种子风格

### B1 · orange-line 极简(人极小物极大 + 单点色 + 留白)

**方法借 orange-line。** 适合:处境 / 情绪 / 金句("被 X 淹 / 被 X 逼 / 渺小对抗巨物")。

- 纯黑细手绘线,微抖;**除一个单点色外,全图零填色**
- 纯白底,**≥55% 留白**
- **人极小(约画幅 1/12–1/6)、物极大顶天**;情绪从尺度对比出,不靠脸
- 单点色 = **该符号角色的招牌色**(阿冲黄 / 棱角红 / 淡淡灰…),全图只此一处
- 金句:**右下角灰色小字**,安静可读、不喧宾夺主
- ⛔ 角色要**露出招牌、别缩成纯剪影**(阿冲的闪电黄、棱角的怒眉三角要认得出)

**prompt 骨架(B1):**
```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article illustration in a MINIMALIST New Yorker line style.
PURE BLACK thin hand-drawn ink line ONLY, slight hand wobble, NO color fills anywhere EXCEPT one single accent. PURE WHITE background, LOTS of empty white space (≥55% empty). Witty, quiet, restrained. NOT colored, NOT 3D, NOT grainy, NOT a slide.
SCALE — the signature: an ENORMOUS {巨物} fills most of the frame and looms huge. {符号角色} is TINY at {脚下 / 角落}, about 1/12 of the frame, {贴人设的姿态} — and {角色招牌色} is the ONLY color in the whole image. The drama comes from the SIZE CONTRAST, not the face. Keep {角色} recognizable (露脸/露招牌, not a solid silhouette).
A couple of tiny black labels on the {巨物} only: {标签1} / {标签2}. One quiet GRAY small caption at the bottom-right corner: 「{金句}」.
⛔ Pure black line everywhere except {角色}'s single accent color. Keep huge white negative space. No title top-left. Color names/values are guidance only — do NOT render as text. Every Chinese character clean and correct.
```

### B2 · 小黑式真实物件现场(白底 + 黑角色 + 写实 3D 物件)

**方法借小黑 2.0 scenes。** 适合:产品演化 / 工作压力 / AI 时代状态。**用皮肤 G 渲染**(见 `style-dna.md` 皮肤 G,本就是"黑墨草图 + 写实 3D 物体")。

- 纯白背景,一个**真实物件小现场**
- 关键概念 = **照片级写实 3D 物体**(真手机 / 沙漏 / 夹子…),跟手绘符号角色**物理互动**(不是摆旁边)
- 符号角色承担核心动作,2-4 个中文短标签,少量点缀色(蓝 / 粉 / 黄 / 绿 / 红)
- 骨架直接套 `prompt-template.md` 轨道一 + `style-dna.md` 皮肤 G 的 STYLE 块

## 模式 B 的反 PPT 底线(跟主流程一致)

一图一核心、金句不喧宾夺主、中文零错字、**留白是主角不是边角料**。模式 B 失败信号:角色缩成看不出是谁的纯剪影 / 留白被填满 / 单点色变成多色 / 金句压过主物件。命中即重生。

## 验证记录

- 2026-06-16 阿冲「被未读消息淹」A/B 实测:模式 A(占 C 位演表情)= 吵、表情包感;模式 B1(消息山顶天 + 阿冲极小 + 单点黄 + 右下灰金句)= 高级、会心一笑。符号角色走 B 一眼更对,坐实路由规则。
