<div align="center">
  <img src="docs/assets/banner.svg" alt="BLABAN dessert-inspired project banner" width="100%"/>
</div>

<div align="center">

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-scaffolding-orange.svg)](#status)
[![Tests](https://img.shields.io/badge/tests-pytest-0A9EDC?logo=pytest&logoColor=white)](tests/)
[![Course](https://img.shields.io/badge/course-MCTR%201021-9c27b0.svg)](docs/instructions/project_overview.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-2ea44f.svg)](LICENSE)

**B**io-inspired **L**earning **A**lgorithms for **B**enchmarking **A**gent **N**avigation

*MCTR 1021 — Optimization Techniques for Multi-Cooperative Systems · GUC · Winter 2026 · Team 18*

</div>

---

## What this is

Working space for the MCTR 1021 project on **metaheuristic optimization for
multi-agent cooperative systems**. It holds the course brief, the literature
review, and the Python package where algorithms land milestone by milestone.

**No optimizer is implemented yet** — the package is a skeleton; the literature
corpus and tooling are done.

## Status

Brief parsed · 21-paper corpus, notes, bibliography done · proposal drafts done ·
package skeleton plus tests done · formulation and algorithms (Milestones 2–6) not
started.

## Layout

```
├── docs/            brief, milestones, templates, meeting pack
├── literature/      papers/ · notes/ · reviews/ · bibliography/
├── proposals/       use cases, idea_1, idea_2, compiled proposal
├── src/blaban/      problems/ · algorithms/{simulated_annealing,
│                    genetic_algorithm, swarm, novel} · common/
│                    visualization/ · experiments/
├── data/ results/ reports/ scripts/ tests/
```

## Workflow

1. Brief: `docs/instructions/project_overview.md`; progress: `docs/milestones.md`.
2. Review: fill `literature/notes/`, update each note's `status`/`relevance`.
3. Ideas: draft `proposals/idea_1.md`, `idea_2.md`; compile `proposals/proposal.md`.
4. Formulate (Milestone 2): implement in `src/blaban/problems/` with tests.
5. Algorithms (Milestones 3–6): implement under `src/blaban/algorithms/`, run from
   `src/blaban/experiments/`, write outputs to `results/`.
6. Report: milestone writeups in `reports/`; final IEEE paper in `reports/milestone6_final/`.

## Milestones

| # | Deliverable | Weight | Due |
| --- | --- | --- | --- |
| 1 | 2-page proposal (2 ideas) | 3% | 1 Oct 2026 |
| 2 | Literature survey + formulation | 5% | 8 Oct 2026 |
| 3 | Simulated Annealing | 6% | 19 Oct 2026 |
| 4 | Genetic Algorithm | 8% | 11 Nov 2026 |
| 5 | PSO / ACO / WOA / GWO | 8% | 2 Dec 2026 |
| 6 | Novel metaheuristic + report + poster | 10% | 17 Dec 2026 |

## Setup

```bash
git clone https://github.com/NoureldinAbdelrahman/blaban-18.git && cd blaban-18
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && pip install -e ".[dev]"
pytest
```

## Conventions

- Planned interface: one algorithm per package exposing `optimize(problem, **params)`.
- Experiments reproducible from a config; results generated, never hand-edited.
- Run `pytest` before committing (`ruff check .` once installed).
- Literature metadata lives in the `CURATED` table of `scripts/build_bibliography.py`.

## Citation and license

See [`CITATION.cff`](CITATION.cff). Released under the [MIT License](LICENSE).
