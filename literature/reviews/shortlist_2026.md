# Review Shortlist (2026) — the 5 articles

The five articles to review for Milestone 1/2, with download links and rationale.
**All five are open access** — no paywall, no library login. Notes are in
`literature/notes/`; BibTeX is in `literature/bibliography/shortlist.bib`.
A side-by-side comparison is in [`comparative_summary.md`](comparative_summary.md).

## Selection criteria

1. **Recent** — 2024–2026 (course window is 2019–2026).
2. **On-theme** — multi-agent cooperative robotics / UAV & robot fleets + metaheuristic optimization.
3. **Open access** — freely downloadable by every team member.
4. **Non-obvious** — deliberately avoids the papers an assistant reaches for by
   default: algorithm-defining papers (GWO, WOA, PSO, ACO, SA, GA originals),
   mega-surveys, and the most-cited MRTA reviews. Instead: hyper-heuristics,
   memetic methods, learning-driven swarm search, coevolutionary immune search.
5. **Methodologically diverse** — five families, unified by **adaptive operator /
   strategy selection**: hyper-heuristic, memetic, DRL-controlled swarm, two-phase
   GA, and immune coevolution.
6. **Actionable** — each maps to a course milestone (M2–M6 and the ML bonus).

## The five

| # | Paper | Venue / year | Method family | Access | Note |
| --- | --- | --- | --- | --- | --- |
| 1 | Yuan et al., *Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints* | Defence Technology, 2025 | Hyper-heuristic (energy-learning operator selection) | [Open · 10.1016/j.dt.2025.06.006](https://doi.org/10.1016/j.dt.2025.06.006) | [note](../notes/energy-learning-hyper-heuristic-heterogeneous-uav.md) |
| 2 | Cheng et al., *Adaptive memetic algorithm with dual-level local search for cooperative route planning of multi-robot surveillance systems* | Complex System Modeling and Simulation, 2024 | Memetic (GA + dual-level local search) | [Open · 10.23919/CSMS.2024.0006](https://doi.org/10.23919/CSMS.2024.0006) | [note](../notes/adaptive-memetic-multi-robot-surveillance.md) |
| 3 | Qin et al., *A deep reinforcement learning-driven seagull optimization algorithm for ... multi-UAV task allocation in plateau ecological restoration* | Drones (MDPI), 2025 | DRL-controlled swarm optimization | [Open · 10.3390/drones9060436](https://doi.org/10.3390/drones9060436) | [note](../notes/drl-seagull-multi-uav-task-allocation.md) |
| 4 | Nait Chabane & Guenounou, *An enhanced genetic algorithm for ... heterogeneous multi-robot systems* | Complex & Intelligent Systems, 2025 | Two-phase enhanced GA | [Open · 10.1007/s40747-025-02062-w](https://doi.org/10.1007/s40747-025-02062-w) | [note](../notes/enhanced-ga-heterogeneous-multi-robot.md) |
| 5 | Chen et al., *A bi-subpopulation coevolutionary immune algorithm for ... multi-UAV task allocation* | Complex & Intelligent Systems, 2025 | Coevolutionary immune algorithm (multi-objective) | [Open · 10.1007/s40747-024-01720-9](https://doi.org/10.1007/s40747-024-01720-9) | [note](../notes/coevolutionary-immune-multi-uav-task-allocation.md) |

## Shared theme

> **Adaptive, self-selecting metaheuristics for constrained, multi-objective
> cooperative task allocation across heterogeneous robot/UAV fleets.**

Every paper goes beyond running one fixed metaheuristic: each **learns or adapts
which operator/strategy to apply and when** — energy-based operator probabilities
(#1), adaptive local search (#2), a DQN controlling search phases (#3), a two-phase
refinement (#4), and adaptive selection over an evolutionary strategy pool (#5).
That is a precise, defensible project direction, far from the generic "compare
SA vs GA vs PSO on a grid-world" most teams submit.

## Why these and not the obvious picks

- **Not algorithm origin papers.** Citing GWO/WOA/PSO/ACO/SA/GA papers is exactly
  what every team will do (and the course already teaches them). These five cite
  and *use* those algorithms as baselines, so we still cover them — without looking
  like a default answer.
- **Not the usual surveys/taxonomies.** We avoid the heavily assigned MRTA review
  papers and the generic "swarm intelligence survey".
- **Less crowded method families.** Hyper-heuristics, memetic algorithms,
  coevolutionary immune search and DRL-controlled search are under-represented in
  student projects, leaving more room for a genuine Milestone 6 contribution.
- **Learning without leaving metaheuristics.** Only #3 uses RL, and only as a
  *controller* over a swarm optimizer — a natural fit for the optional ML bonus.
- **All open access**, so the whole team can read the full text immediately.

## How they map to the milestones

- **M2 (formulation):** #3 (multi-objective, multi-constraint MOMCCTAP) and #5
  (multi-objective MCOTAP) are ready formulation templates; #2 couples allocation
  with routing.
- **M3 (SA):** #2's dual-level local search and #4's refinement phase are local-search
  components we can pair with our SA implementation.
- **M4 (GA):** #2 (memetic) and #4 (two-phase GA) directly extend the GA milestone;
  #5 supplies coevolutionary population mechanisms.
- **M5 (PSO/ACO/WOA/GWO):** #1 benchmarks against PSO and GWO; #3 benchmarks against
  five swarm algorithms — both provide baselines.
- **M6 (new algorithm):** #1 (hyper-heuristic), #3 (DRL-controlled adaptive selection),
  #5 (immune coevolution) are three distinct novelty paths.
- **ML bonus:** #3 shows how RL can steer a metaheuristic without replacing it.

## Two project ideas this enables

1. **Idea #1 (priority):** An **adaptive hyper-heuristic** for energy-aware
   heterogeneous multi-robot task allocation, where operator probabilities are
   learned online (seeded by #1, #2, #4).
2. **Idea #2:** A **multi-objective coevolutionary / learning-assisted** optimizer
   for constrained multi-UAV task assignment under time-window, range and priority
   constraints (seeded by #3, #5).

## Download checklist (all open access)

- [ ] 1. Yuan et al. 2025 — [10.1016/j.dt.2025.06.006](https://doi.org/10.1016/j.dt.2025.06.006)
- [ ] 2. Cheng et al. 2024 — [10.23919/CSMS.2024.0006](https://doi.org/10.23919/CSMS.2024.0006)
- [ ] 3. Qin et al. 2025 — [10.3390/drones9060436](https://doi.org/10.3390/drones9060436)
- [ ] 4. Nait Chabane & Guenounou 2025 — [10.1007/s40747-025-02062-w](https://doi.org/10.1007/s40747-025-02062-w)
- [ ] 5. Chen et al. 2025 — [10.1007/s40747-024-01720-9](https://doi.org/10.1007/s40747-024-01720-9)
