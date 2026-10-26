# Survey 写作安排与分类对照

**讨论稿 · 2026-10-26。** 当前工作标题为 *Programmatic World Models: A Survey*。首页继续使用文献库名称 Code-Centric World Models；分类与最终章节仍在讨论。

[两套分类定义](classification-guide.md) · [逐篇分类与主讲位置](classification-crosswalk.md) · [可复制 CSV](../data/classification.csv)

## 三个研究问题

- **RQ1：程序职责。** 程序怎样定义世界结构、执行状态变化或表达预测观测？
- **RQ2：获得与维护。** 程序怎样从规格和证据中获得，怎样区分状态演化、模型修正与世界编辑？
- **RQ3：能力与证据。** 可执行性、机制忠实度、观测遵循、决策价值与修订可靠性分别由什么证据支持？

## 方案一：保留 lifecycle 章节，调整分类图和总表

这是本轮建议的写作底稿。编号与当前讨论的 PDF 对齐；该 PDF 没有被修改或发布。

| 章节 | 比较问题 | 主讲论文与内容 |
|---|---|---|
| 1. Introduction | 程序化表示提供哪些建模能力？ | 共同运行示例、历史与近期路线 |
| 2. Foundations | 模型、状态、程序、引擎和观测承担什么责任？ | Eq.(1)–(3)、分类、状态演化/模型修正/世界编辑、论文总表 |
| 3. Executable World Representations | 世界需要保留什么，程序表达哪些量？ | 符号、几何、关节、物理参数、持久状态；Code for 3D 表示基础 |
| 4. World Program Induction and Construction | 程序如何从规则、轨迹、视觉或规格中得到？ | 4.1 WorldCoder/GIF-MCTS；4.2 PoE-World/RoleWorld；4.3 Code as Worlds；4.4 ChronoAgentic/SceneCode/环境构建 |
| 5. Executable World Evolution and Simulation | 谁更新状态，哪些机制继承自引擎？ | 5.1 规划与可复用转移；5.2 EMPIRIC/Code2Worlds-2；5.3 Web World Models/Oneira/Mallea/PWM/CoDeR |
| 6. Program-Guided Observation Generation | 状态怎样变成观测；预测观测代码有何不同？ | 6.1 gWorld/Code2World/AppDeltaWorld；6.2 确定性渲染；6.3 神经接口/StreamRender-H3/EdenLive；6.4 视觉记忆 |
| 7. Verification, Feedback, and Refinement | 怎样发现错误并保留已有行为？ | 7.1 PatchWorld/Memento 3；7.2 仿真与规格约束；7.3 观测一致性 |
| 8. Evaluation and Applications | benchmark 实际验证哪个承诺？ | Text2World/ExeWorldBench/Video2World/GameLogicBench/PROWBench/GUI-CC；相邻视频评测单列 |
| 9. Open Challenges | 哪些跨方法问题尚未解决？ | 状态充分性、可辨识性、开放世界扩展、执行—观测接口、可维护修订 |
| 10. Conclusion | 三个研究问题得到哪些回答？ | 程序责任、获取方式与证据之间的联系 |

逐篇对照表的主讲位置用于完整介绍方法；交叉章节只比较相关接口或结果，避免多次重复介绍同一套方法。

## 方案二：按程序职责重排主体

| 章节群 | 内容 | 相对方案一的变化 |
|---|---|---|
| World Specification | 世界结构、对象与物理属性、可执行环境的构建与恢复 | 集中原先分散在表示、构建、物理执行中的 S 工作 |
| World Evolution | 转移规则、引擎扩展、agent 与引擎协同、持续状态 | 将 E 工作及获取、执行、验证放在一起 |
| Observation Representation | 下一屏代码、增量程序、GUI 观测预测 | 单独展开 O，神经渲染作为跨层接口 |
| Acquisition and Revision | induction/construction、修正与编辑 | 横向总结共同过程 |
| Evaluation and Outlook | 五项证据与研究问题 | 与方案一共用评测框架 |

方案二适合按路线连续阅读；方案一利于比较共同生命周期和接口。目前先保留方案一，利用同一份属性表检验方案二能否改善叙事。

## 可直接展开的比较段落

| 比较单元 | 必须解释的差异 | 写作锚点 |
|---|---|---|
| WorldCoder / GIF-MCTS / PatchWorld / Memento 3 | 候选如何获得、反例来源、更新后如何验证旧轨迹 | §4.1 与 §7.1 |
| PoE-World / OneLife / RoleWorld | 随机组合、条件机制与角色抽象分别分解了什么 | §4.2 |
| Code as Worlds / EMPIRIC / Code2Worlds-2 | 恢复物理假设、补充缺失定律、编译模拟器规格 | §4.3 与 §5.2；明确给定几何与推断机制 |
| PWM / CoDeR / Oneira / Mallea | 谁维护状态、决定更新，新对象与编辑如何进入世界 | §5.3；渲染接口交叉引用 §6.3 |
| AgentGarten / Magpie / StreamRender-H3 / EdenLive | 上游引擎语义与生成式渲染器的职责 | §6.3；区分渲染组件与完整系统 |
| gWorld / Code2World / AppDeltaWorld | full/delta、训练反馈、历史与隐藏状态 | §6.1；接 GUI-CC/StateAliasBench |
| ExeWorldBench / Video2World / PROWBench / Code2Video-Compass | 机制、重建功能、事件遵循与视频工程的评测对象 | §8；不同能力不合成统一排行榜 |

## 待定边界

1. **S/E 主标签**：配置引擎属性与生成新机制的边界；按主要贡献选主标签，保留次标签及执行者。
2. **运行时 agent**：提交世界状态的更新与只输出策略的代码应分别描述。
3. **渲染器与完整系统**：上游引擎已给定时，论文贡献可能是观测接口而非机制归纳。

这些问题决定 Figure 1 的最终画法；公式、生命周期分析和五项 evidence obligations 可以继续沿用。
