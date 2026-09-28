---
id: enhanced-ga-heterogeneous-multi-robot
title: "An enhanced genetic algorithm for optimized task allocation and planning in heterogeneous multi-robot systems"
authors: ["Ahmed Nait Chabane", "Ouahib Guenounou"]
year: 2025
venue: "Complex & Intelligent Systems"
doi: "10.1007/s40747-025-02062-w"
url: "https://doi.org/10.1007/s40747-025-02062-w"
pdf: literature/papers/enhanced-ga-heterogeneous-multi-robot.pdf
tags: ["genetic-algorithm", "heterogeneous-fleet", "task-allocation", "path-planning", "benchmark", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# An enhanced genetic algorithm for optimized task allocation and planning in heterogeneous multi-robot systems

> [!info] Citation
> A. Nait Chabane and O. Guenounou, "An enhanced genetic algorithm for optimized task allocation and planning in heterogeneous multi-robot systems," *Complex & Intelligent Systems*, vol. 11, art. 435, 2025.
> **Access:** Open access (Springer). [Local PDF](../papers/enhanced-ga-heterogeneous-multi-robot.pdf) · [DOI](https://doi.org/10.1007/s40747-025-02062-w)

## Why this paper (pre-selected)

- **Open access + reproducible benchmark design** — it compares against MILP, standard GA, PSO and a surrogate-assisted EA across 50-site / 4-robot instances. That is a ready-made methodology template for Milestones 2 and 4.
- **Two-phase GA** (capability-constrained assignment, then per-robot route refinement) is a clean structure we can adapt for heterogeneous fleets.
- Ground-robot (not UAV) focus adds domain diversity to the review set.

## TL;DR

This paper introduces a novel two-phase enhanced genetic algorithm (EGA) for multi-robot task allocation and path planning in heterogeneous industrial inspection fleets. By decoupling capability-constrained global task assignment (Phase 1) from individual route refinement (Phase 2), EGA yields near-optimal solutions (<1.5% optimality gap) while reducing computational runtime by up to 90% compared to exact MILP solvers.

## Problem & Motivation

- **Problem addressed:** Task allocation and path planning for heterogeneous multi-robot systems (varying sensing capabilities) in industrial inspection.
- **Why it matters:** Coordinating heterogeneous multi-robot fleets is NP-hard. Suboptimal task allocation leads to excessive downtime, increased energy consumption, and safety risks, while exact mathematical methods (e.g., MILP) suffer from exponential computational complexity and fail to scale for real-time or large-scale industrial missions.
- **Application domain:** Industrial inspection with heterogeneous robot fleets across spatially distributed sites (e.g., oil & gas pipelines, manufacturing maintenance, logistics warehouses).

## Research Question / Objective

- How to design a scalable, robust, and computationally efficient optimization algorithm (EGA) that solves the combined task allocation and route planning problem for heterogeneous multi-robot fleets under strict capability constraints, minimizing total travel distance while scaling effectively to large industrial inspection scenarios.

## Contributions

- [x] Comprehensive mathematical problem formulation (MILP) with MTZ subtour elimination constraints capturing heterogeneous robot capability matching and interdependencies.
- [x] Phase 1: Domain-specific 3-row chromosome matrix encoding (Site, Measurement, Robot) and capability-aware genetic operators that enforce constraint feasibility by construction.
- [x] Phase 2: Local genetic refinement of individual robot routes using single-row route permutations and modified cycle crossover (CX2) to minimize total travel distance and balance workload.
- [x] Extensive empirical benchmarking against MILP (Gurobi), single-phase GA, PSO, and BL-SAEA across 30 scenario configurations (up to 50 sites and 4 robots), as well as empirical complexity modeling ($t \propto S^{2.37} R^{1.01}$) and a dynamic robot breakdown scenario.

## Methodology

- **Problem formulation:** Capability-constrained task assignment + route optimization. Formulated as a Mixed Integer Linear Programming (MILP) model minimizing total Euclidean travel distance with binary decision variables ($x_{ij}^r, y_i^r, z^r$) and Miller–Tucker–Zemlin (MTZ) subtour elimination constraints.
- **Algorithm:** Two-phase Enhanced Genetic Algorithm (EGA):
  - *Phase 1 (Global Task Allocation & Planning):* Uses a $3 \times L$ integer matrix encoding (Row 1: Sites, Row 2: Required Measurements, Row 3: Assigned Robot IDs). Initialization draws robot assignments strictly from compatible sets $R_m = \{r \mid m \in C_r\}$. Applies binary tournament selection, duplicate-preventing column crossover, and column swap/re-assignment mutation.
  - *Phase 2 (Route Refinement):* Decouples assigned tasks per robot into 1D chromosome route permutations. Applies binary tournament selection, modified cycle crossover (CX2), and 2-site swap mutation to locally optimize each robot's visiting sequence.
- **Baselines compared:** MILP (exact solver using Gurobi with 60s and 600s time limits), standard GA (Phase 1 only), PSO (swap-sequence variant), and BL-SAEA (adapted bi-level surrogate-assisted evolutionary algorithm with Gaussian Process regression).
- **Validation:** 30 benchmark instances ranging from 5 to 50 inspection sites (with site coordinates and required measurement sets) and 2 to 4 heterogeneous robots ($r_1: \{m_1, m_3\}$, $r_2: \{m_2, m_4\}$, $r_3: \{m_1, m_2\}$, $r_4: \{m_3\}$).

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Average optimality gap | < 1.5% | near-optimal (for instances up to 30 sites; <3% up to 50 sites) |
| Runtime reduction vs MILP | up to 90% | large-scale instances (~82s for 50 sites / 4 robots vs 600s+ timeout for MILP) |

- **Key findings:**
  - **Near-optimality & Computational Speedup:** EGA achieves average optimality gaps below 1.5% for instances up to 30 sites and below 3% up to 50 sites, while reducing execution time by over 90% compared to MILP.
  - **Critical Impact of Phase 2 Refinement:** Phase 2 significantly improves final solution quality and reduces performance variance (lower medians and narrower IQRs across 30 runs), preventing premature plateauing in medium and large-scale scenarios (e.g., an 18.86% improvement over Phase 1 alone in 50-site instances).
  - **Metaheuristic Performance Comparison:** EGA consistently outperforms single-phase GA and PSO across all problem sizes ($p < 0.0001$, Cohen's $d > 0.8$). While BL-SAEA offers faster runtimes in some configurations, EGA yields superior solution accuracy in complex, large-scale cases.
  - **Fleet Heterogeneity & Dynamic Resiliency:** Increasing robot team size and capability overlap reduces total travel distance. In a mid-mission robot failure scenario, EGA successfully re-allocates remaining tasks and re-plans feasible paths without full re-optimization from scratch.
- **Best-performing method:** EGA (achieves the best overall balance of solution quality, convergence stability, and computational scalability).

## Strengths

- **Constraint-Preserving Genetic Operators:** Domain-specific 3-row chromosome structure and customized crossover/mutation operators enforce capability matching and prevent duplicate assignments by construction, avoiding infeasible solutions without relying on heavy penalty functions.
- **Effective Two-Phase Decoupling:** Separating global assignment complexity from local TSP route refinement allows Phase 1 to search the fleet allocation space efficiently while Phase 2 optimizes local route quality and convergence stability.
- **Rigorous Statistical & Empirical Validation:** Validated across 30 independent runs per instance using Welch's t-tests, Cohen's d effect size estimations, 95% confidence intervals, and a fitted power-law empirical complexity model ($t \propto S^{2.37} R^{1.01}, R^2=0.99$).
- **Dynamic Re-planning Capability:** Demonstrated ability to quickly re-allocate tasks and adapt routes following an unexpected robot breakdown during execution.

## Limitations & Threats to Validity

- **Static Task Assumptions:** The primary benchmark evaluations assume static inspection site locations and deterministic measurement requirements, omitting real-time stochastic task influx or dynamic environmental obstacles.
- **Single-Objective Minimization:** Focuses solely on minimizing total travel distance (as a proxy for energy), without explicitly optimizing multi-objective trade-offs like mission completion time (makespan), peak battery state of charge, or communication delays.
- **Idealized Spatial Environment:** Distance calculations rely on 2D Euclidean spatial metrics between site coordinates without 3D terrain modeling, kinodynamic constraints, or detailed collision avoidance trajectories.
- **Empirical Fleet Scale Bound:** Tested on physical benchmark instances up to 4 robots and 50 sites, with larger scales (up to 200 sites and 20 robots) evaluated via power-law model extrapolations.

## Relevance to Our Project

- **Which milestones it informs:** M2 (formulation), M4 (GA), results analysis (benchmark design).
- **Ideas it suggests:**
  - Adapt the 3-row matrix chromosome encoding (Site, Measurement, Robot) to cleanly separate task-capability matching from path planning.
  - Implement a two-phase architecture to decouple global multi-robot task allocation from per-robot local route TSP optimization.
  - Utilize capability-restricted initialization and modified cycle crossover (CX2) to eliminate infeasible offspring during evolutionary search.
  - Adopt their empirical runtime modeling ($t = a S^b R^c$) and statistical validation framework (Welch's t-test, Cohen's d) for Milestone 4 evaluation.
- **Can we reproduce or extend it?** Yes. The benchmark dataset (50 sites with coordinates and required measurement sets in Table 3) and robot capabilities (Table 2) are fully published in the paper. We can extend the framework by adding makespan (min-max individual distance) optimization, battery discharge/recharging constraints, or asynchronous decentralized Phase 2 execution.

## Open Questions

- How can Phase 1 and Phase 2 be adapted to multi-objective evolutionary algorithms (e.g., NSGA-II/NSGA-III) to construct Pareto fronts balancing total travel distance, makespan, and energy usage?
- Can Phase 2 route refinement be executed locally on individual robot microcontrollers in an asynchronous, decentralized manner after receiving Phase 1 assignments?
- How does performance scale when adding non-linear energy consumption models and mandatory visits to charging depots?

## Keywords

enhanced genetic algorithm, heterogeneous multi-robot systems, task allocation, route planning, MILP benchmark

## Abstract (verbatim)

Efficient task allocation and path planning in heterogeneous multi-robot systems (MRS) remains a significant challenge in industrial inspection contexts, particularly when robots exhibit diverse sensing capabilities and must operate across spatially distributed sites. To address the limitations of exact methods and conventional heuristics, we propose a novel two-phase enhanced genetic algorithm (EGA) tailored for capability-constrained task assignment and route optimization. The first phase employs a domain-specific chromosome encoding to assign tasks while enforcing robot-measurement compatibility. The second phase locally refines each robot’s path to minimize travel distance and improve load balancing. We benchmark the EGA against an exact mixed integer linear programming (MILP) model, a standard genetic algorithm (single-phase), a particle swarm optimization (PSO) approach, and an adapted version of the bi-level surrogate-assisted evolutionary algorithm (BL-SAEA) across scenarios involving up to 50 inspection sites and 4 heterogeneous robots. Experimental results show that our EGA consistently produces near-optimal solutions, achieving average optimality gaps below 1.5%, while reducing computation times by up to 90% compared to MILP. Furthermore, the second phase significantly enhances convergence stability and solution robustness, especially in large-scale instances. These results demonstrate the scalability and practical suitability of the proposed method for real-time, resource-constrained industrial inspection missions.