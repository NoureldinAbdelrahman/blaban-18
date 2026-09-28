# Comparative Summary of the Five Review Papers

All five papers are open access. This document compares them across problem,
method, adaptive mechanism, encoding, validation and results, and then draws out
what it means for our project. Acronyms are avoided throughout; method and
algorithm names are written in full.

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
| **Application** | Cooperative combat / indoor flight | Surveillance | Plateau ecological restoration | Industrial inspection | Reconnaissance / mission planning |
| **Objective character** | Single aggregated score with penalties | Weighted combination (energy, time, balance) | Two objectives (maximum completion time, total flow time) | Single objective (total travel distance) | Two objectives (completion time, total flight range) |
| **Constraints** | Eleven complex constraints | Task-load variance threshold | Range, priority, collaboration, non-overlap | Vehicle–measurement capability compatibility | Endurance, cruising speed, task precedence |
| **Core search family** | Hyper-heuristic over low-level operators | Memetic (evolutionary search plus local search) | Swarm optimization controlled by learning | Two-phase genetic algorithm | Coevolutionary immune algorithm |
| **Adaptive mechanism** | Energy-based (Boltzmann) operator selection | Scheduled adaptive local-search probabilities | Deep reinforcement learning selects strategy | Structural phase decoupling, no operator learning | Scheduled adaptive strategy selection |
| **Encoding** | Three layers (task, vehicle, waiting time) | Continuous floor-rounding and order-by-value | Swarm positions mapped to task assignments | Three-row capability matrix, constraint-preserving | Zero-padded permutation, idle vehicles allowed |
| **Baselines** | Four classical swarm optimizers | Four metaheuristics plus ablations | Five advanced swarm / evolutionary methods | Exact solver, genetic algorithm, particle swarm, surrogate-assisted method | Multi-objective evolutionary and immune algorithms |
| **Validation** | Two simulations plus physical quadrotor test | Standard routing benchmarks plus simulated robots | Eight benchmark cases | Thirty instances plus statistical tests and a failure scenario | Four benchmarks plus six task cases plus ablation |
| **Reported outcome** | Highest fitness and fastest convergence | Best distance, time and balance; top rank | Best Hypervolume in seven of eight cases | Gap under one and a half percent; up to ninety percent faster | Best or comparable Hypervolume; fast solving time |
| **Main limitation** | Partial time-window handling; static map | Static targets; homogeneous robots | No energy model; static environment | Single objective; idealized flat space | Static environment; simplified constraints |

## 1. Problem and domain

Three papers address aerial fleets (Yuan, Qin, Chen) and two address ground robots
(Cheng, Nait Chabane). All five frame **task assignment**, and four of the five
(Yuan, Cheng, Nait Chabane, and partly Chen) also decide some form of **ordering or
routing**. The clearest coupling of assignment and routing appears in Cheng and in
Nait Chabane, both of which solve the two decisions together instead of in separate
stages.

The optimization character forms a spectrum rather than a single type:

- **Single aggregated objective with penalties** — Yuan folds rewards and penalty
  terms into one bounded score; Nait Chabane minimizes a single distance.
- **Weighted combination** — Cheng blends total distance, maximum distance and
  workload balance into one function.
- **True two-objective** — Qin minimizes maximum completion time and total flow
  time; Chen minimizes completion time and total flight range. Only these two
  return a set of trade-off solutions rather than one answer.

Only **Yuan** treats **energy as an explicit optimization currency**; Cheng and
Nait Chabane use path length as an energy proxy, and Qin and Chen do not model
energy directly. This is the single clearest gap across the set.

## 2. Search strategy

The five papers occupy four different search families:

- **Hyper-heuristic** (Yuan) — searches over the space of low-level operators
  rather than directly over solutions, choosing among three selection operators and
  eleven action operators grouped by task, vehicle, and task-vehicle effect.
- **Memetic** (Cheng) — combines evolutionary operators with two local searches,
  one that reassigns targets between robots and one that improves each robot's
  route by reversing sub-sequences.
- **Learning-driven swarm** (Qin) — a seagull-inspired swarm optimizer whose
  migration, attack and refinement phases are steered by three Deep Q-Network
  agents.
- **Coevolutionary immune** (Chen) — an elite subpopulation and a common
  subpopulation coevolve, drawing crossover operators from an adaptive strategy
  pool.
- **Structured genetic** (Nait Chabane) — a two-phase genetic algorithm that first
  allocates tasks under capability limits, then refines each route locally.

## 3. The unifying thread — adaptive operator or strategy selection

Every paper except Nait Chabane adapts *how* it searches, and the differences are
instructive because they sit on a scale from fixed schedules to genuine learning:

1. **Learning-based (Qin).** A Deep Q-Network chooses parameter decay and local
   search operators according to a reward built from Hypervolume improvement. This
   is the only paper where the adaptation is learned from feedback rather than
   prescribed.
2. **Adaptive but not learned (Yuan).** Operator selection probabilities follow a
   Boltzmann distribution over operator "energy" values that rise and fall with
   fitness gains — a performance-feedback rule, not a learned policy.
3. **Scheduled adaptation (Cheng, Chen).** Both vary search behaviour with the
   generation number: Cheng decays task-level search and grows route-level search;
   Chen uses a sigmoid curve to shift from exploration to exploitation. These are
   fixed schedules, not feedback.
4. **No adaptive selection (Nait Chabane).** Gains come from decomposition and from
   constraint-preserving operators, plus one dynamic re-planning case after a robot
   failure. This is the control case: it shows how much can be achieved by structure
   alone, without any adaptive or learned operator selection.

This scale is directly useful to us: it suggests our novel algorithm can occupy the
empty middle ground — **feedback-driven, learning-assisted operator selection that
is cheaper than full deep reinforcement learning but smarter than a fixed
schedule.**

## 4. Encoding and constraint handling

The encodings differ sharply and are worth borrowing selectively:

- **Three-layer encoding** (Yuan) keeps task order, vehicle assignment and waiting
  time separate, which makes precedence and time-window repair tractable; loops are
  removed with depth-first search and times are adjusted by topological sorting.
- **Continuous encoding** (Cheng) turns discrete assignment and permutation into
  continuous values interpreted by floor-rounding and value-ranking, so ordinary
  genetic operators apply without repair.
- **Capability-preserving matrix** (Nait Chabane) enforces vehicle–measurement
  compatibility during initialization and mutation, so infeasible offspring never
  appear and heavy penalties are unnecessary.
- **Zero-padded permutation** (Chen) lets a vehicle be idle, which avoids wasting
  energy on vehicles whose participation adds little — a small but practical detail.

A common lesson: handling constraints **inside the encoding or operators** (Nait
Chabane, Chen, Cheng) is more robust than penalizing violations after the fact
(Yuan).

## 5. Validation rigor and reproducibility

Ranked by the strength of the evidence:

1. **Nait Chabane** is the most rigorous. It benchmarks against an exact solver,
   repeats each instance thirty times, reports Welch's t-tests and Cohen's effect
   sizes, fits an empirical runtime model, and adds a mid-mission failure scenario.
2. **Chen** reports benchmark and task-case results over thirty runs with
   Wilcoxon rank-sum tests and a full component ablation.
3. **Cheng** runs twenty repetitions across standard routing benchmarks with
   varied team sizes, reports a Friedman ranking, and validates in a physics
   simulation with a real robot model.
4. **Qin** reports Hypervolume and Inverted Generational Distance over eight cases
   and tunes its hyperparameters with an orthogonal design.
5. **Yuan** is the only paper with **physical hardware** validation (indoor
   quadrotors with motion capture), but its statistical benchmarking is lighter
   than the others.

All five are open access and specify their parameters, so all five are
reproducible. Reproducibility is strongest where an exact-solver baseline and
standard benchmark instances are used (Nait Chabane, Cheng, Chen).

## 6. Scale and reported performance

- **Yuan:** up to six vehicles and eighteen tasks, plus three physical quadrotors;
  highest fitness and fastest convergence against four swarm baselines.
- **Cheng:** up to one hundred and one nodes and eight robots; best total distance,
  maximum distance and workload balance; top average ranking.
- **Qin:** up to fifty tasks and ten vehicles; best mean Hypervolume in seven of
  eight cases and the lowest Inverted Generational Distance.
- **Nait Chabane:** up to fifty sites and four robots (extrapolated to two hundred
  sites and twenty robots); optimality gap under one and a half percent, up to
  ninety percent faster than the exact solver.
- **Chen:** up to five vehicles and thirty targets; best or comparable Hypervolume
  on all six task cases and faster solving time than several planners.

Because the problem sizes and metrics differ so much, the reported numbers are not
directly comparable; the comparison is meaningful at the level of method, not at
the level of a single score.

## 7. Shared limitations (our opportunity space)

- **Static tasks.** Every paper assumes fixed targets; only Nait Chabane tests a
  single robot failure. Dynamic task arrival, vehicle loss and weather are open.
- **Weak energy modelling.** Only Yuan optimizes energy explicitly; the rest use
  distance as a proxy. A realistic battery or discharge model is missing throughout.
- **Narrow objective sets.** The true two-objective papers stop at two objectives;
  none explore four or more (for example risk, communication and fatigue).
- **Homogeneous assumptions.** Except Yuan and Nait Chabane, the fleets are treated
  as identical.
- **No standard shared benchmark.** Each paper invents its own instances, so
  cross-paper numbers cannot be compared directly.

## 8. What this means for our project

**Convergent ideas worth combining**

- Take the **feedback-driven operator selection** of Yuan and upgrade it toward the
  **learned selection** of Qin, but keep it lightweight (a bandit or shallow
  learner) rather than a full Deep Q-Network.
- Adopt the **adaptive local search** of Cheng to bridge our genetic algorithm step
  and our novel-algorithm step.
- Reuse the **constraint-preserving encoding** of Nait Chabane and the **idle-aware
  zero-padded permutation** of Chen.
- Copy the **benchmark discipline** of Nait Chabane: an exact-solver baseline on
  small instances, repeated runs, statistical tests and an effect-size measure.

**Clear differentiators for our novel algorithm**

1. Make **energy explicit** and multi-objective (completion time, energy and
   workload balance together), which no reviewed paper does.
2. Use **learning-assisted feedback** for operator selection instead of a fixed
   schedule (the middle ground identified in Section 3).
3. Evaluate on a **shared, documented benchmark** with an exact baseline and proper
   statistics, so our results are comparable rather than bespoke.

**Two candidate project directions**

- **First priority:** an energy-aware, learning-assisted hyper-heuristic for
  heterogeneous multi-robot task allocation, where operator probabilities are
  updated from performance feedback (drawing on Yuan, Cheng and Nait Chabane).
- **Second:** a multi-objective coevolutionary or learning-assisted optimizer for
  constrained multi-aerial-vehicle assignment under time-window, range and priority
  constraints (drawing on Qin and Chen).

**Mapping to course milestones**

- **Milestone 2 (formulation):** the multi-objective models of Qin and Chen, and the
  coupled assignment-routing model of Cheng.
- **Milestone 3 (Simulated Annealing):** the local-search acceptance ideas in Cheng
  and Nait Chabane.
- **Milestone 4 (Genetic Algorithm):** the memetic structure of Cheng and the
  two-phase genetic algorithm of Nait Chabane.
- **Milestone 5 (swarm methods):** the swarm baselines in Yuan and the seagull
  optimizer in Qin.
- **Milestone 6 (novel algorithm):** the hyper-heuristic of Yuan, the learned
  control of Qin, and the coevolutionary immune structure of Chen.
- **Optional machine-learning bonus:** the Deep Q-Network control in Qin.

## 9. Bottom line

The five papers agree on a direction and disagree on how far to take it. They agree
that **multi-agent task allocation is best solved by searching over strategies, not
just over solutions**, and that constraints are best handled inside the encoding.
They disagree on the mechanism: fixed schedules (Cheng, Chen), performance-driven
rules (Yuan), learned control (Qin), or pure structure (Nait Chabane). The gap our
project can fill is a **lightweight, learning-assisted, energy-aware
hyper-heuristic** that borrows the strongest element of each paper and evaluates it
with the rigor of the best of them.
