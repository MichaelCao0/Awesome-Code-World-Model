# Taxonomy & scope

The repository uses one public classification layer with three primary families, split by how much of the world the code carries:

1. **WorldCoder-type — Programmatic Dynamics (state only):** code predicts action consequences or extends a simulator with executable mechanisms; it does not produce rendered appearance.
2. **Code-as-World-type — Whitebox Worlds + Generative Rendering:** code maintains persistent state and rules over a whitebox/proxy world, and a generative renderer supplies the appearance.
3. **VibeWorlding-type — Agentic 3D World Construction (full 3D):** an agent writes or edits a complete 3D world in code (geometry, materials, layout, optionally physics), rendered or simulated by conventional engines. Static scenes are included.

Everything else sits under **Other**, split into **GUI world models** (including renderable-code screen predictors such as gWorld and Code2World) and **benchmarks** grouped by what they evaluate. Related surveys are listed at the top of the README with a note on how this survey differs.

The [three-family guide](coarse-taxonomy.md) defines the placement rules. The [paper master list](paper-master-list.md) gives one primary family for every record, and [data/classification.json](../data/classification.json) stores the same assignment for filtering.

Robotics is not a separate survey family. A robot or physics-engine setting appears only when it supports an executable-dynamics, world-program, or world-construction contribution.
