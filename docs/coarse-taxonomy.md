# Three-family working taxonomy / 三类工作分类（初版）

This is the initial editorial map for the survey. It gives each catalogue record one primary family so that the literature can be written as a coherent story; `code_roles`, acquisition source, renderer, verification, and lifecycle tags remain orthogonal attributes.

**Domain boundary:** Robotics is not a separate survey family. A robot or physics-engine setting is included only when the contribution is executable dynamics, a world program, simulator extension, or world construction; the robot is the evaluation substrate. Pure robot control, manipulation policy, or Real2Sim tooling is not core merely because it uses code.

这是综述当前采用的初版主分类。每条记录只分配一个主类，便于组织正文；`code_roles`、知识来源、渲染器、验证方式和生命周期标签仍是正交属性，不被主分类吞掉。

**Domain boundary / 领域边界：** 机器人不是本综述的独立主线。涉及机器人或物理仿真的论文只有在其核心贡献是可执行动力学、世界程序、模拟器扩展或世界构建时才纳入；机器人本体只是实验载体。纯机器人控制、操作策略或 Real2Sim 工具不会因为使用代码就自动进入核心范围。

## 1. WorldCoder-type: Programmatic Dynamics / World Program Induction

**Question:** Can a program predict what will happen after an action?

The program is the transition mechanism or a structured extension of it. Typical interfaces expose `next_state`, legal actions, reward, termination, latent-state updates, or a simulator-callable residual. Evidence comes from interaction, trajectories, experiments, counterexamples, replay, and planning value. WorldCoder, GIF-MCTS, TheoryCoder, PoE-World, OneLife, ARC executable-world-model papers, and EMPIRIC are the main anchors.

**判据：** 如果代码的核心职责是把动作映射为后果，或补充一个已有引擎缺失的因果机制，就放入 WorldCoder-type。输入可以是轨迹、规则、视频或实验；关键是程序承担了可执行的动力学/机制预测，而不是只生成一个外观场景。

## 2. Code-as-World-type: Executable World Programs

**Question:** Can the world continue to exist, update, and be queried because its state and rules are executable?

The output is a persistent world program or an executable environment family. It may contain entities, geometry, physics parameters, rules, state tables, a simulator interface, and a renderer interface. A neural renderer can be attached, but the family assignment follows the persistent executable world substrate. Code as Worlds, Code2Worlds and Code2Worlds-2, Programmable World Model, CoDeR, GameDirector, AgentGarten, Oneira, Mallea, Web World Models, and WorldStream are representative anchors.

**判据：** 如果代码定义或维持了一个可持续运行的世界，包括实体、状态、规则、物理引擎接口或渲染接口，就放入 Code-as-World-type。它可以由文本、图像、视频或 agent 交互得到，也可以是预先设计的程序；重点是世界程序本身成为可复用的环境载体。

## 3. VibeWorlding-type: Agentic 3D World Construction

**Question:** Can an agent turn intent, references, and tools into an editable, simulation-ready 3D world?

The central output is a constructed or edited 3D world: scene layout, assets, articulation, materials, collision or physical properties, and executable scene code. The central evidence is construction quality, editability, geometric/physical feasibility, render feedback, or simulation readiness. VibeWorlding is the naming anchor; Holodeck, SceneCraft, WorldClaw, FuncRoom-Agent, Recursive Code World Models, LEGO-Anything, USDCraft, NeoWorld-3, 3DCodeVerse, and SceneRig are representative entries.

**判据：** 如果 coding agent 主要在 Blender、USD、仿真工具或类似沙盒中检索资产、编写/修改场景程序，并通过渲染或仿真反馈完成 3D 世界构建，就放入 VibeWorlding-type。静态场景构建可以属于这一类，但不能因为可渲染就自动宣称它发现了未知时间动力学。

## Unassigned records / 未归类来源

GUI observation-code models, renderer-only systems, benchmarks, learned simulators without a code-defined world substrate, surveys, and historical representations remain in the corpus without a primary family. They are still part of the master list and can support the survey; they are simply not forced into one of the three main lines.

GUI 观测代码模型、只负责渲染的系统、基准测试、没有代码世界基底的学习型模拟器、综述和表示历史保留在总表中，但不强行分进三条主线。它们仍可作为对照或证据使用。

## How to use the taxonomy in the manuscript

1. Use the three families for the top-level narrative and the master list.
2. Use acquisition source as a second axis: interaction/trajectory induction, specification-driven construction, visual or physical reconstruction, or hybrid evidence.
3. Use execution and rendering as a third axis: symbolic transition, external engine, deterministic scene renderer, neural renderer, or GUI renderer.
4. Use verification as a fourth axis: replay, counterexample repair, simulator-in-the-loop, state-to-render consistency, or downstream agent utility.
5. Assign exactly one primary family in `data/classification.json`. Keep the catalogue section, scope, and mechanism tags as browsing metadata; they are not additional public classification families.

The three family labels are the only public classification layer in this repository. The [paper master list](paper-master-list.md) gives the current one-row-per-record assignment; the structured [classification JSON](../data/classification.json) and [CSV](../data/classification.csv) keep the same three family values; unassigned records have a blank family for filtering.
