# Survey 写作安排与三类主线

**讨论稿 · 2026-10-29。** 当前工作标题为 *Programmatic World Models: A Survey*；首页使用文献库名称 *Code-Centric World Models*。README 首页直接采用三类主线，论文总表提供逐条记录和来源信息。

[三类主线说明](coarse-taxonomy.md) · [全量论文总表](paper-master-list.md) · [分类 JSON](../data/classification.json) · [可复制 CSV](../data/classification.csv)

## 三个研究问题

- **RQ1：程序承担什么职责？** 它是动作后果的动力学、持续存在的世界程序，还是 3D 世界的构建与编辑工具？
- **RQ2：程序如何获得和维护？** 它来自交互轨迹、文本/视觉规格、物理证据、资产工具，还是这些来源的组合？
- **RQ3：什么证据支持它？** 如何分别验证执行正确性、状态持久性、构建质量、观测一致性、规划价值和修订可靠性？

## 建议的顶层组织

| 主线 | 核心问题 | 正文重点 | 代表工作 |
|---|---|---|---|
| **WorldCoder-type**（纯状态） | 代码能否预测动作后果？ | 转移程序、随机/层次机制、规划、反例修复与主动实验；不生成外观的物理/符号世界 | WorldCoder、GIF-MCTS、TheoryCoder、PoE-World、OneLife、PatchWorld、Algebraic World Model、EMPIRIC、Code as Worlds |
| **Code-as-World-type**（白模 + 生成式渲染） | 代码维护的状态与规则能否驱动生成式渲染的世界？ | 状态权威、实体和规则、白模/proxy 条件、神经渲染接口、持久性与记忆 | Code World Model、Programmable World Model、CoDeR、GameDirector、AgentGarten、Oneira、Mallea、BoxWorld、State World Models、Matrix-Game 4.0 |
| **VibeWorlding-type**（完整 3D） | agent 能否用代码构建和编辑完整 3D 世界？ | 资产检索、场景程序、空间布局、关节/物理属性、渲染反馈与仿真准备度；含静态场景 | VibeWorlding、Holodeck、SceneCraft、WorldClaw、USDCraft、NeoWorld-3、SceneRig、Code2Worlds-2、SceneCode、ChronoAgentic |

三类之外的记录放在"其他"下：GUI 世界模型（包括 gWorld、Code2World、AppDeltaWorld 等可渲染代码预测）和按评测对象分组的评测基准。相关综述放在开头，用来说明本综述与它们的不同。

## 章节草案

| 章节 | 比较问题 | 主讲内容 |
|---|---|---|
| 1. Introduction | 为什么需要代码中心的世界模型？ | 共同示例；代码、状态、规则和观测之间的关系 |
| 2. Foundations | 三类主线分别把什么交给程序？ | 世界模型定义、状态权威、程序接口、执行与观测边界 |
| 3. WorldCoder-type | 如何从交互和证据获得可执行动力学？ | WorldCoder/GIF-MCTS；TheoryCoder/PoE-World/OneLife；PatchWorld/Memento 3/EMPIRIC |
| 4. Code-as-World-type | 代码世界如何驱动生成式渲染？ | Code World Model/PWM/CoDeR/GameDirector；AgentGarten/Oneira/Mallea/Web World Models；Magpie/AnyGameRenderer 等渲染器侧 |
| 5. VibeWorlding-type | 如何把意图和工具转成完整 3D 世界？ | VibeWorlding、SceneCraft、WorldClaw、USDCraft、SceneRig、NeoWorld-3；Code2Worlds/Code2Worlds-2/SceneCode/ChronoAgentic；SceneEvolve/WorldMirror/InfiniDream |
| 6. Observation and rendering interfaces | 世界状态如何变成可见观测？ | 确定性渲染、神经渲染与状态—观测一致性；GUI 分组（gWorld/Code2World/AppDeltaWorld）作为对照讨论 |
| 7. Verification and maintenance | 错误如何发现、修复和回归验证？ | 回放、反例、仿真反馈、事件遵循、长期一致性 |
| 8. Evaluation | benchmark 实际验证哪个承诺？ | WorldCoder-Bench、ExeWorldBench、Video2World、GameLogicBench、PROWBench、GUI-CC |
| 9. Open challenges | 三类方法共同缺少什么？ | 状态充分性、可辨识性、开放世界扩展、接口信息损失、成本与可审计修订 |

同一论文可以在交叉章节中被再次比较，但主线归属只保留一个。这样既能保持三类叙事清楚，也能讨论共享的执行、渲染和验证问题。

## 范围边界

机器人不是独立研究主线。只有当论文研究可执行动力学、世界程序、模拟器扩展或世界构建时，机器人实验才作为验证载体出现；纯机器人控制、操作策略或 Real2Sim 工具不会因为使用代码而自动成为核心文献。
