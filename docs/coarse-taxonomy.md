# Three-family working taxonomy / 三类工作分类（初版）

This is the initial editorial map for the survey. It gives each catalogue record one primary family so that the literature can be written as a coherent story; `code_roles`, acquisition source, renderer, verification, and lifecycle tags remain orthogonal attributes.

这是综述当前采用的初版主分类。每条记录只分配一个主类，便于组织正文；`code_roles`、知识来源、渲染器、验证方式和生命周期标签仍是正交属性，不被主分类吞掉。

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

## Other / Benchmarks / Adjacent

GUI observation-code models, renderer-only systems, benchmarks, learned simulators without a code-defined world substrate, surveys, and historical representations may remain in `other`. They are still part of the catalogue and can support the survey. “Other” means the three-family assignment would obscure the paper’s actual contribution; it does not mean unimportant.

GUI 观测代码模型、只负责渲染的系统、基准测试、没有代码世界基底的学习型模拟器、综述和表示历史可以保留在 `other`。它们仍然属于总目录，并可在相应章节中作为对照或证据使用。

## How to use the taxonomy in the manuscript

1. Use the three families for the top-level narrative and the master list.
2. Use acquisition source as a second axis: interaction/trajectory induction, specification-driven construction, visual or physical reconstruction, or hybrid evidence.
3. Use execution and rendering as a third axis: symbolic transition, external engine, deterministic scene renderer, neural renderer, or GUI renderer.
4. Use verification as a fourth axis: replay, counterexample repair, simulator-in-the-loop, state-to-render consistency, or downstream agent utility.
5. Assign one primary family in `data/classification.json`; record overlap through `roles`, `section`, tags, and the writing crosswalk rather than duplicating a paper in several primary lists.

The family labels are an editorial starting point, not a claim that the papers are mutually exclusive. The [paper master list](paper-master-list.md) gives the current one-row-per-record assignment, while the [classification crosswalk](classification-crosswalk.md) preserves the earlier S/E/O and manuscript-family discussion.
