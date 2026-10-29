# Taxonomy & scope

The repository uses one public classification layer with three primary families:

1. **WorldCoder-type — Programmatic Dynamics / World Program Induction:** code predicts action consequences or extends a simulator with executable mechanisms.
2. **Code-as-World-type — Executable World Programs:** code maintains a persistent world, its entities, state, rules, simulator interfaces, or renderer interfaces.
3. **VibeWorlding-type — Agentic 3D World Construction:** an agent constructs or edits an editable, renderable, or simulation-ready 3D world.

Benchmarks, GUI observation-code models, renderer-only systems, historical foundations, surveys, and adjacent work remain in **Other / Benchmarks / Adjacent** when forcing one of the three families would obscure their contribution.

The [three-family guide](coarse-taxonomy.md) defines the placement rules. The [paper master list](paper-master-list.md) gives one primary family for every record, and [data/classification.json](../data/classification.json) stores the same assignment for filtering.

Robotics is not a separate survey family. A robot or physics-engine setting appears only when it supports an executable-dynamics, world-program, or world-construction contribution.
