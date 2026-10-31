# Three-family working taxonomy / 三类工作分类

The three families are split along a single axis: **how much of the world the code carries**. WorldCoder-type code carries state and rules only; Code-as-World-type code carries state, rules and a whitebox/proxy world whose appearance comes from a generative renderer; VibeWorlding-type code carries the full 3D world itself. Each catalogue record gets at most one primary family; acquisition source, verification and lifecycle tags remain orthogonal attributes.

三类沿同一条轴划分：**代码承担了世界的多少部分**。WorldCoder-type 只承担状态与规则；Code-as-World-type 承担状态、规则和白模/proxy 世界，外观由生成式渲染器补全；VibeWorlding-type 由代码写出完整的 3D 世界本身。每条记录最多分配一个主类；知识来源、验证方式和生命周期标签仍是正交属性。

| Family / 主类 | Code carries state & rules / 代码负责状态与规则 | Where appearance comes from / 外观来源 |
|---|---|---|
| WorldCoder-type | Yes / 是 | None, or diagnostic visualization only / 无外观，或仅诊断用可视化 |
| Code-as-World-type | Yes / 是 | Generative renderer conditioned on a whitebox/proxy / 由白模或 proxy 条件化的生成式渲染器 |
| VibeWorlding-type | Optional / 可有可无 | The code itself (geometry, materials, layout), via conventional rendering or simulation / 代码本身（几何、材质、布局），经常规渲染或仿真 |

**Domain boundary:** Robotics is not a separate survey family. A robot or physics-engine setting is placed by the same axis; the robot is the evaluation substrate.

**领域边界：** 机器人不是独立主线，涉及机器人或物理引擎的论文同样按上表归类，机器人只是实验载体。

## Placement order / 判定顺序

Apply the questions in order and stop at the first match. / 按顺序判断，命中即停。

1. Is it a GUI, web, or computer-use world model (including renderable-code screen prediction)? → **Other · GUI**
2. Does code hold persistent state and rules while a generative model (video, image, diffusion renderer) produces the observations? → **Code-as-World-type**
3. Does code specify a full 3D world (geometry, assets, layout, articulation, optionally physics) that a conventional renderer or simulator executes? → **VibeWorlding-type**
4. Does code carry state-level dynamics: transitions, legal actions, reward, latent state, simulator residuals, or symbolic/physical worlds without generated appearance? → **WorldCoder-type**
5. Otherwise: benchmarks → **Other · Benchmarks**; surveys → **Related surveys**; anything else is out of scope.

## 1. WorldCoder-type: Programmatic Dynamics / 纯状态

**Question:** Can a program predict what will happen after an action?

The program is the transition mechanism or a structured extension of it. Typical interfaces expose `next_state`, legal actions, reward, termination, latent-state updates, or a simulator-callable residual. Physical worlds whose output is state, trajectories or training labels rather than rendered appearance also belong here (Code as Worlds, PhysEvolve, World-Time Compute). Anchors: WorldCoder, GIF-MCTS, TheoryCoder, PoE-World, OneLife, PatchWorld, the ARC-AGI-3 executable-model papers, and EMPIRIC.

**判据：** 代码的核心职责是把动作映射为后果，或补充已有引擎缺失的因果机制，并且不负责生成外观。渲染若只用于和观测比对、验证假设（如 Code as Worlds），仍归入此类。

## 2. Code-as-World-type: Whitebox Worlds + Generative Rendering / 白模 + 生成式渲染

**Question:** Can executable state and rules govern a world whose appearance a generative model renders?

Code (an engine, state table, game definition, or coding agent) owns entities, persistent state and rules; it exports a whitebox, low-poly proxy, skeleton, box layout, semantic frame, or event record; a video or diffusion renderer turns that proxy into observations. Renderer-side systems built specifically to render such proxies (Magpie, EdenLive, AnyGameRenderer, SolarRenderer) are kept here as the other half of the interface. Anchors: Code World Model, Programmable World Model, CoDeR, GameDirector, AgentGarten, Oneira, Mallea, BoxWorld, State World Models, Matrix-Game 4.0.

**判据：** 代码维护持久状态与规则，但只给出白模/proxy，外观由生成式渲染器补全。如果代码已经写出完整几何与材质、由常规引擎直接渲染，就归入 VibeWorlding-type；如果完全不涉及外观，就归入 WorldCoder-type。

## 3. VibeWorlding-type: Agentic 3D World Construction / 完整 3D

**Question:** Can an agent turn intent, references and tools into a 3D world written in code?

The central output is a constructed or edited 3D world: scene layout, assets, articulation, materials, collision or physical properties, and executable scene code, rendered or simulated by Blender, USD, MuJoCo, PyChrono, Unreal or similar engines. **Static scenes are included** for now, together with their representation lineage (CSGNet, ShapeAssembly, Infinigen, Holodeck, SceneCraft). Simulation-ready world construction formerly listed under Code-as-World-type (Code2Worlds, Code2Worlds-2, SceneCode, ChronoAgentic, WorldStream, CineU) is placed here because conventional engines, not a generative renderer, produce its appearance.

**判据：** coding agent 在 Blender、USD、仿真工具或类似沙盒中写出或修改完整的 3D 世界，外观由代码本身决定。当前版本收录静态场景；可仿真、可交互的世界构建同样属于此类。

## Other and related surveys / 其他与相关综述

Every record outside the three families carries an `unassigned_group`:

- **Other · GUI world models / 其他 · GUI 世界模型** (`"gui"`): GUI, web and computer-use world models, whether they predict text, screenshots or renderable code (gWorld, Code2World, AppDeltaWorld), and their environment-synthesis work. Code here at most carries the predicted observation, not persistent world state, so they do not sit on the three-family axis.
- **Other · Benchmarks / 其他 · 评测基准** (`"benchmark"`): benchmarks and diagnostic studies, with `benchmark_target` naming what they evaluate: `worldcoder` (state-level dynamics), `code_as_world` (program-to-video rendering), `vibeworlding` (3D world construction, including ExeWorldBench and BlenderWorld), or `video_wm` (non-code video and learned world models).
- **Related surveys / 相关综述** (`"survey"`): shown at the top of the README with a `comparison` / `comparison_zh` note on how this survey differs.

Comparator and adjacent records that fit none of these (learned simulators, code-as-skill models) were removed from the corpus on 2026-10-31.

三类之外的每条记录都必须属于以上三组之一：GUI 世界模型、按评测对象分组的评测基准，或放在 README 开头、附"与本综述的区别"说明的相关综述。不属于这三组的对照/相邻工作已于 2026-10-31 从文献库中移除。

## Data files

Assign at most one primary family in `data/classification.json` (and the matching `section` in `data/papers.json`). Every other record must set `unassigned_group` to `"gui"`, `"benchmark"` (plus `benchmark_target`) or `"survey"` (plus `comparison` and `comparison_zh`); the build fails otherwise. Run `python3 scripts/build_catalog.py` to regenerate the READMEs, [paper master list](paper-master-list.md), [classification CSV](../data/classification.csv) and [annotated catalogue](catalogue.md).
