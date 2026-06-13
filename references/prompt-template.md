# 单张生图提示词模板

每张图单独生成,不拼图。按正文内容替换变量。**画风段(STYLE_DNA / IP)从 style-dna.md、characters/<名>/character.md 注入——这两个定调前是占位,模板暂时跑不出图。**

## ⛔ 比例 / 方向词联动表(组 prompt 前先查)

`{ASPECT}` = 这张图定的比例(全篇默认或单张覆盖),`{ORIENTATION}` = 对应方向词。两者必须取自同一行,否则模型收到"画横版但画布竖"的矛盾指令,出图变形:

| 比例 `{ASPECT}` | 方向词 `{ORIENTATION}` |
|---|---|
| 16:9 / 4:3 / 3:2 | horizontal |
| 9:16 / 3:4 | vertical |
| 1:1 | square |

模板第一句写成 `Generate one standalone {ASPECT} {ORIENTATION} ...`,YAML 头的 `aspect_ratio` 填同一个 `{ASPECT}` 值。比例按内容判断(见 SKILL.md 2.5),移动端场景无横向理由时偏竖 `3:4`,不要无脑套 16:9。

## 三轨 prompt 骨架(按 SKILL 1.5 分流结果选一个)

挑完图类型,按轨道选骨架——情绪锚点→**轨道一**(角色隐喻);解释图→**轨道二**(图表骨架,小互当讲解员);四格漫画→**轨道三**。三轨共用上面的比例联动表 + 下面的「文字渲染铁律 / 文字层方案」。

⛔ **视觉契约句(三轨通用——每张 prompt 的 Constraints/STYLE 段必须粘这句,这是全篇风格一致的根)**:
> `Clean white or light solid studio background. Soft even studio lighting — NO dramatic cinematic light, NO depth-of-field background blur. Blind-box designer-toy finish, NOT photorealistic cinematic rendering. Warm orange-red palette.`

背景/光影/景深/精致度全锁这一句,情绪图和四格就不会飘成电影感场景(2026-06-01 根治:同皮肤词但背景没锁,四格飘电影感、信息图白底,一篇裂成两种)。

### 轨道一:情绪锚点图(小互演情绪,角色隐喻)

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article illustration.

[STYLE_DNA — 注入本篇选定皮肤,三选一,见 style-dna.md]
皮肤A 3D: 3D rendered Pixar / blind-box designer-toy style, chibi, big round eyes, soft volumetric lighting, detailed texture, warm orange-red palette.
皮肤B 黑白: hand-drawn sketch, thin wobbly black ink lines, pure white background, lots of white space, sparse red accents, napkin doodle, NOT 3D NOT vector.
皮肤C 扁平: flat minimalist vector, bold clean outlines, solid color blocks, modern, white bg.

[IP — 小互 Xiaohu,跨皮肤一致]
Recurring IP character 小互 (Xiaohu): a chibi office-worker kid, black bob with straight blunt bangs (NO buns, NO side-buns), thin round RED-framed glasses, orange-red knit sweater + denim overalls, a small yellow VERTICAL "小互" badge on a black neck lanyard (portrait, NOT a horizontal tag). 小互 performs the core conceptual action.
{FOX — 按需,见 characters/xiaohu/character.md 出场规则。需要狐狸时加: "a tiny lazy droopy-eyed fennec fox nearby, ≤10% of frame, NOT competing with 小互"。不需要则整句不写}
Expression & pose for THIS image: {本张表情/情绪} + {本张动作/道具} — MUST match the emotion (anxious/smug/guilty/confident/focused...).
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

借鉴宝玉技能的结构化字段。小互**只当讲解员**(传长相锚**不**传演技锚),图表是主体不是小互。

```text
Generate one standalone {ASPECT} {ORIENTATION} Chinese article {INFOGRAPHIC|FLOWCHART|COMPARISON|FRAMEWORK|TIMELINE} (clean diagram, NOT a character scene).

ONE reference = 小互 identity (keep EXACTLY: bangs bob / red round glasses / orange-red sweater + denim overalls / yellow VERTICAL 小互 neck-lanyard badge, portrait not horizontal). 小互 ONLY as a small friendly PRESENTER in a corner pointing — neutral, NOT a strong emotion, NOT dominating (~20% of frame). NO fennec fox in diagrams unless explicitly needed — the chart is the star, not the character.

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
