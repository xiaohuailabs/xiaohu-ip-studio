# 单页信息图海报(篇级轨)

> 一张多panel整版图顶 N 格。**这是篇级轨,不是第四条单点轨**——前三轨(情绪 / 解释 / 四格)判"单个锚点画成哪种图",本轨判"整条流程 / 整组对比要不要打包成一张总览版"。一篇最多一张,放开头当导览或结尾当总结。
>
> **血统**:形态启发自开源技能 editorial-line-system(2026-06-22 对照实验验证:它的多panel编辑信息图形态是 ip-studio 三轨没覆盖的产物类型)。**只借形态,不借它的方法论**——editorial 的核心指令是"把一切抽象转成日常场景隐喻",那套对机制图有害(会画好看但漏 / 错)。锁结构 / 角色克制 / 皮肤统一全部沿用 ip-studio 自有方法论。

## 何时起海报(默认不起,命中才起)

命中任一 → 考虑配一张(且仅一张)总览海报,其余点照常走三轨散图:
- **≥3 步完整主流程**:管线 / 工作流 / 操作步骤 / 生命周期 → 纵向编号流程海报
- **一组并列对比 / 功能矩阵**:A vs B、N 个方案横排、能力矩阵 → 横向分栏 or 网格海报
- **需要一眼看全貌**:文章信息多,读者要先有张地图再逐段深入 → 开头放总览海报

⛔ 不起海报(退回别的轨):
- **单个机制 / 单个结构点**(一次 MoE 路由、一个内存布局、一种注意力)→ 走**解释图轨**,别硬塞海报。判据:它是"一个点讲透"还是"多个点串成全貌"?一个点 = 解释图。
- **流程 >6 步 / 每格要塞长文字 / 各点需要分别放进不同段落** → 退回三轨散图。海报焊死一块,改一处重生成整张,panel 不可单独复用。
- 纯叙事 / 纯情绪 → 四格 or 情绪图。

## ⛔ 核心铁律:锁结构,不是凑版面

海报最大的坑(就是 editorial 的坑):**先想好看的多panel版式,再把内容往格子里塞 → 出来好看但漏关键点 / 机制画错。** 反过来做:

1. 先列要进版的 N 个点(回原文 grep,每个 panel = 一个真实步骤 / 对比项 / 部件,沿用 `deep-reading.md` 的 Q4 内容锁定)
2. 每个点锁死"这格非画不可的真实部件 / 数字 / 标注"(MoE 例:8 个专家、top-2、权重 0.7/0.3)
3. **最后**才给每格配一个最小场景 + 编号 + 短标注

先有结构清单,再有版式。版式服务结构,不是结构迁就版式。

## 版式配方(按内容自然形状选,沿用 2.5 比例联动)

- **纵向编号流程(3:4)**:N 步从上到下堆叠,大号编号 01–0N,左侧一条贯穿流程线串起;每格一个最小场景。适合管线 / 步骤流。
- **横向流程 / 左右对比(4:3)**:数据左→右流动,or 左右分栏 A vs B。适合"输入→处理→输出"、双方案对比。
- **网格矩阵(1:1 / 4:3)**:M×N 格每格一个单元。适合功能矩阵 / 能力对比 / 角色阵列。
- ⛔ 手机封顶 4:3(沿用 2.5),不上 16:9——公众号移动端 16:9 只 ~1/4 屏、字和图糊。
- ⛔ 比例数值与 prompt 第一句方向词联动(`3:4`→VERTICAL portrait / `4:3`→HORIZONTAL landscape / `1:1`→SQUARE;改漏会变形)。

## 角色与画风(沿用固化层,海报不破例)

- **角色占比默认「小·嵌入」~15%**:每格里角色是小 actor,整版靠编号 / 排版 / 流程线撑,不靠角色撑(沿用 SKILL 步骤 2 角色占比法则 + orange/小黑思路)。
- **画风沿用 `style-dna.md` 皮肤**(默认手绘线稿),一张海报内同一皮肤 + 同一视觉契约六维统一。
- **pastel 选择性**:只标关键 / 激活 / 选中路径(MoE 例:高亮被激活的 top-2),其余保持单色黑白;别整版上色。
- **角色一致**:用选定 IP 的锚点图锁形象;同一个人在每格出现要像同一个人(生图传 `--reference` 锚点)。

## 文字

每格只放短标注:大号编号 + 关键词(3-6 字)+ 一句注脚(≤12 字)。**长机制 / 公式 / 大段说明放不进海报**——要讲深的拆回解释图轨。GPT-image-2 中文 ~99% 准,短标注放心让它写;但标注越多越容易乱,克制。

## prompt 骨架(套 `prompt-template.md` 的 STYLE_DNA + IP 段)

```text
A modern editorial-style infographic poster, [VERTICAL 3:4 / HORIZONTAL 4:3 / SQUARE 1:1] layout, titled "[中文标题]", minimalist [STYLE_DNA 皮肤] line art. [N]-panel layout, [纵向堆叠 / 左→右流动 / 网格]:
  Panel 01 [关键词] — [选定IP角色] [最小动作 embodying 该步], label "[短标注]"
  Panel 02 ...
  ...
Each panel keeps the character small (~15%, embedded actor not hero). Strong magazine typography: one bold Chinese headline, large two-digit numbers 01–0N, short Chinese labels. Large negative space, thin connecting flow arrows. Soft pastel accents ([暖橙/奶黄/奶油]) ONLY on the key/active path; inactive elements plain black-and-white. Flat vector-like finish, high contrast, no realistic lighting.

Negative: realistic lighting, 3D, glossy, painterly, anime, childish mascot, excessive color, busy background, cluttered layout, heavy gradients, illegible typography, wrong count of items.
```
⛔ panel 数 = 步骤 1.9 锁的结构点数;负面词必带 `wrong count of items` 防它多画 / 少画。

## 生成 + 自检

- **基准图先行**:多panel海报信息多,先生 1 张确认版面 / 数量 / 标注对不对再定。错了调 prompt 别将就。
- ⛔ **数量自检(海报独有,普通三轨没这么严)**:海报最易错"该 8 个画成 7 个 / 该激活 2 个高亮成 3 个"。生成后逐一数:panel 数对不对?高亮 / 激活数对不对?权重和对不对?数字标注对不对?
- **短板诚实告知用户**:海报焊死一块,改一处重生成整张,不能单独复用 panel;信息密度封顶 ~6 格。交付时说清这是"总览图",深点仍在文章正文 + 解释图里。

## 与三轨的关系(别打架)

- 一篇可以:**1 张海报(开头导览)+ N 张三轨散图(各段深入)**。海报是地图,散图是景点。
- 一篇别:整篇只有一张海报扛所有——读者点不进细节,深机制糊在小格里。**海报 ≠ 偷懒把 N 张图合一张省事。**
