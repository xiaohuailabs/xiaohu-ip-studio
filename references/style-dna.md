# 画风皮肤库(多风格可选)

> ✅ 定调 2026-05-31(v3)。**角色锁定(见 characters/<名>/character.md),画风做成可选皮肤**。每次生图按文章调性选一种,或用户 `--style` 指定。默认 3D 盲盒。

## 通用约定(所有皮肤共享)

- 画幅:比例按内容逐张判断、移动端偏竖(见 SKILL.md「2.5 定比例」+ prompt-template 方向词联动表)。皮肤与比例正交,任何皮肤都能出 16:9/9:16/4:3/3:4/1:1
- 招牌:**红框圆眼镜 + "小互"名牌**任何皮肤都在
- **⛔ 表情随内容情绪变化**(核心,见角色包 character.md 映射表)
- 中文气泡/便签标注,最多 5-8 处,短
- 一张图只讲一个核心动作/结构/隐喻

## ⛔ 视觉契约(一篇内六维必须统一——风格一致的根,2026-06-01 根治)

光锁"皮肤词"不够:背景/光影/景深没锁,情绪图和四格会飘成电影感场景、信息图却是白底,一篇就裂成两种风格(用户提点)。**一篇内所有图、所有轨道,这六维取同一组值**:

1. **背景**:白色 / 浅纯色棚拍底(clean white / light solid studio bg)。⛔ 不要沉浸式场景房间
2. **光影**:柔和均匀棚拍光(soft even studio light)。⛔ 不要戏剧性电影光 / 强逆光 / 霓虹
3. **景深**:背景清晰无虚化(no depth-of-field blur)。⛔ 不要电影级背景虚化
4. **精致度**:盲盒手办 icon 感(blind-box toy finish)。⛔ 不要电影级厚涂写实
5. **色调**:暖橙红为主(warm orange-red)
6. **角色**:小互锁定(见 characters/xiaohu/character.md)

判据:任意两张并排,背景/光影/精致度看不出区别 = 统一。一张飘了(场景/景深/电影光)就重生。具体注入靠 prompt-template 的「视觉契约句」。

> ⚠️ **皮肤 G(混合媒介)是例外**:它自带一套独立契约(白纸 + 黑墨草图 + 写实物体 + 主题配色),不走本节这套「盲盒 / 非写实 / 暖橙红」契约。一篇选了 G 就整篇走 G,见下方皮肤 G。

## 皮肤 A:3D 盲盒手办(默认,最吸睛)

```
3D rendered Pixar / blind-box designer-toy style, chibi proportions, big round expressive eyes, soft volumetric lighting, detailed texture (knit sweater, denim), warm palette orange-red dominant. NOT flat, NOT line art.
```
- 适合:产品发布、封面级吸睛、强 IP 感
- 锚点:传 examples 齐刘海 3D 图作 --reference

## 皮肤 B:黑白线稿(轻、反 PPT)

```
PURE BLACK AND WHITE line art ONLY, monochrome, hand-drawn black ink lines with slight wobble, NO color fills at all, pure white background, lots of empty white space. The ONLY allowed color is a small RED on the glasses frame and key labels — everything else strictly black and white. NOT colored, NOT painterly, NOT 3D, NOT vector.
```
- 适合:深度解读、不抢文字、留白呼吸
- ⛔ 传 3D 锚点锁角色,但 prompt 必须写"keep the character identity but IGNORE the reference colors, render PURE black and white"——否则会跟着彩色锚点漏色变成"线稿淡彩"(2026-05-31 踩坑)

## 皮肤 C:扁平矢量(干净现代)

```
flat minimalist vector illustration, bold clean even outlines, solid flat color blocks, modern IP look, white background, warm accents.
```
- 适合:教程、信息清晰、量产
- ⛔ 仍要传 3D 锚点锁角色,prompt 写"keep exact same character, only change to 扁平 style"(不传角色会漂移)

## 皮肤 D:编辑插画(纽约客风,高级有态度)

```
editorial magazine illustration like a New Yorker cover, limited flat color palette, textured grainy shapes, tasteful and stylized, smart and a bit minimal.
```
- 适合:观点文、深度评论、有态度的解读(最高级)
- 传双锚点(长相+演技)同 A

## 皮肤 E:水彩淡彩(温暖文艺,质感最好)

```
soft hand-painted watercolor illustration, visible paper texture and gentle brush washes, warm tones, storybook feel.
```
- 适合:人文向、深度解读、温暖叙事
- 传双锚点同 A

## 皮肤 F:马克笔手账(活泼梗感)

```
loose thick marker and crayon doodle, hand-drawn sketchbook journal vibe, casual playful rough lines.
```
- 适合:轻松话题、日常、梗图感
- 传双锚点同 A

## 皮肤 G:混合媒介(手绘草图 + 写实物体)⚠️ 特例皮肤,自带独立契约

> ⚠️ **本皮肤不走上面那套「盲盒手办 / 非写实 / 暖橙红」视觉契约**——它的灵魂就是照片级写实 3D 物体 + 按主题配色。一篇选了 G 就整篇走 G 自己的契约,不跟 A–F 混。来源:用户 Mixed-Media「Golden Aesthetics」spec(2026-06-05)。

```
Mixed-media infographic on clean bright white textured paper with generous negative space. BASE layer: minimalist black ink doodle sketches. KEY concepts rendered as PHOTOREALISTIC tangible 3D objects — studio lighting, tactile texture, realistic drop shadows — physically interacting with the flat sketch (pinning it down, casting shadows across the ink lines, taping corners, wrapping around sketched elements, or breaking through the paper). Main titles in large bold hand-drawn marker font; labels in small casual pen font. Cohesive themed color palette for the real objects ONLY (cool blue/metallic = tech, warm tones = lifestyle, metallic gold = finance); the rest stays black ink on white. Stark contrast between flat 2D black ink sketch and hyper-realistic 3D objects. All in-image text MUST match the input language (Chinese input → Chinese text).
```

**独立视觉契约(皮肤 G 专用,六维取这组值)**:
1. 背景:干净明亮的白色纹理纸,大量留白
2. 草图层:极简黑墨手绘涂鸦(minimalist black ink doodle)
3. 高光层:照片级真实 3D 物体(studio light + 真实质感 + 真实投影)——⚠️ 覆盖默认「非写实」那条
4. 物理互动(灵魂,不能省):真实物体跟草图物理互动——按住纸 / 投影压过墨线 / 贴胶带 / 缠住草图元素 / 破纸而出。⛔ 物体只是「摆在旁边」= 没做到
5. 字体:主标题手绘马克笔大字,标签随意钢笔小字
6. 色调:写实物体按主题配色——科技=冷蓝/金属,生活=暖色,金融=金。⚠️ 不强制橙红(覆盖默认契约);草图层始终黑墨白底

**布局智能适配**(按内容选,来自原 spec):
- 流程 / 步骤 / 时间线 → 左右流程图 + 箭头
- 对比 / vs → 分屏对比
- 中心主题 + 多个特征(默认)→ 中心辐射(hub & spoke)

**小互怎么融**:
- 默认:小互以**黑墨手绘草图**形态出现(属于草图层),当讲解员 / 指路人;红框眼镜仍红色点睛;关键概念才用 3D 写实物体当焦点
- 图表本身够强时,可纯信息图不放小互
- ⛔ 小互**不做 3D 写实**(会跟草图层打架),他永远在草图层。锚点传齐刘海图,但 prompt 写「render 小互 as a flat black ink doodle, NOT 3D」

**最适合**:轨道二·解释图(产品对比 / 流程 / 概念拆解),要强视觉冲击的信息图。⛔ 不适合轨道一情绪锚点图(那是角色演情绪,本皮肤是信息图风)。

**注意**:
- 每个点只挑 **1 个**元素做 3D 写实焦点,别堆满(堆满就乱、就丢留白)
- 图内中文是文生图画的,仍受「字少 2-8 字 + 错字重生」铁律——标注一多就糊,精确文字不是它强项

## 怎么选皮肤

1. 用户 `--style 3d/sketch/flat/mixmedia` 指定 → 用指定
2. 没指定 → 按调性推荐:**产品/封面→3D,观点深度→editorial,人文温暖→watercolor,教程→扁平或黑白,轻松梗→marker,信息图/强冲击对比→mixmedia(混合媒介)**;报给用户一句"这篇建议用 X 皮肤,要换吗",不确定就用默认 3D
3. 一篇文章内所有配图**用同一种皮肤**,不要混(否则一组图风格不统一)

## 颜色 / 情绪色

- 3D/扁平:暖色调橙红为主;黑白:黑线 + 红点睛
- 情绪色:沮丧加灰蓝、得意加金光、紧张加红
