# Two classification schemes: a working comparison

**Discussion draft · 2026-10-26.** This comparison supports writing decisions. The responsibility labels and an alternative chapter order are proposals, not an adopted final taxonomy.

[Three-family working map / 三类主线](coarse-taxonomy.md) · [Paper master list / 全量论文总表](paper-master-list.md) · [Paper-by-paper crosswalk / 逐篇对照表](classification-crosswalk.md) · [CSV](../data/classification.csv) · [Structured annotations](../data/classification.json) · [Writing plan / 写作安排](survey-outline.md)

## Scheme A: manuscript families

| Label | Family / subcategory | Emphasis |
|---|---|---|
| A1 | World Program Induction — Transition Rule Synthesis | Recovering executable transition rules |
| A2 | World Program Induction — Compositional & Stochastic Dynamics | Mechanism structure, stochasticity, transfer |
| A3 | World Program Induction — Feedback-Guided World Model Refinement | Revising models using feedback |
| A4 | World Program Induction — Physical Mechanism Discovery | Inferring physical mechanisms |
| B1 | Executable World Construction — Scene & World Program Construction | Building world programs from requirements |
| B2 | Executable World Construction — Dynamic & Physics-Grounded Simulation | Constructing executable physical environments |
| C1 | Program-Driven World Generation — Code–Neural Hybrid World Models | Explicit worlds and neural observations |
| C2 | Program-Driven World Generation — Renderable-Code Interface Models | Predicting observations as executable code |

The crosswalk distinguishes labels actually printed in the working manuscript's Figure 1 from suggested placements under the same scheme. The separate [three-family working map](coarse-taxonomy.md) is the current top-level writing scaffold: it is intentionally coarser than the manuscript families. Absence from that figure does not mean absence from the manuscript. The unpublished manuscript itself is not distributed here.

A/B describe the modeling objective and reference for correctness; C describes architecture and program responsibility. A2 and A3 also describe properties recurring in A1. Suggested Scheme A labels retain these overlaps rather than silently changing the original definitions.

## Scheme B: program responsibilities

| Label | Responsibility | Operational test |
|---|---|---|
| **S** | **World Specification** | Does the program specify entities, geometry, properties, constraints, or simulator configuration? |
| **E** | **World Evolution** | Does an explicit program or code-backed engine commit state changes that determine later consequences? |
| **O** | **Observation Representation** | Is the predicted observation itself represented as executable rendering code, such as next-screen HTML or a code delta? |

S/E/O describe program components, not a disjoint partition of papers. `primary_role` selects a writing anchor; `roles` retains other responsibilities. The execution provider is separate, so inherited dynamics are not presented as learned rules. Benchmark roles identify evaluated targets; enabling-source roles identify supporting representations. Neither implies a new world-model method.

**S/E boundary.** Setting friction, collision shapes, joints, or initial conditions supplies a world specification. Synthesizing a missing force law or an interaction update supplies evolution logic. An existing engine may execute both. EMPIRIC primarily extends evolution; Code2Worlds-2 primarily compiles and refines simulator specifications. Code as Worlds spans physical specifications and mechanisms.

**E/O boundary.** In a state-driven visual world, code commits state and a renderer realizes it. In a next-screen code predictor, a learned predictor produces observation code. Neural rendering is an interface attribute, not the criterion for O.

**Static 3D boundary.** Scene/asset programs can carry S while remaining enabling work. Renderability, articulation, executable simulation, interaction, and fidelity are distinct properties. Static reconstruction supports the representation discussion without becoming a complete dynamics model.

**Agent boundary.** A coding agent can author mechanisms, maintain a state table, construct scenes, or write an action policy. Assign roles from the artifact and runtime, not from the method name.

The existing catalogue `code_roles` field is a broad browsing index: its `observation` value includes scene/appearance rendering and is not synonymous with the proposed O. The crosswalk is separately curated; do not obtain S/E/O by renaming legacy fields.

## Coarse family fields

`coarse_family` is the initial one-primary-family editorial assignment used by the [paper master list](paper-master-list.md): `worldcoder`, `code_as_world`, `vibeworlding`, or `other`. `source_provenance` records whether an entry is supported by the GitHub catalogue, directly visible in the pasted Feishu text, or explicitly added from a later user request. These fields do not replace S/E/O or the manuscript-family annotations; they provide a stable top-level grouping for drafting and future revision.

## Orthogonal attributes and evidence

| Attribute | Question |
|---|---|
| Modeling basis | Target-world evidence, construction specification, both, or an evaluation protocol? |
| Execution provider | Synthesized program, supplied engine, engine plus residual code, runtime agent plus engine, or learned predictor? |
| Observation interface | No visual requirement, conventional rendering, neural rendering, or executable observation code? |
| Scope | Core, historical, enabling, benchmark/resource, comparator, adjacent, or survey? |
| Writing anchor | Where should the main comparison appear in the retained lifecycle outline? |
| Evidence depth | Metadata, abstract, or targeted full text, as recorded in the bibliography? |

Annotations are editorial interpretations of reviewed sources, not author-provided classes. This update does not imply a fresh full-text review of every old record. Provisional assignments are explicit. State accessibility and quantitative controls should be expanded before manuscript-level performance comparisons.

## 中文判读与写作原则

- 保留当前 lifecycle 章节，先用两套分类对照表检验 Figure 1；分类和章节可以承担不同功能。
- 每篇方法设一个主讲位置，其他章节只比较相关接口，不重复完整介绍。
- Oneira 是 agent 与引擎共同更新状态、视频模型补全细节，适合 E + neural rendering。
- Mallea 同时覆盖 S/E；状态演化、用户编辑与纹理记忆分别承担不同职责。
- Code for 3D 在表示、构建、物理执行中展开；静态几何保留为支撑文献。
- ExeWorldBench 的 S/E 机制评测与 Code2Video-Compass 的视频工程评测分别描述。
- renderer-only 工作没有自动获得 O 或 E；可以作为 C1 的接口支撑文献。

最终是否更换分类图，由边界案例的归类稳定性和正文比较效果决定。
