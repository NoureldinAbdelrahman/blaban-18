# Review Shortlist (2026) — the 5 articles

The five articles for Milestones 1–2. **All open access.** Notes are in
`literature/notes/`, PDFs in `literature/papers/`, BibTeX in
`literature/bibliography/shortlist.bib`. Comparison:
[`comparative_summary.md`](comparative_summary.md).

## Selection criteria

Recent (2024–2026), on-theme (cooperative robotics plus metaheuristics), open
access, non-obvious (no algorithm-defining papers, no mega-surveys), diverse
across five method families, and each maps to a course milestone.

## The five

| # | Paper | Venue | Method family | Access | Note |
| --- | --- | --- | --- | --- | --- |
| 1 | Yuan et al., *Energy learning hyper-heuristic … heterogeneous UAVs* | Defence Technology, 2025 | Hyper-heuristic (operator selection) | [Open](https://doi.org/10.1016/j.dt.2025.06.006) | [note](../notes/energy-learning-hyper-heuristic-heterogeneous-uav.md) |
| 2 | Cheng et al., *Adaptive memetic algorithm … multi-robot surveillance* | Complex System Modeling and Simulation, 2024 | Memetic (dual-level local search) | [Open](https://doi.org/10.23919/CSMS.2024.0006) | [note](../notes/adaptive-memetic-multi-robot-surveillance.md) |
| 3 | Qin et al., *Deep reinforcement learning-driven seagull optimization …* | Drones, 2025 | Learning-driven swarm | [Open](https://doi.org/10.3390/drones9060436) | [note](../notes/drl-seagull-multi-uav-task-allocation.md) |
| 4 | Nait Chabane and Guenounou, *Enhanced genetic algorithm … heterogeneous multi-robot systems* | Complex and Intelligent Systems, 2025 | Two-phase genetic algorithm | [Open](https://doi.org/10.1007/s40747-025-02062-w) | [note](../notes/enhanced-ga-heterogeneous-multi-robot.md) |
| 5 | Chen et al., *Bi-subpopulation coevolutionary immune algorithm …* | Complex and Intelligent Systems, 2025 | Coevolutionary immune (multi-objective) | [Open](https://doi.org/10.1007/s40747-024-01720-9) | [note](../notes/coevolutionary-immune-multi-uav-task-allocation.md) |

## Shared theme

**Adaptive, self-selecting metaheuristics for constrained, multi-objective
cooperative task allocation.** Each paper adapts which operator or strategy to
apply and when — the precise direction most teams will not take.

## Milestone mapping

Formulation from 3 and 5; simulated annealing and genetic baselines from 2 and 4;
swarm baselines from 1 and 3; novel algorithm from 1, 3, 5; machine-learning bonus
from 3.

## Project ideas enabled

1. **Priority:** learning-assisted swarm optimization for cooperative agricultural
   ground robots (`proposals/idea_1.md`).
2. **Fallback:** multi-objective coevolutionary planner for planetary-surface
   exploration (`proposals/idea_2.md`).
