---
id: adaptive-memetic-multi-robot-surveillance
title: "Adaptive memetic algorithm with dual-level local search for cooperative route planning of multi-robot surveillance systems"
authors: ["Hao Cheng", "Jin Yi", "Wei Xia", "Huayan Pu", "Jun Luo"]
year: 2024
venue: "Complex System Modeling and Simulation"
doi: "10.23919/CSMS.2024.0006"
url: "https://doi.org/10.23919/CSMS.2024.0006"
pdf: literature/papers/adaptive-memetic-multi-robot-surveillance.pdf
tags: ["memetic-algorithm", "multi-robot", "route-planning", "local-search", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Adaptive memetic algorithm with dual-level local search for cooperative route planning of multi-robot surveillance systems

> [!info] Citation
> H. Cheng, J. Yi, W. Xia, H. Pu, and J. Luo, "Adaptive memetic algorithm with dual-level local search for cooperative route planning of multi-robot surveillance systems," *Complex System Modeling and Simulation*, vol. 4, no. 2, pp. 210–221, 2024.
> **Access:** Open access (SciOpen / Tsinghua University Press). [Local PDF](../papers/adaptive-memetic-multi-robot-surveillance.pdf) · [DOI](https://doi.org/10.23919/CSMS.2024.0006)

## Why this paper (pre-selected)

- **Memetic = GA + adaptive local search** with *dual-level* (among-robots and within-robot) refinement — a strong template for our M4 GA → M6 novel algorithm path.
- **Unified allocation + routing model** for multi-robot surveillance: exactly the coupled problem our project targets.
- Open access and fully reproducible-style experiments across team and target scales.

## TL;DR

This paper presents an adaptive dual-level memetic algorithm (DL-AMA) using continuous solution encoding to solve joint target allocation and route planning for multi-robot surveillance. By dynamically balancing inter-robot target reallocation and intra-robot route inversion, it significantly reduces total energy consumption, task completion time, and workload imbalance compared to state-of-the-art meta-heuristics.

## Problem & Motivation

- **Problem addressed:** Allocate key target positions among robots and concurrently plan each robot's route (multi-robot surveillance).
- **Why it matters:** Disaster search and rescue, agricultural irrigation, environmental monitoring.
- **Application domain:** Multi-robot surveillance.

## Research Question / Objective

- How to formulate and concurrently solve target position allocation and route planning for multi-robot surveillance in a unified optimization framework, while minimizing energy consumption (total path length), minimizing task completion time (maximum route length), and balancing workload distribution among robots?

## Contributions

- [x] Unified optimization model for target allocation + route planning minimizing total travel distance ($L$) and maximum route length ($L_{\max}$) subject to a task load variance threshold ($T_d \le T_h$).
- [x] Continuous solution encoding strategy leveraging floor-rounding and value-sorting to map continuous chromosome vectors directly into multi-robot target assignments and visiting sequences.
- [x] Adaptive memetic algorithm with dual-level local search (DL-AMA) operating independently at the task-assignment level (inter-robot) and path-planning level (intra-robot) with iteration-adaptive local search probabilities ($P_{tm}, P_{pm}$).
- [x] Comprehensive validation on TSPLIB benchmarks (eil51, eil76, eil101) across 2–8 robot teams alongside ROS/Gazebo physics simulations using Agilex Hunter 2.0 UGV models.

## Methodology

- **Problem formulation:** Joint allocation and route planning modeled via an integrated objective function $f = w_1 L + w_1 L_{\max} + w_2 C - w_2 D$ subject to task load difference constraint $T_d \le T_h$ (where $C$ is target concentration within a robot, $D$ is dispersion between robot centroids, and weights are $w_1=0.2, w_2=0.8, T_h=0.5$) [15–22, 36].
- **Algorithm:** Adaptive dual-level memetic algorithm (DL-AMA) combining genetic operators (tournament selection, two-point crossover) with:
  - *Task-level local search:* Reassigns targets between robots by mutating continuous vector values with an adaptive probability decaying over time: $P_{tm} = 0.05 - 0.04 \sqrt{\frac{\text{gen}}{\text{max\_gen}}}$.
  - *Path-level local search:* Reverses path sub-sequences within an individual robot's route with an adaptive probability increasing over time: $P_{pm} = 0.01 + 0.05 \left(\frac{\text{gen}}{\text{max\_gen}}\right)^2$.
  - *Continuous Encoding:* Solution dimension $M$ (targets) with values in $[1, N+1)$. Integer part $\lfloor \text{val} \rfloor$ assigns the robot $1..N$, and fractional values dictate visit order.
- **Baselines compared:** Equilibrium Optimizer (EO), Harris Hawks Optimization (HHO), Particle Swarm Optimization (PSO), Grey Wolf Optimization (GWO). Ablation variants: No-tm (lacks task-level search), No-pm (lacks path-level search), and DL-MA (fixed search probability).
- **Validation:** 20 independent runs on TSPLIB instances (eil51, eil76, eil101 with 2, 4, 6, 8 robots) and ROS/Gazebo simulations using Agilex Hunter 2.0 UGVs operating at $2\text{ m/s}$ max speed.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| **eil51 (4 robots) - Total / Max / Std** | **463.22 m / 125.85 m / 9.22 m** | DL-AMA vs EO (700.19m / 207.21m), PSO (1377.16m / 383.11m) |
| **eil76 (4 robots) - Total / Max / Std** | **620.07 m / 165.92 m / 9.04 m** | DL-AMA vs EO (1234.04m / 366.05m), GWO (1794.21m / 538.94m) |
| **eil101 (4 robots) - Total / Max / Std** | **771.53 m / 209.81 m / 14.12 m** | DL-AMA vs EO (1745.96m / 502.86m), PSO (3142.63m / 849.40m) |
| **Gazebo 51 targets (2 robots)** | 247.16 m / 126.22 m / 2.64 m | Task completion time: 110 s |
| **Gazebo 51 targets (6 robots)** | 258.94 m / 50.65 m / 5.99 m | Task completion time: 48 s |
| **Gazebo 51 targets (8 robots)** | 262.75 m / 42.49 m / 6.33 m | Task completion time: 40 s |

- **Key findings:**
  - DL-AMA significantly outperforms EO, HHO, PSO, and GWO across total distance (energy), maximum distance (completion time), and workload standard deviation (balance).
  - Task-level local search is vital early in evolution; omitting it (No-tm) leads to severe performance degradation that exacerbates as target scale increases.
  - Adaptive search probabilities ($P_{tm}$ decreasing, $P_{pm}$ increasing) effectively shift focus from global assignment space exploration to local path exploitation.
  - Increasing robot team size slightly increases total path distance due to cluster splitting overhead, but drastically reduces maximum route length and completion time (from 110s down to 40s in Gazebo).
- **Best-performing method:** DL-AMA (ranked #1 with average Friedman rank of 1.3).

## Strengths

- Simultaneous optimization of target allocation and route planning avoids the sub-optimality and lack of interaction inherent in traditional two-stage hierarchical approaches.
- Continuous encoding scheme enables standard evolutionary algorithms to optimize discrete assignment and permutation routing without requiring specialized repair operators.
- Adaptive dual-level local search efficiently allocates computational effort between global task redistribution and local route refinement.
- High workload balance and non-overlapping spatial route division reduce inter-robot interference and collisions.
- Thoroughly validated on standard benchmark instances and physically simulated in Gazebo/ROS with real-world robot kinematics.

## Limitations & Threats to Validity

- Assumes static surveillance targets and environments; does not evaluate dynamic target insertion or moving obstacles during execution.
- Assumes homogeneous robots with identical velocities ($2\text{ m/s}$) and capabilities.
- Continuous encoding vector scale ($M$-dimensional search space) may face computational scalability bottlenecks when applied to extremely large target scales ($>1000$ points).
- Does not explicitly account for energy/battery discharge constraints, refueling stops, or communication bandwidth/range constraints.

## Relevance to Our Project

- **Which milestones it informs:** M2 (coupled problem formulation), M4 (GA baseline), M6 (memetic + adaptive local search implementation).
- **Ideas it suggests:**
  - Adopt the continuous floor-rounding and sorting representation to handle combined allocation and TSP ordering within standard genetic operators.
  - Implement time-varying local search probabilities ($P_{tm}$ decaying, $P_{pm}$ growing) to manage exploration vs. exploitation in multi-level search spaces.
  - Combine inter-robot task reallocation operations with intra-robot route inversion (2-opt-like) operators.
- **Can we reproduce or extend it?** Yes; the algorithm structure is fully specified (Algorithms 1–3), uses public TSPLIB benchmarks, and details all parameter configurations ($P_c=0.95, \text{Pop\_size}=200, \text{Max\_gen}=500$). Extensions can incorporate heterogeneous robot speeds, battery limits, or dynamic obstacles.

## Open Questions

- How effectively does the dual-level local search adapt to heterogeneous multi-robot fleets with varying speeds and payload capacities?
- Can the continuous solution encoding maintain real-time responsiveness under dynamic target additions or agent failures?
- How can communication limits or non-line-of-sight constraints be integrated into the dual-level local search criteria?

## Keywords

adaptive memetic algorithm, dual-level local search, multi-robot, cooperative route planning, surveillance

## Abstract (verbatim)

The heightened autonomy and robust adaptability inherent in a multi-robot system have proven pivotal in disaster search and rescue, agricultural irrigation, and environmental monitoring. This study addresses the coordination of multiple robots for the surveillance of various key target positions within an area. This involves the allocation of target positions among robots and the concurrent planning of routes for each robot. To tackle these challenges, we formulate a unified optimization model addressing both target allocation and route planning. Subsequently, we introduce an adaptive memetic algorithm featuring dual-level local search strategies. This algorithm operates independently among and within robots to effectively solve the optimization problem associated with surveillance. The proposed method’s efficacy is substantiated through comparative numerical experiments and simulated experiments involving diverse scales of robot teams and different target positions.