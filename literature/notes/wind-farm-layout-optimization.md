---
id: wind-farm-layout-optimization
title: "Advancing Sustainable Energy: Analyzing Stochastic Algorithms and Q-Learning for Wind Farm Layout Optimization"
authors: ["Mohamed Elsheikh", "Amr Yonis", "Jessica Magdy", "Omar M. Shehata"]
year: null
tags: ["energy", "wind-farm", "layout-optimization", "reinforcement-learning"]
pdf: literature/papers/wind-farm-layout-optimization.pdf
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Advancing Sustainable Energy: Analyzing Stochastic Algorithms and Q-Learning for Wind Farm Layout Optimization

> [!info] Citation
> Mohamed Elsheikh, Amr Yonis, Jessica Magdy, Omar M. Shehata. *Advancing Sustainable Energy: Analyzing Stochastic Algorithms and Q-Learning for Wind Farm Layout Optimization*. [PDF](../papers/wind-farm-layout-optimization.pdf)

## TL;DR

This paper presents a comparative benchmark of four meta-heuristic algorithms (Simulated Annealing, Genetic Algorithm, Particle Swarm Optimization, Moth Flame Optimization) and Deep Q-Learning for Wind Farm Layout Optimization across multiple grid scales. The study reveals that Genetic Algorithm yields the highest solution quality, Moth Flame Optimization achieves the best trade-off between speed and optimality, and Simulated Annealing offers maximum computational speed and repeatability.

## Problem & Motivation

- **Problem addressed:** Wind Farm Layout Optimization (WFLO) — strategically placing wind turbines within a constrained grid layout to maximize total energy production while minimizing procurement/maintenance costs and wake effect interference.
- **Why it matters:** Wake dynamics significantly reduce downstream wind speeds and power generation. Because WFLO is a non-convex, NP-hard problem with vast search spaces (e.g., \\(>10^{44}\\) unique layout configurations for fewer than 30 turbines), standard numerical optimization methods are computationally intractable.
- **Application domain:** Onshore wind energy engineering, multi-turbine layout design, and sustainable energy infrastructure optimization.

## Research Question / Objective

- How do stochastic meta-heuristic algorithms (SA, GA, Discrete PSO, MFO) and Reinforcement Learning (Deep Q-Learning) compare in terms of computational runtime, solution optimality (fitness value), and repeatability when optimizing wind farm layouts under identical physical and operational constraints across varying grid scales (15x15, 20x20, 25x25)?

## Contributions

- [x] Comprehensive comparative benchmark evaluating four stochastic meta-heuristics (SA, GA, Discrete PSO, MFO) alongside Deep Q-Learning on identical WFLO benchmark setups.
- [x] Mathematical problem formulation incorporating a modified Jensen single wake model, 36 weighted wind directions, spacing rules, non-linear turbine cost functions, dead zone obstacles, and a Minimum Operational Power Coefficient (MOPC).
- [x] Custom adaptations of continuous algorithms (PSO and MFO) and formulation of a discrete state-action-reward structure for Deep Q-Network grid layout optimization.
- [x] Rigorous statistical analysis based on 20 independent runs per algorithm across three grid sizes (15x15, 20x20, 25x25), measuring best/worst/average fitness, standard deviation, coefficient of variation, and average execution time.
- [x] Open-source modular implementation released on GitHub (`IrrationalInteger/WFLO-Optimization`) for reproducibility.

## Methodology

- **Problem formulation:**
  - **Decision variables:** Total number of turbines \\(N_{total}\\) (integer) and turbine grid coordinates array \\(M\\) (1D array of occupied cell coordinate pairs).
  - **Objective function:** Minimize \\(\text{Cost}_P / \text{Power}_{total}\\), where \\(\text{Power}_{total}\\) is the weighted average power across 36 wind directions using Jensen's single wake model (\\(\alpha = 0.075\\)), and \\(\text{Cost}_P = N_{total} \cdot \left(\frac{2}{3} + \frac{1}{3} e^{-0.00174 \cdot N_{total}^2}\right)\\) models bulk procurement/maintenance discounts.
  - **Constraints:** Grid dimensions (\\(n \times m\\)), spacing distance (minimum 3 cells separation in all 8 directions), dead zones (forbidden cells representing topographical obstacles), maximum allowable turbine count, and Minimum Operational Power Coefficient (\\(MOPC\\) ensuring directional power \\(\ge MOPC \times \text{Power}_{avg}\\)).
- **Algorithms / techniques:**
  - **Simulated Annealing (SA):** Linear/geometric cooling schedule (temperature 500 down to 0), Boltzmann-Gibbs acceptance criterion.
  - **Genetic Algorithm (GA):** Population 50, 10% elitism, 80% rank selection with 1-point/2-point/uniform crossover, 10% bit-flip mutation.
  - **Particle Swarm Optimization (PSO):** Discrete PSO re-defining velocity/position operators to add/remove/move turbines (\\(w=0.792, c_1=c_2=1.4944\\), star topology).
  - **Moth Flame Optimization (MFO):** Adapted continuous spiral movement (\\(b=0.3, t \in [-1, 1]\\) adaptive to \\(-2\\)) with discretized turbine position deltas and moth-to-flame reduction mapping.
  - **Deep Q-Learning (DQN):** Neural network (24 input neurons, 2 hidden layers of 24 neurons, \\(m \times n \times 2\\) output actions), Adam optimizer (\\(lr=0.001\\)), \\(\epsilon\\)-decay (\\(1.0 \to 0.01\\), decay 0.99), batch size 32, replay memory 2000.
- **Baselines compared:** Direct head-to-head benchmarking among SA, GA, PSO, MFO, and DQN under identical grid configurations.
- **Datasets / environments:** Synthetic grid environments of size 15x15, 20x20, and 25x25 with fixed dead zone placements and 36 weighted wind direction frequency profiles.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Best Fitness (15x15) | **0.001870** | GA (1-Crossover); Avg: 0.001888, Run time: 12.34 min |
| Best Fitness (20x20) | **0.001671** | GA (2-Crossover); Avg: 0.001725, Run time: 11.01 min |
| Best Fitness (25x25) | **0.001495** | GA (2-Crossover); Avg: 0.001508, Run time: 115.97 min |
| Fastest Execution Time (25x25) | **47.38 min** | SA (Geometric schedule); 0.41 min (15x15), 0.79 min (20x20) |
| Highest Stability / Lowest CV (25x25) | **0.00260** | PSO (Star topology); Std Dev: \\(4.0 \times 10^{-6}\\) |
| Balanced Solution / Speed (25x25) | Fitness: **0.001512**, Time: **53.25 min** | MFO (Geometric); Near-GA solution quality at \\(<50\%\\) runtime |
| Deep Q-Learning Best Fitness | **0.001914** (15x15), **0.001702** (20x20), **0.001541** (25x25) | Achieved competitive results but fell short of top meta-heuristics |

- **Key findings:**
  - GA achieved the overall best solution optimality across all grid sizes, though it required significantly longer runtimes (nearly 2 hours on 25x25).
  - SA was exponentially faster than all other meta-heuristics and exhibited high repeatability, but converged to sub-optimal local minima on smaller grids.
  - MFO provided an optimal balance between execution speed and solution quality, converging quickly while remaining close to GA's solution fitness.
  - Discrete PSO showed strong stability and consistent performance across multiple independent runs.
  - DQN learned valid policies and improved cumulative rewards, but displayed reward fluctuations and slightly lower solution quality compared to meta-heuristics.
- **Best-performing method:** **Genetic Algorithm (GA)** for solution optimality; **Moth Flame Optimization (MFO)** for overall trade-off between fitness quality and execution speed.

## Strengths

- Direct empirical comparison of traditional meta-heuristics, nature-inspired swarm algorithms, and reinforcement learning on the exact same WFLO benchmark.
- Realistic problem formulation incorporating 36 wind directions, non-linear procurement/maintenance cost scaling, dead zone obstacles, and directional power constraints.
- Effective discrete operator adaptations for continuous swarm algorithms (PSO, MFO).
- Comprehensive statistical reporting over 20 independent runs per configuration (mean, worst, std dev, CV).
- Publicly accessible, modular open-source codebase.

## Limitations & Threats to Validity

- Uses a simplified single-wake Jensen model which neglects complex multi-wake interactions, atmospheric turbulence, and complex topography.
- High computational scalability burden: runtimes escalate significantly for larger grid dimensions (e.g., 115.97 min for GA on 25x25).
- DQN instability: reinforcement learning experienced reward fluctuations, signaling potential hyperparameter sensitivity or state-space constraints.
- Restricted to 2D flat grid layouts without considering non-uniform terrain or 3D wind dynamics.

## Relevance to Our Project

- **Which of our milestones it informs:** Problem formulation (wake model & constraint implementation), SA, GA, Swarm intelligence (PSO/MFO), and Reinforcement Learning benchmarks.
- **Ideas it suggests for our problem:** Discrete position-update operators for continuous swarm algorithms; hybrid approaches combining fast initial search (SA/MFO) with local GA refinement.
- **Can we reproduce or extend it?** Yes, open-source code is available at `github.com/IrrationalInteger/WFLO-Optimization`. Can be extended to 3D/topographic layouts and multi-wake dynamics.

## Open Questions

- How do these algorithms perform under complex 3D atmospheric wake dynamics or non-flat terrain elevations?
- Can hybrid algorithms (e.g., MFO + GA or RL + meta-heuristics) combine the speed of swarm methods with the solution quality of GAs?
- Can continuous state representations or graph neural networks improve DQN stability and performance on larger grid sizes?

## Notable Quotes

> "Due to the large number of possible solutions, conventional numerical methods are impractical, and metaheuristic algorithms are employed to find optimal solutions. For example, even for a low number of WTs (< 30), there exists over 1044 unique solutions" (p. 2)

> "GA provided highly optimal solutions but with longer runtime. SA, while efficient in runtime, may sacrifice optimality. The choice of algorithm should align with requirements, considering factors like optimality, efficiency, and repeatability." (p. 5)

## Keywords

Sustainable Energy, Wind Farm Layout Optimization, Meta-Heuristic, Stochastic Algorithms, MultiCooperative Systems, Simulated Annealing, Genetic Algorithm, Particle Swarm, Moth Flame, Reinforcement Learning, QLearning

## Abstract (verbatim)

This paper presents a comprehensive study on the optimization of wind farm layouts, a critical aspect of enhancing the efficiency and effectiveness of wind energy production. We delve into various optimization techniques, including Simulated Annealing, Genetic Algorithm, Particle Swarm Optimization, Moth Flame Optimization, and Deep Q-Learning. Each optimization technique is explored through a series of case studies, where different configurations and parameters are applied to assess their effectiveness in optimizing wind farm layouts. These techniques are evaluated based on criteria such as computational complexity, optimality of solutions, and repeatability of results. The paper’s findings offer insightful comparisons and analyses of each technique, providing an understanding of their respective strengths and limitations in the context of wind farm layout optimization.