# Survey 组织建议

建议标题：**Code-Centric World Models: Executable Dynamics, Persistent Worlds, and Renderable Observations**。

主线是程序承担哪些世界语义、这些语义怎样获得与修订，以及它们怎样转化为可以检查的世界一致性和 agent 使用价值。可执行动力学、GUI 观测代码和持久视觉世界由同一分析框架贯通，文献之间的设计差异构成综述的比较贡献。

## 三个研究问题

- **RQ1：程序职责。** 代码在状态转移、世界构建与观测生成中承担哪些语义，这些职责怎样组合？
- **RQ2：获得与维护。** 世界程序怎样从规格、交互和视觉中获得，并在新证据下验证、抽象和修订？
- **RQ3：能力与证据。** 不同职责与获取方式在世界忠实度、长程一致性和 agent 使用价值上得到什么证据支持？

## 推荐目录

| 章节 | 回答的问题 | 代表内容 |
|---|---|---|
| 1. Introduction | 为什么需要将程序动力学、可见观测与持久世界联系起来？ | 运行示例、共同问题、三个 RQ、综述贡献 |
| 2. Scope, Definitions, and Review Protocol | 纳入对象、任务角色与文献核查方式是什么？ | target-world model / constructed world / observation predictor；检索与筛选 |
| 3. A Functional Taxonomy | 程序负责哪些语义，怎样组合？ | transition / observation / both；程序来源与生命周期标签 |
| 4. Learning and Revising Executable Dynamics | 规则如何从描述、交互和视频中得到？ | WorldCoder、GIF-MCTS、TheoryCoder、PoE-World、OneLife、Baba、ARC 系列、EMPIRIC；PDDL 生成 |
| 5. Constructing Persistent Executable Worlds | 怎样构造可运行、可干预和可维护的世界？ | Web World Models、Code2Worlds、Code as Worlds、ChronoAgentic、SceneCode、验证世界与训练数据 |
| 6. Predicting Observations as Renderable Code | 为什么以代码预测观测，怎样学习？ | gWorld、Code2World、AppDeltaWorld；full / delta、render feedback、retrieval |
| 7. Coupling Execution with Visual Generation | 执行状态怎样约束未来像素？ | Code World Model、Programmable World Model、CoDeR、GameDirector、Magpie、AgentGarten |
| 8. Evaluation and Evidence | 运行、转移、状态、呈现与使用价值各如何检验？ | Text2World、GameLogicBench、WorldCoder-Bench、Video2World、PROWBench、GUI-CC、StateAliasBench、ScratchWorld |
| 9. Cross-Branch Findings and Research Agenda | 不同路线共同揭示哪些可检验问题？ | predictive state、program-to-render alignment、regression-preserving repair、matched-budget model utility |
| 10. Conclusion | 三个 RQ 得到怎样的答案？ | 程序语义框架、获取与验证规律、证据和下一步方向 |

## 分类层级怎样保持一致

运行时职责作为主轴：程序承载转移、观测，或二者的耦合。程序合成、归纳、重建、验证和修补是横向属性，也可以成为组织比较的流程章节。这样，一篇从视频发现物理程序、执行仿真并渲染验证的论文拥有多个标签，但不会迫使分类树增加一个专属分支。

README 的九个文献分区是阅读导航。投稿稿的 taxonomy 使用 [taxonomy.md](taxonomy.md) 中的语义轴，避免把导航章节写成互斥的自然类别。PDDL 与 Python 世界模型都讨论转移、反馈和规划；两者的接口与建模假设用于比较。

场景和资产程序连接程序化世界构建。静态重建可以压缩为 enabling representations；关节、动态或仿真行为则按实际证据接入执行机制。这样保留程序几何的来源，同时将正文重心放在世界模型问题上。

## 五个值得建立的图表

1. **运行示例和总览图。** 同一个动作经过程序转移、状态编译和观测渲染，并展示 GUI 代码预测的对应路径。
2. **语义—生命周期矩阵。** 每篇方法的 task role、code responsibility、program origin、state status、feedback 和 use。
3. **获取与修订比较表。** 候选如何提出、反例怎样得到、全局重写或局部修补、怎样保留旧行为、模型如何进入 planner。
4. **历史时间线。** Game Engine Learning from Video → EMPA → AutumnSynth / LLM-to-PDDL → LLM Python 模型 → 持久世界和执行—视觉耦合。会议年份与预印本年份分别记录。
5. **评测证据地图。** program acquisition → transition fidelity → state consistency → observation alignment → closed-loop utility，并标明每个 benchmark 覆盖的接口。

## 文献比较的写法

每段围绕一个共同问题，比较设计差异，再解释它支持的能力与成立条件。例如，WorldCoder、GIF-MCTS 和 PatchWorld 可比较候选搜索、反例来源、模型更新方式与 planner 接口；GUI 三篇可比较输出粒度、训练反馈与结构复用，再接入分布变化、状态别名和多步一致性的证据。

正文重点解释程序职责如何创造新能力。共同定义和评价条件集中在范围章节及比较表中；与某个结论直接相关的实验条件放在对应论证处。这样综述形成清晰的学术叙事，同时让读者能够核对每项判断。

## 邻域定位

相邻综述通常按生成模态、3D 场景任务或 code intelligence 架构组织。本稿可以用程序职责、状态所有权、程序获取、执行验证和下游价值建立自己的分析视角。独特性应由分类框架及跨路线比较体现。

文献库是持续扩充的研究基础。下一轮写正文时，以选定章节的问题筛选详述论文，并把实验证据矩阵补到具体版本、split、预算和指标；每条性能结论都关联它所依赖的配置。
