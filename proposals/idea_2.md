# Project Idea #2 (Fallback)

**Title:** Cooperative Planetary-Surface Exploration under Energy, Terrain, and
Communication Constraints

## Setting

Heterogeneous rovers explore a Mars-like site with a lander relay. See Use Case B
in `proposals/use_case.md`.

## Problem

Assign science targets and plan traverses jointly to maximize science return while
cutting energy and makespan, under instrument match, slope and crater no-go zones,
battery plus solar recharge, communication range, and precedence constraints.

## Research question

Can a multi-objective coevolutionary optimizer return a diverse set of
energy-versus-science plans that stay feasible when recharging is required and a
rover fails, outperforming classical multi-objective evolutionary algorithms?

## Why it matters

- Planetary missions must trade science return against energy and time, and survive
  faults with no human in the loop.
- Reviewed work ignores recharging and failure handling, and stops at two
  objectives without communication limits.
- A Pareto set of plans is operationally useful: fast-and-costly versus slow-and-cheap.

## Approach

- Variables: assignment, per-rover route, charging stops and waiting timing.
- Objectives: energy, makespan, science return.
- Constraints: instrument match, terrain no-go zones, energy budgets with recharge,
  depot start and end, time windows, precedence, lander communication range.
- Method: two coevolving subpopulations with an adaptive operator pool and
  idle-aware encoding; a reallocation operator repairs the plan on simulated rover
  failure. Simulated annealing, genetic algorithm, and one swarm method are the
  baselines (Milestones 3–5); the coevolutionary planner is the final Milestone.

## Novelty

Explicit recharge, communication limits, and fault-triggered replanning inside a
multi-objective coevolutionary exploration planner.

## Metrics

Hypervolume and front coverage versus baselines; energy, makespan, coverage after
failure, reassignment count; component ablation; repeated runs with statistical tests.

## References

1. Chen et al. 2025. Complex and Intelligent Systems. https://doi.org/10.1007/s40747-024-01720-9
2. Qin et al. 2025. Drones. https://doi.org/10.3390/drones9060436
3. Yuan et al. 2025. Defence Technology. https://doi.org/10.1016/j.dt.2025.06.006
