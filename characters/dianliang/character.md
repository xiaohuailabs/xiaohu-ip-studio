# 角色包:电量(Diànliàng / Batt)

> 小互宇宙 IP 库成员 · 简单符号角色(2026-06-13)。格式样板见 `characters/xiaohu/character.md`。

## 角色包元信息

| 字段 | 值 |
|---|---|
| **名称 / 英文** | 电量 / Diànliàng (Batt) |
| **基础造型** | 竖立电池,身上有电量格 |
| **主色** | 绿(满电)/ 红(没电) |
| **一句人设** | 社畜能量条,满电 ↔ 1% 红格,**情绪就是电量** |
| **默认画风** | 黑白线稿(皮肤B)——手绘黑线 + 淡彩 + 白底 |
| **招牌** | 身上电量格高低 = 它的状态(核心机制) |
| **锚点图** | `refs/dianliang-锚点.png` |

## 外形

1. **竖立电池**身体,顶部有正极小凸点
2. 身上几格**电量条**(满=绿、空=红)
3. 两点眼 + 小短手短脚
4. 没电时身体歪斜、冒小闪电

## 性格

社畜能量条本体——满电时蹦跶,1% 时瘫红。**它的"表情"主要靠电量格演**:这是它跟别人最不一样的地方,配"精力/状态/续航/电量焦虑"类话题专用。

## 表情随情绪变(靠电量 + 脸双管)

满电:绿格 + 精神;半电:黄格 + 一般;1%:红格 + 瘫 + 冒汗;充电:插着线满足。判据:看电量格就能猜出状态。

## 英文 prompt 段({表情}{动作}按本张替换)

```
Recurring IP character 电量 (Diànliàng): an upright battery body with a small positive nub on top and a few horizontal CHARGE BARS on its belly (green = full, red = empty), two dot eyes, tiny stubby arms and legs. Its mood shows mainly through the charge level. A little social-battery on legs.
Expression & charge for THIS image: {电量高低 + 表情/情绪} + {动作/道具} — MUST match this point's emotion.
```
