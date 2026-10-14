# Evaluation and evidence

A code-centric world model has several interfaces that can be evaluated independently: the program, its transitions, its state, its rendered observations, and the agent that uses them. A useful evaluation reports which interface is tested and what reference establishes correctness.

## Evidence layers

| Layer | Question | Representative sources | Essential controls |
|---|---|---|---|
| Program and runtime validity | Does the artifact run and satisfy the required interface and behavior contracts? | Text2World, WorldCoder-Bench, GameLogicBench | Fixed API, hidden scenarios, repeatability, mutation tests, tool and asset access |
| Target-world transition fidelity | Does the model predict the external world's consequences? | GIF-MCTS, OneLife, Mind-Studio, ARC executable-model studies | One-step and multi-step tests, held-out mechanisms, stochastic outcomes, real interaction budget |
| Persistent and hidden state | Does maintained state capture information that determines future behavior? | ScratchWorld, StateAliasBench, AutumnSynth | Aliased observations, history access, oracle versus inferred state, no-op and copying controls |
| State-to-observation alignment | Do rendered events follow executed world facts? | PROWBench, CombatStateBench within Programmable World Model | Program logs, instance-level event identity, temporal alignment, occlusion, judge calibration |
| Geometry and perceptual quality | Are images, interfaces, geometry, and dynamics faithful to their references? | Video2World, LEGO-Anything, WorldModelBench | Separate geometry, appearance, dynamics, and task functionality |
| Closed-loop consistency | Does the model remain useful as actions and observations accumulate? | GUI-CC, AppDeltaWorld, online model-revision methods | Reference-action and agent-loop tracks, rollout horizon, state reset policy, accumulated error |
| Downstream decision or learning value | Does the model improve the agent using it? | How Mobile World Model Guides GUI Agents?, planning studies, AgentGarten | Frozen or matched policies, training versus inference use, total compute and interaction budgets |
| Resource cost | What does acquiring, maintaining, and consuming the model cost? | Kepler, EMPIRIC, interactive rendering studies | Tokens, wall time, tool calls, samples, renderer throughput, action latency |

These layers form a chain of evidence. Runtime correctness validates execution of an artifact. Target-world fidelity additionally validates the modeled behavior against an external environment. Render alignment connects executed events to visible outcomes. Agent utility tests whether the model supplies decision-relevant information under the chosen budget.

## Benchmarks have different targets

Text2World evaluates generated symbolic domains. WorldCoder-Bench and GameLogicBench evaluate world or game implementations against behavior contracts. Video2World evaluates reconstruction from embodied video. PROWBench evaluates a renderer's adherence to program-specified events. GUI-CC tests contextual consistency across sequences, while StateAliasBench isolates hidden-state ambiguity. ScratchWorld evaluates executable consequences and uses changed-field metrics to address persistent-state copying.

Their scores should be compared within compatible task definitions, splits, interfaces, and resource conditions. A benchmark table should therefore display the evaluated interface and reference signal before its performance columns.

## Conditions that change the interpretation

| Source | Condition to preserve in comparisons |
|---|---|
| TheoryCoder | High-level PDDL abstractions are supplied; low-level dynamics are synthesized. TheoryCoder-2 has a different abstraction-learning target. |
| OneLife | Crafter-OO exposes structured object-oriented state and a pure transition function. |
| PatchWorld | The executable program advances inferred belief state; external fidelity is checked from trajectories. |
| VisualPatchWorld | Structured traces train the dynamics. Visual replanning and oracle-state induction are distinct evaluation conditions. |
| Do Coding Agents Need Executable World Models… | All variants have shell/Python. The verification condition also changes interface discipline and simplification. |
| Tycho | Transition matching and action efficiency need separate reporting; their strongest settings differ. |
| ARC-AGI-3 program studies | Public-game results, held-out mechanisms, and private validation represent different generalization evidence. |
| EMPIRIC | Geometry and object features are supplied; the physical experiment is one Fan-Domino domain demonstration. |
| Programmable World Model | CombatStateBench's death check detects whether a dead character appears, at coarse scene level. |
| PROWBench | Program logs provide event references, but the VLM-based visual judge has not been human-calibrated in the reported study. |
| AgentGarten | Skill reuse includes written playbooks inherited by later pretrained agents. Distinguish this from weight updates and matched-budget RL. |
| Memento 3 | Recursive improvement updates external rulebooks and programs with a frozen base language model. |
| Magpie | Frames per second and action-response latency measure different system properties. |
| MASS | Authoritative state is a runtime ownership choice; its transition engine is learned. |

These conditions belong in shared comparison tables and the argument they affect. Concentrating them here makes the method discussion clearer and keeps claims aligned with the observed experimental setting.

## Recommended comparison matrix

For each detailed method comparison, record:

1. Target task role and program responsibility.
2. Input evidence: descriptions, states, screenshots, video, trajectories, or active experiments.
3. Program origin, transition representation, state estimation, and observation pathway.
4. Feedback and repair mechanism, including regression preservation.
5. Evidence protocol: one-step, multi-step, held-out, counterfactual, or closed-loop.
6. Model and agent versions, environment splits, tools, and total budget.
7. Program correctness, world fidelity, perceptual results, and agent utility as separate outcomes.

The structured catalogue provides bibliographic and high-level mechanism fields. Detailed experimental matrices should be filled from the relevant full-text sections and record the tested configurations alongside any numbers.

## Research questions emerging from the evidence

- **Predictive state:** what history information is sufficient for future transitions when visible observations alias different states?
- **Program-to-render control:** which compiled state facts retain their event identity through a neural renderer over long horizons?
- **Safe model revision:** how can a local update explain new behavior while preserving validated older transitions?
- **Model acquisition value:** under the same total budget, when does building and maintaining a program improve planning or training?

Each question supports explicit interventions, matched comparisons, and a measurable downstream consequence.
