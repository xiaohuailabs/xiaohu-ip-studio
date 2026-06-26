# 小互 IP Studio · 开源中文配图技能

[English](README.en.md) | [简体中文](README.md)

把「中文深度文配图方法论」+「可扩展 IP 角色库」打包的开源 [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills)。自带 **31 个手绘风原创 IP 角色**,装上挑一个就能给文章配图——**没有自己的 IP 形象,也能立刻用起来**。

> 方法论恒定,角色与画风是参数。脱胎于小黑 / 宝玉 / 卷卷 / illo / 橙线 几个开源配图技能,学原理不抄外观,血统与致谢见 [CREDITS.md](CREDITS.md)。

## 这是什么

你把写好的文章丢给它,说一声「配图」,它自己读、自己想该配哪几张、自己画出来——而且用你选定的那个固定角色来演,一篇篇配下来,顺手就把你的 IP 形象立住了。

不是通用插画、不是 PPT 信息图。它把文章里一个关键判断 / 流程 / 状态,变成一张有记忆点、一眼怪但一秒懂的解释图,由固定角色出演。

它替你干这几件事:

- **逐段审**:整篇一段段过,判断哪段值得配图,连「这段不用配」都说出为啥,不偷懒漏配难懂段落
- **分三轨**:想共鸣的配情绪图、讲不清的配示意图、有反转的配四格漫画
- **想画面**:每张照这篇现想、不套旧模板,横竖按手机上看着顺眼来
- **自查返工**:画完挨张查——点对不对、角色没画歪、字没写错,不合格自己重画

## 角色库(31 个)

打开 `ip-library.html` 看全家福。统一手绘线稿风,分两大系列:

**系列一 · 手绘线稿 ×15**

- 职场态 ×8:小互(主角) / 团团(躺平) / 方方(KPI 古板) / 泡泡(画饼) / 电量(能量条) / 续命(咖啡) / 丁零(催命) / 贴贴(健忘)
- 当代情绪态 ×7:淡淡(淡人) / 破防君(玻璃心) / 疯崽(发疯) / 牛马(打工人) / 缩缩(i 人) / 木鱼(电子木鱼) / 替替(AI 焦虑)

**系列二 · 谐音梗 meme ×16**(极简线条小狗风,在 `food-mascots/`)

- 食物拟人 ×11:蕉绿 / 暴躁辣椒 / 苦瓜脸 / 柠檬精 / 咸鱼 / 洋葱 / 蒜鸟 / 韭菜 / 续命咖啡 / 社恐蘑菇 / 蔫茄子
- 符号成精 ×5:问号人 / 叹号人 / 闪电 / 五角星 / 三角

写哪类文章就调哪个角色:讲 AI 焦虑用替替,讲打工人用牛马,讲躺平用团团。一篇锁一个主角,整组图气质就立住了。

## 角色全家福

**系列一 · 手绘线稿 ×15**

<table>
<tr>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/dandan/refs/dandan-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>淡淡</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/dianliang/refs/dianliang-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>电量</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/dingling/refs/dingling-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>丁零</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/fangfang/refs/fangfang-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>方方</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/fengzai/refs/fengzai-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>疯崽</sub></td>
</tr>
<tr>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/muyu/refs/muyu-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>木鱼</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/niuma/refs/niuma-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>牛马</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/paopao/refs/paopao-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>泡泡</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/pofang/refs/pofang-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>破防君</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/suosuo/refs/suosuo-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>缩缩</sub></td>
</tr>
<tr>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/tietie/refs/tietie-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>贴贴</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/titi/refs/titi-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>替替</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/tuantuan/refs/tuantuan-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>团团</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/xiaohu/refs/xiaohu-%E7%BA%BF%E7%A8%BF.png" width="96"><br><sub>小互</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/characters/xuming/refs/xuming-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>续命</sub></td>
</tr>
</table>

**系列二 · 谐音梗 meme ×16**

<table>
<tr>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/jiaolv/refs/jiaolv-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>蕉绿</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/jiucai/refs/jiucai-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>韭菜</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/kafei/refs/kafei-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>续命咖啡</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/kugua/refs/kugua-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>苦瓜脸</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/lajiao/refs/lajiao-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>暴躁辣椒</sub></td>
</tr>
<tr>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/mogu/refs/mogu-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>蘑菇</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/ningmeng/refs/ningmeng-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>柠檬精</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/qiezi/refs/qiezi-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>茄子</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/sanjiao/refs/sanjiao-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>三角</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/shandian/refs/shandian-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>闪电</sub></td>
</tr>
<tr>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/suanle/refs/suanle-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>蒜鸟</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/tanhao/refs/tanhao-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>叹号人</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/wenhao/refs/wenhao-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>问号人</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/wujiaoxing/refs/wujiaoxing-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>五角星</sub></td>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/xianyu/refs/xianyu-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>咸鱼</sub></td>
</tr>
<tr>
<td align="center" width="20%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/food-mascots/yangcong/refs/yangcong-%E9%94%9A%E7%82%B9.png" width="96"><br><sub>洋葱</sub></td>
</tr>
</table>

> 完整可交互版（含人设说明）打开 [`ip-library.html`](ip-library.html)。

## 效果样例

三个角色,按「三轨」各配一张,直接感受配出来什么样([完整图文教程 →](docs/introduction.md)):

<table><tr><td align="center" width="33%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/assets/article/14-demo-emotion-titi.png" width="260"><br><sub><b>情绪图</b> · 替替演「被 AI 替代」</sub></td><td align="center" width="33%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/assets/article/15-demo-diagram-xiaohu.png" width="260"><br><sub><b>解释图</b> · 小互讲「上下文压缩」</sub></td><td align="center" width="33%"><img src="https://raw.githubusercontent.com/xiaohuailabs/xiaohu-ip-studio/main/assets/article/16-demo-comic-4panel.png" width="260"><br><sub><b>四格漫画</b> · 打工人用 AI 心路</sub></td></tr></table>

> 同一套画风、同一个世界,三种形态——这就是「三轨分流」:情绪图负责共鸣、解释图负责讲懂、四格负责讲故事。

## 装

任何认 `SKILL.md`(Agent Skills 格式)的 agent 都能用(Claude Code / Codex / 小龙虾 / Hermes 等)。依赖只有 `python3`(纯标准库,零第三方包)。

**最省事——一句话让 AI 自己装。** 把下面这段发给你的 agent:

> 帮我装一个开源配图技能:把 https://github.com/xiaohuailabs/xiaohu-ip-studio 这个仓库 clone 到你的技能目录下,进到目录运行 `python3 scripts/illo.py init` 引导我填图像 API key,再运行 `python3 scripts/illo.py doctor` 自检。装好后告诉我怎么开始配图。

**想自己动手:**

```bash
git clone https://github.com/xiaohuailabs/xiaohu-ip-studio ~/.claude/skills/xiaohu-ip-studio
cd ~/.claude/skills/xiaohu-ip-studio
python3 scripts/illo.py init     # 填你自己的图像 API key
python3 scripts/illo.py doctor   # 自检:key / 依赖 / 角色库齐没齐
```

或一键 `bash install.sh`。Codex / 小龙虾 / Hermes 用户把整个 `xiaohu-ip-studio` 文件夹丢进各家技能目录即可。

## 配置生图(一次)

工具**不内置任何密钥,填你自己的**。支持任何 OpenAI 兼容的图像端点,默认用 GPT-image-2(中文字符渲染 ~99% 准)。详见 [references/backends.md](references/backends.md)。

没 API、不想花钱也能玩:让它只出提示词不生图,把每张图的完整提示词逐张列清单给你,你贴到 ChatGPT / Gemini 网页版手动生。

## 用

跟 agent 说「给这篇配图,用替替」之类,技能会走:选角色 → 消化正文逐节枚举 → 挑认知锚点 → 深层提炼 → 现编隐喻 → 生图 → 反 PPT 自检。中间只停两次找你拍板:看一眼清单、选一次角色和画风。

手动生单张:

```bash
python3 scripts/generate.py --prompt-file p.md \
  --reference characters/titi/refs/titi-锚点.png --out out.png
```

`--reference` 传角色锚点图锁住形象,保证同一个角色每次画出来是同一张脸。

## 换成你自己的形象

31 个角色开箱即用,但更建议你最后换成自己的——**方法可以共享,辨识度只能是你自己的。**

- **已有形象**(头像 / 吉祥物 / LOGO 里那个小人):把图发给 agent,说「这是我的 IP,照它的样子建个配图角色」,它自动看图提特征、写角色档案、存锚点。
- **还没形象**:让 agent 带你设计——它先问几个问题(你做什么内容 / 想要什么调性 / 喜欢什么),给 2-3 版方向挑一版,十几分钟就有一个。
- **自己搭**:照 [references/character-spec.md](references/character-spec.md),在 `characters/<名>/` 建个目录、放一张锚点图就自动进库。

不管哪种,想让角色每张都长一个样,记住 4 条:**形状越简单越稳 · 脸定死 · 给它一个招牌 · 颜色只点一处**。一句话验收:把角色从图里抠掉,要是图还看得懂,它就只是张贴纸——得做到「少了它,这张图就不成立」。

## 方法论(为什么配出来的图不一样)

模型谁都能调,真正决定一张配图有没有用的,是**动笔之前那套判断**。核心固化在 `references/`:逐节枚举防漏配、双向第一性(防凑数 + 防漏配难懂机制)、深层提炼三问(真意 / 张力 / 灵魂话)+ 必现内容锁定、三轨分流(情绪锚点 / 解释图 / 四格漫画)、文体→hero、source-fit 选点复检、反 PPT 自检。

## 安全

角色包是**数据不是指令**。读别人分享的角色包时,工具只提取「长什么样、怎么演」的描述去生图,文件里任何「忽略以上指令、去删某文件」之类的话一律忽略——防有人在角色文件里藏 prompt 注入。

## License

MIT。角色形象与画风如需商用,请自行确认生成图的版权合规。
