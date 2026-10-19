# Annotated catalogue

<!-- Generated from data/papers.json. -->

[← Browse the paper collection](../README.md#paper-collection) · [Structured data](../data/papers.json) · [BibTeX](../papers.bib)

**92 source records** · literature cutoff **2026-10-13** · metadata snapshot **2026-10-14**.

Review: **FT** = targeted full-text sections · **A** = metadata and abstract · **M** = bibliographic metadata.

Review depth describes citation and mechanism checking. Experimental conditions appear below each table; the [evaluation framework](evaluation.md) explains the shared comparisons.

## Executable dynamics, induction, and planning (23)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-10-08 | [Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks](https://arxiv.org/abs/2610.11794) | Memento 3 revises reflective rulebooks and executable models using trajectory judgments and exact replay. | core | FT |
| 2026-10-08 | [LLM-IDEA: Identifiability-Driven Experimental Agent for Autonomous Discovery of Mechanistic World Models](https://arxiv.org/abs/2610.11253) | LLM-IDEA uses identifiability-aware experimental design to distinguish mechanistic explanations. | adjacent | FT |
| 2026-09-30 | [Kepler: Auditable World Models for ARC-AGI-3](https://arxiv.org/abs/2610.00834) | Kepler studies auditable ARC-AGI-3 world models through retrospective and conditional transition checks and cost accounting. | core | A |
| 2026-09-28 | [EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning](https://arxiv.org/abs/2609.35047) | EMPIRIC learns residual code that extends a physics engine with missing forces, constraints, and hidden state. | core | FT |
| 2026-08-14 | [Twin: Playing an Unknown Game with a Test-Time Digital Twin](https://arxiv.org/abs/2608.14490) | Twin builds a test-time digital twin and checks historical transitions before choosing actions in unknown games. | core | A |
| 2026-07-30 | [Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3](https://arxiv.org/abs/2607.28287) | Tycho actively revises abstractions and programmatic hypotheses while solving ARC-AGI-3 games. | core | A |
| 2026-07-28 | [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/abs/2607.25236) | VisualPatchWorld fits dynamics from structured state-action traces and uses visual scene graphs for replanning. | core | FT |
| 2026-07-20 | [Program Synthesis for Simulation-Based Inference: Joint Model Selection and Parameter Estimation](https://arxiv.org/abs/2607.17540) | Combines LLM-generated simulator families with neural simulation-based inference to select mechanisms and estimate parameters. | adjacent | A |
| 2026-07-01 | [OPINE-World: Programmatic World Modeling with Ontology-error-Prioritized Interactive Exploration for ARC-AGI-3](https://arxiv.org/abs/2607.01531) | OPINE-World jointly revises symbolic ontology, transition hypotheses, and goals through error-prioritized exploration. | core | A |
| 2026-06-14 | [Mind-Studio: Executable World Models with Lookahead Evaluation for Partially Observable Games](https://arxiv.org/abs/2606.16070) | Mind-Studio constructs executable models for partially observable games and evaluates same-state multi-step lookahead fidelity. | core | A |
| 2026-05-29 | [PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments](https://arxiv.org/abs/2605.30880) | PatchWorld optimizes executable belief-state models through counterexample-guided patches and uses them for action lookahead. | core | FT |
| 2026-05-16 | [Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models **(Alice / Baba in Wonderland)**](https://arxiv.org/abs/2605.16725) | Alice learns executable dynamics under misaligned lexical priors, using preservation conflicts to revise hypotheses and guide exploration. | core | A |
| 2026-05-06 | [Executable World Models for ARC-AGI-3 in the Era of Coding Agents](https://arxiv.org/abs/2605.05138) | Builds executable ARC-AGI-3 models with history replay, simplification, and planning. | core | A |
| 2026-01-31 | [Learning Abstractions for Hierarchical Planning in Program-Synthesis Agents **(TheoryCoder-2)**](https://arxiv.org/abs/2602.00929) | TheoryCoder-2 learns and reuses planning abstractions in program-synthesis agents. | core | A |
| 2025-12-26 | [Agent2World: Learning to Generate Symbolic World Models via Adaptive Multi-Agent Feedback](https://arxiv.org/abs/2512.22336) | Agent2World uses research, development, and adaptive testing agents to generate symbolic world models and training trajectories. | core | A |
| 2025-10-14 | [One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration **(OneLife)**](https://arxiv.org/abs/2510.12088) | OneLife learns conditionally activated probabilistic laws from unguided exploration in Crafter-OO. | core | A |
| 2025-10-06 | [Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542) | Synthesizes Python transitions, legal moves, termination, value heuristics, and hidden-state inference for board and card games. | core | A |
| 2025-08-15 | [Finite Automata Extraction: Low-data World Model Learning as Programs from Gameplay Video **(FAE)**](https://arxiv.org/abs/2508.11836) | FAE extracts sprite-grid behavior programs from gameplay video through a constrained reactive DSL. | core | FT |
| 2025-05-16 | [PoE-World: Compositional World Modeling with Products of Programmatic Experts](https://arxiv.org/abs/2505.10819) | PoE-World composes programmatic experts into a stochastic world model for prediction and planning. | core | A |
| 2025-03-26 | [Synthesizing world models for bilevel planning **(TheoryCoder)**](https://arxiv.org/abs/2503.20124) | TheoryCoder combines synthesized low-level Python dynamics with supplied high-level PDDL abstractions for bilevel planning. | core | FT |
| 2025-02-07 | [Generating Symbolic World Models via Test-time Scaling of Large Language Models](https://arxiv.org/abs/2502.04728) | Generates and corrects PDDL world models with Best-of-N search and fine-grained verbalized feedback. | core | FT |
| 2024-05-24 | [Generating Code World Models with Large Language Models Guided by Monte Carlo Tree Search **(GIF-MCTS)**](https://arxiv.org/abs/2405.15383) | GIF-MCTS searches executable Python world models using descriptions, offline transitions, and execution feedback. | core | A |
| 2024-02-19 | [WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment](https://arxiv.org/abs/2402.12275) | WorldCoder synthesizes Python transition and reward models from interaction, coupling model consistency with optimistic planning. | core | FT |

<details>
<summary>Evidence notes (9)</summary>

- **Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks:** Self-improvement updates external rulebooks and programs while the base language model remains frozen.
- **Kepler: Auditable World Models for ARC-AGI-3:** The arXiv comment names a non-archival NeurIPS 2026 workshop; it should not be labeled as a main-conference paper.
- **EMPIRIC: Experiment-Driven Learning of Residual World Models for Robot Planning:** Geometry and object features are supplied; the physical Fan-Domino experiment is one domain demonstration.
- **Tycho: Active Abstraction with Programmatic World Models for ARC-AGI-3:** Improved transition matching and the best action-efficiency result occur under different settings in the reported public-game evaluation.
- **VisualPatchWorld: Code World Models as Latent Structured Representations for Planning:** Dynamics induction uses structured traces. Visual planning and oracle-state induction conditions should be compared separately.
- **PatchWorld: Gradient-Free Optimization of Executable World Models for Agent Environments:** The program maintains inferred belief state; execution consistency and target-world fidelity are separate properties.
- **TheoryCoder-2:** TheoryCoder-2 is the method name. The arXiv first-public date is 2026-01-31 despite the identifier prefix.
- **OneLife:** Uses structured object-oriented Crafter-OO state. Distinct from Code World Models for General Game Playing (2510.04542).
- **TheoryCoder:** TheoryCoder is the method name; the high-level PDDL abstraction is supplied in this work.

</details>

## Persistent executable worlds and physical simulation (6)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-08-27 | [Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning](https://arxiv.org/abs/2608.27549) | Code as Worlds discovers executable physical representations through propose, instantiate, execute, render, and verify loops. | core | FT |
| 2026-07-07 | [World-Time Compute with Verified Code World Models](https://arxiv.org/abs/2609.09163) | World-Time Compute uses verified symbolic code worlds to generate exactly labeled trajectories for model training. | core | A |
| 2026-05-19 | [SceneCode: Executable World Programs for Editable Indoor Scenes with Articulated Objects](https://arxiv.org/abs/2605.19587) | SceneCode builds editable indoor world programs with articulated objects, simulation exports, and persistent scene organization. | core | FT |
| 2026-05-14 | [ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction](https://arxiv.org/abs/2605.14398) | ChronoAgentic constructs PyChrono simulation programs using planning, coding, visual review, and trajectory checks. | core | FT |
| 2026-02-12 | [Code2Worlds: Empowering Coding LLMs for 4D World Generation](https://arxiv.org/abs/2602.11757) | Code2Worlds generates object and scene programs for 4D simulation, using Blender dynamics and visual motion feedback. | core | FT |
| 2025-12-29 | [Web World Models](https://arxiv.org/abs/2512.23676) | Web World Models uses typed web state and code-defined rules as the substrate for persistent, generative worlds. | core | FT |

<details>
<summary>Evidence notes (2)</summary>

- **World-Time Compute with Verified Code World Models:** The first-public date is taken from source metadata (2026-07-07), rather than inferred from the arXiv identifier.
- **Code2Worlds: Empowering Coding LLMs for 4D World Generation:** ICML 2026 is stated on author sources; this catalogue uses the arXiv citation without an independently verified proceedings assignment.

</details>

## Coupling execution with visual generation (6)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-10-08 | [AgentGarten: Code Worlds for Evolving Agents](https://arxiv.org/abs/2610.12374) | AgentGarten connects program-defined simulation backends to a shared real-time renderer and reusable agent playbooks. | core | FT |
| 2026-09-22 | [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling **(CoDeR)**](https://arxiv.org/abs/2609.26458) | CoDeR coordinates executable whitebox world construction with a generative Artist for open-ended visual worlds. | core | FT |
| 2026-09-22 | [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652) | GameDirector uses visual situation estimates and explicit gameplay rules to control game-video generation. | core | FT |
| 2026-09-09 | [Programmable World Model](https://arxiv.org/abs/2609.10540) | Programmable World Model compiles persistent engine state, including nonvisual facts, into controls for video generation. | core | FT |
| 2026-08-27 | [Magpie: Real-Time World Renderer for Interactive Games](https://arxiv.org/abs/2608.27168) | Magpie combines persistent game-engine state and rules with a whitebox-conditioned interactive neural renderer. | core | FT |
| 2026-08-26 | [Code World Model: Coding Agent as World Brain](https://arxiv.org/abs/2608.25927) | Code World Model separates a coding world brain from a visual world engine through executable proxy representations. | core | FT |

<details>
<summary>Evidence notes (4)</summary>

- **AgentGarten: Code Worlds for Evolving Agents:** Reported skill reuse includes inherited written playbooks; parameter learning and matched-budget training gains require separate evidence. Mechanism review uses v1; the author list was refreshed from current arXiv metadata on 2026-10-14.
- **Programmable World Model:** CombatStateBench is included in this paper. Its death metric checks a dead character appears, at coarse scene level.
- **Magpie: Real-Time World Renderer for Interactive Games:** Frame throughput and action-response latency measure different aspects of interactivity.
- **Code World Model: Coding Agent as World Brain:** The reported renderer training is a small-scale gameplay study; the real-video pipeline and trained-renderer evidence have different scopes.

</details>

## Renderable-code observation prediction (3)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-08-06 | [AppDeltaWorld: Transition-Grounded Delta Code World Model for Mobile GUI Agents](https://arxiv.org/abs/2608.05891) | AppDeltaWorld predicts transition-grounded HTML updates with retrieved structure, visual assets, and closed-loop refinement. | core | FT |
| 2026-02-10 | [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856) | Code2World learns next-GUI code generation with AndroidCode, visual revision, and render-aware learning. | core | FT |
| 2026-02-02 | [Generative Visual Code Mobile World Models **(gWorld)**](https://arxiv.org/abs/2602.01576) | gWorld predicts mobile GUI observations as renderable web code with a single vision-language model. | core | FT |

<details>
<summary>Evidence notes (2)</summary>

- **Code2World: A GUI World Model via Renderable Code Generation:** Code2World is the GUI paper; Code2Worlds (2602.11757) is the 4D-generation paper.
- **gWorld:** Renderable code represents a predicted observation; browser execution renders that observation.

</details>

## Benchmarks and verification resources (11)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-10-03 | [Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos](https://arxiv.org/abs/2610.04432) | Video2World evaluates video-to-interactive-world reconstruction through geometry, dynamics, and function. | benchmark | FT |
| 2026-10-01 | [PROWBench: Do Video Models Render What the Program Specifies?](https://arxiv.org/abs/2610.02205) | PROWBench compares rendered video events with executable program specifications and event logs. | benchmark | FT |
| 2026-09-26 | [The GUI Is Not the State: Diagnosing State Aliasing in GUI World Models **(StateAliasBench)**](https://arxiv.org/abs/2609.32679) | StateAliasBench pairs identical visible GUI conditions with different futures to diagnose hidden transition state. | benchmark | FT |
| 2026-09-18 | [GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions](https://arxiv.org/abs/2609.21562) | GameLogicBench checks Godot game rules at every simulation tick across varied reproducible scenarios. | benchmark | A |
| 2026-08-30 | [GUI-CC: Benchmarking Contextual Consistency of GUI World Models as Agent Environments](https://arxiv.org/abs/2609.00048) | GUI-CC evaluates multi-step contextual consistency through offline reference actions and online agent loops. | benchmark | FT |
| 2026-06-30 | [ScratchWorld: Evaluating If World Models Compute Executable Consequences](https://arxiv.org/abs/2606.31689) | ScratchWorld uses replay-verified Scratch transitions and changed-field metrics to evaluate executable consequences. | benchmark | A |
| 2026-06-01 | [WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis](https://arxiv.org/abs/2606.01869) | WorldCoder-Bench tests physically grounded 3D world synthesis using hidden runtime behavior contracts. | benchmark | FT |
| 2026-05-19 | [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/abs/2605.19769) | OpenComputer provides real software environments with structured state verification and auditable task rewards. | resource | A |
| 2025-12-16 | [MobileWorldBench: Towards Semantic World Modeling For Mobile Agents](https://arxiv.org/abs/2512.14014) | MobileWorldBench evaluates semantic mobile state transitions and their usefulness for GUI agents. | benchmark | A |
| 2025-02-28 | [WorldModelBench: Judging Video Generation Models As World Models](https://arxiv.org/abs/2502.20694) | WorldModelBench evaluates video world models using instruction adherence, physical plausibility, and human preferences. | benchmark | FT |
| 2025-02-18 | [Text2World: Benchmarking Large Language Models for Symbolic World Model Generation](https://arxiv.org/abs/2502.13092) | Text2World evaluates text-to-PDDL world-model generation with diverse domains and execution-based criteria. | benchmark | A |

<details>
<summary>Evidence notes (3)</summary>

- **PROWBench: Do Video Models Render What the Program Specifies?:** Program logs provide event references; visual adherence is read by a VLM judge that has not been human-calibrated in the paper.
- **WorldCoder-Bench: Benchmarking Physically Grounded 3D World Synthesis:** This is a 2026 world-synthesis benchmark, distinct from the evaluation of WorldCoder (2402.12275).
- **OpenComputer: Verifiable Software Worlds for Computer-Use Agents:** A real-software environment and verification resource, rather than a learned world-model method.

</details>

## Scene and asset programs (11)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-10-08 | [USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation](https://arxiv.org/abs/2610.11322) | USDCraft converts source geometry into executable modeling programs that export articulated USD simulation assets. | enabling | FT |
| 2026-09-28 | [LEGO-Anything: Coding Agents for 3D Scene Reconstruction](https://arxiv.org/abs/2609.36380) | LEGO-Anything reconstructs 3D scenes as executable programs and separates artifact, geometry, and appearance evaluation. | enabling | FT |
| 2026-09-10 | [Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs](https://arxiv.org/abs/2609.11499) | Recursive Code World Models reconstruct complex scenes using recursive programs, global-local refinement, and shared reference views. | enabling | FT |
| 2026-08-30 | [FuncRoom-Agent: Sequential Feed-Forward 3D Functional Indoor Scene Generation](https://arxiv.org/abs/2608.29519) | FuncRoom-Agent generates functional indoor scenes with a recursive DSL, sequential expert, and execution-grounded process reward. | enabling | FT |
| 2026-08-05 | [WorldClaw: Agentic 3D Open-World Generation at Scale](https://arxiv.org/abs/2608.05248) | WorldClaw builds large editable 3D scenes through region planning, terrain generation, and render-guided refinement. | enabling | FT |
| 2025-10-17 | [Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search](https://arxiv.org/abs/2510.16147) | Studies procedural scene programs and error correction through program search. | enabling | A |
| 2025-04-07 | [Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation](https://arxiv.org/abs/2504.05482) | Studies imperative and declarative scene-program representations and program-based error correction. | enabling | A |
| 2024-08-05 | [SceneMotifCoder: Example-driven Visual Program Learning for Generating 3D Object Arrangements](https://arxiv.org/abs/2408.02211) | SceneMotifCoder learns editable object-arrangement programs from a few visual examples. | enabling | A |
| 2024-03-02 | [SceneCraft: An LLM Agent for Synthesizing 3D Scene as Blender Code](https://arxiv.org/abs/2403.01248) | SceneCraft translates scene blueprints into Blender code and refines them with rendered visual feedback. | enabling | FT |
| 2024-02-05 | [Open-Universe Indoor Scene Generation using LLM Program Synthesis and Uncurated Object Databases](https://arxiv.org/abs/2403.09675) | Open-Universe Indoor Scene Generation synthesizes executable layout constraints over uncurated object databases. | enabling | A |
| 2023-12-14 | [Holodeck: Language Guided Generation of 3D Embodied AI Environments](https://arxiv.org/abs/2312.09067) | Holodeck builds language-guided 3D embodied environments through spatial constraints and optimization. | enabling | A |

<details>
<summary>Evidence notes (5)</summary>

- **USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation:** Source geometry is input, executable modeling programs are generated, and articulated USD is the exported artifact.
- **Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs:** The reported reconstruction is static; dynamic behavior belongs to a separate evaluation axis.
- **WorldClaw: Agentic 3D Open-World Generation at Scale:** Scene generation and editable geometry are the reviewed capabilities.
- **Procedural Scene Programs for Open-Universe Scene Generation: LLM-Free Error Correction via Program Search:** Closely related title, authors, and abstract to 2504.05482. Treat the relationship as unresolved when counting distinct methods.
- **Imperative vs. Declarative Programming Paradigms for Open-Universe Scene Generation:** Closely related title, authors, and abstract to 2510.16147. Treat the relationship as unresolved when counting distinct methods.

</details>

## Historical foundations and program representations (9)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2023-05-24 | [Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning](https://arxiv.org/abs/2305.14909) | Uses LLMs to construct and correct PDDL domain models for sound model-based task planning. | historical | FT |
| 2023-01-09 | [Combining Functional and Automata Synthesis to Discover Causal Reactive Programs **(AutumnSynth)**](https://doi.org/10.1145/3571249) | AutumnSynth alternates transition-function synthesis and automata synthesis to recover reactive programs with latent state. | historical | A |
| 2023 | [Infinite Photorealistic Worlds Using Procedural Generation **(Infinigen)**](https://openaccess.thecvf.com/content/CVPR2023/html/Raistrick_Infinite_Photorealistic_Worlds_Using_Procedural_Generation_CVPR_2023_paper.html) | Infinigen provides procedural rules for generating photorealistic geometry and materials at world scale. | enabling | A |
| 2021-07-27 | [Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning **(EMPA)**](https://arxiv.org/abs/2107.12544) | EMPA learns probabilistic game-engine programs and runs internal simulations for exploration and planning. | historical | A |
| 2020-09-17 | [ShapeAssembly: Learning to Generate Programs for 3D Shape Structure Synthesis](https://arxiv.org/abs/2009.08026) | ShapeAssembly represents 3D part structure with hierarchical parametric assembly programs. | enabling | A |
| 2020-06-15 | [DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning](https://arxiv.org/abs/2006.08381) | DreamCoder supplies a program-induction and reusable-library-learning foundation for compositional representations. | enabling | A |
| 2018 | [CSGNet: Neural Shape Parser for Constructive Solid Geometry](https://openaccess.thecvf.com/content_cvpr_2018/html/Sharma_CSGNet_Neural_Shape_CVPR_2018_paper.html) | CSGNet parses visual shapes into executable constructive-solid-geometry programs. | enabling | A |
| 2017 | [Game Engine Learning from Video](https://www.ijcai.org/proceedings/2017/518) | Learns executable game-engine rules from video and evaluates future-state prediction and agent training. | historical | A |
| 2013-02 | [Procedural content generation for games](https://doi.org/10.1145/2422956.2422957) | Historical reference on procedural content generation for games; bibliographic metadata reviewed. | enabling | M |

<details>
<summary>Evidence notes (1)</summary>

- **Procedural content generation for games:** Only bibliographic metadata was reviewed; this entry serves as historical context.

</details>

## Comparators and adjacent approaches (20)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-10-08 | [Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://arxiv.org/abs/2610.11942) | Studies GUI world models as transition verifiers and separates screen similarity from transition correctness. | comparator | A |
| 2026-10-04 | [Software World Models: From Consequence Prediction to Decision Value](https://arxiv.org/abs/2610.04940) | Software World Models predicts consequences of code edits and evaluates their value for decisions. | comparator | A |
| 2026-10-01 | [AutoGUIWorld: Image Generators as Visual World Models for GUI Agent](https://arxiv.org/abs/2610.01215) | AutoGUIWorld synthesizes GUI trajectories by planning visual consequences and iteratively editing screenshots. | comparator | A |
| 2026-09-23 | [Agent-Editing World Model: Rethinking World Modeling for LLM Agents](https://arxiv.org/abs/2609.28416) | Agent-Editing World Model models editable agent reasoning and task continuation as an adjacent world-model formulation. | adjacent | A |
| 2026-09-02 | [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885) | Discriminative World Models evaluates predicted states through their ability to distinguish web actions. | comparator | FT |
| 2026-08-31 | [WebWorld: The Browser as a World Model for Self-Improving Web Code](https://arxiv.org/abs/2608.30530) | Uses the browser to execute and verify self-improving web code against interaction contracts and preserved behaviors. | adjacent | FT |
| 2026-08-29 | [Learning Simple Test-Time Environments for LLM Web Agents](https://arxiv.org/abs/2608.29305) | TTED learns simple sub-environment observations at test time to improve compositional web-agent generalization. | adjacent | A |
| 2026-08-06 | [MASS: Multiplayer World Models with Authoritative Shared State](https://arxiv.org/abs/2608.06257) | MASS learns a Logic Engine over authoritative shared state for multiplayer world modeling. | comparator | FT |
| 2026-07-29 | [StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation](https://arxiv.org/abs/2607.26754) | StatePlay jointly predicts game states and video, providing a learned-dynamics comparison for explicit code transitions. | comparator | FT |
| 2026-07-18 | [Simulate to Generalize: Scaling Stateful Supervision for API-calling Agents using LLM World Models](https://arxiv.org/abs/2607.16900) | Uses language-model simulators to generate stateful API-calling supervision for agents. | comparator | A |
| 2026-07-16 | [Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?](https://arxiv.org/abs/2607.15439) | Tests executable-model discipline, simplification, and replay verification in coding agents for ARC-AGI-3. | comparator | FT |
| 2026-05-11 | [How Mobile World Model Guides GUI Agents?](https://arxiv.org/abs/2605.10347) | Compares text, image, and renderable-code mobile predictions across reconstruction, online use, and agent-consumption strategies. | comparator | FT |
| 2026-02-19 | [Computer-Using World Model](https://arxiv.org/abs/2602.17365) | Computer-Using World Model predicts textual changes and then screenshots for desktop software interactions. | comparator | A |
| 2026-02-16 | [WebWorld: A Large-Scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721) | WebWorld learns a large-scale web simulator for agent training. | comparator | A |
| 2025-09-30 | [CWM: An Open-Weights LLM for Research on Code Generation with World Models](https://arxiv.org/abs/2510.02387) | FAIR CWM learns computational execution and code-generation behavior through interpreter and container interaction. | comparator | A |
| 2025-04-15 | [ViMo: A Generative Visual GUI World Model for App Agents](https://arxiv.org/abs/2504.13936) | ViMo models mobile GUI futures through graphic and textual decomposition. | comparator | A |
| 2024-11-10 | [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents **(WebDreamer)**](https://arxiv.org/abs/2411.06559) | WebDreamer uses language-model world simulation for planning web-agent actions. | comparator | A |
| 2024-10-30 | [VisualPredicator: Learning Abstract World Models with Neuro-Symbolic Predicates for Robot Planning](https://arxiv.org/abs/2410.23156) | VisualPredicator learns task-specific abstract world models using neuro-symbolic predicates for robot planning. | adjacent | A |
| 2024-10-17 | [Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation](https://arxiv.org/abs/2410.13232) | Predicts transition-focused natural-language changes for model-based web navigation. | comparator | A |
| 2023-03-09 | [PDSketch: Integrated Planning Domain Programming and Learning](https://arxiv.org/abs/2303.05501) | PDSketch combines programmed transition structure with learned neural details and automatically derived planning heuristics. | adjacent | A |

<details>
<summary>Evidence notes (4)</summary>

- **MASS: Multiplayer World Models with Authoritative Shared State:** Authoritative state describes runtime ownership. Its transition logic is learned, without handwritten transition functions.
- **Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?:** All compared variants have shell/Python tools. Verification also changes interface and simplification, forming a bundled treatment.
- **CWM: An Open-Weights LLM for Research on Code Generation with World Models:** Code is the computational modeling object here; the environment dynamics are learned by a neural model.
- **PDSketch: Integrated Planning Domain Programming and Learning:** The catalogue year follows the arXiv first-public date (2023); the source comment names NeurIPS 2022.

</details>

## Related surveys (3)

| Date | Paper | Mechanism / relevance | Scope | Review |
|---|---|---|---|---|
| 2026-09 | [3D Scene Generation: A Survey](https://doi.org/10.1007/s11263-026-02999-6) | Adjacent survey of 3D scene generation; bibliographic metadata reviewed. | survey | M |
| 2026-04-09 | [Beyond the Autoregressive Horizon: A Comprehensive Survey of Diffusion Models, World Modelling, and State Space Models for Code](https://arxiv.org/abs/2606.23690) | Adjacent survey connecting diffusion, world modeling, and state-space models in code intelligence. | survey | A |
| 2025-09-04 | [3D and 4D World Modeling: A Survey](https://arxiv.org/abs/2509.07996) | Adjacent survey of 3D and 4D world modeling; useful for comparing modality-based and program-semantics taxonomies. | survey | FT |

<details>
<summary>Evidence notes (1)</summary>

- **3D Scene Generation: A Survey:** Only bibliographic metadata was reviewed; method coverage has not been extracted.

</details>
