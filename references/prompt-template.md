# 单张生图提示词模板

每张图单独生成,不拼图。按正文内容替换变量。**画风段从 `style-dna.md`(已填:皮肤 A–K)取本篇选定皮肤注入下面的 `[STYLE_DNA]` 占位处;IP 段从选定角色的 `characters/<名>/character.md` 取「英文 prompt 段」注入 `[IP]` 占位处。两处都填好,模板就能直接出图。**

## ⛔ 比例 / 方向词联动表(组 prompt 前先查)

`{ASPECT}` = 这张图定的比例(全篇默认或单张覆盖),`{ORIENTATION}` = 对应方向词。两者必须取自同一行,否则模型收到"画横版但画布竖"的矛盾指令,出图变形:

| 比例 `{ASPECT}` | 方向词 `{ORIENTATION}` |
|---|---|
| 16:9 / 4:3 / 3:2 | horizontal |
| 9:16 / 3:4 | vertical |
| 1:1 | square |

模板第一句写成 `Generate one standalone {ASPECT} {ORIENTATION} ...`,YAML 头的 `aspect_ratio` 填同一个 `{ASPECT}` 值。比例按内容判断(见 SKILL.md 2.5),移动端场景无横向理由时偏竖 `3:4`,不要无脑套 16:9。

⚠️ **GPT-image-2 有时无视 aspect 直接返回方图**(aspect 只是文字 hint,不是硬约束):想要 3:4 / 16:9 却出了方图 → 重生(2026-06-14 借 illo models)。

## 三轨 prompt 骨架(按 SKILL 1.5 分流结果选一个)

挑完图类型,按轨道选骨架——情绪锚点→**轨道一**(角色隐喻);解释图→**轨道二**(图表骨架,小互当讲解员);四格漫画→**轨道三**。三轨共用上面的比例联动表 + 下面的「文字渲染铁律 / 文字层方案」。

⛔ **视觉契约句(三轨通用——每张 prompt 的 Constraints/STYLE 段必须粘这句,这是全篇风格一致的根)**:
> `Clean white or light solid studio background. Soft even studio lighting — NO dramatic cinematic light, NO depth-of-field background blur. Blind-box designer-toy finish, NOT photorealistic cinematic rendering. Warm orange-red palette.`

背景/光影/景深/精致度全锁这一句,情绪图和四格就不会飘成电影感场景(2026-06-01 根治:同皮肤词但背景没锁,四格飘电影感、信息图白底,一篇裂成两种)。

⛔ **角色防崩坏铁律(三轨通用——每张 prompt 的 Constraints 段也粘这句;2026-06-14 借 illo prompt-recipe)**:角色是**实心不透明**的形状挡在场景前;地平线 / 桌沿 / 货架 / 背景线**在角色轮廓处停止,不穿过身体**;四肢按设计数量**干净连接**——不多长手、不漂浮、不从肚子中段长出胳膊;道具**握在手里、跟躯干留缝**,不贴脸、不从身上长出来;**每只手最多拿一个道具**,多的放桌上 / 地上。英文句:
> `The character is a solid OPAQUE shape in front of the scene; horizon / desk-edge / shelf / background lines STOP at its outline and never pass through its body; limbs connect cleanly at the designed count — no extra / floating / mid-torso arms or legs; any tool is held in a hand with a clear gap from the torso, not glued to the face or growing out of the body; at most one prop per hand. Props, arrows and underlines share the character's exact line treatment — one artist, no loose sketchy props next to a clean character.`

(GPT-image-2 照样会画三只手 / 道具糊胸口,这段纯收益;末句"道具/箭头/标注跟角色同一种线"治"角色利落但道具潦草=废图")

### 轨道一:情绪锚点图(小互演情绪,角色隐喻)

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article illustration.

[STYLE_DNA — 注入本篇选定皮肤,三选一,见 style-dna.md]
皮肤A 3D: 3D rendered Pixar / blind-box designer-toy style, chibi, big round eyes, soft volumetric lighting, detailed texture, warm orange-red palette.
皮肤B 黑白: hand-drawn sketch, thin wobbly black ink lines, pure white background, lots of white space, sparse red accents, napkin doodle, NOT 3D NOT vector.
皮肤C 扁平: flat minimalist vector, bold clean outlines, solid color blocks, modern, white bg.
皮肤H 极简: ultra-minimal few-stroke line-dog drawing, fewest possible wobbly mono-ink lines, huge white space, ONE signature accent color only, no shading no texture no bg, cute sticker vibe. 结构/标注照画全,极简只减质感不减信息.
皮肤I Notion小蓝人: clean simple Notion blue-people, monochrome blue ink + flat soft-blue fills, off-white bg, friendly flat, huge white space, only the signature stays non-blue (小互红眼镜). SaaS 讲解感.
皮肤J Notion文学线稿: loose literary pen-and-ink (Roman Muradov 风), expressive black ink + light cross-hatch on cream paper, bookish whimsical, 比皮肤B更松更艺术不是简笔.
皮肤K Notion暖色编辑: warm muted editorial, friendly ink line on cream, desaturated terracotta/sage/dusty-blue/ochre flat fills + riso grain + off-register, mid-century. ⚠️跟皮肤D近,二选一.

[IP — 小互 Xiaohu,跨皮肤一致]
Recurring IP character 小互 (Xiaohu): a chibi office-worker kid, black bob with straight blunt bangs (NO buns, NO side-buns), thin round RED-framed glasses, orange-red knit sweater + denim overalls, a small yellow VERTICAL "小互" badge on a black neck lanyard (portrait, NOT a horizontal tag). 小互 performs the core conceptual action.
{FOX — 按需,见 characters/xiaohu/character.md 出场规则。需要狐狸时加: "a tiny lazy droopy-eyed fennec fox nearby, ≤10% of frame, NOT competing with 小互"。不需要则整句不写}
⛔ ACT THE SITUATION, not the face: place 小互 INSIDE a real-life situation that produces this emotion — half-buried / tangled / pulled at / cornered / swamped by the relevant objects — so the feeling comes from the SITUATION. 小互 is SMALL and embedded in the scene doing a physical action in it, NOT posing center-stage with a big face. Expression for THIS image: only a light natural reaction ({本张情绪}), NOT a dramatic grimace. (见 metaphor-method「演处境 > 演表情」)
⛔ ALL skins: pass a 齐刘海 anchor (characters/xiaohu/refs/xiaohu-ip-正面挥手.png) as --reference to LOCK the character. For 黑白/扁平 skins, write in prompt: "This is the SAME character as the reference — keep EXACTLY the bangs bob hair, red round glasses, vertical yellow 小互 neck-lanyard badge (portrait, not horizontal), orange sweater + denim overalls; ONLY change the rendering to [skin] style."

Theme:
{这张图的主题}

Structure type:
{Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜 —— 选一}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面:主体在哪、在做什么、主物件是什么、信息怎么流动}

Suggested elements:
{物件1} / {物件2}   (只选 1-2 个,别堆满)

Chinese handwritten labels:
{标注1} / {标注2} / {标注3}   (最多 5-8 处,每处 2-8 字)

Color use:
Warm palette, orange-red dominant (小互's sweater). Signature: RED round glasses + yellow VERTICAL "小互" neck-lanyard badge (portrait). Mood color: cool gray-blue for anxiety/down, golden glow for triumph, red accents for tension.

Constraints:
One image explains only one core structure. Main subject ~40%-60% of canvas, keep ≥35% blank space. At most 5-8 short Chinese labels. No title in top-left corner. Do not write the structure type on the image. Not a formal diagram / slide / dense explainer. Invent a fresh metaphor for THIS article, do not copy prior examples unless explicitly asked. Clear but not instructional, interesting but not childish, strange but clean.
```

### 轨道二:解释图(流程/信息/对比/阶梯/关系)

借鉴宝玉技能的结构化字段。角色**嵌入结构当行动者**(爬台阶 / 卡断点 / 操作机器 / 拉线汇聚,⛔不站旁边指点;传长相锚**不**传演技锚)。**2026-06-19 重订**:角色**小而有戏 ~15-18%**(不是 25-35%)、与图表框**同墨同线扁平**(禁铅笔阴影 / 写实 / 3D)、招牌色保留但 **muted 不堆角色身上**——抢不抢戏的开关是同墨不是大小。小互等复杂彩色角色要额外硬写 "VERY SMALL ~15%" + 传极简形态锚。选角双适配闸 + 锁定角色三档适配,见 explanatory-diagrams.md「IP 占比/用法」。

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article {INFOGRAPHIC|FLOWCHART|COMPARISON|FRAMEWORK|TIMELINE} (clean diagram, NOT a character scene).

ONE reference = {角色} identity (keep its signature features EXACTLY). {角色} is a SMALL WORKING PART of the structure — climbing the steps / stuck at the broken node / operating the machine / pulling the lines together, mid-action, doing the work the diagram explains (NOT a presenter standing aside pointing). ⛔ Draw {角色} in the SAME flat line-art as the boxes — same line weight, NO pencil shading / realism / 3D — so it reads as ONE picture with the diagram. Keep its signature color but MUTED so it does NOT outshine the orange-red flow / red accents. The structure stays the main subject (~82-85%); {角色} is embedded SMALL at ~15-18%, neutral focused expression. (小互 etc. complex colored chars render too big — write "VERY SMALL ~15%" + use 极简形态 anchor.) NO fennec fox in diagrams unless explicitly needed — the chart is the star.

[STYLE_DNA — 注入本篇皮肤,见 style-dna.md]

Layout: {grid / radial / hierarchical / left-to-right / top-down}

ZONES / STEPS / NODES (按图类型选一种,逐个写清):
- {区块1}: {具体内容 + 真实数据}
- {区块2}: {...}
箭头/连线: {流向 / 汇聚 / 对比分隔 / 台阶递进 / 谁连谁}

LABELS(⛔ 必须填文章里的真实数字 / 术语 / 引用,不许占位符):
{标注1} / {标注2} / ...   (每处 2-8 字,大而醒目)

COLORS(语义批注色,2026-06-12 借 juju 补全——见下「语义批注色表」): 暖色橙红为主,强调色 2-4 个封顶,每个色必须有含义。Color values and color names are rendering guidance only — do NOT display them as visible text in the image.

STYLE: {皮肤渲染}, clean, evenly spaced, generous white space, NOT cluttered, icons match content.
ASPECT: {ASPECT}
```

### 轨道三:四格漫画(起承转合)

传长相锚**不**传单一演技锚(四格四情绪靠分格描述递进)。比例用 `1:1`(2x2 方版)或 `3:4`。

```text
Generate one standalone {ASPECT} {ORIENTATION} four-panel comic (a 2x2 grid), Chinese captions.

ONE reference = 小互 identity (keep EXACTLY: bangs bob / red round glasses / orange-red sweater + overalls / yellow VERTICAL 小互 tag). The SAME 小互 across ALL 4 panels; EXPRESSION PROGRESSES with the story — do NOT copy one fixed face into every panel. {FOX — 按需: 狐狸能当反应角(如格2跟着崩溃)才放,否则不放。放时 ≤10% per panel}

[STYLE_DNA — 注入本篇皮肤]

Clean 2x2 grid with visible thin panel borders and white gutter. Each panel = scene + emotion + ONE short Chinese caption:
- Panel 1 (起): {现状 / 期待} — {情绪}. Caption: {≤8字}
- Panel 2 (承): {冲突 / 崩溃,情绪最低} — Caption: {≤8字}
- Panel 3 (转): {转机 / 解法,情绪反转} — Caption: {≤8字}
- Panel 4 (合): {结局 / 真香,情绪最高} — Caption: {≤8字}

Expression arc across panels: {期待 → 崩溃 → 惊喜 → 惬意}. Each panel clean and uncluttered, ONE caption each.
ASPECT: {ASPECT}
```

## 人小物大 / 极简留白模板(演处境的极致,2026-06-15 加,4 角色实测成功)

> 适用:情绪图走"尺度戏剧"(被工作埋 / 被需求逼疯 / 被人群淹)。**极简角色**直接传其锚点;**小互**传极简形态锚点 `refs/xiaohu-极简形态.png`(见 character.md 两档形态)。

```text
A clean minimal hand-drawn line illustration on a PURE WHITE background with LOTS of empty white space. Light black ink lines, a single warm orange-red accent. New Yorker restraint, big negative space.

Dramatic SCALE CONTRAST: an ENORMOUS {巨物: 文件山 / 红色警告墙 / 人群 / KPI表格山} looms huge, filling most of the frame. The character {角色} (KEEP from reference: {角色招牌}) is TINY at {脚下 / 角落 / 被埋}, {贴人设的姿态: 躺平 / 炸毛 / 缩成团} — "{一句处境}". The feeling comes from the SIZE CONTRAST, not from a face. A few short Chinese labels on the {巨物}: {标签1} / {标签2} / {标签3}. Keep {角色} cute and recognizable (露脸,别缩成纯剪影). Black lines + one accent, lots of white space.
```

**要点**:① 物极大顶天、人极小但**露脸**(别成纯剪影,招牌才保得住) ② 靠尺度不靠脸 ③ 巨物贴真实中文标签(99+ / 紧急!! / KPI) ④ 单 accent 克制 ⑤ 角色姿态贴人设(躺平角懒摊 / 发疯角炸毛 / 社恐角缩团)。详见 metaphor-method「人小物大」+「全库通用」。

## 语义批注色表(三轨通用,2026-06-12 借 juju 补全)

原则:**颜色澄清动作,不装饰画面**——每个用色说得出含义,说不出的去掉;每张图强调色 **2-4 个封顶**(白底黑线不算)。

| 色 | 含义 |
|---|---|
| **橙红** | **当前步骤 / 主路径 / 小互正在做的动作**(IP 招牌色兼任"读者现在看这里"的指示色,一图只标一处当前) |
| 红 | 警示 / 风险 / 纠偏(用量最小,小标记不大面积) |
| 青绿 | 正向 / 解决 / 可复用 |
| 灰蓝 | 低落 / 次要路径 |
| 金 | 成功 / 高光时刻 |
| 紫灰 | 模糊地带 / 未定论 / 还没名字的状态 |

适用:轨道二解释图最严格(每条连线/区块用色对表);轨道一情绪图沿用原情绪色逻辑(灰蓝沮丧/金得意/红紧张),但同样 2-4 色封顶。

## 中文标注位置池(可选,防一组图标注全在同一个位置;2026-06-12 借 juju)

标注不悬空,**必须依附在画面物件上**(便签/吊牌/路牌/纸片/箭头注)。位置可在这些里换着用:顶部手写标题 / 侧边标签 / 路牌式 / 物件贴签 / 角落便签 / 分裂式标题(二选一对比时左右各半) / 竖排侧标(竖版图)。标注不压脸、不压主物件、不压关键路径。

## ⛔ 文字渲染铁律(2026-06-10 按 GPT-image-2 能力重写,三轨通用)

> GPT-image-2(默认生图模型)中文字符级准确率 ~99%、能排密集标注。所以"防糊 / 强制字少"不再是硬约束——**重心移到"标注内容对不对":文字交给模型,内容由你把关。**

1. **标注必须从原文抽、准确(现在唯一要严防的)**:数字 / 术语 / 部件名逐个回 source 核对(45.6% 就写 45.6%,AFM 3 Cloud 不写成 AFM Cloud)。模型字写得对,但你喂错它照样画错——见 deep-reading Q4 必现内容清单。
2. **色值 / 色名别当标注**:prompt 里写 hex / 颜色名只是渲染指导,末尾加 `Color values and color names are rendering guidance only — do NOT display them as visible text.` 防它把 "#E8655A""橙红"画成字。
3. **能写密集标注了,但仍"一图一核心意思"**:别因为模型能写就堆满,该几个标注就几个。万一个别字糊了:改 prompt 重生(新文件名留旧候选),⛔ 仍禁 PS / SVG / Pillow 在成图上涂改文字。
4. **宁可无字,不要乱码**(2026-06-12 借 juju):字号太小或连续重生仍不稳的位置(四格格内小标、远景里的名牌字、微缩物件上的字),宁可去掉文字留纯图形,也不留乱码/错字上线。小互名牌同理:画面太小写不清"小互"二字时保持空白黄牌,不让它漂成乱码。
5. **⛔ 代码 / 表格 / 密集专业文字 → 示意化,别写满(2026-06-15 g1 根治,是上面"~99% 准"的例外)**:上面说"~99% 准"指的是**普通短标注**;**密集代码 / 表格 / 一堆专业字段名是雷区**——实测 g1 一段真 SQL 糊出"销售泰 / GRDER / 销售飙"5 个错字。画代码 / 表格时:① **代码只写骨架**(`SELECT … FROM … WHERE …` 几个词 + `…` 省略 + 后面用潦草线条带过,⛔别写整段真代码)② **文件柜 / 表格标签 ≤3 个**或留空白牌 ③ 总字量压最低。宁可"看着像代码"也不追求每个字段名写对。详见 anti-ppt-qa「代码/表格示意化」。

## 文字层方案(⚠️ 2026-06-10 起基本废弃)

> 这条是 GPT-image-2 之前为"标注零错字"搞的 workaround(AI 画少字底 + 矢量中文叠层)。GPT-image-2 中文 ~99% 准确后**默认不用了**:直接让模型写、个别字糊了改 prompt 重生即可。仅在极端情况(单张标注极多、产品名 / 数字一个不能错、连重生几次仍糊)才退回这条作兜底;一般忘了它,别再为它多走叠字工序。

YAML 头(交给 generate.py 归档时):必须含 `aspect_ratio: "{ASPECT}"`(填这张实际定的比例,如 `"16:9"` / `"9:16"`),否则生图脚本报错。务必和 prompt 第一句的 `{ASPECT} {ORIENTATION}` 同步。

## 图像编辑提示

去掉左上角误生成的标题:
```text
Edit the provided image. Remove only the handwritten title "{要删的文字}" and its underline from the top-left corner. Fill with the same clean background. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio. Add no new text or objects.
```

让隐喻主体更突出:
```text
Regenerate with the same core meaning and simple layout, but make the main subject more central to the conceptual action — doing the strange work that explains the idea, not standing beside a diagram. Keep it clean, sparse, and not cute.
```
