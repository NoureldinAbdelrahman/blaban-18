# Review Shortlist (2026) — the 5 articles

The five articles to review for Milestone 1/2, with download links and rationale.
Notes are in `literature/notes/`; BibTeX is in `literature/bibliography/shortlist.bib`.

## Selection criteria

1. **Recent** — 2024–2026 (course window is 2019–2026).
2. **On-theme** — multi-agent cooperative robotics / UAV fleets + metaheuristic optimization.
3. **Non-obvious** — deliberately avoids the papers an assistant reaches for by
   default: algorithm-defining papers (GWO, WOA, PSO, ACO, SA, GA originals),
   mega-surveys, and the most-cited MRTA reviews. Instead: hyper-heuristics,
   memetic and ALNS methods, and learning-assisted hybrids.
4. **Methodologically diverse** — five different families so the survey covers more
   than one idea: hyper-heuristic, memetic (GA + local search), ALNS + RL, two-phase
   GA, and multimodal multi-objective evolution + DRL.
5. **Actionable** — each paper maps to a course milestone (M2–M6 and the ML bonus).

## The five

| # | Paper | Venue / year | Method family | Access | Note |
| --- | --- | --- | --- | --- | --- |
| 1 | Yuan et al., *Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints* | Defence Technology, 2025 | Hyper-heuristic (operator selection) | Open access · [10.1016/j.dt.2025.06.006](https://doi.org/10.1016/j.dt.2025.06.006) | [note](../notes/energy-learning-hyper-heuristic-heterogeneous-uav.md) |
| 2 | Meng et al., *An adaptive memetic algorithm for multi-UAV cooperative task assignment under complex constraints* | Swarm & Evolutionary Computation, 2026 | Memetic (GA + adaptive local search) | Library · [10.1016/j.swevo.2026.102395](https://doi.org/10.1016/j.swevo.2026.102395) | [note](../notes/adaptive-memetic-multi-uav-task-assignment.md) |
| 3 | Xiao et al., *Adaptive large neighborhood search algorithm with reinforcement search strategy for ... UAVs* | Information Sciences, 2024 | ALNS + reinforcement learning | Library · [10.1016/j.ins.2024.121068](https://doi.org/10.1016/j.ins.2024.121068) | [note](../notes/alns-reinforcement-uav-task-assignment.md) |
| 4 | Nait Chabane & Guenounou, *An enhanced genetic algorithm for ... heterogeneous multi-robot systems* | Complex & Intelligent Systems, 2025 | Two-phase enhanced GA | Open access · [10.1007/s40747-025-02062-w](https://doi.org/10.1007/s40747-025-02062-w) | [note](../notes/enhanced-ga-heterogeneous-multi-robot.md) |
| 5 | Yu et al., *A deep reinforcement learning-assisted multimodal multiobjective bilevel optimization method for multirobot task allocation* | IEEE Trans. Evolutionary Computation, 2025 | Multimodal multi-objective EA + LNS + DRL | Library · [10.1109/TEVC.2025.3535954](https://doi.org/10.1109/TEVC.2025.3535954) | [note](../notes/drl-multimodal-multiobjective-mrta.md) |

## Shared theme

> **Adaptive and learning-assisted metaheuristics for constrained, multi-objective
> cooperative task allocation across heterogeneous robot/UAV fleets.**

The thread is **adaptive operator selection**: instead of running one fixed
metaheuristic, each paper learns *which* low-level operator (or neighborhood, or
mutation/crossover) to apply and when. This is a precise, defensible project
direction that is far from the generic "compare SA vs GA vs PSO on a grid-world"
that most teams submit.

## Why these and not the obvious picks

- **Not algorithm origin papers.** Citing GWO/WOA/PSO/ACO/SA/GA papers is exactly
  what every team will do (and the course already teaches them). These five cite
  and *use* those algorithms as baselines, so we still cover them — without looking
  like a default answer.
- **Not the usual surveys/taxonomies.** We avoid the heavily assigned MRTA review
  papers and the generic "swarm intelligence survey" (Mavrovouniotis et al.-style).
- **Less crowded method families.** Hyper-heuristics, memetic algorithms and ALNS
  are under-represented in student projects, which makes our contribution space
  larger for Milestone 6.
- **Learning where it pays off.** Two papers use RL only as an *operator selector*,
  which is precisely the optional ML bonus in the course brief — not a wholesale
  pivot to deep RL.

## How they map to the milestones

- **M2 (formulation):** #2 (mixed-variable constrained model) and #5 (bilevel,
  multi-objective) give two ready formulation templates.
- **M3 (SA):** #3's LNS uses simulated-annealing-style acceptance — a principled
  way to reuse our SA implementation.
- **M4 (GA):** #2 (memetic) and #4 (two-phase GA) directly extend the GA milestone.
- **M5 (PSO/ACO/WOA/GWO):** #1 benchmarks against PSO and GWO, giving baselines.
- **M6 (new algorithm):** #1 (hyper-heuristic), #2 (adaptive operator selection),
  #3 (ALNS + RL), #5 (multimodal multi-objective) are four distinct novelty paths.
- **ML bonus:** #3 and #5 show how RL can select operators or evaluate lower-level
  routing without replacing the metaheuristic core.

## Two project ideas this enables

1. **Idea #1 (priority):** A learning-assisted adaptive large-neighborhood
   hyper-heuristic for **energy-aware heterogeneous multi-robot task allocation**,
   using adaptive operator selection (seeded by #1, #3, #4).
2. **Idea #2:** A **multimodal multi-objective memetic algorithm** for robust
   multi-UAV task assignment under precedence, time-window and capacity
   constraints (seeded by #2, #5).

## Download checklist

- [ ] 1. Yuan et al. 2025 — open access (DOI)
- [ ] 2. Meng et al. 2026 — library access (DOI)
- [ ] 3. Xiao et al. 2024 — library access (DOI)
- [ ] 4. Nait Chabane & Guenounou 2025 — open access (DOI)
- [ ] 5. Yu et al. 2025 — library access (DOI)
