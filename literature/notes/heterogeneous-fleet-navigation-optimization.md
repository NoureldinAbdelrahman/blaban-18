---
id: heterogeneous-fleet-navigation-optimization
title: "Metaheuristic-Based Navigation Optimization for Heterogeneous Autonomous Vehicle Fleets"
authors: ["Seifeldin Abbas", "Rasheed Atia", "Yassin Otifa", "Jessica Magdy", "Omar M. Shehata"]
year: 2025
tags: ["vehicle-routing", "heterogeneous-fleet", "navigation", "metaheuristics"]
pdf: literature/papers/heterogeneous-fleet-navigation-optimization.pdf
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Metaheuristic-Based Navigation Optimization for Heterogeneous Autonomous Vehicle Fleets

> [!info] Citation
> Seifeldin Abbas, Rasheed Atia, Yassin Otifa, Jessica Magdy, Omar M. Shehata. *Metaheuristic-Based Navigation Optimization for Heterogeneous Autonomous Vehicle Fleets*. [PDF](../papers/heterogeneous-fleet-navigation-optimization.pdf)

## TL;DR

A comparative evaluation of four metaheuristic algorithms (SA, GA, ACO, TLBO) for solving the Heterogeneous Fleet Vehicle Routing Problem (HFVRP) under strict hard feasibility constraints, showing that Simulated Annealing yields the best solution quality and computational efficiency while ACO provides superior stability across independent runs.

## Problem & Motivation

- **Problem addressed:** Optimizing routing for heterogeneous vehicle fleets with distinct capacities and maximum travel distances under strict hard feasibility constraints (prohibiting any infeasible solutions during search).
- **Why it matters:** Real-world logistics and supply chain operations rely on mixed fleets (trucks, vans, motorcycles). Large-scale instances are computationally intractable ($NP$-hard with search spaces exceeding $10^{90}$ configurations). Hard constraints prevent generating unviable routes but make search space navigation challenging.
- **Application domain:** Logistics, supply chain management, autonomous vehicle fleet routing, last-mile delivery, and multi-robot navigation.

## Research Question / Objective

- How do trajectory-based (Simulated Annealing) and population-based (Genetic Algorithm, Ant Colony Optimization, TLBO) metaheuristics compare in terms of solution quality, execution time, and stability when applied to the HFVRP under strict hard feasibility constraints?

## Contributions

- [x] Formulated a hard-constraint HFVRP model enforcing strict capacity and distance limits without allowing invalid intermediate solutions.
- [x] Implemented a randomized "Best Insertion" constructive heuristic guaranteeing 100% feasible initial solution populations.
- [x] Provided a systematic comparative statistical benchmark across 7 test cases (4 to 60 customers, up to 7 vehicles) evaluating SA, GA, ACO, and TLBO across key performance indicators (Best Cost, Mean Cost, Std Dev, Wall-clock Time).

## Methodology

- **Problem formulation:**
  - *Decision variables:* Binary $x_{ijv} \in \{0,1\}$ (vehicle $v$ travels from $i$ to $j$), binary $y_v \in \{0,1\}$ (vehicle $v$ is used).
  - *Objective:* Minimize weighted sum of distance and active vehicle count $F = w_1 \sum_{v} \sum_{i \neq j} d_{ij} x_{ijv} + w_2 \sum_v y_v$ where $w_1 \gg w_2$.
  - *Constraints:* Exactly one visit per customer, strict vehicle capacities ($\sum q_i \le Q_v$), and maximum distance limits ($\sum d_{ij} \le D_v$). Direct "List of Lists" route encoding allows $O(1)$ constraint evaluation.
- **Algorithms / techniques:**
  - *Simulated Annealing (SA):* Trajectory-based with geometric cooling ($T_{init}=1000, T_{final}=1.0, \alpha=0.933$).
  - *Genetic Algorithm (GA):* Best-Cost Route Crossover (BCRC) and Best Insertion repair ($N=50, 150 \text{ gen}, p_c=0.8, p_m=0.3$).
  - *Ant Colony Optimization (ACO):* Swarm intelligence with pheromone weight $\alpha=1.0$, heuristic weight $\beta=3.0$, 50 ants, 150 iterations.
  - *Teaching-Learning Based Optimization (TLBO):* Teacher and Learner phases using BCRC crossover ($N=50, 75 \text{ iter}$).
  - *Operators:* Inter-route Swap, Relocate (Shift), and Intra-route 2-Opt.
- **Baselines compared:** Systematic comparison among the four implemented metaheuristics (SA, GA, ACO, TLBO).
- **Datasets / environments:** Seven synthetically generated test cases of increasing complexity (from 4-customer proof-of-concept up to 60-customer/7-vehicle challenge).

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Best Cost (Case 6 - 25 Customers) | SA: **3593.45** / GA: **3593.45** | SA and GA tied for best solution cost |
| Execution Time (Case 6 - 25 Customers) | TLBO: **0.44s**, SA: 0.57s, GA: 0.66s, ACO: 12.14s | TLBO and SA achieved fastest convergence |
| Best Cost (Case 7 - 60 Customers) | SA: **15323.91**, ACO: 15657.85, GA: 16463.94, TLBO: 17794.96 | SA found the absolute lowest cost solution |
| Mean Cost & Std Dev (Case 7 - 10 Runs) | ACO: **15824.67** (SD: **236.08**), SA: 16217.15 (SD: 733.31) | ACO demonstrated highest reliability/stability |
| Execution Time (Case 7 - 60 Customers) | SA: **0.96s**, TLBO: 1.38s, GA: 2.90s, ACO: 67.66s | SA was ~70x faster than ACO |
| Evaluation Budget | ~7,500 fitness evaluations per run | Calibrated across all algorithms for fair comparison |

- **Key findings:**
  - SA dominated in raw optimality and speed on large instances (Case 7 cost 15,323.91 in 0.96s), producing compact, radially fanned routes.
  - ACO delivered the lowest mean cost and variance (Std Dev 236.08 vs SA's 733.31 on Case 7), but suffered high computational runtime ($67.66\text{s}$) due to $O(I \cdot A \cdot n^2)$ complexity.
  - GA and TLBO struggled in highly constrained large spaces due to the "Best Insertion" repair mechanism getting trapped, producing route-crossing artifacts.
- **Best-performing method:** **Simulated Annealing (SA)** for speed and peak solution quality; **Ant Colony Optimization (ACO)** for consistency and stability.

## Strengths

- Hard-constraint feasibility model prevents spending evaluation budget on infeasible solutions.
- Direct "List of Lists" direct encoding provides fast $O(1)$ access for vehicle route validation.
- Standardized evaluation budget (~7,500 evaluations) and multi-run statistical analysis (10 independent runs on Cases 6 and 7) ensure experimental rigor.
- SA achieves near-optimal global solutions in under 1 second wall-clock time.

## Limitations & Threats to Validity

- Benchmark test cases are synthetically generated rather than drawn from standard public HFVRP benchmarks.
- Trajectory-based SA shows high standard deviation, requiring multiple independent restarts to guarantee peak performance.
- Best Insertion repair heuristic limits exploration capabilities for population-based methods (GA/TLBO) in dense spaces.
- Prohibiting soft constraints / penalty functions prevents algorithms from traversing infeasible intermediate states to escape local optima.

## Relevance to Our Project

- **Which of our milestones it informs:** Problem formulation, Simulated Annealing (SA), Genetic Algorithm (GA), Swarm Intelligence (ACO), and novel/hybrid metaheuristic optimization milestones.
- **Ideas it suggests for our problem:**
  - Utilize Direct Route Encoding ("List of Lists") to optimize memory access and enable instant $O(1)$ feasibility checks.
  - Implement a hybrid SA-ACO algorithm to combine SA's rapid search speed with ACO's global stability.
- **Can we reproduce or extend it?** Yes; core algorithms, neighborhood operators (Swap, Relocate, 2-Opt), and Best Insertion heuristics are detailed in pseudocode. We can extend it by testing soft constraint penalty functions or applying deep reinforcement learning policies (DQN/PPO) for route repair.

## Open Questions

- Could temporary soft constraint violations with dynamic penalty factors enable GA and TLBO to escape local optima without route crossing?
- How well do these metaheuristics perform when scaled to standard public HFVRP benchmarks (e.g., Golden or Li instances)?
- Can learned policies (DQN/PPO) replace greedy "Best Insertion" logic to anticipate congestion and constraint bottlenecks?

## Notable Quotes

> "Results indicate that while population-based methods like ACO and TLBO offer robust search capabilities, the singlepoint Simulated Annealing algorithm demonstrates superior efficiency and solution quality for the specific constraints and scale of the tested instances." (p. 1)

> "The primary contribution of this work lies not in proposing a novel metaheuristic, but in providing a systematic comparative analysis under strict hard-constraint feasibility, a setting that is less explored in existing HFVRP literature." (p. 2)

## Keywords

HFVRP, Simulated Annealing, Genetic Algorithm, Ant Colony Optimization, TLBO, Metaheuristics

## Abstract (verbatim)

The Heterogeneous Fleet Vehicle Routing Problem (HFVRP) represents a complex combinatorial optimization challenge with significant real-world applications in logistics and supply chain management. This paper presents a comparative study of four metaheuristic algorithms-Simulated Annealing (SA), Genetic Algorithm (GA), Ant Colony Optimization (ACO), and Teaching-Learning Based Optimization (TLBO)-applied to the HFVRP. The problem is modeled with strict hard constraints on vehicle capacity and maximum travel distance, prohibiting any infeasible solutions during the search process. A ”Best Insertion” heuristic is implemented to generate feasible initial solutions. The algorithms are evaluated on a set of seven test cases of increasing complexity, ranging from simple 4-customer scenarios to a largescale 60-customer challenge. Performance is analyzed based on solution quality (final cost), execution time, and convergence behavior. Results indicate that while population-based methods like ACO and TLBO offer robust search capabilities, the singlepoint Simulated Annealing algorithm demonstrates superior efficiency and solution quality for the specific constraints and scale of the tested instances.
