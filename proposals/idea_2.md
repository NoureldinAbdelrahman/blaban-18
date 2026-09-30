# Project Idea #2 (Fallback)

**Working title:** Robust Multi-Objective Inspection Planning under Recharging and
Robot Failure for a Renewable-Energy Site

## Domain / Application

- **Theme:** multi-agent cooperative systems in robotics / autonomous systems.
- **Setting:** the same renewable-energy inspection site as Idea #1
  (`proposals/use_case.md`), extended with battery recharging and a mid-mission
  robot failure.

## Problem Statement

Plan inspection assignments and routes for a heterogeneous fleet that must recharge
during the mission and remain effective when one robot fails, returning a set of
trade-off solutions between fleet energy consumption and mission makespan instead of
a single answer.

## Research Question

Can a multi-objective coevolutionary optimizer produce a diverse set of
energy-versus-makespan inspection plans that stay feasible and near-optimal when
recharging is required and a robot fails mid-mission, outperforming classical
multi-objective evolutionary algorithms?

## Motivation & Justification

- Every reviewed paper assumes static tasks and, except Yuan, ignores energy
  explicitly; none handles recharging or faults. This is the clearest open gap.
- Operators care about a frontier of options (fast-and-costly versus slow-and-cheap)
  rather than one plan, so a Pareto set is practically useful.
- Fault tolerance matters for costly aerial inspection missions.

## Supporting Literature

| Paper | How it supports this idea |
| --- | --- |
| Chen et al. 2025 | Coevolutionary immune population structure, idle-aware encoding, Pareto results |
| Qin et al. 2025 | Two-objective formulation; adaptive strategy selection |
| Yuan et al. 2025 | Explicit energy modelling and complex constraints |
| Nait Chabane and Guenounou 2025 | Dynamic re-planning after a robot failure; statistical rigor |

## Proposed Approach

- **Agents / environment:** heterogeneous fleet plus charging stations; one robot may
  fail during execution.
- **Decision variables:** assignment, per-robot sequence, and charging stops/timing.
- **Objective(s):** minimize fleet energy and minimize makespan (Pareto front);
  robustness as a secondary measure.
- **Constraints:** capability matching, energy budgets with recharge, depot start
  and end, time windows, precedence, no-go zones, and feasibility after failure.
- **Algorithm design:**
  - Two coevolving subpopulations (elite and exploratory) with an adaptive pool of
    crossover and mutation operators, following Chen.
  - Idle-aware encoding so underused robots can stay at the depot.
  - Reallocation operator triggered by a simulated robot failure, so the plan is
    repaired rather than rebuilt.

## Algorithms to Implement (milestones)

- [ ] Milestone 3 — Simulated Annealing for the single-objective relaxation.
- [ ] Milestone 4 — Genetic Algorithm as the evolutionary baseline.
- [ ] Milestone 5 — one swarm method, adapted to multiple objectives if possible.
- [ ] Milestone 6 — the multi-objective coevolutionary algorithm with
      recharging and fault re-planning (novel algorithm).
- [ ] Bonus — a machine-learning predictor for failure or recharge needs.

## Novelty

Explicit recharging and fault-triggered re-planning inside a multi-objective
coevolutionary inspection planner, a combination absent from the reviewed work.

## Expected Results & Metrics

- Hypervolume and Pareto-front coverage versus multi-objective evolutionary
  baselines on static and failure scenarios.
- Energy, makespan, coverage after failure, and number of reassignments.
- Ablation of the coevolution and idle-aware encoding components.

## Feasibility & Risks

- **Compute/time:** multi-objective runs are heavier; use small-to-medium instances.
- **Risks:** added complexity from recharging and failures; harder benchmarking.
- **Mitigations:** implement the static single-objective case first, then add
  recharging, then failure; keep a clear baseline.

## Keywords

`robotics`, `multi-agent`, `cooperative`, `meta-heuristics`, `optimization`

## References

1. Chen, X., Wan, Y., Qi, J., Zhao, Z., Ruan, Y., Tang, J. (2025). Bi-subpopulation
   coevolutionary immune algorithm for multi-aerial-vehicle task allocation.
   *Complex & Intelligent Systems*, 11(2), 149.
2. Qin, L., Zhou, Z., Liu, H., Yan, Z., Dai, Y. (2025). Deep reinforcement
   learning-driven seagull optimization for multi-aerial-vehicle task allocation.
   *Drones*, 9(6), 436.
3. Yuan, M., Chen, M., Zhou, T., Han, Z. (2025). Energy learning hyper-heuristic for
   heterogeneous aerial vehicle task assignment. *Defence Technology*, 54, 1–14.
4. Nait Chabane, A., Guenounou, O. (2025). Enhanced genetic algorithm for
   heterogeneous multi-robot task allocation and planning. *Complex & Intelligent
   Systems*, 11, 435.
