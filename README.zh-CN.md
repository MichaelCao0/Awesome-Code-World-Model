<div align="center">

# Code-Centric World Models

**可执行动力学 · 持久世界 · 可渲染观测**

持续维护的文献集合，以及正在撰写的综述的配套主页。

[English](README.md) | **简体中文**

<!-- BADGES:BEGIN -->

[![Source records](assets/badges/sources.svg)](#paper-collection) [![Reading sections](assets/badges/topics.svg)](#contents) [![Literature cutoff](assets/badges/cutoff.svg)](docs/review-protocol.md) [![Contributions welcome](assets/badges/contributions.svg)](CONTRIBUTING.md)

![Survey arXiv](assets/badges/survey-arxiv.svg) ![Survey Semantic Scholar citations](assets/badges/survey-citations.svg)

<!-- BADGES:END -->

[综述入口](docs/survey.md) · [文献目录](#paper-collection) · [分类框架](docs/taxonomy.md) · [BibTeX](papers.bib) · [参与贡献](CONTRIBUTING.md)

<p><img src="./assets/banner.png" alt="以程序构建可执行世界：代码、持久状态与渲染观测" width="1280"></p>

</div>

代码使世界模型能够被**执行、编辑和检查**。本仓库围绕“**代码承担什么世界语义**”这一问题，连接程序合成、基于模型的 agent、物理仿真、GUI 预测与可控视觉生成，梳理程序如何获得、验证和使用。

<a id="news"></a>
## 更新

- **2026-10-29** — 加入 VibeWorlding，整理覆盖 124 条记录的全量论文总表，并将 README 主分类收敛为 WorldCoder-type、Code-as-World-type、VibeWorlding-type 三类。封面改为代码—状态—数字世界主题的栅格图。
- **2026-10-26** — 补入 31 条核实来源，形成当前文献目录基础。
- **2026-10-19** — 加入中英双语 README、PNG 封面、综述标签占位与分类导航。
- **2026-10-14** — 初始版本收录 92 条文献记录，提供结构化元数据、BibTeX、分类框架与评测框架。

<a id="contents"></a>
## 导航

[综述与资源](#survey--resources) · [核心视角](#at-a-glance) · [文献目录](#paper-collection) · [参与贡献](#contributing) · [致谢](#acknowledgements)

**写作讨论：** [三类框架](docs/coarse-taxonomy.md) · [全量论文总表](docs/paper-master-list.md) · [分类 JSON](data/classification.json) · [本轮更新](docs/updates/2026-10-29.md)

<!-- NAVIGATION:BEGIN -->

| 建模与评测 | 基础与相邻研究 |
|---|---|
| [01 · 可执行动力学与规划](#papers-dynamics) <sub>(26)</sub> | [06 · 场景与资产程序](#papers-scene_programs) <sub>(14)</sub> |
| [02 · 持久的可执行世界](#papers-construction) <sub>(12)</sub> | [07 · 历史与表示基础](#papers-foundations) <sub>(9)</sub> |
| [03 · 执行与视觉生成的连接](#papers-coupling) <sub>(14)</sub> | [08 · 对照与相邻方法](#papers-comparators) <sub>(26)</sub> |
| [04 · 以可渲染代码预测观测](#papers-observation) <sub>(3)</sub> | [09 · 相关综述](#papers-surveys) <sub>(3)</sub> |
| [05 · 基准与验证资源](#papers-evaluation) <sub>(17)</sub> | [详细核查表 →](docs/catalogue.md) |

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

[三类框架说明](docs/coarse-taxonomy.md) 给出具体判据。若强行归类会掩盖论文贡献，则保留在 **Other / Benchmarks / Adjacent**；[全量总表](docs/paper-master-list.md) 仍保留每条记录。

<a id="paper-collection"></a>
## 文献目录

<!-- CATALOG:BEGIN -->

**124 条文献来源** · 文献截止日期：**2026-10-29**。

按研究方向浏览。[完整注释、核查深度与证据说明 →](docs/catalogue.md)

各分区按记录日期倒序排列；首发日期未知的项目按已公开时间上界排序，详见注释表。支撑与相邻分支可展开浏览。

<a id="papers-dynamics"></a>
### 01 · 可执行动力学与规划

*学习可执行的规则、抽象与机制，用于预测和规划。*

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

[↑ 返回导航](#contents)

<a id="papers-construction"></a>
### 02 · 持久的可执行世界

*构建交互世界、物理仿真和经过验证的世界族。*

- **WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.28827)
  <br><sub>分层规划预测区域与地块的类型化规格，固定过程生成器将其编译成场景；持久记录保留对象身份、边界约束和编辑，以支持流式加载与重访。</sub>

- **NeoWorld-3: From Pixels to Code-Defined Physical Worlds** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.27690)
  <br><sub>通过分层编码智能体、可微参数拟合以及关节与物理检查，从视觉证据重建可编辑几何程序。</sub>

- **Agent World Model in the Wild: Computer-Use Agent Environment Synthesis (WildAWM)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.26828)
  <br><sub>合成贯通 GUI、MCP 和 CLI 的可执行计算机环境，以可重放状态构建程序和基于执行的任务、验证器质量门控支持智能体训练。</sub>

- **LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.25019)
  <br><sub>研究编码智能体根据描述与数据组合、校准可执行 Modelica 物理系统模型，并以行为拟合、物理不变量与可解释性进行验收。</sub>

- **RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.18835)
  <br><sub>基于 Newton 的交互式工具包，将求解器、接触模型与物理参数显式开放给人类和编码智能体，依据观测行为迭代调整操作仿真。</sub>

- **Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.17651)
  <br><sub>将生成的视觉场景编译为具有物理属性的 MuJoCo 世界，通过仿真器反馈修正可执行动力学与场景设置。</sub>

- **Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.27549)
  <br><sub>Code as Worlds 通过提出、实例化、执行、渲染和验证的循环，发现可执行物理表示。</sub>

- **World-Time Compute with Verified Code World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.09163)
  <br><sub>World-Time Compute 利用经验证的符号代码世界，生成具有精确标签的训练轨迹。</sub>

- **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.19587)
  <br><sub>SceneCode 构建可编辑的室内世界程序，包含关节物体、仿真导出与持久场景组织。</sub>

- **ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.14398)
  <br><sub>ChronoAgentic 结合规划、编码、视觉审阅与轨迹检查，构建 PyChrono 仿真程序。</sub>

- **Code2Worlds: Empowering Coding LLMs for 4D World Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.11757)
  <br><sub>Code2Worlds 生成用于四维仿真的物体与场景程序，并结合 Blender 动力学与视觉运动反馈。</sub>

- **Web World Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2512.23676)
  <br><sub>Web World Models 以类型化 Web 状态和代码定义的规则，支撑持久的生成式世界。</sub>

[↑ 返回导航](#contents)

<a id="papers-coupling"></a>
### 03 · 执行与视觉生成的连接

*将持久程序状态连接到传统渲染与神经视觉输出。*

- **EdenLive: Real-Time Generative Rendering from Any Visual Reference** `2026` [![Project](assets/badges/project.svg)](https://github.com/VAST-AI-Research/EdenLive)
  <br><sub>生成式渲染器把上游参考视频、目标首帧和提示转换为增强视频；状态和规则由上游程序维护。官方还提供从提示生成可玩游戏的 skill 与工作台。</sub>

- **Mundo: Customized World Model** `2026` [![Project](assets/badges/project.svg)](https://mundo-world-model.github.io/)
  <br><sub>从图像重建可编辑的三维代理场景；场景程序指定对象和物理参数，脚本及通常采用的 MuJoCo 推进状态，代理帧与参考视图共同控制视频渲染。</sub>

- **SolarRenderer: Few-Step Generative Reference Rendering** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.28630)
  <br><sub>通过控制与加速 LoRA 适配冻结视频骨干，将对齐的结构视频转成细节视频，并支持流式生成。</sub>

- **Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.27999)
  <br><sub>编码智能体把玩家要求写成游戏代码与规则；引擎维护持久状态，因果视频模型根据低模画面生成细节视图。</sub>

- **State World Models: Execute the Rules, Generate the Pixels** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.26811)
  <br><sub>编码智能体生成有类型的游戏定义；运行时先执行语义与空间状态规则，再调用冻结视频渲染器，之后接收与规则兼容的视觉反馈。</sub>

- **Mallea: Building, Steering, and Memorizing Worlds with Coding Agent** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.21283)
  <br><sub>编码智能体联合构建对象结构与规则，支持保留未受影响状态的运行时编辑，并结合执行状态与对象纹理记忆进行渲染。</sub>

- **StreamRender-H3: Interactive Coding Worlds with Real-time Streaming Diffusion Render** `2026` [![Project](assets/badges/project.svg)](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/)
  <br><sub>three.js 游戏引擎维护地图、规则和状态，并根据玩家输入推进；语义帧连接引擎和流式 MiniMax-H3 渲染器，构成执行式模拟与生成外观分离的系统。</sub>

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

- **Magpie: Real-Time World Renderer for Interactive Games** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.27168)
  <br><sub>Magpie 将持久的游戏引擎状态与规则，连接到由白盒观测驱动的交互式神经渲染器。</sub>

- **Code World Model: Coding Agent as World Brain** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.25927)
  <br><sub>Code World Model 通过可执行代理表示，连接编码世界大脑与视觉世界引擎。</sub>

[↑ 返回导航](#contents)

<a id="papers-observation"></a>
### 04 · 以可渲染代码预测观测

*通过可执行的渲染代码，预测动作条件下的 GUI 观测。*

- **AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.05891)
  <br><sub>AppDeltaWorld 结合检索结构、视觉资产与闭环修订，预测由动作转移约束的 HTML 更新。</sub>

- **Code2World: A GUI World Model via Renderable Code Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.09856)
  <br><sub>Code2World 结合 AndroidCode、视觉修订与渲染感知学习，生成下一屏 GUI 代码。</sub>

- **Generative Visual Code Mobile World Models (gWorld)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.01576)
  <br><sub>gWorld 使用单一视觉语言模型，将移动 GUI 的未来观测预测为可渲染 Web 代码。</sub>

[↑ 返回导航](#contents)

<a id="papers-evaluation"></a>
### 05 · 基准与验证资源

*检验程序行为、状态、渲染后果以及面向 agent 的一致性。*

- **Events, Not Pixels: Where World Models Get the Return Wrong** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.29435)
  <br><sub>在匹配预算下用真实转移替换部分想象转移诊断回报误差；对所测模型，奖励或终止事件比视觉误差大的帧更影响回报。</sub>

- **Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.28416)
  <br><sub>以文本、图像和视频为输入，评估可执行程序生成完整视频的能力，并测量执行、质量、指令对齐与参考保真。</sub>

- **GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.22708)
  <br><sub>以实际执行得到的结果为参照，结合确定性检查与语义评判，测试文本模型对动作后环境响应的预测。</sub>

- **BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.23986)
  <br><sub>通过多模态任务要求、渲染视图和任务评分细则，评估智能体创建的可编辑 Blender 场景。</sub>

- **WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.18826)
  <br><sub>以配对真实执行评估动作条件机器人世界模型，覆盖状态正确性、交互空间对齐、局部交互保真及多视角动作一致性。</sub>

- **ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.15166)
  <br><sub>评估单个机制、多阶段组合机械系统以及意图驱动的可执行三维世界合成。</sub>

- **Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.04432)
  <br><sub>Video2World 从几何、动力学和功能三个方面，评价具身视频到交互世界的重建。</sub>

- **PROWBench: Do Video Models Render What the Program Specifies?** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.02205)
  <br><sub>PROWBench 将渲染视频中的事件与可执行程序规格及事件日志进行对齐比较。</sub>

- **The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models (StateAliasBench)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.32679)
  <br><sub>StateAliasBench 配对可见 GUI 条件相同、未来却不同的案例，诊断隐藏转移状态。</sub>

- **GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.21562)
  <br><sub>GameLogicBench 在多种可复现情景下，以逐仿真 tick 的状态检查验证 Godot 游戏规则。</sub>

- **GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.00048)
  <br><sub>GUI-CC 结合离线参考动作与在线 agent 闭环，评价多步上下文一致性。</sub>

- **ScratchWorld: Evaluating If World Models Compute Executable Consequences** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.31689)
  <br><sub>ScratchWorld 利用可回放验证的 Scratch 转移与变化字段指标，评价可执行后果。</sub>

- **WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.01869)
  <br><sub>WorldCoder-Bench 通过隐藏的运行时行为合同，评价具有物理依据的三维世界构建。</sub>

- **OpenComputer: Verifiable Software Worlds for Computer-Use Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.19769)
  <br><sub>OpenComputer 提供真实软件环境、结构化状态验证与可审计的任务奖励。</sub>

- **MobileWorldBench: Towards Semantic World Modeling For Mobile Agents** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2512.14014)
  <br><sub>MobileWorldBench 评价移动环境的语义状态转移及其对 GUI agent 的使用价值。</sub>

- **WorldModelBench: Judging Video Generation Models As World Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2502.20694)
  <br><sub>WorldModelBench 从指令遵从、物理合理性和人类偏好评价视频世界模型。</sub>

- **Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2502.13092)
  <br><sub>Text2World 以多样化域和执行指标评价文本到 PDDL 世界模型的生成。</sub>

[↑ 返回导航](#contents)

<a id="papers-scene_programs"></a>
### 06 · 场景与资产程序

*程序化几何、重建、关节建模与场景组合。*

<details>
<summary><strong>展开 14 条文献</strong></summary>

- **SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.28585)
  <br><sub>从单张图像重建物体与布局，通过场景代码编辑、受限位姿搜索和仿真验证，保留物理稳定且与图像对齐的场景配置。</sub>

- **3DCodeVerse: Exploring 3D Worlds as Code** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.22341)
  <br><sub>将可执行 3D 程序、资产与验证记录组成数据资源，并通过执行检查、几何测量及视觉反馈迭代生成和修正程序。</sub>

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

</details>

[↑ 返回导航](#contents)

<a id="papers-foundations"></a>
### 07 · 历史与表示基础

*早期可执行动力学、程序归纳与程序化表示。*

<details>
<summary><strong>展开 9 条文献</strong></summary>

- **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2305.14909)
  <br><sub>利用 LLM 构建和修正 PDDL 域模型，再通过可靠的外部规划器进行任务规划。</sub>

- **Combining Functional and Automata Synthesis to Discover Causal Reactive Programs (AutumnSynth)** `2023` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3571249)
  <br><sub>AutumnSynth 交替合成转移函数与自动机，恢复包含潜在状态的响应式程序。</sub>

- **Infinite Photorealistic Worlds Using Procedural Generation (Infinigen)** `2023` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html)
  <br><sub>Infinigen 通过程序化规则生成世界尺度的逼真几何与材质。</sub>

- **Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning (EMPA)** `2021` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2107.12544)
  <br><sub>EMPA 学习概率游戏引擎程序，并通过内部仿真支持探索与规划。</sub>

- **ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis** `2020` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2009.08026)
  <br><sub>ShapeAssembly 以层次化参数装配程序表示三维部件结构。</sub>

- **DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning** `2020` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2006.08381)
  <br><sub>DreamCoder 通过程序归纳与可复用库学习，为组合式表示提供基础。</sub>

- **CSGNet: Neural Shape Parser for Constructive Solid Geometry** `2018` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html)
  <br><sub>CSGNet 将视觉形状解析为可执行的构造实体几何程序。</sub>

- **Game Engine Learning from Video** `2017` [![Paper](assets/badges/paper.svg)](https://www.ijcai.org/proceedings/2017/518)
  <br><sub>从视频中学习可执行的游戏引擎规则，以未来状态预测和 agent 训练进行评价。</sub>

- **Procedural content generation for games** `2013` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/2422956.2422957)
  <br><sub>游戏程序化内容生成的历史参考文献；本轮核查书目信息。</sub>

</details>

[↑ 返回导航](#contents)

<a id="papers-comparators"></a>
### 08 · 对照与相邻方法

*比较其他状态表示、学习型仿真器与相邻机制。*

<details>
<summary><strong>展开 26 条文献</strong></summary>

- **Agentic World Action Models (AW-0)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.30136)
  <br><sub>以耦合专家联合建模代码、未来视频和动作；程序提供可复用技能与控制结构，视频和动作专家预测视觉未来与低层运动命令。</sub>

- **Beyond Next-Screen Prediction: The Decision Value of GUI World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.24372)
  <br><sub>控制预测呈现方式和监督条件，对比 GUI 前瞻预测与直接动作排序器，检验预测画面对决策的增量价值。</sub>

- **Self-Building Labs** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.23826)
  <br><sub>智能体从科学目标、照片和设备信息构建实验室数字孪生、机器人技能与工作流，并通过观测和物理反馈改进场景模型。</sub>

- **Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation (ATAS)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.20571)
  <br><sub>将剧本编译为带空间和事件时间引用的镜头请求，检索配准场景与事件记忆，并在检查通过后将生成观测写入记忆。</sub>

- **Neurosymbolic Learning of Interpretable World Models (CGWM)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.19955)
  <br><sub>学习视觉概念落地，而无可学习参数的预测器执行给定时序逻辑转移规则；通过符号想象轨迹进行可微规划。</sub>

- **From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction (DR-WM)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.17630)
  <br><sub>结合 RGB 场景重建、真实动作响应校准的地形接触先验与物理仿真，以模拟运动和几何指导视频世界模型。</sub>

- **Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11942)
  <br><sub>研究以 GUI 世界模型验证状态转移，并区分界面相似度与转移正确性。</sub>

- **Software World Models: From Consequence Prediction to Decision Value** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.04940)
  <br><sub>Software World Models 预测代码编辑的后果，并评价其对决策的价值。</sub>

- **AutoGUIWorld: Image Generators as Visual World Models for GUI Agent** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.01215)
  <br><sub>AutoGUIWorld 通过规划视觉后果并迭代编辑截图，合成 GUI 交互轨迹。</sub>

- **Agent-Editing World Model: Rethinking World Modeling for LLM Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.28416)
  <br><sub>Agent-Editing World Model 将可编辑的 agent 推理与任务延续作为相邻的世界建模形式。</sub>

- **Discriminative World Models for Web Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.02885)
  <br><sub>Discriminative World Models 根据预测状态区分网页动作的能力进行评价。</sub>

- **WebWorld: The Browser as a World Model for Self-Improving Web Code** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.30530)
  <br><sub>通过浏览器执行与验证自改进 Web 代码，检查交互合同及已有行为的保持。</sub>

- **Learning Simple Test-Time Environments for LLM Web Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.29305)
  <br><sub>TTED 在测试时学习简单子环境观测，以改善网页 agent 的组合泛化。</sub>

- **MASS: Multiplayer World Models with Authoritative Shared State** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.06257)
  <br><sub>MASS 学习面向多人世界建模的 Logic Engine，并维护权威共享状态。</sub>

- **StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.26754)
  <br><sub>StatePlay 联合预测游戏状态与视频，为显式代码转移提供学习型动力学对照。</sub>

- **Simulate to Generalize: Scaling Stateful Supervision for API-calling Agents using LLM World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.16900)
  <br><sub>利用语言模型仿真器，为 agent 生成有状态的 API 调用监督数据。</sub>

- **Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.15439)
  <br><sub>在 ARC-AGI-3 编码 agent 中，检验维护可执行模型、简化和回放验证的作用。</sub>

- **How Mobile World Model Guides GUI Agents?** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.10347)
  <br><sub>比较文本、图像和可渲染代码表示，分析重建、在线使用及 agent 消费预测的不同方式。</sub>

- **Computer-Using World Model** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.17365)
  <br><sub>Computer-Using World Model 先预测文本变化，再生成桌面软件交互后的截图。</sub>

- **WebWorld: A Large-Scale World Model for Web Agent Training** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.14721)
  <br><sub>WebWorld 学习大规模网页仿真器，用于 agent 训练。</sub>

- **CWM: An Open-Weights LLM for Research on Code Generation with World Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.02387)
  <br><sub>FAIR CWM 通过解释器和容器交互学习计算执行过程与代码生成行为。</sub>

- **ViMo: A Generative Visual GUI World Model for App Agents** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2504.13936)
  <br><sub>ViMo 通过图形与文本分解建模移动 GUI 的未来观测。</sub>

- **Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents (WebDreamer)** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2411.06559)
  <br><sub>WebDreamer 利用语言模型模拟世界，为网页 agent 规划动作。</sub>

- **VisualPredicator: Learning Abstract World Models with Neuro-Symbolic Predicates for Robot Planning** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2410.23156)
  <br><sub>VisualPredicator 通过神经符号谓词学习面向任务的抽象世界模型，用于机器人规划。</sub>

- **Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2410.13232)
  <br><sub>预测以状态转移为中心的自然语言变化，用于基于模型的网页导航。</sub>

- **PDSketch: Integrated Planning Domain Programming and Learning** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2303.05501)
  <br><sub>PDSketch 将预设的转移结构与学习到的神经组件结合，并自动导出规划启发式。</sub>

</details>

[↑ 返回导航](#contents)

<a id="papers-surveys"></a>
### 09 · 相关综述

*世界建模、场景生成与代码智能的更广泛研究视角。*

<details>
<summary><strong>展开 3 条文献</strong></summary>

- **3D Scene Generation: A Survey** `2026` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1007/s11263-026-02999-6)
  <br><sub>三维场景生成的相邻综述；本轮核查书目信息。</sub>

- **Beyond the Autoregressive Horizon: A Comprehensive Survey of Diffusion Models, World Modelling, and State Space Models for Code** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.23690)
  <br><sub>代码智能方向的相邻综述，连接扩散模型、世界建模与状态空间模型。</sub>

- **3D and 4D World Modeling: A Survey** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2509.07996)
  <br><sub>三维与四维世界建模的相邻综述，可用于比较生成模态与程序语义两种分类视角。</sub>

</details>

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
