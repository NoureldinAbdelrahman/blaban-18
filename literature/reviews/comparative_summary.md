# Comparative Summary of the Five Review Papers

All five papers are open access. This document compares them across problem,
method, adaptive mechanism, encoding, validation and results, then draws out what
it means for our project. Acronyms are avoided throughout; method and algorithm
names are written in full.

## Papers covered

1. **Yuan and colleagues (2025)** — energy learning hyper-heuristic for heterogeneous
   aerial vehicle task assignment.
2. **Cheng and colleagues (2024)** — adaptive dual-level memetic algorithm for
   multi-robot surveillance route planning.
3. **Qin and colleagues (2025)** — deep reinforcement learning-driven seagull
   optimization for multi-aerial-vehicle task allocation.
4. **Nait Chabane and Guenounou (2025)** — two-phase enhanced genetic algorithm for
   heterogeneous multi-robot inspection.
5. **Chen and colleagues (2025)** — bi-subpopulation coevolutionary immune algorithm
   for multi-aerial-vehicle task allocation.

## At-a-glance comparison

| | Yuan 2025 | Cheng 2024 | Qin 2025 | Nait Chabane 2025 | Chen 2025 |
| --- | --- | --- | --- | --- | --- |
| **Fleet** | Heterogeneous aerial vehicles | Ground robots | Aerial vehicles | Heterogeneous ground robots | Aerial vehicles |
| **Application** | Cooperative operations / indoor flight | Surveillance | Ecological restoration | Industrial inspection | Reconnaissance / mission planning |
| **Objectives** | Single aggregated score with penalties | Weighted blend (energy, time, balance) | Two: completion time, flow time | Single: travel distance | Two: completion time, flight range |
| **Constraints** | Eleven complex constraints | Task-load variance limit | Range, priority, collaboration, non-overlap | Vehicle–measurement capability match | Endurance, speed, precedence |
| **Search family** | Hyper-heuristic over operators | Memetic (evolution plus local search) | Learning-driven swarm | Two-phase genetic algorithm | Coevolutionary immune algorithm |
| **Adaptive mechanism** | Energy-based operator selection | Scheduled local-search probabilities | Deep reinforcement learning selects strategy | Phase decoupling, no operator learning | Scheduled strategy selection |
| **Encoding** | Three layers (task, vehicle, waiting time) | Continuous floor-rounding and order-by-value | Swarm positions mapped to assignments | Capability matrix, constraint-preserving | Zero-padded permutation, idle vehicles allowed |
| **Baselines** | Four classical swarm optimizers | Four metaheuristics plus ablations | Five swarm / evolutionary methods | Exact solver, genetic, swarm, surrogate-assisted | Multi-objective evolutionary and immune methods |
| **Validation** | Two simulations plus quadrotor test | Benchmarks plus simulated robots | Eight benchmark cases | Thirty instances, statistics, failure case | Benchmarks, six task cases, ablation |
| **Outcome** | Highest fitness, fastest convergence | Best distance, time, balance | Best Hypervolume in 7 of 8 cases | Gap under 1.5%, up to 90% faster | Best or comparable Hypervolume |
| **Limitation** | Partial time windows; static map | Static targets; identical robots | No energy model; static setting | Single objective; flat space | Static setting; simplified constraints |

## Problem and domain

Three papers use aerial fleets, two use ground robots. All five assign tasks; four
also order or route them, with Cheng and Nait Chabane solving both decisions
together. Objectives range from a single penalized score (Yuan, Nait Chabane) to a
weighted blend (Cheng) to true two-objective trade-off sets (Qin, Chen). Only Yuan
models energy explicitly; the rest use distance as a proxy or ignore energy. That
is the clearest gap in the set.

## Search strategy

- **Hyper-heuristic** (Yuan): searches over low-level operators instead of solutions.
- **Memetic** (Cheng): evolutionary search plus two local searches (reassign targets
  between robots; reverse route sub-sequences within a robot).
- **Learning-driven swarm** (Qin): swarm phases steered by Deep Q-Network agents.
- **Coevolutionary immune** (Chen): elite and common subpopulations coevolve,
  drawing operators from an adaptive pool.
- **Structured genetic** (Nait Chabane): global allocation first, per-robot route
  refinement second.

## The unifying thread: adaptive operator selection

The five sit on a scale from fixed schedules to genuine learning:

1. **Learned (Qin):** a Deep Q-Network picks operators from Hypervolume feedback.
2. **Adaptive rule (Yuan):** Boltzmann probabilities over operator energy, updated
   by fitness gains — feedback, not a learned policy.
3. **Fixed schedules (Cheng, Chen):** search behaviour varies with generation
   number, prescribed in advance.
4. **No selection (Nait Chabane):** gains come from decomposition and
   constraint-preserving operators — the control case showing what structure alone
   achieves.

Our novel algorithm can occupy the empty middle: **feedback-driven,
learning-assisted selection, cheaper than full deep reinforcement learning but
smarter than a fixed schedule.**

## Encoding and constraint handling

Borrow selectively: three-layer encoding with graph-based precedence repair (Yuan);
continuous floor-rounding needing no repair (Cheng); capability-preserving matrix
that never produces infeasible offspring (Nait Chabane); zero-padded permutation
allowing idle vehicles (Chen). Lesson: constrain **inside the encoding**, not with
after-the-fact penalties.

## Validation rigor

Strongest first: Nait Chabane (exact-solver baseline, thirty runs, significance
tests, effect sizes, failure scenario); Chen (thirty runs, rank tests, ablation);
Cheng (twenty runs, rankings, physics simulation); Qin (Hypervolume and distance
metrics, tuned hyperparameters); Yuan (only physical hardware validation, lighter
statistics). Scores are not comparable across papers — compare methods, not numbers.

## Shared limitations (our opportunity space)

Static tasks everywhere; weak or missing energy models; at most two objectives;
mostly identical fleets; no shared benchmark. Each gap is a differentiator for us.

## What this means for our project

**Combine:** feedback-driven selection (Yuan) upgraded toward learned selection
(Qin) but kept lightweight; adaptive local search (Cheng); constraint-preserving
encoding (Nait Chabane); idle-aware permutation (Chen); benchmark discipline
(exact baseline, repeats, statistics).

**Differentiate:** explicit energy plus multi-objective trade-offs; learning-assisted
rather than fixed-schedule selection; a shared documented benchmark.

**Our two directions**

- **Priority:** learning-assisted swarm optimization for cooperative agricultural
  ground robots — energy, makespan, balance (`proposals/idea_1.md`).
- **Fallback:** multi-objective coevolutionary planner for planetary-surface
  exploration under energy, terrain, communication and failure constraints
  (`proposals/idea_2.md`).

**Milestone mapping:** formulation from Qin, Chen, Cheng; simulated annealing and
genetic baselines from Cheng and Nait Chabane; swarm baselines from Yuan and Qin;
novel algorithm from Yuan, Qin, Chen; machine-learning bonus from Qin.
