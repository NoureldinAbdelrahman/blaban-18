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

This repository is the working space for the MCTR 1021 course project on
**metaheuristic optimization for multi-agent cooperative systems** (autonomous
vehicles, UAVs, UGVs, robot fleets). It collects the course requirements, the
literature review, and the Python package where the algorithms are implemented
milestone by milestone.

**No optimization algorithm is implemented yet.** The package tree is a skeleton
with placeholder subpackages; the literature corpus and tooling below are
complete.

## Status

| Area | State |
| --- | --- |
| Course brief parsed into docs | done |
| Curated 21-paper corpus, notes, bibliography | done |
| Proposal drafts and templates | done |
| Python package skeleton + tests | done |
| Problem formulation (M2) | not started |
| SA / GA / swarm / novel algorithms (M3–M6) | not started |

## Repository layout

```
.
├── docs/
│   ├── assets/banner.svg        # repo banner
│   ├── instructions/            # parsed course brief
│   ├── milestones.md            # milestone checklist (1–6)
│   └── templates/               # proposal + literature-note templates
├── literature/
│   ├── papers/                  # 21 curated course PDFs (stable ids)
│   ├── notes/                   # one structured note per paper
│   ├── reviews/                 # literature survey + review tracker
│   └── bibliography/            # catalog.json, references.bib/.md, manifest.csv
├── proposals/                   # idea_1.md, idea_2.md, compiled proposal
├── src/blaban/                  # Python package (skeleton for now)
│   ├── problems/                # problem formulation            (M2)
│   ├── algorithms/
│   │   ├── simulated_annealing/ # SA                             (M3)
│   │   ├── genetic_algorithm/   # GA                             (M4)
│   │   ├── swarm/               # PSO / ACO / WOA / GWO          (M5)
│   │   └── novel/               # new population-based method    (M6)
│   ├── common/                  # shared types, objectives, constraints
│   ├── visualization/           # plotting and animation
│   └── experiments/             # configs + benchmark harness
├── data/{raw,processed}/        # datasets (not tracked)
├── results/{figures,tables,logs}/
├── reports/                     # milestone writeups, IEEE report, poster
├── scripts/                     # literature + bibliography tooling
└── tests/                       # pytest suites
```

## Workflow

1. **Read the brief** — `docs/instructions/project_overview.md`; track progress in
   `docs/milestones.md`.
2. **Review papers** — fill the pre-generated notes in `literature/notes/`
   (template: `docs/templates/literature_note_template.md`), updating
   `status`/`relevance` in each note's frontmatter.
3. **Pick two ideas** — draft `proposals/idea_1.md` and `proposals/idea_2.md`, then
   compile the 2-page `proposals/proposal.md`.
4. **Formulate (M2)** — implement the problem model in `src/blaban/problems/` with
   tests in `tests/`.
5. **Implement algorithms (M3–M6)** under `src/blaban/algorithms/`, running
   experiments from `src/blaban/experiments/` and writing outputs to `results/`.
6. **Report** — keep milestone writeups in `reports/`; final 6-page IEEE-format
   LaTeX paper in `reports/milestone6_final/`.

## Milestones

| Milestone | Deliverable | Where | Weight | Due |
| --- | --- | --- | --- | --- |
| 1 | 2-page proposal (2 ideas) | `proposals/` | 3% | 1 Oct 2026 |
| 2 | Literature survey + formulation | `src/blaban/problems/` | 5% | 8 Oct 2026 |
| 3 | Simulated Annealing | `src/blaban/algorithms/simulated_annealing/` | 6% | 19 Oct 2026 |
| 4 | Genetic Algorithm | `src/blaban/algorithms/genetic_algorithm/` | 8% | 11 Nov 2026 |
| 5 | PSO / ACO / WOA / GWO | `src/blaban/algorithms/swarm/` | 8% | 2 Dec 2026 |
| 6 | Novel metaheuristic + report + poster | `src/blaban/algorithms/novel/` | 10% | 17 Dec 2026 |

## Setup

```bash
git clone https://github.com/NoureldinAbdelrahman/blaban-18.git
cd blaban-18

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -e ".[dev]"      # editable install + pytest/ruff
pytest
```

## Literature tooling

```bash
# Heuristic metadata extraction from the PDFs (review the output)
python scripts/extract_paper_metadata.py

# Rebuild papers/, catalog.json, references.bib/.md, manifest.csv and notes
python scripts/build_bibliography.py            # --force to overwrite notes
```

The canonical metadata lives in the `CURATED` table of
`scripts/build_bibliography.py`; `catalog.json` is generated from it.

## Conventions

- Planned interface: one algorithm per package exposing
  `optimize(problem, **params) -> Result`.
- Experiments should be reproducible from a config; results are generated, not
  hand-edited.
- Run `pytest` before committing (and `ruff check .` once installed).

## Citation

See [`CITATION.cff`](CITATION.cff).

## License

Released under the [MIT License](LICENSE).
