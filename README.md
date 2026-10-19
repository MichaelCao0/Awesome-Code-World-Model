<div align="center">

# Code-Centric World Models

**Executable Dynamics · Persistent Worlds · Renderable Observations**

A living literature collection and home for our forthcoming survey.

**English** | [简体中文](README.zh-CN.md)

<!-- BADGES:BEGIN -->

[![Source records](assets/badges/sources.svg)](#paper-collection) [![Reading sections](assets/badges/topics.svg)](#contents) [![Literature cutoff](assets/badges/cutoff.svg)](docs/review-protocol.md) [![Contributions welcome](assets/badges/contributions.svg)](CONTRIBUTING.md)

![Survey arXiv](assets/badges/survey-arxiv.svg) ![Survey Semantic Scholar citations](assets/badges/survey-citations.svg)

<!-- BADGES:END -->

[Survey Hub](docs/survey.md) · [Paper Collection](#paper-collection) · [Taxonomy](docs/taxonomy.md) · [BibTeX](papers.bib) · [Contributing](CONTRIBUTING.md)

<p><img src="./assets/banner.png" alt="Worlds, made executable: code, persistent state, and rendered observations" width="1280"></p>

</div>

Code makes world models **executable, editable, and inspectable**. This collection connects program synthesis, model-based agents, physical simulation, GUI prediction, and controllable visual generation through one question: **what world semantics does code carry?**

## News

- **2026-10-19** — Bilingual READMEs, a PNG cover, reserved survey links, and visual navigation.
- **2026-10-14** — Initial release: 92 source records, structured metadata, BibTeX, and a shared taxonomy and evaluation framework.

## Contents

[Survey & resources](#survey--resources) · [At a glance](#at-a-glance) · [Paper collection](#paper-collection) · [Contributing](#contributing) · [Acknowledgements](#acknowledgements)

<!-- NAVIGATION:BEGIN -->

| Modeling & evaluation | Foundations & context |
|---|---|
| [01 · Executable dynamics & planning](#papers-dynamics) <sub>(23)</sub> | [06 · Scene & asset programs](#papers-scene_programs) <sub>(11)</sub> |
| [02 · Persistent executable worlds](#papers-construction) <sub>(6)</sub> | [07 · Historical foundations](#papers-foundations) <sub>(9)</sub> |
| [03 · Execution meets visual generation](#papers-coupling) <sub>(6)</sub> | [08 · Comparators & adjacent approaches](#papers-comparators) <sub>(20)</sub> |
| [04 · Renderable-code observations](#papers-observation) <sub>(3)</sub> | [09 · Related surveys](#papers-surveys) <sub>(3)</sub> |
| [05 · Benchmarks & verification](#papers-evaluation) <sub>(11)</sub> | [All annotations →](docs/catalogue.md) |

<!-- NAVIGATION:END -->

## Survey & resources

Our survey is **in preparation**. The [survey hub](docs/survey.md) brings together the current outline, conceptual framework, and bibliography, and will host the manuscript and accompanying materials when released.

| Read & explore | Write & contribute |
|---|---|
| [**Taxonomy & scope**](docs/taxonomy.md) — the semantic roles of code | [**Survey outline / 中文大纲**](docs/survey-outline.md) — research questions and chapters |
| [**Evaluation framework**](docs/evaluation.md) — from runtime correctness to agent utility | [**BibTeX bibliography**](papers.bib) — stable citation keys |
| [**Annotated catalogue**](docs/catalogue.md) — dates, scope, review depth, and evidence notes | [**Structured data**](data/papers.json) — source metadata and mechanism tags |

## At a glance

| Code carries… | What it enables | Start with |
|---|---|---|
| **Transitions & mechanisms** | Execute rules, predict consequences, and plan | [WorldCoder](https://arxiv.org/abs/2402.12275), [OneLife](https://arxiv.org/abs/2510.12088), [General Game Playing](https://arxiv.org/abs/2510.04542) |
| **Observations & appearance** | Predict a screen or scene as renderable code | [gWorld](https://arxiv.org/abs/2602.01576), [Code2World](https://arxiv.org/abs/2602.09856), [AppDeltaWorld](https://arxiv.org/abs/2608.05891) |
| **Execution + observation** | Maintain world state and connect it to visual output | [Web World Models](https://arxiv.org/abs/2512.23676), [Programmable World Model](https://arxiv.org/abs/2609.10540), [Magpie](https://arxiv.org/abs/2608.27168) |

Program origin, verification, and downstream use form a second set of attributes. The [taxonomy](docs/taxonomy.md) explains how they connect across branches.

<a id="paper-collection"></a>
## Paper collection

<!-- CATALOG:BEGIN -->

**92 sources** · literature through **2026-10-13**.

Browse by research direction below. [Full annotations, review depth, and evidence notes →](docs/catalogue.md)

Within each section, sources are ordered by their recorded first-public date. Supporting and adjacent branches can be expanded.

<a id="papers-dynamics"></a>
### 01 · Executable dynamics & planning

*Learning rules, abstractions, and mechanisms that can be executed for prediction and planning.*

- **Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11794)
  <br><sub>Memento 3 revises reflective rulebooks and executable models using trajectory judgments and exact replay.</sub>

- **LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11253)
  <br><sub>LLM-IDEA uses identifiability-aware experimental design to distinguish mechanistic explanations.</sub>

- **Kepler: Auditable World Models for ARC-AGI-3** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.00834)
  <br><sub>Kepler studies auditable ARC-AGI-3 world models through retrospective and conditional transition checks and cost accounting.</sub>

- **EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.35047)
  <br><sub>EMPIRIC learns residual code that extends a physics engine with missing forces, constraints, and hidden state.</sub>

- **Twin: Playing an Unknown Game with a Test-Time Digital Twin** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.14490)
  <br><sub>Twin builds a test-time digital twin and checks historical transitions before choosing actions in unknown games.</sub>

- **Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.28287)
  <br><sub>Tycho actively revises abstractions and programmatic hypotheses while solving ARC-AGI-3 games.</sub>

- **VisualPatchWorld: Code World Models as Latent Structured Representations for Planning** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.25236)
  <br><sub>VisualPatchWorld fits dynamics from structured state-action traces and uses visual scene graphs for replanning.</sub>

- **Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.17540)
  <br><sub>Combines LLM-generated simulator families with neural simulation-based inference to select mechanisms and estimate parameters.</sub>

- **OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.01531)
  <br><sub>OPINE-World jointly revises symbolic ontology, transition hypotheses, and goals through error-prioritized exploration.</sub>

- **Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.16070)
  <br><sub>Mind-Studio constructs executable models for partially observable games and evaluates same-state multi-step lookahead fidelity.</sub>

- **PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.30880)
  <br><sub>PatchWorld optimizes executable belief-state models through counterexample-guided patches and uses them for action lookahead.</sub>

- **Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models (Alice / Baba in Wonderland)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.16725)
  <br><sub>Alice learns executable dynamics under misaligned lexical priors, using preservation conflicts to revise hypotheses and guide exploration.</sub>

- **Executable World Models for ARC-AGI-3 in the Era of Coding Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.05138)
  <br><sub>Builds executable ARC-AGI-3 models with history replay, simplification, and planning.</sub>

- **Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents (TheoryCoder-2)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.00929)
  <br><sub>TheoryCoder-2 learns and reuses planning abstractions in program-synthesis agents.</sub>

- **Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2512.22336)
  <br><sub>Agent2World uses research, development, and adaptive testing agents to generate symbolic world models and training trajectories.</sub>

- **One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration (OneLife)** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.12088)
  <br><sub>OneLife learns conditionally activated probabilistic laws from unguided exploration in Crafter-OO.</sub>

- **Code World Models for General Game Playing** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.04542)
  <br><sub>Synthesizes Python transitions, legal moves, termination, value heuristics, and hidden-state inference for board and card games.</sub>

- **Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video (FAE)** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2508.11836)
  <br><sub>FAE extracts sprite-grid behavior programs from gameplay video through a constrained reactive DSL.</sub>

- **PoE-World: Compositional World Modeling with Products of Programmatic Experts** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2505.10819)
  <br><sub>PoE-World composes programmatic experts into a stochastic world model for prediction and planning.</sub>

- **Synthesizing world models for bilevel planning (TheoryCoder)** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2503.20124)
  <br><sub>TheoryCoder combines synthesized low-level Python dynamics with supplied high-level PDDL abstractions for bilevel planning.</sub>

- **Generating Symbolic World Models via Test-time Scaling of Large Language Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2502.04728)
  <br><sub>Generates and corrects PDDL world models with Best-of-N search and fine-grained verbalized feedback.</sub>

- **Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search (GIF-MCTS)** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2405.15383)
  <br><sub>GIF-MCTS searches executable Python world models using descriptions, offline transitions, and execution feedback.</sub>

- **WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2402.12275)
  <br><sub>WorldCoder synthesizes Python transition and reward models from interaction, coupling model consistency with optimistic planning.</sub>

[↑ Contents](#contents)

<a id="papers-construction"></a>
### 02 · Persistent executable worlds

*Constructing interactive worlds, physical simulations, and verified world families.*

- **Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.27549)
  <br><sub>Code as Worlds discovers executable physical representations through propose, instantiate, execute, render, and verify loops.</sub>

- **World-Time Compute with Verified Code World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.09163)
  <br><sub>World-Time Compute uses verified symbolic code worlds to generate exactly labeled trajectories for model training.</sub>

- **SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.19587)
  <br><sub>SceneCode builds editable indoor world programs with articulated objects, simulation exports, and persistent scene organization.</sub>

- **ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.14398)
  <br><sub>ChronoAgentic constructs PyChrono simulation programs using planning, coding, visual review, and trajectory checks.</sub>

- **Code2Worlds: Empowering Coding LLMs for 4D World Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.11757)
  <br><sub>Code2Worlds generates object and scene programs for 4D simulation, using Blender dynamics and visual motion feedback.</sub>

- **Web World Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2512.23676)
  <br><sub>Web World Models uses typed web state and code-defined rules as the substrate for persistent, generative worlds.</sub>

[↑ Contents](#contents)

<a id="papers-coupling"></a>
### 03 · Execution meets visual generation

*Connecting persistent program state to conventional and neural visual output.*

- **AgentGarten: Code Worlds for Evolving Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.12374)
  <br><sub>AgentGarten connects program-defined simulation backends to a shared real-time renderer and reusable agent playbooks.</sub>

- **Code Plans, Diffusion Renders: Open-Ended Generative World Modeling (CoDeR)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.26458)
  <br><sub>CoDeR coordinates executable whitebox world construction with a generative Artist for open-ended visual worlds.</sub>

- **GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.25652)
  <br><sub>GameDirector uses visual situation estimates and explicit gameplay rules to control game-video generation.</sub>

- **Programmable World Model** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.10540)
  <br><sub>Programmable World Model compiles persistent engine state, including nonvisual facts, into controls for video generation.</sub>

- **Magpie: Real-Time World Renderer for Interactive Games** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.27168)
  <br><sub>Magpie combines persistent game-engine state and rules with a whitebox-conditioned interactive neural renderer.</sub>

- **Code World Model: Coding Agent as World Brain** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.25927)
  <br><sub>Code World Model separates a coding world brain from a visual world engine through executable proxy representations.</sub>

[↑ Contents](#contents)

<a id="papers-observation"></a>
### 04 · Renderable-code observations

*Predicting action-conditioned GUI observations through executable rendering code.*

- **AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.05891)
  <br><sub>AppDeltaWorld predicts transition-grounded HTML updates with retrieved structure, visual assets, and closed-loop refinement.</sub>

- **Code2World: A GUI World Model via Renderable Code Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.09856)
  <br><sub>Code2World learns next-GUI code generation with AndroidCode, visual revision, and render-aware learning.</sub>

- **Generative Visual Code Mobile World Models (gWorld)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.01576)
  <br><sub>gWorld predicts mobile GUI observations as renderable web code with a single vision-language model.</sub>

[↑ Contents](#contents)

<a id="papers-evaluation"></a>
### 05 · Benchmarks & verification

*Testing program behavior, state, rendered consequences, and agent-facing consistency.*

- **Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.04432)
  <br><sub>Video2World evaluates video-to-interactive-world reconstruction through geometry, dynamics, and function.</sub>

- **PROWBench: Do Video Models Render What the Program Specifies?** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.02205)
  <br><sub>PROWBench compares rendered video events with executable program specifications and event logs.</sub>

- **The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models (StateAliasBench)** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.32679)
  <br><sub>StateAliasBench pairs identical visible GUI conditions with different futures to diagnose hidden transition state.</sub>

- **GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.21562)
  <br><sub>GameLogicBench checks Godot game rules at every simulation tick across varied reproducible scenarios.</sub>

- **GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.00048)
  <br><sub>GUI-CC evaluates multi-step contextual consistency through offline reference actions and online agent loops.</sub>

- **ScratchWorld: Evaluating If World Models Compute Executable Consequences** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.31689)
  <br><sub>ScratchWorld uses replay-verified Scratch transitions and changed-field metrics to evaluate executable consequences.</sub>

- **WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.01869)
  <br><sub>WorldCoder-Bench tests physically grounded 3D world synthesis using hidden runtime behavior contracts.</sub>

- **OpenComputer: Verifiable Software Worlds for Computer-Use Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.19769)
  <br><sub>OpenComputer provides real software environments with structured state verification and auditable task rewards.</sub>

- **MobileWorldBench: Towards Semantic World Modeling For Mobile Agents** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2512.14014)
  <br><sub>MobileWorldBench evaluates semantic mobile state transitions and their usefulness for GUI agents.</sub>

- **WorldModelBench: Judging Video Generation Models As World Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2502.20694)
  <br><sub>WorldModelBench evaluates video world models using instruction adherence, physical plausibility, and human preferences.</sub>

- **Text2World: Benchmarking Large Language Models for Symbolic World Model Generation** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2502.13092)
  <br><sub>Text2World evaluates text-to-PDDL world-model generation with diverse domains and execution-based criteria.</sub>

[↑ Contents](#contents)

<a id="papers-scene_programs"></a>
### 06 · Scene & asset programs

*Programmatic geometry, reconstruction, articulation, and scene composition.*

<details>
<summary><strong>Explore 11 sources</strong></summary>

- **USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11322)
  <br><sub>USDCraft converts source geometry into executable modeling programs that export articulated USD simulation assets.</sub>

- **LEGO-Anything: Coding Agents for 3D Scene Reconstruction** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.36380)
  <br><sub>LEGO-Anything reconstructs 3D scenes as executable programs and separates artifact, geometry, and appearance evaluation.</sub>

- **Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.11499)
  <br><sub>Recursive Code World Models reconstruct complex scenes using recursive programs, global-local refinement, and shared reference views.</sub>

- **FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.29519)
  <br><sub>FuncRoom-Agent generates functional indoor scenes with a recursive DSL, sequential expert, and execution-grounded process reward.</sub>

- **WorldClaw: Agentic 3D Open-World Generation at Scale** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.05248)
  <br><sub>WorldClaw builds large editable 3D scenes through region planning, terrain generation, and render-guided refinement.</sub>

- **Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.16147)
  <br><sub>Studies procedural scene programs and error correction through program search.</sub>

- **Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2504.05482)
  <br><sub>Studies imperative and declarative scene-program representations and program-based error correction.</sub>

- **SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2408.02211)
  <br><sub>SceneMotifCoder learns editable object-arrangement programs from a few visual examples.</sub>

- **SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2403.01248)
  <br><sub>SceneCraft translates scene blueprints into Blender code and refines them with rendered visual feedback.</sub>

- **Open-Universe Indoor Scene Generation using LLM Program Synthesis and Uncurated Object Databases** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2403.09675)
  <br><sub>Open-Universe Indoor Scene Generation synthesizes executable layout constraints over uncurated object databases.</sub>

- **Holodeck: Language Guided Generation of 3D Embodied AI Environments** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2312.09067)
  <br><sub>Holodeck builds language-guided 3D embodied environments through spatial constraints and optimization.</sub>

</details>

[↑ Contents](#contents)

<a id="papers-foundations"></a>
### 07 · Historical foundations

*Earlier executable dynamics, program induction, and procedural representations.*

<details>
<summary><strong>Explore 9 sources</strong></summary>

- **Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2305.14909)
  <br><sub>Uses LLMs to construct and correct PDDL domain models for sound model-based task planning.</sub>

- **Combining Functional and Automata Synthesis to Discover Causal Reactive Programs (AutumnSynth)** `2023` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3571249)
  <br><sub>AutumnSynth alternates transition-function synthesis and automata synthesis to recover reactive programs with latent state.</sub>

- **Infinite Photorealistic Worlds Using Procedural Generation (Infinigen)** `2023` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html)
  <br><sub>Infinigen provides procedural rules for generating photorealistic geometry and materials at world scale.</sub>

- **Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning (EMPA)** `2021` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2107.12544)
  <br><sub>EMPA learns probabilistic game-engine programs and runs internal simulations for exploration and planning.</sub>

- **ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis** `2020` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2009.08026)
  <br><sub>ShapeAssembly represents 3D part structure with hierarchical parametric assembly programs.</sub>

- **DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning** `2020` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2006.08381)
  <br><sub>DreamCoder supplies a program-induction and reusable-library-learning foundation for compositional representations.</sub>

- **CSGNet: Neural Shape Parser for Constructive Solid Geometry** `2018` [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html)
  <br><sub>CSGNet parses visual shapes into executable constructive-solid-geometry programs.</sub>

- **Game Engine Learning from Video** `2017` [![Paper](assets/badges/paper.svg)](https://www.ijcai.org/proceedings/2017/518)
  <br><sub>Learns executable game-engine rules from video and evaluates future-state prediction and agent training.</sub>

- **Procedural content generation for games** `2013` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/2422956.2422957)
  <br><sub>Historical reference on procedural content generation for games; bibliographic metadata reviewed.</sub>

</details>

[↑ Contents](#contents)

<a id="papers-comparators"></a>
### 08 · Comparators & adjacent approaches

*Alternative state representations, learned simulators, and neighboring mechanisms.*

<details>
<summary><strong>Explore 20 sources</strong></summary>

- **Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.11942)
  <br><sub>Studies GUI world models as transition verifiers and separates screen similarity from transition correctness.</sub>

- **Software World Models: From Consequence Prediction to Decision Value** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.04940)
  <br><sub>Software World Models predicts consequences of code edits and evaluates their value for decisions.</sub>

- **AutoGUIWorld: Image Generators as Visual World Models for GUI Agent** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2610.01215)
  <br><sub>AutoGUIWorld synthesizes GUI trajectories by planning visual consequences and iteratively editing screenshots.</sub>

- **Agent-Editing World Model: Rethinking World Modeling for LLM Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.28416)
  <br><sub>Agent-Editing World Model models editable agent reasoning and task continuation as an adjacent world-model formulation.</sub>

- **Discriminative World Models for Web Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.02885)
  <br><sub>Discriminative World Models evaluates predicted states through their ability to distinguish web actions.</sub>

- **WebWorld: The Browser as a World Model for Self-Improving Web Code** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.30530)
  <br><sub>Uses the browser to execute and verify self-improving web code against interaction contracts and preserved behaviors.</sub>

- **Learning Simple Test-Time Environments for LLM Web Agents** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.29305)
  <br><sub>TTED learns simple sub-environment observations at test time to improve compositional web-agent generalization.</sub>

- **MASS: Multiplayer World Models with Authoritative Shared State** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2608.06257)
  <br><sub>MASS learns a Logic Engine over authoritative shared state for multiplayer world modeling.</sub>

- **StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.26754)
  <br><sub>StatePlay jointly predicts game states and video, providing a learned-dynamics comparison for explicit code transitions.</sub>

- **Simulate to Generalize: Scaling Stateful Supervision for API-calling Agents using LLM World Models** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.16900)
  <br><sub>Uses language-model simulators to generate stateful API-calling supervision for agents.</sub>

- **Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2607.15439)
  <br><sub>Tests executable-model discipline, simplification, and replay verification in coding agents for ARC-AGI-3.</sub>

- **How Mobile World Model Guides GUI Agents?** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2605.10347)
  <br><sub>Compares text, image, and renderable-code mobile predictions across reconstruction, online use, and agent-consumption strategies.</sub>

- **Computer-Using World Model** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.17365)
  <br><sub>Computer-Using World Model predicts textual changes and then screenshots for desktop software interactions.</sub>

- **WebWorld: A Large-Scale World Model for Web Agent Training** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2602.14721)
  <br><sub>WebWorld learns a large-scale web simulator for agent training.</sub>

- **CWM: An Open-Weights LLM for Research on Code Generation with World Models** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2510.02387)
  <br><sub>FAIR CWM learns computational execution and code-generation behavior through interpreter and container interaction.</sub>

- **ViMo: A Generative Visual GUI World Model for App Agents** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2504.13936)
  <br><sub>ViMo models mobile GUI futures through graphic and textual decomposition.</sub>

- **Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents (WebDreamer)** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2411.06559)
  <br><sub>WebDreamer uses language-model world simulation for planning web-agent actions.</sub>

- **VisualPredicator: Learning Abstract World Models with Neuro-Symbolic Predicates for Robot Planning** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2410.23156)
  <br><sub>VisualPredicator learns task-specific abstract world models using neuro-symbolic predicates for robot planning.</sub>

- **Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation** `2024` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2410.13232)
  <br><sub>Predicts transition-focused natural-language changes for model-based web navigation.</sub>

- **PDSketch: Integrated Planning Domain Programming and Learning** `2023` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2303.05501)
  <br><sub>PDSketch combines programmed transition structure with learned neural details and automatically derived planning heuristics.</sub>

</details>

[↑ Contents](#contents)

<a id="papers-surveys"></a>
### 09 · Related surveys

*Broader perspectives on world modeling, scene generation, and code intelligence.*

<details>
<summary><strong>Explore 3 sources</strong></summary>

- **3D Scene Generation: A Survey** `2026` [![Paper](assets/badges/paper.svg)](https://doi.org/10.1007/s11263-026-02999-6)
  <br><sub>Adjacent survey of 3D scene generation; bibliographic metadata reviewed.</sub>

- **Beyond the Autoregressive Horizon: A Comprehensive Survey of Diffusion Models, World Modelling, and State Space Models for Code** `2026` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2606.23690)
  <br><sub>Adjacent survey connecting diffusion, world modeling, and state-space models in code intelligence.</sub>

- **3D and 4D World Modeling: A Survey** `2025` [![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2509.07996)
  <br><sub>Adjacent survey of 3D and 4D world modeling; useful for comparing modality-based and program-semantics taxonomies.</sub>

</details>

[↑ Contents](#contents)

<!-- CATALOG:END -->

## Contributing

Papers, corrections, and useful comparisons are welcome. See the [contribution guide](CONTRIBUTING.md) for source verification and classification conventions, or [open an issue](https://github.com/MichaelCao0/Code-world-survey/issues/new).

The collection is generated from [data/papers.json](data/papers.json). To update it locally:

```bash
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

<details>
<summary><strong>Source policy & naming guide</strong></summary>

Records link to primary arXiv, DOI, or official proceedings pages. Paper titles and method aliases are stored separately. Dates follow the source metadata; conference years may differ. Review depth and paper-specific experimental conditions are available in the [annotated catalogue](docs/catalogue.md) and [review protocol](docs/review-protocol.md).

| Similar names | Distinction |
|---|---|
| Code2World / Code2Worlds | GUI observation prediction / 4D simulation generation |
| Web World Models / WebWorld | Code-defined persistent worlds / learned web simulation / browser-based code verification; three separate sources |
| WorldCoder / WorldCoder-Bench | Model-based agent / 3D world-synthesis benchmark |
| TheoryCoder / TheoryCoder-2 | Method aliases; their exact publication titles are retained in the bibliography |
| OneLife / General Game Playing | Stochastic dynamics from exploration / executable models from game rules and trajectories |
| FAIR CWM | Neural modeling of computational execution and code generation |

Related preprints are linked in the structured data. Counts describe bibliographic source records, with core methods, historical lineage, enabling representations, benchmarks, and comparators labeled in the annotated catalogue.

</details>

## Acknowledgements

The presentation takes inspiration from [Awesome World Models](https://github.com/knightnemo/Awesome-World-Models). The cover illustration is original to this repository. We thank the authors whose papers and public resources make this collection possible.

<p align="center"><a href="#code-centric-world-models">Back to top ↑</a></p>
