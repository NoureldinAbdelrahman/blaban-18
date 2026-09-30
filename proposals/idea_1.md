# Project Idea #1 (Priority)

**Working title:** A Learning-Assisted Energy-Aware Hyper-Heuristic for Cooperative
Heterogeneous Inspection of a Renewable-Energy Site

## Domain / Application

- **Theme:** multi-agent cooperative systems in robotics / autonomous systems.
- **Setting:** preventive inspection of a solar (or wind) farm by a mixed fleet of
  ground robots and aerial drones. See `proposals/use_case.md`.

## Problem Statement

Assign a set of inspection tasks, each requiring a specific sensing capability, to a
heterogeneous fleet and plan each robot's route at the same time, so that fleet
energy consumption and mission makespan are minimized and workload is balanced,
without violating capability, battery, time-window, precedence and obstacle
constraints.

## Research Question

Can a hyper-heuristic whose operator-selection probabilities are updated from
performance feedback outperform fixed-schedule hyper-heuristics and classical
single-operator metaheuristics on an energy-aware, capability-constrained
inspection planning problem?

## Motivation & Justification

- The five reviewed papers each adapt *how they search*, but the adaptation is
  either a fixed schedule or a heavy learned policy; a lightweight feedback-driven
  rule is unexplored in this setting.
- Energy is the operational bottleneck for aerial inspection yet is rarely modelled
  explicitly in multi-robot task allocation.
- Heterogeneous sensing makes the assignment genuinely constrained, not a pure
  routing problem.

## Supporting Literature

| Paper | How it supports this idea |
| --- | --- |
| Yuan et al. 2025 | Energy-based operator selection in a hyper-heuristic; proves the mechanism |
| Nait Chabane and Guenounou 2025 | Capability-preserving encoding; exact-solver benchmarking discipline |
| Cheng et al. 2024 | Adaptive dual-level local search (reallocation plus route refinement) |
| Chen et al. 2025 | Idle-aware permutation encoding; multi-objective framing |

## Proposed Approach

- **Agents / environment:** the heterogeneous fleet and site in `proposals/use_case.md`.
- **Decision variables:** task-to-robot assignment, per-robot visiting sequence.
- **Objective(s):** energy (primary), makespan and workload balance (secondary).
- **Constraints:** capability matching, per-robot energy budget, depot start/end,
  time windows, precedence, no-go zones.
- **Hyper-heuristic design:**
  - Low-level operator pool: inter-robot task reassignment, route-segment reversal,
    insertion, swap, capability-repair move, and short local re-optimization.
  - Operator selection probabilities updated from observed fitness improvement
    using an energy/Boltzmann rule (following Yuan) or a lightweight multi-armed
    bandit, rather than a fixed schedule.
  - Capability-preserving initialization so solutions start feasible.

## Algorithms to Implement (milestones)

- [ ] Milestone 3 — Simulated Annealing as the baseline local search.
- [ ] Milestone 4 — Genetic Algorithm with capability-preserving encoding.
- [ ] Milestone 5 — one swarm method (Particle Swarm, Ant Colony, Whale or Grey Wolf).
- [ ] Milestone 6 — the learning-assisted hyper-heuristic (novel algorithm).
- [ ] Bonus — the feedback rule as a light machine-learning component.

## Novelty

Feedback-driven operator selection combined with an explicit energy objective and
heterogeneous-capability constraints, on a use case not covered by the reviewed work.

## Expected Results & Metrics

- Energy, makespan, workload balance and coverage versus simulated annealing,
  genetic algorithm, the swarm method and a fixed-schedule hyper-heuristic.
- Ablation of the feedback-driven operator selection.
- Repeated runs with statistical tests and effect sizes.

## Feasibility & Risks

- **Compute/time:** small instances (tens of tasks) run in seconds in Python.
- **Risks:** hyper-heuristic complexity; weak benefit over a strong genetic
  algorithm; energy model credibility.
- **Mitigations:** keep the operator pool small; include a fixed-schedule control;
  justify the energy model with a sensitivity study.

## Keywords

`robotics`, `multi-agent`, `cooperative`, `meta-heuristics`, `optimization`

## References

1. Yuan, M., Chen, M., Zhou, T., Han, Z. (2025). Energy learning hyper-heuristic for
   heterogeneous aerial vehicle task assignment. *Defence Technology*, 54, 1–14.
2. Nait Chabane, A., Guenounou, O. (2025). Enhanced genetic algorithm for
   heterogeneous multi-robot task allocation and planning. *Complex & Intelligent
   Systems*, 11, 435.
3. Cheng, H., Yi, J., Xia, W., Pu, H., Luo, J. (2024). Adaptive memetic algorithm
   with dual-level local search for multi-robot surveillance. *Complex System
   Modeling and Simulation*, 4(2), 210–221.
4. Chen, X., Wan, Y., Qi, J., Zhao, Z., Ruan, Y., Tang, J. (2025). Bi-subpopulation
   coevolutionary immune algorithm for multi-aerial-vehicle task allocation.
   *Complex & Intelligent Systems*, 11(2), 149.
