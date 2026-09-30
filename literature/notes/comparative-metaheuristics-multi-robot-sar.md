---
id: comparative-metaheuristics-multi-robot-sar
title: "Comparative Analysis of Meta-Heuristic Algorithms for Multi-Robot Search and Rescue"
authors: ["Nada Ehab", "Farah Khaled", "Martin Morcos", "Ibrahim Abdelaty", "Abdelrahman Y. Altaher", "Omar M. Shehata"]
year: null
tags: ["multi-robot", "search-and-rescue", "path-planning", "comparative-study"]
pdf: literature/papers/comparative-metaheuristics-multi-robot-sar.pdf
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Comparative Analysis of Meta-Heuristic Algorithms for Multi-Robot Search and Rescue

> [!info] Citation
> Nada Ehab, Farah Khaled, Martin Morcos, Ibrahim Abdelaty, Abdelrahman Y. Altaher, Omar M. Shehata. *Comparative Analysis of Meta-Heuristic Algorithms for Multi-Robot Search and Rescue*. [PDF](../papers/comparative-metaheuristics-multi-robot-sar.pdf)

## TL;DR

This study empirically evaluates four metaheuristic optimization algorithms—Simulated Annealing (SA), Genetic Algorithm (GA), Ant Colony Optimization (ACO), and Harris Hawks Optimization (HHO)—on a Multi-Robot Search and Rescue (MRSAR) path planning problem with travel distance, battery degradation, and time-window constraints. Across 18 independent runs in a $25 \times 25$ grid environment, the Genetic Algorithm achieved the best convergence stability and lowest final operational cost, closely followed by Harris Hawks Optimization.

## Problem & Motivation

- **Problem addressed:** Multi-Robot Path Planning (MRPP) and task coordination in Search and Rescue (SAR) missions under operational constraints (obstacle avoidance, victim rescue time windows, battery capacity, and distance minimization).
- **Why it matters:** MRPP is NP-hard. As robot team size, static/dynamic obstacles, and time constraints scale, exact optimization methods become computationally intractable. Solvers must balance path length, deadline adherence, run-time efficiency, and solution reliability in time-critical environments.
- **Application domain:** Search and Rescue (SAR) robotics, Multi-Robot Systems (MRSs), and autonomous logistics/exploration in hazardous environments.

## Research Question / Objective

- How do trajectory-based (SA), evolutionary (GA), and swarm-based (ACO, HHO) metaheuristic algorithms compare in solution quality, convergence stability, and execution time when solving Multi-Robot Search and Rescue path planning under identical environment and constraint conditions?

## Contributions

- [x] Formulated a multi-robot SAR cost model combining robot travel distance and victim time-window penalties, incorporating dynamic battery decay that linearly reduces robot speed.
- [x] Conducted a side-by-side empirical benchmark of four metaheuristics (SA, GA, ACO, HHO) across 18 independent runs in a controlled $25 \times 25$ grid simulation environment.
- [x] Provided statistical validation using the non-parametric Friedman test and Holm-corrected pairwise Wilcoxon signed-rank tests to establish significant performance rankings among algorithms.

## Methodology

- **Problem formulation:**
  - *Decision variables:* Robot paths (sequence of grid nodes visited), point visitation order, and execution time relative to victim rescue time windows.
  - *Objective:* Minimize total cost combining total distance traveled ($\sum |n_{i+1} - n_i|$) and time-window adherence (rescue chance $TW - T_R$), maximizing saved victims relative to missed victims with objective weights $(w_{\text{dist}}, w_{\text{time}}) = (1.0, 0.5)$.
  - *Constraints:* Number of available robots (5), static obstacles (~13% grid density), maximum battery capacity (reducing velocity linearly over time from 0.8–1.5 units/step), and victim time windows.
- **Algorithms / techniques:**
  - *Simulated Annealing (SA):* Single-trajectory stochastic local search accepting probabilistically worse states controlled by temperature decay.
  - *Genetic Algorithm (GA):* Population-based evolutionary search utilizing selection, crossover, and mutation operators.
  - *Ant Colony Optimization (ACO):* Swarm-based probabilistic path construction guided by artificial pheromone trails.
  - *Harris Hawks Optimization (HHO):* Swarm-based nature-inspired algorithm modeling cooperative surprise-pounce hunting strategies with adaptive exploration/exploitation phases.
- **Baselines compared:** SA, GA, ACO, and HHO benchmarked against each other under identical simulation conditions.
- **Datasets / environments:** Controlled $25 \times 25$ grid simulation environment with 5 robots, static obstacle density of ~13% randomly generated across 18 independent runs, and a maximum budget of 600 iterations (500 for ACO).

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Environment | $25 \times 25$ Grid, 5 Robots | Static obstacles (~13% density) |
| Max Iterations | 600 (500 for ACO) | Standardized iteration cap |
| Independent Runs | 18 runs per algorithm | Matched obstacle scenarios across runs |
| GA Final Cost | **107.78 ± 11.23** | **Best solution quality & tightest spread** |
| HHO Final Cost | 118.11 ± 18.67 | 2nd best solution quality |
| ACO Final Cost | 146.39 ± 25.73 | 3rd place; highest execution time |
| SA Final Cost | 154.25 ± 23.64 | 4th place; fastest execution time |
| GA Execution Time | 117.37 ± 129.13 s | Balanced speed and solution quality |
| HHO Execution Time | 238.76 ± 374.91 s | Moderate execution time |
| ACO Execution Time | **790.21 ± 1108.73 s** | **Highest computational burden** |
| SA Execution Time | **22.92 ± 23.16 s** | **Fastest execution time** |
| Friedman Test | $\chi^2(3) = 48.87, p = 1.39 \times 10^{-10}$ | Confirms statistically significant overall difference |

- **Key findings:**
  - Population-based metaheuristics (GA and HHO) significantly outperformed trajectory-based (SA) and traditional swarm-based (ACO) metaheuristics in solution quality ($p = 0.0012$ across all pairwise Wilcoxon signed-rank comparisons).
  - GA maintained population diversity throughout search, achieving steady convergence, the lowest average cost (107.78), and the tightest standard deviation (11.23).
  - HHO exhibited step-like performance jumps, demonstrating strong local-minima escape capabilities to secure 2nd place (118.11).
  - ACO suffered from rapid early convergence followed by stagnation and carried a heavy computational burden (~790s average execution time).
  - SA was computationally fastest (~23s) but produced the highest average final cost (154.25).
- **Best-performing method:** Genetic Algorithm (GA), followed closely by Harris Hawks Optimization (HHO).

## Strengths

- Rigorous non-parametric statistical evaluation (Friedman test & Holm-adjusted Wilcoxon signed-rank tests) across 18 matched independent runs.
- Practical problem formulation incorporating dynamic state changes (battery charge depletion reducing robot speed linearly) alongside travel distance and time-window penalties.
- Controlled comparative framework establishing fair initial conditions and environment parameters across single-agent trajectory, evolutionary, and swarm approaches.

## Limitations & Threats to Validity

- Static $25 \times 25$ grid map with static obstacles; does not account for dynamic obstacles, continuous kinematic motion, or unmapped environments.
- Inter-robot spatial collision avoidance is treated implicitly via infeasibility filtering rather than explicit real-time path negotiation or collision avoidance constraints.
- Inconsistent iteration budget (ACO capped at 500 iterations due to runtime vs. 600 for others), though statistical time and cost metrics transparently highlight ACO's high runtime overhead.

## Relevance to Our Project

- **Which of our milestones it informs:** Problem formulation, Simulated Annealing (SA), Genetic Algorithm (GA), swarm metaheuristics (ACO/HHO), and comparative algorithm benchmarking.
- **Ideas it suggests for our problem:**
  - Adopting population-based search mechanics (GA or HHO) over single-trajectory annealing (SA) for complex multi-robot SAR objective landscapes.
  - Combining distance cost and time-window expiration into a unified composite objective function weighted by battery-dependent agent velocity.
  - Exploring hybrid metaheuristics (e.g., GA initialized or combined with HHO exploration mechanics) to combine fast global exploration with local refinement.
- **Can we reproduce or extend it?** Yes. The target functions, grid dimensions ($25 \times 25$), robot count (5), obstacle density (~13%), and simulation parameters $(w_{\text{dist}}=1.0, w_{\text{time}}=0.5)$ are fully specified. We can extend it by introducing continuous action spaces, explicit inter-robot collision avoidance constraints, or dynamic obstacle movement.

## Open Questions

- How do these metaheuristics perform in larger, dynamic, or partially known environments where victim locations must be discovered online?
- Can explicit local search or local path repair mechanisms resolve ACO's early stagnation without compounding its computational overhead?
- Would a hybrid GA-HHO architecture achieve faster convergence while preserving the solution quality of pure GA?

## Notable Quotes

> "Experimental results indicate that the Genetic Algorithm (GA) achieved the best convergence and final solution quality (Cost approximately 103), followed closely by Harris Hawks Optimization (HHO)." (p. 1 / Abstract)

> "Multi-Robot Path Planning (MRPP) instances are considered NP-hard which means as the number of robots, obstacles, and time-window constraints grow, exact methods become difficult to manage." (p. 1 / Section I)

> "Overall, the findings indicate that population-based algorithms, especially GA, are more effective for solving multirobot path planning problems with time constraints because they explore the search space more thoroughly and find more reliable solutions." (p. 5 / Section V)

## Keywords

Multi-robot, Optimization Algorithms, Search and Rescue, Path Planning

## Abstract (verbatim)

We present a comparative analysis of four metaheuristic optimization algorithms applied to the Multi-Robot Search and Rescue (MRSAR) problem: Simulated Annealing (SA), Genetic Algorithm (GA), Ant Colony Optimization (ACO), and Harris Hawks Optimization (HHO). The objective of the algorithms was to minimize the cost function of the rescue operation, made up of the robot’s travel distance and the adherence to the rescue time window. Experimental results indicate that the Genetic Algorithm (GA) achieved the best convergence and final solution quality (Cost approximately 103), followed closely by Harris Hawks Optimization (HHO).