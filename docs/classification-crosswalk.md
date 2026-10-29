# Paper-by-paper classification / 逐篇分类对照

<!-- Generated from data/classification.json and data/papers.json. -->

**Discussion draft / 讨论稿 · 2026-10-29**

[Definitions / 两套定义](classification-guide.md) · [Writing plan / 写作安排](survey-outline.md) · [CSV](../data/classification.csv) · [JSON](../data/classification.json)

**124 source records**; **20** appear explicitly in the manuscript classification figure. Source records are not unique-method counts.

- **原图** transcribes Figure 1; **—** means not listed in that figure, not absent from the full manuscript.
- **旧体系建议** applies the manuscript families to the broader corpus. Empty entries are deliberate scope/fit decisions.
- **S / E / O** = world specification / world evolution / predicted observation code. The primary role is bold. Supporting and evaluation roles are explicitly prefixed.
- **†** marks a provisional placement. All assignments, including unmarked ones, remain editorial proposals.
- Writing anchors follow the retained lifecycle chapters. Execution providers, renderers, secondary chapters, and evidence URLs are available in CSV/JSON.
- Existing records retain their prior review depth; this classification pass is not a fresh full-paper audit of every source.

## World evolution methods / 世界演化方法 (37)

| Work / 工作 | 原图 | 旧体系建议 | 程序职责 | 依据 / 来源 | 主讲位置 | 分类与写作说明 |
|---|---|---|---|---|---|---|
| [WorldCoder](https://arxiv.org/abs/2402.12275) | A1 | A1, A3 | **E** | 交互轨迹 | §4.1 | 从交互证据获取可执行转移，比较候选搜索与反馈机制；A3 是跨方法流程。 |
| [GIF-MCTS](https://arxiv.org/abs/2405.15383) | A1 | A1, A3 | **E** | 交互轨迹 | §4.1 | 从交互证据获取可执行转移，比较候选搜索与反馈机制；A3 是跨方法流程。 |
| [Generating Symbolic World Models via Test-time Scaling of Large Language Models](https://arxiv.org/abs/2502.04728) | — | A1, A3 | **E** | 目标域描述与反馈 | §4.1 | 符号规划域与 Python 转移模型按同一职责比较。 |
| [FAE](https://arxiv.org/abs/2508.11836) | — | A1 | **E** | 游戏视频的精灵网格表示 | §4.1 | 从游戏视频恢复行为程序；视觉输入不是物理机制发现 A4 的充分条件。 |
| [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | — | A1 | **E** | 自然语言游戏规则与轨迹 | §4.1 | 已有游戏的规则是建模证据；不要与 OneLife 合并成同一篇。 |
| [Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback](https://arxiv.org/abs/2512.22336) | — | A1, A3 | **E** | 目标域描述与反馈 | §4.1 | 符号规划域与 Python 转移模型按同一职责比较。 |
| [Executable World Models for ARC-AGI-3 in the Era of Coding Agents](https://arxiv.org/abs/2605.05138) | — | A1, A3 | **E** | 在线交互轨迹 | §4.1 | 通过历史回放、简化与规划，构建 ARC-AGI-3 的可执行世界模型。 |
| [Alice / Baba in Wonderland](https://arxiv.org/abs/2605.16725) | — | A1, A3 | **E** | 在线交互轨迹 | §4.1 | Alice 在词汇先验错配下学习可执行动力学，以旧行为保持冲突指导假设修订与探索。 |
| [OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3](https://arxiv.org/abs/2607.01531) | — | A1, A3 | **E** † | 交互与主动探索 | §4.1 | OPINE-World 通过错误优先探索，联合修订符号本体、转移假设与目标。 |
| [Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3](https://arxiv.org/abs/2607.28287) | — | A1, A3 | **E** † | 交互与主动探索 | §4.1 | Tycho 在求解 ARC-AGI-3 游戏时，主动修订抽象与程序化假设。 |
| [A Declared World Model](https://www.preprints.org/manuscript/202610.1139) | — | A1 | **E** | 带标签场景图 | §4.1 | 受控感知与布局迁移实验；不扩大为任意视觉世界重建。 |
| [TheoryCoder](https://arxiv.org/abs/2503.20124) | A1 | A1, A2 | **E** | 交互证据 | §4.2 | 层次抽象与可执行转移共同支持规划。 |
| [PoE-World: Compositional World Modeling with Products of Programmatic Experts](https://arxiv.org/abs/2505.10819) | A2 | A2 | **E** | 轨迹与规则证据 | §4.2 | 比较专家组合、条件机制与角色抽象；三者不等同于同一种模块化。 |
| [OneLife](https://arxiv.org/abs/2510.12088) | A2 | A2 | **E** | 轨迹与规则证据 | §4.2 | 比较专家组合、条件机制与角色抽象；三者不等同于同一种模块化。 |
| [TheoryCoder-2](https://arxiv.org/abs/2602.00929) | — | A1, A2 | **E** | 交互证据 | §4.2 | 层次抽象与可执行转移共同支持规划。 |
| [RoleWorld](https://arxiv.org/abs/2610.13172) | A2 | A2 | **E** | 轨迹与规则证据 | §4.2 | 比较专家组合、条件机制与角色抽象；三者不等同于同一种模块化。 |
| [Write Once, Plan Many](https://arxiv.org/abs/2610.19234) | — | A1, B1 | S + **E** † | 给定领域规则与单个练习场景 | §4.4 | 规则已给定；旧体系 A1/B1 的归属依建模目标，不能写成未知规则发现。 |
| [WildAWM](https://arxiv.org/abs/2610.26828) | — | B1 | S + **E** | 计算机环境与任务规格 | §4.4 | 合成环境与验证器用于训练；不表述为识别现实软件的未知动力学。 |
| [Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games](https://arxiv.org/abs/2606.16070) | — | A1, A3 | **E** | 交互历史 | §5.1 | Mind-Studio 为部分可观测游戏构建可执行模型，并评价同状态起点的多步前瞻保真度。 |
| [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/abs/2607.25236) | — | A1, A3 | **E** | 结构化轨迹与视觉状态 | §5.1 | 结构化轨迹拟合动力学，视觉场景图支持重规划；不表述为纯 RGB 机制归纳。 |
| [Twin: Playing an Unknown Game with a Test-Time Digital Twin](https://arxiv.org/abs/2608.14490) | — | A1, A3 | **E** | 交互历史 | §5.1 | Twin 在测试时构建数字孪生，并在未知游戏中选择动作前检查历史转移。 |
| [EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning](https://arxiv.org/abs/2609.35047) | A4 | A4, A3 | **E** | 主动实验与物理反馈 | §5.2 | 核心新增物是缺失的力、约束与隐藏状态机制；几何和对象特征已给定。 |
| [Web World Models](https://arxiv.org/abs/2512.23676) | — | B1 | S + **E** | 构建规格 | §5.3 | 构造世界把保存状态作为后续执行依据，与外部世界的状态估计区分。 |
| [Code World Model: Coding Agent as World Brain](https://arxiv.org/abs/2608.25927) | C1 | B1, C1 | S + **E** | 构建规格 | §5.3 | 程序决定状态演化，视频模型实现观测；O 专指预测观测代码。 |
| [Programmable World Model](https://arxiv.org/abs/2609.10540) | B1, C1 | B1, C1 | S + **E** | 构建规格 | §5.3 | 程序决定状态演化，视频模型实现观测；O 专指预测观测代码。 |
| [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652) | C1 | B1, C1 | **E** | 用户规则与视觉状态 | §5.3 | GameDirector 利用视觉情境估计和显式玩法规则，控制游戏视频生成。 |
| [CoDeR](https://arxiv.org/abs/2609.26458) | B1, C1 | B1, C1 | S + **E** | 构建规格 | §5.3 | 程序决定状态演化，视频模型实现观测；O 专指预测观测代码。 |
| [Oneira](https://arxiv.org/abs/2610.01614) | — | B1, C1 | **E** | 用户目标 + 持续视觉观测 | §5.3 | 新对象从生成观测进入状态表；粗状态更新由 agent/引擎实现，细节运动由视频模型补全。 |
| [Mallea](https://arxiv.org/abs/2610.21283) | C1 | B1, C1 | S + **E** | 文本规格与用户编辑 | §5.3 | 构建、状态推进、编辑与记忆同属一系统，主讲对象级持久演化。 |
| [State World Models](https://arxiv.org/abs/2610.26811) | — | B1, C1 | S + **E** | 游戏规格 + 受规则约束的视觉反馈 | §5.3 | 先提交语义与空间更新，再渲染并接收兼容反馈。 |
| [Matrix-Game 4.0](https://arxiv.org/abs/2610.27999) | — | B1, C1 | S + **E** | 玩家游戏需求 | §5.3 | 编码智能体把玩家要求写成游戏代码与规则；引擎维护持久状态，因果视频模型根据低模画面生成细节视图。 |
| [Magpie: Real-Time World Renderer for Interactive Games](https://arxiv.org/abs/2608.27168) | — | C1 | **E** | 已给定/构造的引擎世界 | §6.3 | E 属于组合系统中的上游引擎；神经渲染贡献不等于学习转移规则。 |
| [AgentGarten: Code Worlds for Evolving Agents](https://arxiv.org/abs/2610.12374) | C1 | C1 | **E** | 已给定/构造的引擎世界 | §6.3 | E 属于组合系统中的上游引擎；神经渲染贡献不等于学习转移规则。 |
| [PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments](https://arxiv.org/abs/2605.30880) | A3 | A3, A1 | **E** | 轨迹与回放反馈 | §7.1 | 以模型修正与历史回放为主讲位置；维护的模型状态不自动等于真实状态。 |
| [Kepler: Auditable World Models for ARC-AGI-3](https://arxiv.org/abs/2610.00834) | — | A3, A1 | **E** | 轨迹与回放反馈 | §7.1 | 以模型修正与历史回放为主讲位置；维护的模型状态不自动等于真实状态。 |
| [Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks](https://arxiv.org/abs/2610.11794) | A3 | A3, A1 | **E** | 轨迹与回放反馈 | §7.1 | 以模型修正与历史回放为主讲位置；维护的模型状态不自动等于真实状态。 |
| [World-Time Compute with Verified Code World Models](https://arxiv.org/abs/2609.09163) | — | B1 | S + **E** | 构造规格与验证 | §8.2 | 世界构建服务训练轨迹与标签生成；模型使用价值另行验证。 |

## World specification methods / 世界定义与构建方法 (10)

| Work / 工作 | 原图 | 旧体系建议 | 程序职责 | 依据 / 来源 | 主讲位置 | 分类与写作说明 |
|---|---|---|---|---|---|---|
| [VibeWorlding](https://arxiv.org/abs/2608.15265) | — | — | **S** | 文本/视觉意图与场景构建要求 | §3.2 | VibeWorlding 是新增的 VibeWorlding-type 代表：重点是 coding agent 端到端构建和编辑开放式 3D 世界。它提供构建/编辑证据，不应直接计作未知时间动力学发现。 |
| [Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning](https://arxiv.org/abs/2608.27549) | A4 | A4, B2 | **S** + E | 视觉证据或文本规格（依设定） | §4.3 | 按实验设定区分归纳与构造，不能把整篇永久限定为 A4。 |
| [NeoWorld-3](https://arxiv.org/abs/2610.27690) | — | B2 | **S** † | 视觉证据与参数拟合 | §4.3 | 旧 B2 是任务形态近邻，来源是视觉证据；不声称发现未知物理定律。 |
| [Mundo](https://mundo-world-model.github.io/) | — | B2, C1 | **S** + E † | 图像重建与模拟规格 | §4.3 | 按作者项目资料收录；图像代理与仿真条件是主线，独立论文未核实。 |
| [Code2Worlds: Empowering Coding LLMs for 4D World Generation](https://arxiv.org/abs/2602.11757) | — | B1, B2 | **S** + E | 文本规格 | §4.4 | 动态视觉内容与可由接触求解器推进的世界是不同证据层级。 |
| [ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction](https://arxiv.org/abs/2605.14398) | — | B2 | **S** + E | 物理仿真规格与反馈 | §4.4 | ChronoAgentic 结合规划、编码、视觉审阅与轨迹检查，构建 PyChrono 仿真程序。 |
| [SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects](https://arxiv.org/abs/2605.19587) | — | B1, B2 | **S** | 场景规格与反馈 | §4.4 | SceneCode 构建可编辑的室内世界程序，包含关节物体、仿真导出与持久场景组织。 |
| [WorldStream](https://arxiv.org/abs/2610.28827) | — | B1 | **S** | 流式世界规格 | §4.4 | 生成的是类型化规格；固定 runtime 的演化/编辑逻辑单独记录。 |
| [Code2Worlds-2](https://arxiv.org/abs/2610.17651) | B2 | B2 | **S** | 场景规格与仿真反馈 | §5.2 | 主要生成碰撞/质量/关节等可执行规格；基础物理演化继承自引擎。 |
| [LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica](https://arxiv.org/abs/2610.25019) | — | A4, B2 | **S** + E | 描述与观测数据 | §5.2 | 组合、校准可执行物理模型；规格与证据两种来源并存。 |

## Observation-code methods / 观测代码方法 (3)

| Work / 工作 | 原图 | 旧体系建议 | 程序职责 | 依据 / 来源 | 主讲位置 | 分类与写作说明 |
|---|---|---|---|---|---|---|
| [gWorld](https://arxiv.org/abs/2602.01576) | C2 | C2 | **O** | GUI 轨迹 | §6.1 | 完整代码或增量代码表达下一步可见观测；转移预测仍由学习模型承担。 |
| [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856) | C2 | C2 | **O** | GUI 轨迹 | §6.1 | 完整代码或增量代码表达下一步可见观测；转移预测仍由学习模型承担。 |
| [AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents](https://arxiv.org/abs/2608.05891) | C2 | C2 | **O** | GUI 轨迹 | §6.1 | 完整代码或增量代码表达下一步可见观测；转移预测仍由学习模型承担。 |

## Benchmarks and resources / 评测与资源 (20)

| Work / 工作 | 原图 | 旧体系建议 | 程序职责 | 依据 / 来源 | 主讲位置 | 分类与写作说明 |
|---|---|---|---|---|---|---|
| [3DCodeVerse](https://arxiv.org/abs/2610.22341) | — | — | 支撑 **S** | 执行程序数据与验证记录 | §3.2 | 程序化 3D 数据资源，区分数据覆盖与交互世界模型方法。 |
| [RoboSimStudio](https://arxiv.org/abs/2610.18835) | — | B2 | 支撑 **S** | 观测校准与人工/agent 设置 | §5.2 | 仿真配置与校准工具；未证明生成新的求解/转移算法。 |
| [StreamRender-H3](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/) | — | C1 | 支撑 S + **E** | 示例游戏与引擎规则 | §6.3 | S/E 指页面明确包含的上游游戏；renderer 单独没有转移责任。 |
| [Text2World: Benchmarking Large Language Models for Symbolic World Model Generation](https://arxiv.org/abs/2502.13092) | — | A1, B1 | 评测 **E** | 评测协议 | §8.1 | 评测目标是可执行符号世界模型，角色不代表 benchmark 自己学习了机制。 |
| [WorldModelBench: Judging Video Generation Models As World Models](https://arxiv.org/abs/2502.20694) | — | — | — | 评测协议 | §8.1 | 跨表示评测支撑，不强行赋予程序职责。 |
| [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014) | — | — | — | 评测协议 | §8.1 | 跨表示评测支撑，不强行赋予程序职责。 |
| [WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis](https://arxiv.org/abs/2606.01869) | — | A4, B2 | 评测 **S** + E | 评测协议 | §8.1 | WorldCoder-Bench 通过隐藏的运行时行为合同，评价具有物理依据的三维世界构建。 |
| [ScratchWorld: Evaluating If World Models Compute Executable Consequences](https://arxiv.org/abs/2606.31689) | — | — | — | 评测协议 | §8.1 | 跨表示评测支撑，不强行赋予程序职责。 |
| [GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments](https://arxiv.org/abs/2609.00048) | — | C2 | 评测 **O** | 评测协议 | §8.1 | O 是相关被评测分支；协议也可比较其他表示。 |
| [GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions](https://arxiv.org/abs/2609.21562) | — | B1 | 评测 **E** | 评测协议 | §8.1 | GameLogicBench 在多种可复现情景下，以逐仿真 tick 的状态检查验证 Godot 游戏规则。 |
| [StateAliasBench](https://arxiv.org/abs/2609.32679) | — | C2 | 评测 **O** | 评测协议 | §8.1 | O 是相关被评测分支；协议也可比较其他表示。 |
| [PROWBench: Do Video Models Render What the Program Specifies?](https://arxiv.org/abs/2610.02205) | — | C1 | 评测 **E** | 评测协议 | §8.1 | 评测 E 到观测的遵循；O 不指所有被评测视频。 |
| [Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos](https://arxiv.org/abs/2610.04432) | — | A4, B2 | 评测 **S** + E | 评测协议 | §8.1 | Video2World 从几何、动力学和功能三个方面，评价具身视频到交互世界的重建。 |
| [ExeWorldBench](https://arxiv.org/abs/2610.15166) | — | A4, B2 | 评测 **S** + E | 评测协议 | §8.1 | 由机制执行、组合执行到意图驱动世界合成；评测目标跨 S/E。 |
| [WorldOracle](https://arxiv.org/abs/2610.18826) | — | — | — | 评测协议 | §8.1 | 机制/后果/事件诊断支撑，不据此认定被评测模型采用可执行程序。 |
| [BlenderWorld](https://arxiv.org/abs/2610.23986) | — | — | 评测 **S** | 评测协议：视觉参考与构建规格 | §8.1 | 3D 创建评测，部分 agent 使用 UI；不自动构成动态机制评测。 |
| [GlobeBench](https://arxiv.org/abs/2610.22708) | — | — | — | 评测协议 | §8.1 | 机制/后果/事件诊断支撑，不据此认定被评测模型采用可执行程序。 |
| [Code2Video-Compass](https://arxiv.org/abs/2610.28416) | — | — | 评测 **S** | 评测协议：T2V/I2V/V2V | §8.1 | S 仅作相邻程序化视觉构建的评测标签；不是动作条件的持久世界转移评测。 |
| [Events, Not Pixels](https://arxiv.org/abs/2610.29435) | — | — | — | 评测协议 | §8.1 | 机制/后果/事件诊断支撑，不据此认定被评测模型采用可执行程序。 |
| [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/abs/2605.19769) | — | — | 支撑 **E** | 真实可执行软件资源 | §8.2 | 环境资源中的执行责任，不是学习得到的世界模型。 |

## Enabling representations and renderers / 支撑表示与渲染 (18)

| Work / 工作 | 原图 | 旧体系建议 | 程序职责 | 依据 / 来源 | 主讲位置 | 分类与写作说明 |
|---|---|---|---|---|---|---|
| [Procedural content generation for games](https://doi.org/10.1145/2422956.2422957) | — | — | — | 历史/表示背景 | §2 | 背景来源；不强行纳入某个世界模型 family。 |
| [CSGNet: Neural Shape Parser for Constructive Solid Geometry](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html) | — | — | 支撑 **S** | 形状证据或过程生成规则 | §2 | 几何程序表示的历史基础。 |
| [DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning](https://arxiv.org/abs/2006.08381) | — | — | — | 历史/表示背景 | §2 | 背景来源；不强行纳入某个世界模型 family。 |
| [ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis](https://arxiv.org/abs/2009.08026) | — | — | 支撑 **S** | 形状证据或过程生成规则 | §2 | 几何程序表示的历史基础。 |
| [Infinigen](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html) | — | — | 支撑 **S** | 形状证据或过程生成规则 | §2 | 几何程序表示的历史基础。 |
| [Holodeck: Language Guided Generation of 3D Embodied AI Environments](https://arxiv.org/abs/2312.09067) | — | — | 支撑 **S** | 场景/布局规格 | §3.2 | S 表示支撑的场景结构；静态或功能布局证据不自动建立完整世界动力学。 |
| [Open-Universe Indoor Scene Generation using LLM Program Synthesis and Uncurated Object Databases](https://arxiv.org/abs/2403.09675) | — | — | 支撑 **S** | 场景/布局规格 | §3.2 | S 表示支撑的场景结构；静态或功能布局证据不自动建立完整世界动力学。 |
| [SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code](https://arxiv.org/abs/2403.01248) | — | — | 支撑 **S** | 场景/布局规格 | §3.2 | S 表示支撑的场景结构；静态或功能布局证据不自动建立完整世界动力学。 |
| [SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements](https://arxiv.org/abs/2408.02211) | — | — | 支撑 **S** | 视觉重建证据 | §3.2 | 静态程序重建作为表示支撑；旧 A4 不能直接代表所有视觉重建。 |
| [Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation](https://arxiv.org/abs/2504.05482) | — | — | 支撑 **S** | 场景/布局规格 | §3.2 | S 表示支撑的场景结构；静态或功能布局证据不自动建立完整世界动力学。 |
| [Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search](https://arxiv.org/abs/2510.16147) | — | — | 支撑 **S** | 场景/布局规格 | §3.2 | S 表示支撑的场景结构；静态或功能布局证据不自动建立完整世界动力学。 |
| [WorldClaw: Agentic 3D Open-World Generation at Scale](https://arxiv.org/abs/2608.05248) | — | — | 支撑 **S** | 场景/布局规格 | §3.2 | S 表示支撑的场景结构；静态或功能布局证据不自动建立完整世界动力学。 |
| [FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation](https://arxiv.org/abs/2608.29519) | — | — | 支撑 **S** | 场景/布局规格 | §3.2 | S 表示支撑的场景结构；静态或功能布局证据不自动建立完整世界动力学。 |
| [Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs](https://arxiv.org/abs/2609.11499) | — | — | 支撑 **S** | 视觉重建证据 | §3.2 | 静态程序重建作为表示支撑；旧 A4 不能直接代表所有视觉重建。 |
| [LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380) | — | — | 支撑 **S** | 视觉重建证据 | §3.2 | 静态程序重建作为表示支撑；旧 A4 不能直接代表所有视觉重建。 |
| [USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation](https://arxiv.org/abs/2610.11322) | — | — | 支撑 **S** | 给定几何与关节建模要求 | §3.2 | 源几何是输入，生成建模程序和关节资产；不要混作从零发现物理规律。 |
| [SolarRenderer](https://arxiv.org/abs/2610.28630) | — | C1 | — | 上游结构/参考视频 | §6.3 | C1 的接口支撑；renderer 本身不获得 E，也不是预测观测代码 O。 |
| [EdenLive](https://github.com/VAST-AI-Research/EdenLive) | — | C1 | — | 上游结构/参考视频 | §6.3 | C1 的接口支撑；renderer 本身不获得 E，也不是预测观测代码 O。 |

## History, comparisons and context / 历史、对照与背景 (36)

| Work / 工作 | 原图 | 旧体系建议 | 程序职责 | 依据 / 来源 | 主讲位置 | 分类与写作说明 |
|---|---|---|---|---|---|---|
| [Game Engine Learning from Video](https://www.ijcai.org/proceedings/2017/518) | — | A1, A2 | **E** | 视频或交互证据 | §2 | 作为机制归纳历史，不纳入近期新方法数量。 |
| [EMPA](https://arxiv.org/abs/2107.12544) | — | A1, A2 | **E** | 视频或交互证据 | §2 | 作为机制归纳历史，不纳入近期新方法数量。 |
| [AutumnSynth](https://doi.org/10.1145/3571249) | — | A1, A2 | **E** | 视频或交互证据 | §2 | 作为机制归纳历史，不纳入近期新方法数量。 |
| [Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning](https://arxiv.org/abs/2305.14909) | — | A1 | **E** | 目标域描述与反馈 | §2 | LLM-to-PDDL 的历史衔接。 |
| [3D and 4D World Modeling: A Survey](https://arxiv.org/abs/2509.07996) | — | — | — | 相邻综述 | §2 | 背景与范围定位。 |
| [CWM: An Open-Weights LLM for Research on Code Generation with World Models](https://arxiv.org/abs/2510.02387) | — | — | — | 代码执行/软件后果数据 | §2 | world model of code 的相邻方向，与外部世界 as code 区分。 |
| [Beyond the Autoregressive Horizon: A Comprehensive Survey of Diffusion Models, World Modelling, and State Space Models for Code](https://arxiv.org/abs/2606.23690) | — | — | — | 相邻综述 | §2 | 背景与范围定位。 |
| [3D Scene Generation: A Survey](https://doi.org/10.1007/s11263-026-02999-6) | — | — | — | 相邻综述 | §2 | 背景与范围定位。 |
| [Agent-Editing World Model: Rethinking World Modeling for LLM Agents](https://arxiv.org/abs/2609.28416) | — | — | — † | agent 编辑与任务上下文 | §2 | 相邻的 agent-editing 定义，不自动视为环境状态转移程序。 |
| [Software World Models: From Consequence Prediction to Decision Value](https://arxiv.org/abs/2610.04940) | — | — | — | 代码执行/软件后果数据 | §2 | world model of code 的相邻方向，与外部世界 as code 区分。 |
| [PDSketch: Integrated Planning Domain Programming and Learning](https://arxiv.org/abs/2303.05501) | — | A2 | 对照 **E** | 给定规划结构 + 学习组件 | §3.1 | 明确继承的结构与学习的部分。 |
| [VisualPredicator: Learning Abstract World Models with Neuro-Symbolic Predicates for Robot Planning](https://arxiv.org/abs/2410.23156) | — | — | — † | 视觉与任务证据 | §3.1 | 保留为谓词/抽象对照；未据现有摘要断言生成转移代码。 |
| [CGWM](https://arxiv.org/abs/2610.19955) | — | — | 对照 **E** | 给定完整时序逻辑规则 | §3.1 | 显式规则是给定的，学习目标是视觉落地；A 族的归纳定义不直接适用。 |
| [SceneRig](https://arxiv.org/abs/2610.28585) | — | — | 对照 **S** | 单图证据与仿真检查 | §3.2 | 物理稳定配置恢复；当前对象按单刚体处理，不扩展为一般动态机制发现。 |
| [Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation](https://arxiv.org/abs/2607.17540) | — | A4 | 对照 **E** † | 仿真/实验观测 | §4.3 | 将 LLM 生成的仿真器族与神经仿真推断结合，用于机制选择和参数估计。 |
| [LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models](https://arxiv.org/abs/2610.11253) | — | A4 | 对照 **E** † | 仿真/实验观测 | §4.3 | LLM-IDEA 通过考虑可辨识性的实验设计，区分不同机制解释。 |
| [Self-Building Labs](https://arxiv.org/abs/2610.23826) | — | B2 | 对照 **S** † | 科学目标、照片、设备与物理反馈 | §4.4 | 生成场景与生成机器人技能分别描述；技能代码不是世界转移代码。 |
| [DR-WM](https://arxiv.org/abs/2610.17630) | — | A4, C1 | 对照 **S** † | RGB 重建与动作响应校准 | §5.2 | 物理配置指导生成；不将模拟器演化等同于新合成的转移定律。 |
| [StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation](https://arxiv.org/abs/2607.26754) | — | — | — | 数据学习 | §5.3 | 显式或权威共享状态不等于显式可执行转移程序。 |
| [MASS: Multiplayer World Models with Authoritative Shared State](https://arxiv.org/abs/2608.06257) | — | — | — | 数据学习 | §5.3 | 显式或权威共享状态不等于显式可执行转移程序。 |
| [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [WebDreamer](https://arxiv.org/abs/2411.06559) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [ViMo: A Generative Visual GUI World Model for App Agents](https://arxiv.org/abs/2504.13936) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [Computer-Using World Model](https://arxiv.org/abs/2602.17365) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [Simulate to Generalize: Scaling Stateful Supervision for API-calling Agents using LLM World Models](https://arxiv.org/abs/2607.16900) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [Learning Simple Test-Time Environments for LLM Web Agents](https://arxiv.org/abs/2608.29305) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [AutoGUIWorld: Image Generators as Visual World Models for GUI Agent](https://arxiv.org/abs/2610.01215) | — | — | — † | 环境轨迹或任务上下文 | §6.1 | 其他观测/环境预测表示；没有依据把生成画面或动作推理标成 O/E。 |
| [ATAS](https://arxiv.org/abs/2610.20571) | — | — | — | 生成/控制任务 | §6.3 | 代码承担生成编排或技能控制；未据此建立显式世界转移模型。 |
| [AW-0](https://arxiv.org/abs/2610.30136) | — | — | — | 生成/控制任务 | §6.3 | 代码承担生成编排或技能控制；未据此建立显式世界转移模型。 |
| [WebWorld: The Browser as a World Model for Self-Improving Web Code](https://arxiv.org/abs/2608.30530) | — | B1 | 对照 S + **E** | Web 规格与交互反馈 | §7.1 | 自改进 Web 程序的交互契约作为相邻维护案例。 |
| [How Mobile World Model Guides GUI Agents?](https://arxiv.org/abs/2605.10347) | — | C2 | 对照 **O** | 受控比较 | §8.2 | O 指比较中的代码分支，不给全部变体赋予同一表示。 |
| [Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?](https://arxiv.org/abs/2607.15439) | — | A1, A3 | 对照 **E** | 受控比较 | §8.2 | 各比较版本均有 shell/Python；检验模型纪律与组合验证，而非有无工具。 |
| [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885) | — | — | — | 评测/决策比较 | §8.2 | 比较预测对动作选择与验证的价值。 |
| [Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://arxiv.org/abs/2610.11942) | — | — | — | 评测/决策比较 | §8.2 | 比较预测对动作选择与验证的价值。 |
| [Beyond Next-Screen](https://arxiv.org/abs/2610.24372) | — | — | — | 受控决策比较 | §8.2 | 比较前瞻预测相对动作排序的决策增益。 |
