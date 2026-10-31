<div align="center">

# Code-Centric World Models

**可执行动力学 · 持久世界 · 可渲染观测**

持续维护的文献集合，以及正在撰写的综述的配套主页。

[English](README.md) | **简体中文**

<!-- BADGES:BEGIN -->

[![Source records](assets/badges/sources.svg)](#paper-collection) [![Reading sections](assets/badges/topics.svg)](#contents) [![Literature cutoff](assets/badges/cutoff.svg)](docs/review-protocol.md) [![Contributions welcome](assets/badges/contributions.svg)](CONTRIBUTING.md)

![Survey arXiv](assets/badges/survey-arxiv.svg) ![Survey Semantic Scholar citations](assets/badges/survey-citations.svg)

<!-- BADGES:END -->

[📝 综述入口](docs/survey.md) · [📚 文献目录](#paper-collection) · [🧭 分类框架](docs/taxonomy.md) · [📖 BibTeX](papers.bib) · [🤝 参与贡献](CONTRIBUTING.md)

<p><img src="./assets/banner.png" alt="以程序构建可执行世界：代码、持久状态与渲染观测" width="1280"></p>

</div>

<a id="motivation"></a>
## 💡 研究动机：为什么是代码，为什么是现在？

随着编码智能体在**生成、执行和迭代改进复杂程序**方面的能力不断增强，代码正成为世界建模的一种有前景的表示方式。

除了预测像素，以代码为核心的世界模型还支持**显式动力学、持久状态与可编程交互**，为构建更**可控、可编辑、可验证的世界**提供了一条互补路径。

> [!NOTE]
> **📝 我们正在撰写以代码为核心的世界模型综述。** 当前大纲、概念框架与文献资料见[综述入口](docs/survey.md)。
>
> **🤝 欢迎提交 PR！** 无论是补充遗漏论文、修正文献信息、完善分类框架，还是改进综述讨论，都欢迎参与。请先阅读[贡献指南](CONTRIBUTING.md)。

<a id="news"></a>
## 更新

- **2026-10-31** — 根据 10 月 13–29 日检索新增 21 条记录，补充可执行动力学、持久世界引擎、可编辑 3D 构建与运行时评测。严格范围仍由三类主线定义，支撑来源保留在未归类总表中。
- **2026-10-30** — 继续补充三类主线归类；评测、综述和明显相邻来源保留在总表但不强行归类。仓库目录现在只有三个 section。
- **2026-10-29** — 加入 VibeWorlding，整理覆盖 124 条记录的全量论文总表，并将 README 主分类收敛为 WorldCoder-type、Code-as-World-type、VibeWorlding-type 三类。封面改为代码—状态—数字世界主题的栅格图。
- **2026-10-26** — 补入 31 条核实来源，形成当前文献目录基础。
- **2026-10-19** — 加入中英双语 README、PNG 封面、综述标签占位与分类导航。
- **2026-10-14** — 初始版本收录 92 条文献记录，提供结构化元数据、BibTeX、分类框架与评测框架。

<a id="contents"></a>
## 导航

[研究动机](#motivation) · [综述与资源](#survey--resources) · [核心视角](#at-a-glance) · [文献目录](#paper-collection) · [参与贡献](#contributing) · [致谢](#acknowledgements)

**写作讨论：** [三类框架](docs/coarse-taxonomy.md) · [全量论文总表](docs/paper-master-list.md) · [分类 JSON](data/classification.json) · [本轮更新](docs/updates/2026-10-31.md)

<!-- NAVIGATION:BEGIN -->

| 三类主线 |
|---|
| [01 · WorldCoder-type · 程序化动力学](#papers-worldcoder) <sub>(33)</sub> |
| [02 · Code-as-World-type · 可执行世界程序](#papers-code_as_world) <sub>(32)</sub> |
| [03 · VibeWorlding-type · agentic 3D 世界构建](#papers-vibeworlding) <sub>(26)</sub> |
| [全量论文总表](docs/paper-master-list.md)（含未归类来源） |

<!-- NAVIGATION:END -->

<a id="survey--resources"></a>
## 综述与资源

综述**正在撰写**。[综述入口](docs/survey.md) 集中提供当前大纲、概念框架与文献资料；正式发布后，论文与配套材料也将在这里更新。顶部的 arXiv 与 Semantic Scholar Citations 标签目前预留为空。

| 研究与浏览 | 写作与贡献 |
|---|---|
| [**分类与范围**](docs/taxonomy.md) — 代码的语义职责 | [**中文综述大纲**](docs/survey-outline.md) — 研究问题与章节组织 |
| [**评测框架**](docs/evaluation.md) — 从运行正确性到 agent 使用价值 | [**BibTeX 文献库**](papers.bib) — 稳定的引用键 |
| [**详细核查表**](docs/catalogue.md) — 日期、定位、核查深度与证据说明 | [**结构化数据**](data/papers.json) — 原始来源与机制标签 |

论文标题和方法名保留原文，本页提供中文机制摘要。README 首页只采用三类主线；评测框架及详细核查文档以英文为主。

<a id="at-a-glance"></a>
## 核心视角

| 代码承载的语义 | 支持的能力 | 代表工作 |
|---|---|---|
| **转移与机制** | 执行规则、预测后果与规划 | [WorldCoder](https://arxiv.org/abs/2402.12275)、[OneLife](https://arxiv.org/abs/2510.12088)、[General Game Playing](https://arxiv.org/abs/2510.04542) |
| **观测与外观** | 以可渲染代码预测界面或场景 | [gWorld](https://arxiv.org/abs/2602.01576)、[Code2World](https://arxiv.org/abs/2602.09856)、[AppDeltaWorld](https://arxiv.org/abs/2608.05891) |
| **执行与观测的耦合** | 维护世界状态，并连接到视觉输出 | [Web World Models](https://arxiv.org/abs/2512.23676)、[Programmable World Model](https://arxiv.org/abs/2609.10540)、[Magpie](https://arxiv.org/abs/2608.27168) |

程序来源、验证过程与下游用途构成另一组属性。[分类框架](docs/taxonomy.md) 解释这些属性如何贯通不同研究路线。

### 三类写作主线（初版）

| 初版主类 | 核心问题 | 代表工作 |
|---|---|---|
| **WorldCoder-type** · 程序化动力学 | 代码能否预测动作后果并支持规划？ | [WorldCoder](https://arxiv.org/abs/2402.12275)、[TheoryCoder](https://arxiv.org/abs/2503.20124)、[OneLife](https://arxiv.org/abs/2510.12088)、[Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) |
| **Code-as-World-type** · 可执行世界程序 | 代码能否持续维护世界、状态、规则及其接口？ | [Code as Worlds](https://arxiv.org/abs/2608.27549)、[Programmable World Model](https://arxiv.org/abs/2609.10540)、[AgentGarten](https://arxiv.org/abs/2610.12374)、[Oneira](https://arxiv.org/abs/2610.01614) |
| **VibeWorlding-type** · agentic 3D 世界构建 | agent 能否构建并编辑可编辑、可仿真的 3D 世界？ | [VibeWorlding](https://arxiv.org/abs/2608.15265)、[WorldClaw](https://arxiv.org/abs/2608.05248)、[USDCraft](https://arxiv.org/abs/2610.11322)、[SceneRig](https://arxiv.org/abs/2610.28585) |

[三类框架说明](docs/coarse-taxonomy.md) 给出具体判据。小型、评测、GUI、历史和相邻来源保留在[全量总表](docs/paper-master-list.md)，不强行归入三条主线。

<a id="paper-collection"></a>
## 文献目录

<!-- CATALOG:BEGIN -->

**145 条文献来源** · 文献截止日期：**2026-10-29**。

README 只按三类主线浏览；未归类的小型、评测与相邻来源保留在[全量论文总表](docs/paper-master-list.md)。

各主类按记录日期倒序排列；完整核查、证据和未归类来源见注释表。

<a id="papers-worldcoder"></a>
### 01 · WorldCoder-type · 程序化动力学

*可执行转移机制、世界程序归纳、规划与模型修复。*

- **Algebraic World Model: From Exploration to Proofs** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.40503)
  <br><sub>通过可执行 Python 假设、类型化规则和 Lean 证明探索未知游戏中的可达性与不可达性。</sub>

- **LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.25019)
  <br><sub>研究编码智能体根据描述与数据组合、校准可执行 Modelica 物理系统模型，并以行为拟合、物理不变量与可解释性进行验收。</sub>

- **A Declared World Model: Language Models Write the Rules of the Scene They are Shown** `2026` [![Paper](assets/badges/paper.svg)](https://www.preprints.org/manuscript/202610.1139)
  <br><sub>语言模型根据带标签场景图编写世界规则，由确定性引擎检查动作并计算下一状态；实验检验规则能否迁移到未见布局。</sub>

- **Write Once, Plan Many: Building Reusable Visual Planning Systems from One Scene** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.19234)
  <br><sub>由给定领域规则和单个练习场景生成可复用渲染、动力学、感知与规划程序，以执行和重建反馈改进，随后冻结复用。</sub>

- **RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.13172)
  <br><sub>提取可复用角色原型与可执行转移规则，在新环境中更新角色分配和参数估计，保持已获得的转移规则不变。</sub>

- **Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11794)
  <br><sub>Memento 3 结合轨迹判断与精确回放，修订反思式规则手册和可执行模型。</sub>

- **LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11253)
  <br><sub>LLM-IDEA 通过考虑可辨识性的实验设计，区分不同机制解释。</sub>

- **Kepler: Auditable World Models for ARC-AGI-3** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.00834)
  <br><sub>Kepler 通过回溯与条件转移检查以及成本统计，研究可审计的 ARC-AGI-3 世界模型。</sub>

- **EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.35047)
  <br><sub>EMPIRIC 学习残差代码，为物理引擎补充缺失的力、约束与隐藏状态。</sub>

- **Twin: Playing an Unknown Game with a Test-Time Digital Twin** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.14490)
  <br><sub>Twin 在测试时构建数字孪生，并在未知游戏中选择动作前检查历史转移。</sub>

- **Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.28287)
  <br><sub>Tycho 在求解 ARC-AGI-3 游戏时，主动修订抽象与程序化假设。</sub>

- **VisualPatchWorld: Code World Models as Latent Structured Representations for Planning** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.25236)
  <br><sub>VisualPatchWorld 从结构化状态—动作轨迹拟合动力学，并利用视觉场景图重新规划。</sub>

- **Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.17540)
  <br><sub>将 LLM 生成的仿真器族与神经仿真推断结合，用于机制选择和参数估计。</sub>

- **OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.01531)
  <br><sub>OPINE-World 通过错误优先探索，联合修订符号本体、转移假设与目标。</sub>

- **Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.16070)
  <br><sub>Mind-Studio 为部分可观测游戏构建可执行模型，并评价同状态起点的多步前瞻保真度。</sub>

- **PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.30880)
  <br><sub>PatchWorld 通过反例引导的补丁优化可执行信念状态模型，并用于动作前瞻。</sub>

- **Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models (Alice / Baba in Wonderland)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.16725)
  <br><sub>Alice 在词汇先验错配下学习可执行动力学，以旧行为保持冲突指导假设修订与探索。</sub>

- **Executable World Models for ARC-AGI-3 in the Era of Coding Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.05138)
  <br><sub>通过历史回放、简化与规划，构建 ARC-AGI-3 的可执行世界模型。</sub>

- **Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents (TheoryCoder-2)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.00929)
  <br><sub>TheoryCoder-2 在程序合成 agent 中学习和复用规划抽象。</sub>

- **Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2512.22336)
  <br><sub>Agent2World 通过研究、开发和自适应测试 agent，生成符号世界模型与训练轨迹。</sub>

- **One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration (OneLife)** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.12088)
  <br><sub>OneLife 从 Crafter-OO 中的无引导探索学习按条件激活的概率法则。</sub>

- **Code World Models for General Game Playing** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.04542)
  <br><sub>为棋盘和纸牌游戏合成 Python 转移、合法动作、终止检查、价值启发式及隐藏状态推断函数。</sub>

- **Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video (FAE)** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2508.11836)
  <br><sub>FAE 利用受约束的响应式 DSL，从游戏视频的精灵网格表示中提取行为程序。</sub>

- **PoE-World: Compositional World Modeling with Products of Programmatic Experts** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2505.10819)
  <br><sub>PoE-World 将多个程序化专家组合为随机世界模型，支持预测与规划。</sub>

- **Synthesizing world models for bilevel planning (TheoryCoder)** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2503.20124)
  <br><sub>TheoryCoder 将合成的低层 Python 动力学与给定的高层 PDDL 抽象结合，进行双层规划。</sub>

- **Generating Symbolic World Models via Test-time Scaling of Large Language Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2502.04728)
  <br><sub>通过 Best-of-N 搜索与细粒度语言化反馈，生成和修正 PDDL 世界模型。</sub>

- **Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search (GIF-MCTS)** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2405.15383)
  <br><sub>GIF-MCTS 根据描述、离线转移数据和执行反馈，搜索可执行的 Python 世界模型。</sub>

- **WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2402.12275)
  <br><sub>WorldCoder 从交互中合成 Python 转移与奖励模型，将模型一致性与乐观规划结合。</sub>

- **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2305.14909)
  <br><sub>利用 LLM 构建和修正 PDDL 域模型，再通过可靠的外部规划器进行任务规划。</sub>

- **PDSketch: Integrated Planning Domain Programming and Learning** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2303.05501)
  <br><sub>PDSketch 将预设的转移结构与学习到的神经组件结合，并自动导出规划启发式。</sub>

- **Combining Functional and Automata Synthesis to Discover Causal Reactive Programs (AutumnSynth)** `2023` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3571249)
  <br><sub>AutumnSynth 交替合成转移函数与自动机，恢复包含潜在状态的响应式程序。</sub>

- **Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning (EMPA)** `2021` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2107.12544)
  <br><sub>EMPA 学习概率游戏引擎程序，并通过内部仿真支持探索与规划。</sub>

- **Game Engine Learning from Video** `2017` [![Paper](assets/badges/paper.svg)](https://www.ijcai.org/proceedings/2017/518)
  <br><sub>从视频中学习可执行的游戏引擎规则，以未来状态预测和 agent 训练进行评价。</sub>

[↑ 返回导航](#contents)

<a id="papers-code_as_world"></a>
### 02 · Code-as-World-type · 可执行世界程序

*持久世界状态、规则、模拟器以及执行/渲染接口。*

- **Fight World Model: Customizable Combat through Visual Interaction Proxies** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.40607)
  <br><sub>将可执行的战斗状态和规则解析与视频渲染分开，用绑定身份和时间的交互代理保持攻击、受击与生命状态一致。</sub>

- **Cinematize from Unreal: Agentic Choreography for Controllable World Simulation (CineU)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.38468)
  <br><sub>把 Unreal 工程作为可检查的持久世界，利用智能体生成代码执行并验证操作，通过几何约束、时间线和局部修复完成世界编排。</sub>

- **EdenLive: Real-Time Generative Rendering from Any Visual Reference** `2026` [![Project](assets/badges/project.svg)](https://github.com/VAST-AI-Research/EdenLive)
  <br><sub>生成式渲染器把上游参考视频、目标首帧和提示转换为增强视频；状态和规则由上游程序维护。官方还提供从提示生成可玩游戏的 skill 与工作台。</sub>

- **BoxWorld: Let World Engines Control and Video Generators Render** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.36371)
  <br><sub>编码智能体把用户规则写成 Box World Engine，由持久属性和状态变量驱动神经视频渲染，并提出成对状态控制评测。</sub>

- **PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.34921)
  <br><sub>由 VLM 提出可执行物理世界，确定性物理引擎验证反事实分支并生成可验证的训练任务。</sub>

- **Mundo: Customized World Model** `2026` [![Project](assets/badges/project.svg)](https://mundo-world-model.github.io/)
  <br><sub>从图像重建可编辑的三维代理场景；场景程序指定对象和物理参数，脚本及通常采用的 MuJoCo 推进状态，代理帧与参考视图共同控制视频渲染。</sub>

- **WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.28827)
  <br><sub>分层规划预测区域与地块的类型化规格，固定过程生成器将其编译成场景；持久记录保留对象身份、边界约束和编辑，以支持流式加载与重访。</sub>

- **Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.27999)
  <br><sub>编码智能体把玩家要求写成游戏代码与规则；引擎维护持久状态，因果视频模型根据低模画面生成细节视图。</sub>

- **Agent World Model in the Wild: Computer-Use Agent Environment Synthesis (WildAWM)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.26828)
  <br><sub>合成贯通 GUI、MCP 和 CLI 的可执行计算机环境，以可重放状态构建程序和基于执行的任务、验证器质量门控支持智能体训练。</sub>

- **State World Models: Execute the Rules, Generate the Pixels** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.26811)
  <br><sub>编码智能体生成有类型的游戏定义；运行时先执行语义与空间状态规则，再调用冻结视频渲染器，之后接收与规则兼容的视觉反馈。</sub>

- **Mallea: Building, Steering, and Memorizing Worlds with Coding Agent** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.21283)
  <br><sub>编码智能体联合构建对象结构与规则，支持保留未受影响状态的运行时编辑，并结合执行状态与对象纹理记忆进行渲染。</sub>

- **Generative World Simulation with DAO and JING (DAO + JING)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.19726)
  <br><sub>DAO 在交互规则和世界时间下维护共享角色、物体与空间状态，JING 为不同观察者生成视听体验。</sub>

- **Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.17651)
  <br><sub>将生成的视觉场景编译为具有物理属性的 MuJoCo 世界，通过仿真器反馈修正可执行动力学与场景设置。</sub>

- **StreamRender-H3: Interactive Coding Worlds with Real-time Streaming Diffusion Render** `2026` [![Project](assets/badges/project.svg)](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/)
  <br><sub>three.js 游戏引擎维护地图、规则和状态，并根据玩家输入推进；语义帧连接引擎和流式 MiniMax-H3 渲染器，构成执行式模拟与生成外观分离的系统。</sub>

- **ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.15166)
  <br><sub>评估单个机制、多阶段组合机械系统以及意图驱动的可执行三维世界合成。</sub>

- **AgentGarten: Code Worlds for Evolving Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.12374)
  <br><sub>AgentGarten 将程序定义的仿真后端连接到共享实时渲染器，并复用 agent 的文字技能手册。</sub>

- **Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.01614)
  <br><sub>编码智能体与轻量引擎维护可扩展世界状态表，生成粗粒度视觉条件，并纳入新出现的对象以支持持续交互。</sub>

- **Code Plans, Diffusion Renders: Open-Ended Generative World Modeling (CoDeR)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.26458)
  <br><sub>CoDeR 协调可执行白盒世界的构建与生成式 Artist，创建开放式视觉世界。</sub>

- **GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.25652)
  <br><sub>GameDirector 利用视觉情境估计和显式玩法规则，控制游戏视频生成。</sub>

- **Programmable World Model** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.10540)
  <br><sub>Programmable World Model 将包含非视觉事实的持久引擎状态，编译为视频生成控制信号。</sub>

- **WebWorld: The Browser as a World Model for Self-Improving Web Code** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.30530)
  <br><sub>通过浏览器执行与验证自改进 Web 代码，检查交互合同及已有行为的保持。</sub>

- **Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.27549)
  <br><sub>Code as Worlds 通过提出、实例化、执行、渲染和验证的循环，发现可执行物理表示。</sub>

- **Magpie: Real-Time World Renderer for Interactive Games** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.27168)
  <br><sub>Magpie 将持久的游戏引擎状态与规则，连接到由白盒观测驱动的交互式神经渲染器。</sub>

- **Code World Model: Coding Agent as World Brain** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.25927)
  <br><sub>Code World Model 通过可执行代理表示，连接编码世界大脑与视觉世界引擎。</sub>

- **AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.05891)
  <br><sub>AppDeltaWorld 结合检索结构、视觉资产与闭环修订，预测由动作转移约束的 HTML 更新。</sub>

- **World-Time Compute with Verified Code World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.09163)
  <br><sub>World-Time Compute 利用经验证的符号代码世界，生成具有精确标签的训练轨迹。</sub>

- **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.19587)
  <br><sub>SceneCode 构建可编辑的室内世界程序，包含关节物体、仿真导出与持久场景组织。</sub>

- **ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.14398)
  <br><sub>ChronoAgentic 结合规划、编码、视觉审阅与轨迹检查，构建 PyChrono 仿真程序。</sub>

- **Code2Worlds: Empowering Coding LLMs for 4D World Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.11757)
  <br><sub>Code2Worlds 生成用于四维仿真的物体与场景程序，并结合 Blender 动力学与视觉运动反馈。</sub>

- **Code2World: A GUI World Model via Renderable Code Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.09856)
  <br><sub>Code2World 结合 AndroidCode、视觉修订与渲染感知学习，生成下一屏 GUI 代码。</sub>

- **Generative Visual Code Mobile World Models (gWorld)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.01576)
  <br><sub>gWorld 使用单一视觉语言模型，将移动 GUI 的未来观测预测为可渲染 Web 代码。</sub>

- **Web World Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2512.23676)
  <br><sub>Web World Models 以类型化 Web 状态和代码定义的规则，支撑持久的生成式世界。</sub>

[↑ 返回导航](#contents)

<a id="papers-vibeworlding"></a>
### 03 · VibeWorlding-type · agentic 3D 世界构建

*构建和编辑可编辑、可渲染或可仿真的 3D 世界。*

- **Gym-Anything for Robotics: Scaling physical simulations with digital agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.40565)
  <br><sub>把仿真创建视为编码智能体任务，构建并审计 RoboWorld 物理仿真环境；作为 3D/模拟器构建支撑工作收录。</sub>

- **Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction (SceneEvolve)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.37046)
  <br><sub>用可执行代码表示组合式 3D 场景，并在固定模型和执行后端的条件下演化重建 harness。</sub>

- **WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.31834)
  <br><sub>从真实机器人演示构建交互式数字孪生，通过编码智能体迭代修复可执行世界程序并验证物理一致性。</sub>

- **SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.28585)
  <br><sub>从单张图像重建物体与布局，通过场景代码编辑、受限位姿搜索和仿真验证，保留物理稳定且与图像对齐的场景配置。</sub>

- **NeoWorld-3: From Pixels to Code-Defined Physical Worlds** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.27690)
  <br><sub>通过分层编码智能体、可微参数拟合以及关节与物理检查，从视觉证据重建可编辑几何程序。</sub>

- **InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.26853)
  <br><sub>用 VLM 驱动符号约束的程序化生成和确定性布局，构建可编辑、可动画化的开放式 3D 世界。</sub>

- **Self-Building Labs** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.23826)
  <br><sub>智能体从科学目标、照片和设备信息构建实验室数字孪生、机器人技能与工作流，并通过观测和物理反馈改进场景模型。</sub>

- **3DCodeVerse: Exploring 3D Worlds as Code** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.22341)
  <br><sub>将可执行 3D 程序、资产与验证记录组成数据资源，并通过执行检查、几何测量及视觉反馈迭代生成和修正程序。</sub>

- **BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.23986)
  <br><sub>通过多模态任务要求、渲染视图和任务评分细则，评估智能体创建的可编辑 Blender 场景。</sub>

- **RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.18835)
  <br><sub>基于 Newton 的交互式工具包，将求解器、接触模型与物理参数显式开放给人类和编码智能体，依据观测行为迭代调整操作仿真。</sub>

- **USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11322)
  <br><sub>USDCraft 将输入几何转为可执行建模程序，导出具有关节结构的 USD 仿真资产。</sub>

- **LEGO-Anything: Coding Agents for 3D Scene Reconstruction** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.36380)
  <br><sub>LEGO-Anything 将三维场景重建为可执行程序，并分别评价产物有效性、几何和外观。</sub>

- **Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.11499)
  <br><sub>Recursive Code World Models 通过递归程序、全局—局部修订和共享参考视图重建复杂场景。</sub>

- **FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.29519)
  <br><sub>FuncRoom-Agent 通过递归 DSL、顺序专家模型和执行依据的过程奖励，生成功能性室内场景。</sub>

- **VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.15265)
  <br><sub>VibeWorlding 研究多模态 coding agent 如何在 Blender 沙盒中通过资产检索、程序化编辑、渲染反馈与物理可行性检查端到端构建和修改开放式 3D 世界。它的核心任务是世界构建与编辑，不应直接计作时间动力学发现。</sub>

- **WorldClaw: Agentic 3D Open-World Generation at Scale** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.05248)
  <br><sub>WorldClaw 通过区域规划、地形生成和渲染反馈，构建大规模可编辑三维场景。</sub>

- **Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.16147)
  <br><sub>研究程序化场景表示，以及通过程序搜索进行错误修正的方法。</sub>

- **Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2504.05482)
  <br><sub>研究命令式与声明式场景程序的表示差异，以及基于程序的错误修正。</sub>

- **SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2408.02211)
  <br><sub>SceneMotifCoder 从少量视觉示例中学习可编辑的物体排列程序。</sub>

- **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2403.01248)
  <br><sub>SceneCraft 将场景蓝图转为 Blender 代码，并利用渲染反馈迭代修正。</sub>

- **Open-Universe Indoor Scene Generation using LLM Program Synthesis and Uncurated Object Databases** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2403.09675)
  <br><sub>基于未精选的物体数据库，合成可执行的室内场景布局约束。</sub>

- **Holodeck: Language Guided Generation of 3D Embodied AI Environments** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2312.09067)
  <br><sub>Holodeck 通过空间约束与优化构建语言驱动的三维具身环境。</sub>

- **Infinite Photorealistic Worlds Using Procedural Generation (Infinigen)** `2023` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html)
  <br><sub>Infinigen 通过程序化规则生成世界尺度的逼真几何与材质。</sub>

- **ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis** `2020` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2009.08026)
  <br><sub>ShapeAssembly 以层次化参数装配程序表示三维部件结构。</sub>

- **CSGNet: Neural Shape Parser for Constructive Solid Geometry** `2018` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html)
  <br><sub>CSGNet 将视觉形状解析为可执行的构造实体几何程序。</sub>

- **Procedural content generation for games** `2013` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/2422956.2422957)
  <br><sub>游戏程序化内容生成的历史参考文献；本轮核查书目信息。</sub>

[↑ 返回导航](#contents)

<!-- CATALOG:END -->

<a id="contributing"></a>
## 参与贡献

欢迎补充论文、修正信息和提出有价值的比较。来源核查与分类约定见[贡献指南](CONTRIBUTING.md)，也可以[提交 issue](https://github.com/MichaelCao0/Code-world-survey/issues/new)。

两份 README 共享 [data/papers.json](data/papers.json) 中的论文数据，中文摘要保存在 [data/readme.zh-CN.json](data/readme.zh-CN.json)。更新后运行：

```bash
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

<details>
<summary><strong>来源约定与同名工作说明</strong></summary>

文献记录链接到 arXiv、DOI 或正式会议页面。论文标题与方法别名分别保存；日期遵循原始来源元数据，可能与会议年份不同。核查深度与影响结论的实验条件见[详细核查表](docs/catalogue.md)和[核查协议](docs/review-protocol.md)。

| 相似名称 | 对应区别 |
|---|---|
| Code2World / Code2Worlds | GUI 观测预测 / 四维仿真生成 |
| Web World Models / WebWorld | 代码定义的持久世界 / 学习型网页仿真 / 基于浏览器的代码验证，分别对应三项工作 |
| WorldCoder / WorldCoder-Bench | 基于模型的 agent / 三维世界构建基准 |
| TheoryCoder / TheoryCoder-2 | 方法别名；文献库保留各自的正式论文标题 |
| OneLife / General Game Playing | 从探索中学习随机动力学 / 根据游戏规则和轨迹构建可执行模型 |
| FAIR CWM | 计算执行与代码生成的神经建模 |

相关预印本在结构化数据中互相链接。数量表示文献来源记录，详细核查表分别标注核心方法、历史来源、支撑表示、基准和对照方法。

</details>

<a id="acknowledgements"></a>
## 致谢

首页组织参考了 [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models)。封面为本仓库原创。感谢相关论文作者开放研究成果与资源。

<p align="center"><a href="#code-centric-world-models">返回顶部 ↑</a></p>
