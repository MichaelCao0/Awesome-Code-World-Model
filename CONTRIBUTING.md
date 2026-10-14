# Contributing literature

The canonical bibliography is `data/papers.json`. README catalogue tables and `papers.bib` are generated from this file. Edit the prose outside the README catalogue markers directly; edit the generated catalogue through the JSON records.

## Adding or updating a paper

1. Open the primary source and verify the exact title, author list, identifier, and first-public date.
2. Read the abstract and the sections needed for the proposed summary. Set `review_depth` to the material actually checked.
3. Search the existing catalogue for its arXiv ID, DOI, title, and aliases. Update an existing record when it is the same source; link related sources with symmetric `related_ids` when their relationship is unresolved.
4. Choose an editorial `section`, a `scope` label, semantic `code_roles`, and lifecycle `tags` using [the taxonomy](docs/taxonomy.md).
5. Write a concise mechanism or relevance summary. Record evaluation conditions that materially affect comparisons in `evidence_notes`.
6. Update `updated_on` and the literature cutoff when appropriate, then regenerate and validate:

```bash
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
git diff --check
```

The builder requires Python 3.9 or later and has no third-party dependencies. Its checks are offline: they validate record structure and generated content. Source verification remains part of the literature review.

## Record fields

| Field | Convention |
|---|---|
| `id` | Versionless arXiv identifier, or a stable descriptive ID for a publisher-only source |
| `citation_key` | Stable BibTeX key; preserve it when the record is updated |
| `title`, `authors` | Exact primary-source title; complete author list in source order |
| `alias` | Optional method or benchmark name, separate from the title |
| `year`, `first_public_date` | Source-publication year and date; date precision may be year, month, or day |
| `source_url`, `arxiv_id`, `doi` | HTTPS primary link and identifiers where available |
| `section` | One reading section from the collection's `sections` list |
| `scope` | `core`, `historical`, `enabling`, `benchmark`, `resource`, `comparator`, `adjacent`, or `survey` |
| `code_roles` | Array containing `transition`, `observation`, both, or neither |
| `tags` | Nonempty list of lowercase lifecycle or use descriptors with hyphens |
| `summary` | A supported mechanism or bibliographic relevance statement |
| `review_depth`, `reviewed_on` | `targeted_fulltext`, `abstract`, or `metadata`; citation-review date |
| `metadata_checked_on` | Optional date of a separate bibliographic metadata refresh |
| `reviewed_version` | Optional arXiv version used for the mechanism review, such as `v1` |
| `evidence_notes` | Optional conditions affecting the interpretation of reported capabilities |
| `related_ids` | Optional links to related catalogue records, mirrored in both records |

## Citation discipline

Use primary sources. Separate first-public dates from conference years and workshop status. Put an exact venue assignment into manuscript citations only after checking its official source. Keep the summary within the checked source's scope: structured-state dynamics, oracle-state conditions, static reconstruction, rendered observations, and real-environment interaction have distinct evidence requirements.

Use `FT`, `A`, and `M` review depth honestly. Preserve method-level counter-evidence relevant to the survey question and compare like-for-like experimental conditions. Counts in this repository describe source records; linked preprints and benchmark components require additional reconciliation before counting independent methods.
