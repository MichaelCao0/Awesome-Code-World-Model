# Literature review protocol

The initial collection has a literature cutoff of **2026-10-13** and was organized into this repository on **2026-10-14**. The collection answers three questions: what semantics programs carry, how programs are acquired and maintained, and what evaluation establishes their value as world models.

## Search perspectives

| Perspective | Search terms and follow-up routes |
|---|---|
| Executable dynamics and planning | `world model`, `dynamics`, `simulator` with `program`, `symbolic`, `synthesis`, `executable`; game rules, PDDL, hierarchical planning, probabilistic programs, active discovery |
| Visual and physical worlds | `code world model`, `programmable world`, code and rendering, 3D scene programs, simulation construction, inverse graphics; follow-up on proxy state, articulation, and program-to-video interfaces |
| GUI, web, software, and evaluation | Renderable code, next-screen prediction, GUI world models, hidden state, web simulators, software consequences, runtime contracts; follow-up on multi-step consistency and decision utility |

Broad searches were followed by exact-title searches and citation chains, including historical predecessors. Primary retrieval used arXiv abstract pages, scholarly API records, selected full-text sections, Crossref metadata or abstracts, and official IJCAI/CVF proceedings pages. Author projects supplied secondary context where available. A failed or rate-limited search was treated as unavailable retrieval rather than evidence that a paper does not exist.

## Inclusion and positioning

A core method should give code an explicit world-model responsibility: executable transition or mechanism, a renderable observation, or a coupling between execution and observation. Historical programs, scene and asset representations, benchmarks, real environments, and competing neural/textual models are retained with their corresponding scope label when they explain the mechanism or its evidence.

Bibliographic identity is established with exact title, authors, and a stable primary identifier. Method aliases have their own field. Related records remain linked until their version or extension relationship is resolved. Benchmark names within a method paper share its bibliographic record.

## Citation and claim review

| `review_depth` | Material checked | Use in the collection |
|---|---|---|
| `targeted_fulltext` | Metadata, abstract, and sections relevant to the catalogue claim | Interface, mechanism, and selected evaluation conditions |
| `abstract` | Metadata and original abstract | High-level mechanism and relevance |
| `metadata` | Publisher/Crossref bibliographic metadata | Bibliographic context; no extracted method claim |

`reviewed_on` records the citation-review date. `first_public_date` records the date given by the primary metadata, at the precision available. `year` follows that date, and is separate from any conference assignment. Several identifiers have prefixes that differ from the recorded date; those differences are preserved in source notes.

All 86 arXiv records had their current title, author list, and first-public date checked directly against the source on 2026-10-14. `metadata_checked_on` records this refresh separately from the mechanism review. AgentGarten's current author list adds Chengyang Li relative to the reviewed v1; its mechanism review version is recorded explicitly.

Review depth describes citation checking. The collection does not report reproduced experiments. Performance numbers belong in detailed evidence tables with the paper version, task, split, model, feedback, and budget. The concise README summaries emphasize supported mechanisms rather than global rankings.

## Updating the collection

New entries should extend a relevant research question, fill a missing mechanism or evaluation axis, or establish an informative comparison. Verify the source first, choose the semantic roles and lifecycle tags, then add the record and regenerate the catalogue. Revisit affected comparison notes when a new version changes the mechanism or evidence. The initial snapshot is a curated coverage base; completeness is assessed through research-question coverage and citation-chain checks as the manuscript develops.
