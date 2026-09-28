---
id: drl-seagull-multi-uav-task-allocation
title: "A deep reinforcement learning-driven seagull optimization algorithm for solving multi-UAV task allocation problem in plateau ecological restoration"
authors: ["Lijing Qin", "Zhao Zhou", "Huan Liu", "Zhengang Yan", "Yongqiang Dai"]
year: 2025
venue: "Drones"
doi: "10.3390/drones9060436"
url: "https://doi.org/10.3390/drones9060436"
pdf: literature/papers/drl-seagull-multi-uav-task-allocation.pdf
tags: ["reinforcement-learning", "swarm-intelligence", "multi-uav", "task-allocation", "adaptive-strategy", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# A deep reinforcement learning-driven seagull optimization algorithm for solving multi-UAV task allocation problem in plateau ecological restoration

> [!info] Citation
> L. Qin, Z. Zhou, H. Liu, Z. Yan, and Y. Dai, "A deep reinforcement learning-driven seagull optimization algorithm for solving multi-UAV task allocation problem in plateau ecological restoration," *Drones*, vol. 9, no. 6, art. 436, 2025.
> **Access:** Open access (MDPI, CC BY 4.0). [Local PDF](../papers/drl-seagull-multi-uav-task-allocation.pdf) · [DOI](https://doi.org/10.3390/drones9060436)

## Why this paper (pre-selected)

- **DRL controls a swarm optimizer's search phases** (migration / attack / post-attack) — a concrete, OA example of learning-assisted metaheuristics, directly feeding the optional ML bonus.
- **Multi-objective, multi-constraint model** (max completion time and total flow time; collaboration, priority, range limits) is a ready M2 template.
- Benchmarked against **five swarm algorithms**, useful baselines for M5.

## TL;DR

This paper proposes DRL-SOA, a deep reinforcement learning-driven seagull optimization algorithm that uses three DQNAgents to adaptively control parameter decay factors and select local-search operators across migration, attack, and post-attack phases for multi-UAV task allocation in plateau ecological grassland restoration.

## Problem & Motivation

- **Problem addressed:** Multi-UAV collaborative task allocation under collaboration, priority and range constraints (plateau grassland restoration).
- **Why it matters:** In plateau ecological restoration (e.g., repairing vegetation destruction and soil degradation caused by marmot activity), individual UAVs suffer from limited carrying capacity and operational range. Efficient multi-UAV coordination prevents task conflicts, resource waste, and prolonged execution times in complex agricultural/ecological environments.
- **Application domain:** Agricultural / ecological multi-UAV operations.

## Research Question / Objective

- How to formulate a realistic multi-objective, multi-constraint collaborative task allocation model for multi-UAV ecological restoration and solve it efficiently by dynamically balancing global exploration and local exploitation through deep reinforcement learning.

## Contributions

- [x] Multi-objective multi-constraint collaborative task allocation problem (MOMCCTAP) model.
- [x] DRL-driven seagull optimization (DRL-SOA): DQN adapts search factors and selects local-search strategies per phase (migration, attack, and post-attack refinement).
- [x] Comprehensive simulation experiments across 8 benchmark cases demonstrating superior convergence speed, Hypervolume (HV), and solution diversity over 5 advanced swarm intelligence algorithms.

## Methodology

- **Problem formulation:** Minimize max completion time ($f_1$) and total flow time ($f_2$), subject to UAV maximum flight range ($dis_i \le max\_dis$), task priorities, task completion requirements, and multi-UAV non-overlapping coordination constraints.
- **Algorithm:** DRL-SOA (seagull optimization controlled by three DQNAgents across migration, attack, and post-attack refinement phases; state representation based on population Hypervolume $HV_t$, Decaying-$\epsilon$-greedy action selection, and experience replay).
- **Baselines compared:** EMoSOA, INSGA-II-MTO, AWPSO, MOSOS, and LeCMPSO.
- **Validation:** Eight sets of benchmark cases spanning 4 task scales (20, 30, 40, and 50 tasks with 6 or 10 UAVs).

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Task Scale & Fleet | 20, 30, 40, 50 tasks | 6 UAVs for 20/30 tasks (3x3 km area); 10 UAVs for 40/50 tasks (4x4 km area) |
| Hypervolume (HV) | DRL-SOA mean HV ranges from 0.931 to 1.097 | Achieves highest mean HV in 7 out of 8 test cases against 5 baselines (ref point: 1.2, 1.2) |
| Inverted Generational Distance (IGD) | Consistently lower IGD trajectory over 500 iterations | Demonstrates superior Pareto-front convergence accuracy and solution distribution uniformity |
| DRL Hyperparameters | $\alpha=0.01, \gamma=0.9, \epsilon=0.9$, Buffer=500, Batch=32 | Optimized via 12-group orthogonal experimental design (4,000 generations) on a 40-task scenario |

- **Key findings:** DRL-SOA significantly outperforms traditional swarm baselines in both convergence speed and solution diversity, effectively avoiding premature local optima through dynamic strategy switching.
- **Best-performing method:** DRL-SOA.

## Strengths

- Replaces fixed heuristic rules with three dedicated DQNAgents that adaptively control parameter decay, local search direction, and post-attack mutations.
- Rich action space design incorporating 7 parameter decay functions, 8 local search operators (4 stochastic, 4 targeted), and 4 refinement mechanisms (sparrow flight mechanism, Cauchy mutation, dynamic inverse learning, and adaptive t-distribution mutation).
- Dual-objective formulation ($f_1$ for max completion time and $f_2$ for total flow time) directly addresses the realistic trade-off between mission completion speed and total fleet resource expenditure.

## Limitations & Threats to Validity

- No explicit energy-consumption model (does not account for aerodynamic drag, wind resistance, altitude variation, or changing payload weights).
- Static task environment assumption (does not handle dynamic task arrivals, unexpected obstacle avoidance, or real-time weather fluctuations during flight execution).

## Relevance to Our Project

- **Which milestones it informs:** M2 (multi-objective model), M5 (swarm baselines), M6 (DRL-driven adaptive selection), ML bonus.
- **Ideas it suggests:** Using Hypervolume delta ($HV_t - HV_{t-1}$) as an explicit RL reward signal; structuring hyper-heuristic action pools into distinct search phases (migration, attack, post-attack refinement).
- **Can we reproduce or extend it?** Yes; the mathematical formulation, reward mechanism, and action space choices are well specified. It can be extended by integrating an explicit energy dissipation model or online dynamic task rescheduling.

## Open Questions

- How well do the offline-trained DQNAgents generalize to larger task scales (>100 tasks) or un-trained spatial topologies without retraining?
- What is the computational overhead of calculating the Hypervolume reward signal online for higher-dimensional objective spaces (>3 objectives)?

## Keywords

deep reinforcement learning, seagull optimization, multi-UAV, task allocation, multi-objective, adaptive search

## Abstract (verbatim)

The rapid advancement of unmanned aerial vehicle (UAV) technology has enabled the coordinated operation of multi-UAV systems, offering significant applications in agriculture, logistics, environmental monitoring, and disaster relief. In agriculture, UAVs are widely utilized for tasks such as ecological restoration, crop monitoring, and fertilization, providing efficient and cost-effective solutions for improved productivity and sustainability. This study addresses the collaborative task allocation problem for multi-UAV systems, using ecological grassland restoration as a case study. A multi-objective, multiconstraint collaborative task allocation problem (MOMCCTAP) model was developed, incorporating constraints such as UAV collaboration, task completion priorities, and maximum range restrictions. The optimization objectives include minimizing the maximum task completion time for any UAV and minimizing the total time for all UAVs. To solve this model, a deep reinforcement learning-based seagull optimization algorithm (DRL-SOA) is proposed, which integrates deep reinforcement learning with the seagull optimization algorithm (SOA) for adaptive optimization. The algorithm improves both global and local search capabilities by optimizing key phases of seagull migration, attack, and post-attack refinement. Evaluation against five advanced swarm intelligence algorithms demonstrates that the DRL-SOA outperforms the alternatives in convergence speed and solution diversity, validating its efficacy for solving the MOMCCTAP.