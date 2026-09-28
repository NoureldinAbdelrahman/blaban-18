---
id: energy-learning-hyper-heuristic-heterogeneous-uav
title: "Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints"
authors: ["Mengshun Yuan", "Mou Chen", "Tongle Zhou", "Zengliang Han"]
year: 2025
venue: "Defence Technology"
doi: "10.1016/j.dt.2025.06.006"
url: "https://doi.org/10.1016/j.dt.2025.06.006"
pdf: literature/papers/energy-learning-hyper-heuristic-heterogeneous-uav.pdf
tags: ["hyper-heuristic", "uav", "task-assignment", "energy", "operator-selection", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints

> [!info] Citation
> M. Yuan, M. Chen, T. Zhou, and Z. Han, "Energy learning hyper-heuristic algorithm for cooperative task assignment of heterogeneous UAVs under complex constraints," *Defence Technology*, vol. 54, pp. 1–14, 2025.
> **Access:** Open access (Elsevier / KeAi). [Local PDF](../papers/energy-learning-hyper-heuristic-heterogeneous-uav.pdf) · [DOI](https://doi.org/10.1016/j.dt.2025.06.006)

## Why this paper (pre-selected)

- **Hyper-heuristic, not another named swarm algorithm** — it learns *how to pick* low-level operators via an "energy learning" mechanism instead of relying on one metaphor. Ideal seed for the Milestone 6 novel algorithm.
- **Energy is the optimization currency**, matching our goal of energy-aware cooperative assignment.
- The authors benchmark **against PSO and GWO**, giving us ready baselines for Milestone 5.

## TL;DR

The paper proposes an Energy Learning Hyper-Heuristic (EL-HH) algorithm for multi-UAV cooperative task assignment under 11 complex operational constraints. It combines a three-layer solution encoding, an adaptive Boltzmann energy-based operator selection mechanism, and directed-graph adjustment strategies to deliver faster convergence and higher solution quality than standard metaheuristics.

## Problem & Motivation

- **Problem addressed:** Cooperative task assignment for heterogeneous UAVs subject to 11 complex constraints (task types, precedence order, time windows, heterogeneous payloads, missile capacities, flight time limits, and safety obstacles).
- **Why it matters:** Heterogeneous UAV swarm missions in complex operational environments require optimal task assignment and scheduling to maximize task completion rewards while minimizing time and energy consumption; conventional metaheuristics often get trapped in local optima or suffer from unfeasible solution encodings.
- **Application domain:** Multi-UAV / UAV-swarm cooperative operations in military combat scenarios (reconnaissance, electronic jamming, deception, communication relay, strike) and autonomous indoor flight operations.

## Research Question / Objective

- How to design an adaptive hyper-heuristic framework that dynamically manages diverse low-level heuristic operators and enforces complex temporal and spatial constraints to assign tasks among heterogeneous UAVs without getting trapped in local optima?

## Contributions

- [x] Three-layer encoding (task sequence, UAV sequence, waiting time).
- [x] Energy-learning hyper-heuristic that adaptively updates operator selection probabilities using a Boltzmann distribution and exponential energy decay.
- [x] Directed-graph task-order (DFS deadlock elimination) and time-adjustment (topological sorting) strategies.

## Methodology

- **Problem formulation:** Formulates a non-convex optimization model with 11 complex constraints and a bounded objective function $J(X) \in (0, 1)$ combining task completion rewards, flight time/energy savings rewards, and penalty costs for load, time, and window violations.
- **Algorithm:** Energy Learning Hyper-Heuristic (EL-HH) managing 3 selection operators and 11 action operators partitioned into Task, UAV, and Task-UAV groups. Operator selection probabilities dynamically adjust via Boltzmann distribution based on energy values updated by fitness improvements.
- **Baselines compared:** Particle Swarm Optimization (PSO), Grey Wolf Optimizer (GWO), Artificial Bee Colony (ABC), and Whale Optimization Algorithm (WOA).
- **Validation:** Evaluated across a simple simulation scene (5 UAVs, 10 tasks), a complex simulation scene (6 UAVs, 18 tasks), and a physical indoor experiment with 3 quadrotors, 6 tasks, and an optical motion capture system.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| **Simple Scene Setup** | 5 UAVs, 10 Tasks | $20\text{ km} \times 20\text{ km} \times 5\text{ km}$ flight space; $T_{max}=500$, population $M=50$ |
| **Complex Scene Setup** | 6 UAVs, 18 Tasks | $20\text{ km} \times 20\text{ km} \times 5\text{ km}$ flight space; $T_{max}=2500$, population $M=50$ |
| **Indoor Experiment Setup** | 3 Quadrotors, 6 Tasks | $5\text{ m} \times 5\text{ m} \times 3\text{ m}$ indoor arena with motion capture & obstacles |
| **Complex Scene Solution Fitness** | $\approx 0.78$ (EL-HH) vs. $0.71$–$0.76$ (Baselines) | EL-HH achieved highest solution fitness and fastest convergence rate [52, Fig. 12] |
| **Indoor Flight Execution Times** | U1: 2.95 min, U2: 2.29 min, U3: 2.08 min | 100% mission success with obstacle avoidance in physical flight test |
| **Theoretical Time Complexity** | $O(T_{max} \cdot M \cdot N_X)$ | Complexity per generation excluding path planning and graph adjustments |

- **Key findings:** EL-HH achieves faster convergence speeds and higher solution quality compared to PSO, GWO, ABC, and WOA as constraints and problem scale grow.
- **Best-performing method:** EL-HH.

## Strengths

- **Adaptive Energy Learning:** Dynamically updates operator selection probabilities via Boltzmann distribution based on performance history, preventing local optimal trapping.
- **Modular Operator Partitioning:** Action operators are separated into Task, UAV, and Task-UAV groups, protecting well-optimized sub-sequences during mutation/crossover.
- **Graph-Based Constraint Handling:** DFS loop detection and topological sorting systematically eliminate execution deadlocks and insert required wait times.
- **Physical Hardware Validation:** Proven on physical quadrotor UAVs in an indoor obstacle field with motion capture tracking, demonstrating real-world feasibility.

## Limitations & Threats to Validity

- **Partial Time-Window Enforcement:** The task time adjustment strategy only partially resolves time window constraints and fails if arrival time exceeds a threshold relative to the earliest start time.
- **Complexity Omissions:** Complexity calculations exclude path planning and directed-graph deadlock detection/topological sorting operations.
- **Static Map Assumption:** Assumes prior knowledge of fixed obstacle locations and constant flight speeds, limiting adaptability in dynamic combat environments.

## Relevance to Our Project

- **Which milestones it informs:** M5 (baselines), M6 (hyper-heuristic / adaptive operator selection), optional ML bonus.
- **Ideas it suggests:**
  - Adapt the Boltzmann-based operator energy learning mechanism for dynamic heuristic selection in Milestone 6.
  - Utilize three-layer scheme encoding (task order, UAV mapping, wait times) to maintain clear solution structures.
  - Implement directed-graph cycle detection and topological sorting for handling complex task precedence dependencies.
- **Can we reproduce or extend it?** Yes, the mathematical model, objective function parameters, low-level operators, and pseudo-code are explicitly detailed and reproducible in Python or MATLAB.

## Open Questions

- How can EL-HH be extended to handle dynamic environment changes, unexpected UAV failures, or moving obstacles in real time?
- Can reinforcement learning methods (e.g., Q-learning or Deep Q-Networks) replace or complement the exponential decay rules for operator energy updates?
- How does EL-HH scale when applied to massive swarms of 50+ UAVs with hundreds of inter-dependent tasks?

## Keywords

hyper-heuristic, operator selection, energy learning, heterogeneous UAVs, cooperative task assignment, complex constraints

## Abstract (verbatim)

Cooperative task assignment is one of the key research focuses in the field of unmanned aerial vehicles (UAVs). In this paper, an energy learning hyper-heuristic (EL-HH) algorithm is proposed to address the cooperative task assignment problem of heterogeneous UAVs under complex constraints. First, a mathematical model is designed to define the scenario, complex constraints, and objective function of the problem. Then, the scheme encoding, the EL-HH strategy, multiple optimization operators, and the task sequence and time adjustment strategies are designed in the EL-HH algorithm. The scheme encoding is designed with three layers: task sequence, UAV sequence, and waiting time. The EL-HH strategy applies an energy learning method to adaptively adjust the energies of operators, thereby facilitating the selection and application of operators. Multiple optimization operators can update schemes in different ways, enabling the algorithm to fully explore the solution space. Afterward, the task order and time adjustment strategies are designed to adjust task order and insert waiting time. Through the iterative optimization process, a satisfactory assignment scheme is ultimately produced. Finally, simulation and experiment verify the effectiveness of the proposed algorithm.