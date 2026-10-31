<div align="center">

# Code-Centric World Models

**可执行动力学 · 持久世界 · 可渲染观测**

持续维护的文献集合，以及正在撰写的综述的配套主页。

[English](README.md) | **简体中文**

<!-- BADGES:BEGIN -->

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome) [![GitHub stars](https://img.shields.io/github/stars/MichaelCao0/Awesome-Code-World-Model?style=social)](https://github.com/MichaelCao0/Awesome-Code-World-Model/stargazers) [![GitHub forks](https://img.shields.io/github/forks/MichaelCao0/Awesome-Code-World-Model?style=social)](https://github.com/MichaelCao0/Awesome-Code-World-Model/network/members) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[![Source records](assets/badges/sources.svg)](#paper-collection) [![Reading sections](assets/badges/topics.svg)](#contents) [![Literature cutoff](assets/badges/cutoff.svg)](docs/review-protocol.md)

![Survey arXiv](https://img.shields.io/badge/arXiv-survey%20pending-b31b1b?style=flat-square&logo=arxiv&logoColor=white) ![Survey Semantic Scholar citations](https://img.shields.io/badge/Semantic%20Scholar-citations%20pending-1857b6?style=flat-square&logo=semanticscholar&logoColor=white)

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

<a id="related-surveys"></a>
## 相关综述：我们的不同之处

<!-- RELATED:BEGIN -->

相关综述以视频模型或通用世界模型为中心；本综述以**可执行代码作为世界的载体**为纳入标准，按代码承担了世界的多少部分（纯状态 / 白模 + 生成式渲染 / 完整 3D）组织文献，视频模型只作为可选的渲染器出现。

- **Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.40191-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.40191)
  <br><sub>围绕视频生成模型的 agent harness 综述视频生产、交互式世界建模和递归自我改进；作为相关综述保留。</sub>
  <br>**与本综述的区别：** 该综述以视频生成模型为中心，梳理围绕它构建的 agent harness（视频制作、交互式世界建模、递归自我改进），代码只是 harness 的组件之一。本综述以代码为世界的载体：代码承担状态与规则、白模世界或完整 3D 世界，视频模型只是可选的渲染器之一。

- **AI for Games in the Foundation Model Era** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.16679-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.16679)
  <br><sub>按六种角色综述游戏全生命周期中的 AI：从玩游戏、建模游戏到构建、运行时适配与测试。</sub>
  <br>**与本综述的区别：** 该综述覆盖游戏领域的方方面面，包括学习型游戏世界模型与 AI 辅助开发。本综述中游戏只是若干领域之一，重点是以可执行代码写成的游戏规则与世界。

- **From Generation to Simulation: How Far Are World Models from Being True Simulators?** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.23070-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.23070)
  <br><sub>以传统模拟器的八项能力为标尺评估 200 项生成式世界模型工作，发现结构化状态反馈最受忽视。</sub>
  <br>**与本综述的区别：** 该综述考察潜变量、视频和联合嵌入世界模型距离模拟器还有多远。代码世界模型走的是相反路线：从带显式状态的可执行基底出发；本综述研究这一基底如何被归纳、构建和渲染。

- **From Pixels to States: Rethinking Interactive World Models as Game Engines** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.14076-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.14076)
  <br><sub>以游戏引擎的&quot;动作—状态—观测&quot;循环为视角综述交互式游戏世界模型，并发布带状态标注的《黑神话：悟空》数据引擎。</sub>
  <br>**与本综述的区别：** 该综述主张视频世界模型应恢复游戏引擎中的显式状态循环。Code-as-World 方法把这一循环保留在可执行代码中，视频模型只负责渲染；本综述比较的是代码承担了这一循环的多少部分。

- **Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2606.12191-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.12191)
  <br><sub>综述 LLM agent 环境的建模、符号与神经合成、评测以及 agent 与环境的协同演化。</sub>
  <br>**与本综述的区别：** 该综述把环境视为 agent 的训练基础设施。本综述只关注其代码充当世界模型、预测或模拟世界演化的情形，基准和合成任务环境居于次要位置。

- **Bridging the Agent-World Gap: Text World Models for LLM-based Agents** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2606.09032-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.09032)
  <br><sub>综述面向 LLM agent 的文本世界模型（预测下一个网页、终端输出或 API 响应），涵盖 LLM 作为世界模型与代码作为世界模型的构建、应用与评测。</sub>
  <br>**与本综述的区别：** 该综述聚焦文本环境，把"代码作为世界模型"视为一种构建范式。本综述以代码世界本身为主题，并从文本与符号状态扩展到白模加生成式渲染以及完整 3D 世界。

- **Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2604.22748-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.22748)
  <br><sub>以&quot;层级 × 规律&quot;分类综述面向 agent 的世界模型：预测器、模拟器、演化器三个层级，横跨物理、数字、社会与科学四类规律。</sub>
  <br>**与本综述的区别：** 该综述按能力层级与规律类型梳理 400 余项工作，代码化模型只是众多实现方式之一。本综述的组织问题是代码在世界中承担什么，只收录以代码为世界载体的方法。

- **LLMs as Planning Formalizers: A Survey for Leveraging Large Language Models to Construct Automated Planning Models** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2503.18971-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.18971)
  <br><sub>综述用 LLM 将规划问题形式化（如 PDDL）并修正规格、交由现成自动规划器求解的研究。</sub>
  <br>**与本综述的区别：** 该综述覆盖 WorldCoder-type 的一个分支：由语言写出的符号规划模型。本综述将其与 Python 转移程序、物理残差、生成式渲染的代码世界和 3D 世界程序放在同一框架下。

<!-- RELATED:END -->

<a id="news"></a>
## 更新

- **2026-10-31（补充检索）** — 针对 2026 年文献补充 42 条记录：WorldCoder-type 11 条、Code-as-World-type 2 条、VibeWorlding-type 7 条、评测基准 11 条、GUI 世界模型 4 条、相关综述 7 篇。详见[更新说明](docs/updates/2026-10-31.md#coverage-pass)。
- **2026-10-31（其他与相关综述）** — 删除 5 条对照/相邻记录（StatePlay、Simulate to Generalize、Software World Models、Agent-Editing World Model、AW-0）。三类之外的记录统一放在**其他**下（GUI 世界模型 · 按评测对象分组的评测基准，ExeWorldBench 和 BlenderWorld 也移入），并在开头新增[相关综述](#related-surveys)一节，说明本综述的不同之处。
- **2026-10-31（重新分类）** — 三类改为按"代码承担了世界的多少部分"划分：WorldCoder-type（纯状态）、Code-as-World-type（白模 + 生成式渲染）、VibeWorlding-type（完整 3D，当前包含静态场景）。收紧 Code-as-World-type，将可仿真 3D 构建移入 VibeWorlding-type，GUI 世界模型集中为未收录的 GUI 分组。详见[更新说明](docs/updates/2026-10-31.md#reclassification)。
- **2026-10-31** — 根据 10 月 13–29 日检索新增 21 条记录，补充可执行动力学、持久世界引擎、可编辑 3D 构建与运行时评测。严格范围仍由三类主线定义，支撑来源保留在未归类总表中。
- **2026-10-30** — 继续补充三类主线归类；评测、综述和明显相邻来源保留在总表但不强行归类。仓库目录现在只有三个 section。
- **2026-10-29** — 加入 VibeWorlding，整理覆盖 124 条记录的全量论文总表，并将 README 主分类收敛为 WorldCoder-type、Code-as-World-type、VibeWorlding-type 三类。封面改为代码—状态—数字世界主题的栅格图。
- **2026-10-26** — 补入 31 条核实来源，形成当前文献目录基础。
- **2026-10-19** — 加入中英双语 README、PNG 封面、综述标签占位与分类导航。
- **2026-10-14** — 初始版本收录 92 条文献记录，提供结构化元数据、BibTeX、分类框架与评测框架。

<a id="contents"></a>
## 导航

[研究动机](#motivation) · [相关综述](#related-surveys) · [综述与资源](#survey--resources) · [核心视角](#at-a-glance) · [文献目录](#paper-collection) · [参与贡献](#contributing) · [致谢](#acknowledgements)

**写作讨论：** [三类框架](docs/coarse-taxonomy.md) · [全量论文总表](docs/paper-master-list.md) · [分类 JSON](data/classification.json) · [本轮更新](docs/updates/2026-10-31.md)

<!-- NAVIGATION:BEGIN -->

| 三类主线 |
|---|
| [01 · WorldCoder-type · 程序化动力学](#papers-worldcoder) <sub>(49)</sub> |
| [02 · Code-as-World-type · 白模世界 + 生成式渲染](#papers-code_as_world) <sub>(24)</sub> |
| [03 · VibeWorlding-type · agentic 3D 世界构建](#papers-vibeworlding) <sub>(40)</sub> |
| [其他](#papers-other): [GUI 世界模型](#papers-other-gui) <sub>(20)</sub> · [评测基准](#papers-other-benchmark) <sub>(28)</sub> |
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
| **WorldCoder-type** · 程序化动力学（纯状态） | 代码能否预测动作后果并支持规划？ | [WorldCoder](https://arxiv.org/abs/2402.12275)、[TheoryCoder](https://arxiv.org/abs/2503.20124)、[OneLife](https://arxiv.org/abs/2510.12088)、[Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) |
| **Code-as-World-type** · 白模世界 + 生成式渲染 | 代码维护的白模/proxy 世界状态与规则，能否驱动生成式渲染的世界？ | [Code World Model](https://arxiv.org/abs/2608.25927)、[Programmable World Model](https://arxiv.org/abs/2609.10540)、[AgentGarten](https://arxiv.org/abs/2610.12374)、[Oneira](https://arxiv.org/abs/2610.01614) |
| **VibeWorlding-type** · agentic 3D 世界构建 | agent 能否用代码写出并编辑完整 3D 世界（含静态与可仿真场景）？ | [VibeWorlding](https://arxiv.org/abs/2608.15265)、[WorldClaw](https://arxiv.org/abs/2608.05248)、[USDCraft](https://arxiv.org/abs/2610.11322)、[SceneRig](https://arxiv.org/abs/2610.28585) |

三类按"代码承担了世界的多少部分"划分：只有状态、白模世界加生成式渲染、完整 3D 世界。[三类框架说明](docs/coarse-taxonomy.md) 给出具体判据。其余记录统一放在[其他](#papers-other)下，分为 [GUI 世界模型](#papers-other-gui)和按评测对象分组的[评测基准](#papers-other-benchmark)。

<a id="paper-collection"></a>
## 文献目录

<!-- CATALOG:BEGIN -->

**169 条文献来源** · 文献截止日期：**2026-10-29**。

README 只按三类主线浏览；未归类的小型、评测与相邻来源保留在[全量论文总表](docs/paper-master-list.md)。

各主类按记录日期倒序排列；完整核查、证据和未归类来源见注释表。

<a id="papers-worldcoder"></a>
### 01 · WorldCoder-type · 程序化动力学

*纯状态层面的可执行动力学：转移机制、世界程序归纳、规划与模型修复，不生成外观。*

- **Algebraic World Model: From Exploration to Proofs** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.40503-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.40503)
  <br><sub>通过可执行 Python 假设、类型化规则和 Lean 证明探索未知游戏中的可达性与不可达性。</sub>

- **PhysEvolve: Verifier-grounded Self-evolution for Physical Reasoning with Executable Worlds** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.34921-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.34921)
  <br><sub>由 VLM 提出可执行物理世界，确定性物理引擎验证反事实分支并生成可验证的训练任务。</sub>

- **Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players (AutoTavern)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.33845-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.33845)
  <br><sub>自我改进的研究 agent 构建并验证 Hearthstone Battlegrounds 模拟器，再训练对手和游戏 agent；作为相邻可执行环境工作保留。</sub>

- **LLM Agents as Suppliers of Physical System Models: Calibration and Acceptance in Modelica** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.25019-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.25019)
  <br><sub>研究编码智能体根据描述与数据组合、校准可执行 Modelica 物理系统模型，并以行为拟合、物理不变量与可解释性进行验收。</sub>

- **Neurosymbolic Learning of Interpretable World Models (CGWM)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.19955-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.19955)
  <br><sub>学习视觉概念落地，而无可学习参数的预测器执行给定时序逻辑转移规则；通过符号想象轨迹进行可微规划。</sub>

- **A Declared World Model: Language Models Write the Rules of the Scene They are Shown** `2026` [![Paper](assets/badges/paper.svg)](https://www.preprints.org/manuscript/202610.1139)
  <br><sub>语言模型根据带标签场景图编写世界规则，由确定性引擎检查动作并计算下一状态；实验检验规则能否迁移到未见布局。</sub>

- **Write Once, Plan Many: Building Reusable Visual Planning Systems from One Scene** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.19234-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.19234)
  <br><sub>由给定领域规则和单个练习场景生成可复用渲染、动力学、感知与规划程序，以执行和重建反馈改进，随后冻结复用。</sub>

- **RoleWorld: Knowledge Transfer in World Modeling with Functional Role Abstractions** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.13172-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.13172)
  <br><sub>提取可复用角色原型与可执行转移规则，在新环境中更新角色分配和参数估计，保持已获得的转移规则不变。</sub>

- **Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.11794-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.11794)
  <br><sub>Memento 3 结合轨迹判断与精确回放，修订反思式规则手册和可执行模型。</sub>

- **LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.11253-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.11253)
  <br><sub>LLM-IDEA 通过考虑可辨识性的实验设计，区分不同机制解释。</sub>

- **Kepler: Auditable World Models for ARC-AGI-3** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.00834-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.00834)
  <br><sub>Kepler 通过回溯与条件转移检查以及成本统计，研究可审计的 ARC-AGI-3 世界模型。</sub>

- **Schema: Discovering Unknown Environments via Agentic Program Induction** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.39140-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.39140)
  <br><sub>agent 在持久的程序工作区中以可执行程序表达对未知环境的理解，对照交互历史检验程序，并在逐步验证下基于程序规划（ARC-AGI-3 等游戏）。</sub>

- **EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.35047-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.35047)
  <br><sub>EMPIRIC 学习残差代码，为物理引擎补充缺失的力、约束与隐藏状态。</sub>

- **Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.27549-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.27549)
  <br><sub>Code as Worlds 通过提出、实例化、执行、渲染和验证的循环，发现可执行物理表示。</sub>

- **PDDLCoder: Agentic PDDL Generation for LLM-Assisted Symbolic Planning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.16637-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.16637)
  <br><sub>agent 循环从自然语言生成、分析并修正 PDDL 域与问题，并提供可自动验证计划可执行性的 gym 环境基准。</sub>

- **Twin: Playing an Unknown Game with a Test-Time Digital Twin** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.14490-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.14490)
  <br><sub>Twin 在测试时构建数字孪生，并在未知游戏中选择动作前检查历史转移。</sub>

- **PhysMind: From Video to Executable Worlds for Training-Free Physical Reasoning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.04575-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.04575)
  <br><sub>为每段视频构建一个可复用的可执行世界：重建物体与位姿，拟合解析动力学和潜在物理参数，再通过延续或编辑该世界回答问题。</sub>

- **Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.28287-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.28287)
  <br><sub>Tycho 在求解 ARC-AGI-3 游戏时，主动修订抽象与程序化假设。</sub>

- **VisualPatchWorld: Code World Models as Latent Structured Representations for Planning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.25236-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.25236)
  <br><sub>VisualPatchWorld 从结构化状态—动作轨迹拟合动力学，并利用视觉场景图重新规划。</sub>

- **Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.17540-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.17540)
  <br><sub>将 LLM 生成的仿真器族与神经仿真推断结合，用于机制选择和参数估计。</sub>

- **Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.15439-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.15439)
  <br><sub>在 ARC-AGI-3 编码 agent 中，检验维护可执行模型、简化和回放验证的作用。</sub>

- **When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.14169-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.14169)
  <br><sub>说明 LLM 合成的代码世界模型即使通过转移准确率检验，仍可能因少数关键动力学出错而在博弈中失败；主张以对规划是否够用、而非预测准确率作为验收标准。</sub>

- **World-Time Compute with Verified Code World Models** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.09163-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.09163)
  <br><sub>World-Time Compute 利用经验证的符号代码世界，生成具有精确标签的训练轨迹。</sub>

- **OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.01531-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.01531)
  <br><sub>OPINE-World 通过错误优先探索，联合修订符号本体、转移假设与目标。</sub>

- **Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2606.16070-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.16070)
  <br><sub>Mind-Studio 为部分可观测游戏构建可执行模型，并评价同状态起点的多步前瞻保真度。</sub>

- **PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.30880-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.30880)
  <br><sub>PatchWorld 通过反例引导的补丁优化可执行信念状态模型，并用于动作前瞻。</sub>

- **Distilling Game Code World Model Generation into Lightweight Large Language Models (GameCWM distillation)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.24375-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.24375)
  <br><sub>通过后训练，将前沿 LLM 生成游戏代码世界模型（规则、合法动作、转移、观测与奖励）的能力蒸馏到小模型中。</sub>

- **Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models (Alice / Baba in Wonderland)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.16725-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.16725)
  <br><sub>Alice 在词汇先验错配下学习可执行动力学，以旧行为保持冲突指导假设修订与探索。</sub>

- **Learning POMDP World Models from Observations with Language-Model Priors (Pinductor)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.13740-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.13740)
  <br><sub>LLM 根据少量观测—动作轨迹提出候选 POMDP 世界模型，并以基于信念的似然迭代修正，无需访问隐藏状态。</sub>

- **Executable World Models for ARC-AGI-3 in the Era of Coding Agents** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.05138-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.05138)
  <br><sub>通过历史回放、简化与规划，构建 ARC-AGI-3 的可执行世界模型。</sub>

- **Neuro-Symbolic Synergy for World Modeling (NeSyS)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.10480-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.10480)
  <br><sub>在对方解释不好的转移上交替训练 LLM 世界模型与可执行符号规则，并通过对数线性重排序将两者结合。</sub>

- **Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents (TheoryCoder-2)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.00929-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.00929)
  <br><sub>TheoryCoder-2 在程序合成 agent 中学习和复用规划抽象。</sub>

- **CASSANDRA: Programmatic and Probabilistic Learning and Inference for Stochastic World Modeling** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2601.18620-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.18620)
  <br><sub>面向商业类规划领域，用 LLM 编写的代码建模确定性部分，并以 LLM 引导概率图模型的结构学习来刻画随机变量，组合成转移模型。</sub>

- **Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2512.22336-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.22336)
  <br><sub>Agent2World 通过研究、开发和自适应测试 agent，生成符号世界模型与训练轨迹。</sub>

- **One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration (OneLife)** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2510.12088-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.12088)
  <br><sub>OneLife 从 Crafter-OO 中的无引导探索学习按条件激活的概率法则。</sub>

- **Code World Models for General Game Playing** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2510.04542-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.04542)
  <br><sub>为棋盘和纸牌游戏合成 Python 转移、合法动作、终止检查、价值启发式及隐藏状态推断函数。</sub>

- **Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video (FAE)** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2508.11836-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.11836)
  <br><sub>FAE 利用受约束的响应式 DSL，从游戏视频的精灵网格表示中提取行为程序。</sub>

- **Programmatic Video Prediction Using Large Language Models (ProgGen)** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2505.14948-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.14948)
  <br><sub>让 LLM/VLM 合成程序：估计每帧的符号状态、向前推演并渲染预测状态，以此完成视频帧预测。</sub>

- **PoE-World: Compositional World Modeling with Products of Programmatic Experts** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2505.10819-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.10819)
  <br><sub>PoE-World 将多个程序化专家组合为随机世界模型，支持预测与规划。</sub>

- **LLM-Guided Probabilistic Program Induction for POMDP Model Estimation** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2505.02216-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2505.02216)
  <br><sub>以 LLM 作为先验生成 POMDP 各组成部分（转移、观测、奖励、初始状态）的短概率程序，并依据经验分布修正，实验包括机器人搜索任务。</sub>

- **WALL-E 2.0: World Alignment by NeuroSymbolic Learning improves World Model-based LLM Agents** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2504.15785-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.15785)
  <br><sub>从探索轨迹中提取动作规则、知识图与场景图，编码为可执行代码以校准 LLM 世界模型，并用模型预测控制进行规划。</sub>

- **Synthesizing world models for bilevel planning (TheoryCoder)** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2503.20124-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.20124)
  <br><sub>TheoryCoder 将合成的低层 Python 动力学与给定的高层 PDDL 抽象结合，进行双层规划。</sub>

- **Generating Symbolic World Models via Test-time Scaling of Large Language Models** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2502.04728-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.04728)
  <br><sub>通过 Best-of-N 搜索与细粒度语言化反馈，生成和修正 PDDL 世界模型。</sub>

- **Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search (GIF-MCTS)** `2024` [![arXiv](https://img.shields.io/badge/arXiv-2405.15383-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2405.15383)
  <br><sub>GIF-MCTS 根据描述、离线转移数据和执行反馈，搜索可执行的 Python 世界模型。</sub>

- **WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** `2024` [![arXiv](https://img.shields.io/badge/arXiv-2402.12275-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2402.12275)
  <br><sub>WorldCoder 从交互中合成 Python 转移与奖励模型，将模型一致性与乐观规划结合。</sub>

- **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** `2023` [![arXiv](https://img.shields.io/badge/arXiv-2305.14909-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2305.14909)
  <br><sub>利用 LLM 构建和修正 PDDL 域模型，再通过可靠的外部规划器进行任务规划。</sub>

- **Combining Functional and Automata Synthesis to Discover Causal Reactive Programs (AutumnSynth)** `2023` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3571249)
  <br><sub>AutumnSynth 交替合成转移函数与自动机，恢复包含潜在状态的响应式程序。</sub>

- **Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning (EMPA)** `2021` [![arXiv](https://img.shields.io/badge/arXiv-2107.12544-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2107.12544)
  <br><sub>EMPA 学习概率游戏引擎程序，并通过内部仿真支持探索与规划。</sub>

- **Game Engine Learning from Video** `2017` [![Paper](assets/badges/paper.svg)](https://www.ijcai.org/proceedings/2017/518)
  <br><sub>从视频中学习可执行的游戏引擎规则，以未来状态预测和 agent 训练进行评价。</sub>

[↑ 返回导航](#contents)

<a id="papers-code_as_world"></a>
### 02 · Code-as-World-type · 白模世界 + 生成式渲染

*代码维护白模/proxy 世界的持久状态与规则，由生成式渲染器补全外观。*

- **Fight World Model: Customizable Combat through Visual Interaction Proxies** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.40607-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.40607)
  <br><sub>将可执行的战斗状态和规则解析与视频渲染分开，用绑定身份和时间的交互代理保持攻击、受击与生命状态一致。</sub>

- **Wizard: Manipulate Any World in Real Time via Agentic Control** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.40339-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.40339)
  <br><sub>用骨架和几何代理结合显式游戏状态，支持实时、可泛化的视频世界控制；摘要未证明代码是世界表示。</sub>

- **EdenLive: Real-Time Generative Rendering from Any Visual Reference** `2026` [![Project](assets/badges/project.svg)](https://github.com/VAST-AI-Research/EdenLive)
  <br><sub>生成式渲染器把上游参考视频、目标首帧和提示转换为增强视频；状态和规则由上游程序维护。官方还提供从提示生成可玩游戏的 skill 与工作台。</sub>

- **BoxWorld: Let World Engines Control and Video Generators Render** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.36371-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.36371)
  <br><sub>编码智能体把用户规则写成 Box World Engine，由持久属性和状态变量驱动神经视频渲染，并提出成对状态控制评测。</sub>

- **Mundo: Customized World Model** `2026` [![Project](assets/badges/project.svg)](https://mundo-world-model.github.io/)
  <br><sub>从图像重建可编辑的三维代理场景；场景程序指定对象和物理参数，脚本及通常采用的 MuJoCo 推进状态，代理帧与参考视图共同控制视频渲染。</sub>

- **AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.31466-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.31466)
  <br><sub>把编码智能体生成的游戏 blockout 渲染成保持实体、布局和时序一致的高质量视频；属于 renderer 相邻工作。</sub>

- **SolarRenderer: Few-Step Generative Reference Rendering** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.28630-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.28630)
  <br><sub>通过控制与加速 LoRA 适配冻结视频骨干，将对齐的结构视频转成细节视频，并支持流式生成。</sub>

- **Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.27999-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.27999)
  <br><sub>编码智能体把玩家要求写成游戏代码与规则；引擎维护持久状态，因果视频模型根据低模画面生成细节视图。</sub>

- **State World Models: Execute the Rules, Generate the Pixels** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.26811-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.26811)
  <br><sub>编码智能体生成有类型的游戏定义；运行时先执行语义与空间状态规则，再调用冻结视频渲染器，之后接收与规则兼容的视觉反馈。</sub>

- **Mallea: Building, Steering, and Memorizing Worlds with Coding Agent** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.21283-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.21283)
  <br><sub>编码智能体联合构建对象结构与规则，支持保留未受影响状态的运行时编辑，并结合执行状态与对象纹理记忆进行渲染。</sub>

- **Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation (ATAS)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.20571-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.20571)
  <br><sub>将剧本编译为带空间和事件时间引用的镜头请求，检索配准场景与事件记忆，并在检查通过后将生成观测写入记忆。</sub>

- **Generative World Simulation with DAO and JING (DAO + JING)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.19726-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.19726)
  <br><sub>DAO 在交互规则和世界时间下维护共享角色、物体与空间状态，JING 为不同观察者生成视听体验。</sub>

- **From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction (DR-WM)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.17630-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.17630)
  <br><sub>结合 RGB 场景重建、真实动作响应校准的地形接触先验与物理仿真，以模拟运动和几何指导视频世界模型。</sub>

- **StreamRender-H3: Interactive Coding Worlds with Real-time Streaming Diffusion Render** `2026` [![Project](assets/badges/project.svg)](https://nvlabs.github.io/Sana/Sol-Engine/StreamRender-H3/)
  <br><sub>three.js 游戏引擎维护地图、规则和状态，并根据玩家输入推进；语义帧连接引擎和流式 MiniMax-H3 渲染器，构成执行式模拟与生成外观分离的系统。</sub>

- **AgentGarten: Code Worlds for Evolving Agents** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.12374-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.12374)
  <br><sub>AgentGarten 将程序定义的仿真后端连接到共享实时渲染器，并复用 agent 的文字技能手册。</sub>

- **Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.01614-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.01614)
  <br><sub>编码智能体与轻量引擎维护可扩展世界状态表，生成粗粒度视觉条件，并纳入新出现的对象以支持持续交互。</sub>

- **Code Plans, Diffusion Renders: Open-Ended Generative World Modeling (CoDeR)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.26458-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.26458)
  <br><sub>CoDeR 协调可执行白盒世界的构建与生成式 Artist，创建开放式视觉世界。</sub>

- **GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.25652-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.25652)
  <br><sub>GameDirector 利用视觉情境估计和显式玩法规则，控制游戏视频生成。</sub>

- **Programmable World Model** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.10540-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.10540)
  <br><sub>Programmable World Model 将包含非视觉事实的持久引擎状态，编译为视频生成控制信号。</sub>

- **Magpie: Real-Time World Renderer for Interactive Games** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.27168-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.27168)
  <br><sub>Magpie 将持久的游戏引擎状态与规则，连接到由白盒观测驱动的交互式神经渲染器。</sub>

- **Code World Model: Coding Agent as World Brain** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.25927-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.25927)
  <br><sub>Code World Model 通过可执行代理表示，连接编码世界大脑与视觉世界引擎。</sub>

- **VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.27380-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.27380)
  <br><sub>coding agent 编写描述场景及其时间演化的 Blender 程序，执行得到确定性的时空草稿，再由视频模型生成最终视频。</sub>

- **RealWonder: Real-Time Physical Action-Conditioned Video Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2603.05449-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2603.05449)
  <br><sub>在单图重建的场景上用物理仿真处理力与机器人动作等 3D 动作，再将仿真得到的光流与 RGB 交给少步视频生成器实时渲染。</sub>

- **Web World Models** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2512.23676-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.23676)
  <br><sub>Web World Models 以类型化 Web 状态和代码定义的规则，支撑持久的生成式世界。</sub>

[↑ 返回导航](#contents)

<a id="papers-vibeworlding"></a>
### 03 · VibeWorlding-type · agentic 3D 世界构建

*代码写出完整 3D 世界（几何、材质、布局，可含物理），由常规渲染器或仿真器执行；包含静态场景。*

- **Gym-Anything for Robotics: Scaling physical simulations with digital agents** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.40565-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.40565)
  <br><sub>把仿真创建视为编码智能体任务，构建并审计 RoboWorld 物理仿真环境；作为 3D/模拟器构建支撑工作收录。</sub>

- **Cinematize from Unreal: Agentic Choreography for Controllable World Simulation (CineU)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.38468-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.38468)
  <br><sub>把 Unreal 工程作为可检查的持久世界，利用智能体生成代码执行并验证操作，通过几何约束、时间线和局部修复完成世界编排。</sub>

- **Learning to Code the World: Harness Evolution for Compositional 3D Reconstruction (SceneEvolve)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.37046-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.37046)
  <br><sub>用可执行代码表示组合式 3D 场景，并在固定模型和执行后端的条件下演化重建 harness。</sub>

- **SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.34745-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.34745)
  <br><sub>通过重建、物理建模、仿真检查和修复，把 3D/4D 采集转换为可交互仿真环境；作为相邻 real-to-sim 工作保留。</sub>

- **SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.32978-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.32978)
  <br><sub>用视觉布局采样、契约引导的 3D 编译和物理稳定性检查生成具身学习环境；作为相邻场景构建工作保留。</sub>

- **WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.31834-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.31834)
  <br><sub>从真实机器人演示构建交互式数字孪生，通过编码智能体迭代修复可执行世界程序并验证物理一致性。</sub>

- **WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.28827-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.28827)
  <br><sub>分层规划预测区域与地块的类型化规格，固定过程生成器将其编译成场景；持久记录保留对象身份、边界约束和编辑，以支持流式加载与重访。</sub>

- **SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.28585-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.28585)
  <br><sub>从单张图像重建物体与布局，通过场景代码编辑、受限位姿搜索和仿真验证，保留物理稳定且与图像对齐的场景配置。</sub>

- **NeoWorld-3: From Pixels to Code-Defined Physical Worlds** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.27690-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.27690)
  <br><sub>通过分层编码智能体、可微参数拟合以及关节与物理检查，从视觉证据重建可编辑几何程序。</sub>

- **InfiniDream: Open-Ended Photorealistic 3D Worlds Through Procedural Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.26853-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.26853)
  <br><sub>用 VLM 驱动符号约束的程序化生成和确定性布局，构建可编辑、可动画化的开放式 3D 世界。</sub>

- **Self-Building Labs** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.23826-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.23826)
  <br><sub>智能体从科学目标、照片和设备信息构建实验室数字孪生、机器人技能与工作流，并通过观测和物理反馈改进场景模型。</sub>

- **3DCodeVerse: Exploring 3D Worlds as Code** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.22341-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.22341)
  <br><sub>将可执行 3D 程序、资产与验证记录组成数据资源，并通过执行检查、几何测量及视觉反馈迭代生成和修正程序。</sub>

- **RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.18835-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.18835)
  <br><sub>基于 Newton 的交互式工具包，将求解器、接触模型与物理参数显式开放给人类和编码智能体，依据观测行为迭代调整操作仿真。</sub>

- **CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.18342-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.18342)
  <br><sub>从每个区域一张航拍图构建可供 agent 操作的参数化 3D 城市，以带实体身份、版本化校验更新的代码状态持久保存。</sub>

- **Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.17651-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.17651)
  <br><sub>将生成的视觉场景编译为具有物理属性的 MuJoCo 世界，通过仿真器反馈修正可执行动力学与场景设置。</sub>

- **USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.11322-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.11322)
  <br><sub>USDCraft 将输入几何转为可执行建模程序，导出具有关节结构的 USD 仿真资产。</sub>

- **Code2Games: Enabling Coding Agents for Gaming World Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.05033-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.05033)
  <br><sub>根据游戏意图，在生成的 Blender 世界上规划玩法，迁移到 Unreal Engine 5，并依据编译与运行时反馈修复，得到可玩的游戏世界。</sub>

- **LEGO-Anything: Coding Agents for 3D Scene Reconstruction** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.36380-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.36380)
  <br><sub>LEGO-Anything 将三维场景重建为可执行程序，并分别评价产物有效性、几何和外观。</sub>

- **Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.11499-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.11499)
  <br><sub>Recursive Code World Models 通过递归程序、全局—局部修订和共享参考视图重建复杂场景。</sub>

- **FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.29519-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.29519)
  <br><sub>FuncRoom-Agent 通过递归 DSL、顺序专家模型和执行依据的过程奖励，生成功能性室内场景。</sub>

- **VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.15265-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.15265)
  <br><sub>VibeWorlding 研究多模态 coding agent 如何在 Blender 沙盒中通过资产检索、程序化编辑、渲染反馈与物理可行性检查端到端构建和修改开放式 3D 世界。它的核心任务是世界构建与编辑，不应直接计作时间动力学发现。</sub>

- **WorldClaw: Agentic 3D Open-World Generation at Scale** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.05248-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.05248)
  <br><sub>WorldClaw 通过区域规划、地形生成和渲染反馈，构建大规模可编辑三维场景。</sub>

- **SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.01766-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.01766)
  <br><sub>由规划、编码、审查多智能体编写 Blender 程序，生成含流体、粒子、刚体和关节机构的动态 4D 场景，并依据渲染视频检查运动。</sub>

- **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.19587-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.19587)
  <br><sub>SceneCode 构建可编辑的室内世界程序，包含关节物体、仿真导出与持久场景组织。</sub>

- **SR-Platform: An Agentic Pipeline for Natural Language-Driven Robot Simulation Environment Synthesis** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.14700-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.14700)
  <br><sub>经场景规划、CadQuery 资产合成、受约束布局和 MJCF 组装，将自然语言描述转为可执行的 MuJoCo 环境。</sub>

- **ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.14398-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.14398)
  <br><sub>ChronoAgentic 结合规划、编码、视觉审阅与轨迹检查，构建 PyChrono 仿真程序。</sub>

- **SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.09423-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.09423)
  <br><sub>自我演化的 coding agent 编写并运行 Unreal Engine 代码，根据语言或图像指令构建带可验证任务的物理具身环境。</sub>

- **Code2Worlds: Empowering Coding LLMs for 4D World Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.11757-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.11757)
  <br><sub>Code2Worlds 生成用于四维仿真的物体与场景程序，并结合 Blender 动力学与视觉运动反馈。</sub>

- **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.10116-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.10116)
  <br><sub>agent 将布局与物体生成器和语义、真实感、物理稳定性评估器结合，大规模生成面向具身任务的可仿真场景。</sub>

- **Imagine a City: CityGenAgent for Procedural 3D City Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.05362-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.05362)
  <br><sub>从语言出发，以街区程序和建筑程序分层生成 3D 城市，并用监督微调与强化学习保证程序有效且语义一致。</sub>

- **Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2510.16147-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.16147)
  <br><sub>研究程序化场景表示，以及通过程序搜索进行错误修正的方法。</sub>

- **Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2504.05482-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.05482)
  <br><sub>研究命令式与声明式场景程序的表示差异，以及基于程序的错误修正。</sub>

- **SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements** `2024` [![arXiv](https://img.shields.io/badge/arXiv-2408.02211-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2408.02211)
  <br><sub>SceneMotifCoder 从少量视觉示例中学习可编辑的物体排列程序。</sub>

- **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code** `2024` [![arXiv](https://img.shields.io/badge/arXiv-2403.01248-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.01248)
  <br><sub>SceneCraft 将场景蓝图转为 Blender 代码，并利用渲染反馈迭代修正。</sub>

- **Open-Universe Indoor Scene Generation using LLM Program Synthesis and Uncurated Object Databases** `2024` [![arXiv](https://img.shields.io/badge/arXiv-2403.09675-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2403.09675)
  <br><sub>基于未精选的物体数据库，合成可执行的室内场景布局约束。</sub>

- **Holodeck: Language Guided Generation of 3D Embodied AI Environments** `2023` [![arXiv](https://img.shields.io/badge/arXiv-2312.09067-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2312.09067)
  <br><sub>Holodeck 通过空间约束与优化构建语言驱动的三维具身环境。</sub>

- **Infinite Photorealistic Worlds Using Procedural Generation (Infinigen)** `2023` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html)
  <br><sub>Infinigen 通过程序化规则生成世界尺度的逼真几何与材质。</sub>

- **ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis** `2020` [![arXiv](https://img.shields.io/badge/arXiv-2009.08026-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2009.08026)
  <br><sub>ShapeAssembly 以层次化参数装配程序表示三维部件结构。</sub>

- **CSGNet: Neural Shape Parser for Constructive Solid Geometry** `2018` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html)
  <br><sub>CSGNet 将视觉形状解析为可执行的构造实体几何程序。</sub>

- **Procedural content generation for games** `2013` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/2422956.2422957)
  <br><sub>游戏程序化内容生成的历史参考文献；本轮核查书目信息。</sub>

[↑ 返回导航](#contents)

<a id="papers-other"></a>
### 其他

*不属于三类主线的记录，分为 GUI 世界模型与评测基准两组。*

<a id="papers-other-gui"></a>
#### GUI 世界模型 (20)

*GUI、网页与 computer-use 世界模型，包括以可渲染代码预测下一屏的工作；不纳入三类主线。*

<details>
<summary>20 条记录</summary>

- **Agent World Model in the Wild: Computer-Use Agent Environment Synthesis (WildAWM)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.26828-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.26828)
  <br><sub>合成贯通 GUI、MCP 和 CLI 的可执行计算机环境，以可重放状态构建程序和基于执行的任务、验证器质量门控支持智能体训练。</sub>

- **Beyond Next-Screen Prediction: The Decision Value of GUI World Models** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.24372-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.24372)
  <br><sub>控制预测呈现方式和监督条件，对比 GUI 前瞻预测与直接动作排序器，检验预测画面对决策的增量价值。</sub>

- **Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.11942-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.11942)
  <br><sub>研究以 GUI 世界模型验证状态转移，并区分界面相似度与转移正确性。</sub>

- **AutoGUIWorld: Image Generators as Visual World Models for GUI Agent** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.01215-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.01215)
  <br><sub>AutoGUIWorld 通过规划视觉后果并迭代编辑截图，合成 GUI 交互轨迹。</sub>

- **The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models (StateAliasBench)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.32679-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.32679)
  <br><sub>StateAliasBench 配对可见 GUI 条件相同、未来却不同的案例，诊断隐藏转移状态。</sub>

- **WebWorld: The Browser as a World Model for Self-Improving Web Code** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.30530-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.30530)
  <br><sub>通过浏览器执行与验证自改进 Web 代码，检查交互合同及已有行为的保持。</sub>

- **GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.00048-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.00048)
  <br><sub>GUI-CC 结合离线参考动作与在线 agent 闭环，评价多步上下文一致性。</sub>

- **AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2608.05891-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2608.05891)
  <br><sub>AppDeltaWorld 结合检索结构、视觉资产与闭环修订，预测由动作转移约束的 HTML 更新。</sub>

- **SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2607.15550-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2607.15550)
  <br><sub>利用预测语义下一状态的安全增强 GUI 世界模型，在移动 agent 执行前筛查指令并评估动作风险。</sub>

- **OpenComputer: Verifiable Software Worlds for Computer-Use Agents** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.19769-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.19769)
  <br><sub>OpenComputer 提供真实软件环境、结构化状态验证与可审计的任务奖励。</sub>

- **How Mobile World Model Guides GUI Agents?** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2605.10347-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.10347)
  <br><sub>比较文本、图像和可渲染代码表示，分析重建、在线使用及 agent 消费预测的不同方式。</sub>

- **Computer-Using World Model** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.17365-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.17365)
  <br><sub>Computer-Using World Model 先预测文本变化，再生成桌面软件交互后的截图。</sub>

- **WebWorld: A Large-Scale World Model for Web Agent Training** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.14721-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.14721)
  <br><sub>WebWorld 学习大规模网页仿真器，用于 agent 训练。</sub>

- **Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.10090-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.10090)
  <br><sub>合成约 1000 个由代码驱动、数据库支撑的工具环境用于 agent 强化学习，其状态转移比 LLM 模拟的环境更一致。</sub>

- **Code2World: A GUI World Model via Renderable Code Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.09856-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.09856)
  <br><sub>Code2World 结合 AndroidCode、视觉修订与渲染感知学习，生成下一屏 GUI 代码。</sub>

- **Generative Visual Code Mobile World Models (gWorld)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.01576-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.01576)
  <br><sub>gWorld 使用单一视觉语言模型，将移动 GUI 的未来观测预测为可渲染 Web 代码。</sub>

- **InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2601.04126-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.04126)
  <br><sub>大规模生成带可验证任务评估器的多页面功能性网站环境，用于训练 GUI agent。</sub>

- **MobileDreamer: Generative Sketch World Model for GUI Agent** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2601.04035-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2601.04035)
  <br><sub>以文本草图世界模型预测移动 GUI 动作后的状态，供 GUI agent 进行前瞻推演。</sub>

- **MobileWorldBench: Towards Semantic World Modeling For Mobile Agents** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2512.14014-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.14014)
  <br><sub>MobileWorldBench 评价移动环境的语义状态转移及其对 GUI agent 的使用价值。</sub>

- **ViMo: A Generative Visual GUI World Model for App Agents** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2504.13936-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.13936)
  <br><sub>ViMo 通过图形与文本分解建模移动 GUI 的未来观测。</sub>

</details>

<a id="papers-other-benchmark"></a>
#### 评测基准 (28)

*评测基准与诊断研究，按评测对象分组。*

<details>
<summary>28 条记录</summary>

**评测 纯状态动力学（WorldCoder-type）**

- **GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.22708-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.22708)
  <br><sub>以实际执行得到的结果为参照，结合确定性检查与语义评判，测试文本模型对动作后环境响应的预测。</sub>

- **PhySimCode: A Benchmark and Evaluation Method for Physics Video to Code Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.15722-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.15722)
  <br><sub>评测从物理视频到代码的生成：从原始视频推断物理规律与参数，并写出能重现场景的可运行 Python。</sub>

- **WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.08720-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.08720)
  <br><sub>评测 LLM agent 能否在固定仿真框架中实现物理求解器，任务取自 168 个经典图形学论文中的仿真现象。</sub>

- **GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.21562-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.21562)
  <br><sub>GameLogicBench 在多种可复现情景下，以逐仿真 tick 的状态检查验证 Godot 游戏规则。</sub>

- **ScratchWorld: Evaluating If World Models Compute Executable Consequences** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2606.31689-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.31689)
  <br><sub>ScratchWorld 利用可回放验证的 Scratch 转移与变化字段指标，评价可执行后果。</sub>

- **MPMWorlds: Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2606.01538-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.01538)
  <br><sub>二维物质点法仿真数据集，用于比较代码生成与视频扩散在从视频推断物理动力学并外推方面的表现。</sub>

- **PhysCodeBench: Benchmarking Physics-Aware Symbolic Simulation of 3D Scenes via Self-Corrective Multi-Agent Refinement** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2604.23580-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.23580)
  <br><sub>评测将物理现象描述转为仿真代码的能力，依据引擎状态上的守恒残差与专家断言判定物理正确性。</sub>

- **VisPhyWorld: Probing Physical Reasoning via Code-Driven Video Reconstruction** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2602.13294-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2602.13294)
  <br><sub>要求多模态模型编写可执行的仿真代码来重建观测视频，以此评估物理推理，并将物理推断与渲染分开。</sub>

- **Benchmarking World-Model Learning with Environment-Level Queries (WorldTest)** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2510.19788-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2510.19788)
  <br><sub>提出在无奖励探索后用环境层面的查询（可达性、反事实效果等）评估世界模型，并实例化为含 43 个交互式网格环境的 AutumnBench。</sub>

- **Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2502.13092-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.13092)
  <br><sub>Text2World 以多样化域和执行指标评价文本到 PDDL 世界模型的生成。</sub>

**评测 程序到视频的渲染（Code-as-World-type）**

- **Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.28416-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.28416)
  <br><sub>以文本、图像和视频为输入，评估可执行程序生成完整视频的能力，并测量执行、质量、指令对齐与参考保真。</sub>

- **PROWBench: Do Video Models Render What the Program Specifies?** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.02205-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.02205)
  <br><sub>PROWBench 将渲染视频中的事件与可执行程序规格及事件日志进行对齐比较。</sub>

**评测 3D 世界构建（VibeWorlding-type）**

- **3DCodeEdit: Benchmarking Instruction-Guided 3D Program Editing** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.38231-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.38231)
  <br><sub>评测对 Blender 程序的指令驱动编辑，用渲染检查暴露“代码可运行但几何结果错误”的问题。</sub>

- **UnityBench-Mini3D: Evaluating LLM Agents for 3D Game Development in Unity** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.35980-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.35980)
  <br><sub>用 Unity 项目和确定性的里程碑测试评测编码智能体对场景结构、组件配置和运行时行为的处理。</sub>

- **BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.23986-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.23986)
  <br><sub>通过多模态任务要求、渲染视图和任务评分细则，评估智能体创建的可编辑 Blender 场景。</sub>

- **ExeWorldBench: Benchmarking Code-Based Executable 3D World Modeling** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.15166-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.15166)
  <br><sub>评估单个机制、多阶段组合机械系统以及意图驱动的可执行三维世界合成。</sub>

- **WorldBench: Evaluating LLMs on Three.js Voxel World Generation** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.10622-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.10622)
  <br><sub>评测 LLM 编写的 Three.js 体素世界；评判器既探索运行中的世界、又阅读代码，只有两者一致时才计为证据。</sub>

- **Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.04432-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.04432)
  <br><sub>Video2World 从几何、动力学和功能三个方面，评价具身视频到交互世界的重建。</sub>

- **Spec2Game: Can LLMs Generate Complete Playable Games from Detailed Specifications?** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.04253-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.04253)
  <br><sub>评测根据详细游戏规格（含受控规则变体）生成完整 Pygame 项目的能力，区分可执行性与规则是否被忠实实现。</sub>

- **4DCodeBench: Benchmarking Agents on Inverse Graphics of Dynamic Scenes** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.03715-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.03715)
  <br><sub>评测 agent 将视频中的动态场景重建为可执行图形程序（包括形变、流体、断裂等物理仿真）的能力。</sub>

- **WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2606.01869-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.01869)
  <br><sub>WorldCoder-Bench 通过隐藏的运行时行为合同，评价具有物理依据的三维世界构建。</sub>

- **3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2606.01057-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2606.01057)
  <br><sub>评测 VLM agent 根据文本与图像参考在 3D 软件中以代码进行程序化建模的能力，并配有基于人类偏好的排名平台。</sub>

**评测 非代码的视频与学习型世界模型**

- **WorldProbe: When Video World Models Fall Apart under Long-Horizon Spatial Exploration** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.39721-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.39721)
  <br><sub>用目标条件多模态 agent 在线调整相机动作，探测视频世界模型的长时空间一致性。</sub>

- **WMEval: Evaluating Interactive World Models Grounded on Physical Simulations** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.33894-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.33894)
  <br><sub>以 Unity 物理仿真为真值，对交互式世界模型进行感知、状态和物理因果层面的对齐评测。</sub>

- **Events, Not Pixels: Where World Models Get the Return Wrong** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.29435-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.29435)
  <br><sub>在匹配预算下用真实转移替换部分想象转移诊断回报误差；对所测模型，奖励或终止事件比视觉误差大的帧更影响回报。</sub>

- **WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2610.18826-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2610.18826)
  <br><sub>以配对真实执行评估动作条件机器人世界模型，覆盖状态正确性、交互空间对齐、局部交互保真及多视角动作一致性。</sub>

- **Training Object Permanence in World Models (WROP)** `2026` [![arXiv](https://img.shields.io/badge/arXiv-2609.28654-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.28654)
  <br><sub>构建物体恒存与实体性任务的 Blender 生成器，用于训练和考查作为世界模型的视频模型。</sub>

- **WorldModelBench: Judging Video Generation Models As World Models** `2025` [![arXiv](https://img.shields.io/badge/arXiv-2502.20694-b31b1b.svg?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2502.20694)
  <br><sub>WorldModelBench 从指令遵从、物理合理性和人类偏好评价视频世界模型。</sub>

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
