---
id: coevolutionary-immune-multi-uav-task-allocation
title: "A bi-subpopulation coevolutionary immune algorithm for multi-objective combinatorial optimization in multi-UAV task allocation"
authors: ["Xi Chen", "Yu Wan", "Jingtao Qi", "Zipeng Zhao", "Yirun Ruan", "Jun Tang"]
year: 2025
venue: "Complex & Intelligent Systems"
doi: "10.1007/s40747-024-01720-9"
url: "https://doi.org/10.1007/s40747-024-01720-9"
pdf: literature/papers/coevolutionary-immune-multi-uav-task-allocation.pdf
tags: ["coevolution", "immune-algorithm", "multi-objective", "multi-uav", "task-allocation", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# A bi-subpopulation coevolutionary immune algorithm for multi-objective combinatorial optimization in multi-UAV task allocation

> [!info] Citation
> X. Chen, Y. Wan, J. Qi, Z. Zhao, Y. Ruan, and J. Tang, "A bi-subpopulation coevolutionary immune algorithm for multi-objective combinatorial optimization in multi-UAV task allocation," *Complex & Intelligent Systems*, vol. 11, no. 2, art. 149, 2025.
> **Access:** Open access (Springer, CC BY-NC-ND 4.0). [Local PDF](../papers/coevolutionary-immune-multi-uav-task-allocation.pdf) · [DOI](https://doi.org/10.1007/s40747-024-01720-9)

## Why this paper (pre-selected)

- **Coevolutionary immune algorithm with adaptive strategy selection** — a less obvious evolutionary family than GWO/WOA, and an ideal M6 novelty path.
- **Multi-objective combinatorial model (MCOTAP)** with Pareto solution sets for decision support — feeds our multi-objective framing in M2.
- Includes an **ablation study** of each component, a good template for our own analysis.

## TL;DR

This paper formulates a realistic Multi-objective Combinatorial Optimization in Multi-UAV Task Allocation Problem (MCOTAP) model and introduces a Bi-subpopulation Coevolutionary Immune Algorithm (BCIA). BCIA leverages bi-subpopulation coevolution (elite and common antibody populations) and an adaptive strategy selection mechanism to effectively balance population diversity with late-stage convergence.

## Problem & Motivation

- **Problem addressed:** High-dimensional, discrete multi-UAV cooperative task allocation modeled as a multi-objective combinatorial optimization problem.
- **Why it matters:** Real-world mission success depends on balancing conflicting operational criteria (e.g., total execution time vs. overall resource consumption) to present trade-off Pareto solution sets to decision-makers.
- **Application domain:** Multi-UAV / UAV-swarm reconnaissance and mission planning.

## Research Question / Objective

- How to construct a discrete multi-objective task allocation model (MCOTAP) that incorporates realistic operational constraints (endurance, speed, task precedence) and natively supports variable UAV participation (including idle UAVs)?
- How to design a multi-objective immune algorithm (BCIA) that overcomes the tendency of traditional immune algorithms to suffer from poor diversity or premature convergence in discrete combinatorial search spaces?
- How to dynamically adapt evolutionary crossover strategies across search stages to maintain exploration early on while accelerating convergence near the Pareto front later in evolution?

## Contributions

- [x] Multi-objective Combinatorial Optimization in Multi-UAV Task Allocation Problem (MCOTAP) model.
- [x] Bi-subpopulation coevolutionary immune algorithm (BCIA) featuring elite-common subpopulation coevolution and adaptive strategy selection.
- [x] Formulated an Evolutionary Strategy Pool containing three discrete crossover operators (\\(ES_1\\) Uniform Crossover, \\(ES_2\\) Random Fragment Crossover, \\(ES_3\\) Bidirectionally Guided Crossover) tailored for permutation-encoded combinatorial optimization.
- [x] Comprehensive empirical benchmarking against state-of-the-art MOEAs/MOIAs across 4 standard MCOP benchmarks and 6 instantiated MCOTAP test cases, backed by a full component ablation study.

## Methodology

- **Problem formulation:** Formulated as the quadruple \\(\{MUAS, Targets, Constraints, Functions\}\\). Features a novel hybrid 0-padded permutation encoding of dimension \\(N \times N_T\\) (where \\(N\\) is UAV count and \\(N_T\\) is target count), allowing code bit `0` to represent idle UAVs or unassigned slots. Optimizes two conflicting objectives: minimizing total mission completion time \\(F_{time}\\) and total system flight range \\(F_{flight}\\). Enforces three hard operational constraints: UAV maximum endurance (\\(Time_{all}^i \le Time\\)), maximum cruising speed (\\(Vol_{ty} < Vol_{ty}^{max}\\)), and task precedence relations via matrix \\(TC\\).
- **Algorithm:** BCIA initializes antibody population \\(B\\), performs non-dominated sorting and crowding distance calculations to form dominant population \\(D\\), and splits it into elite subpopulation \\(E\\) (\\(n_E\\)) and common subpopulation \\(C\\) (\\(n_C\\)). Each elite antibody \\(E_i\\) receives a rating \\(rating_i\\) (based on scaled crowding distance) determining its cloning/coevolution offspring count. Coevolution executes either Adaptive Cooperative Evolution (\\(E_i \times E_{rand}\\) with probability \\(P_{co}\\)) or Adaptive Guided Evolution (\\(C_{rand} \rightarrow E_i\\)). Operator selection uses a sigmoid execution probability \\(P_{de} = 0.2 + 0.8 / (1 + \exp(35 \times (Gen/max\_Gen - 0.5)))\\), smoothly transitioning from global exploration (\\(ES_1\\)) in early generations to local exploitation (\\(ES_2, ES_3\\)) in late generations, followed by Slight Mutation.
- **Baselines compared:** Mainstream MOEAs (NSGA-II, SPEA2, MOEA/D), multi-objective immune algorithms (NNIA), multi-objective coevolutionary algorithms (NNCA), and recent multi-UAV mission planners (H-NSGAII-VNS, C-MOPSO-CD).
- **Validation:** 4 classical MCOP benchmark problems (MONRP, ZDT5, MOTSP, mQAP) plus 6 instantiated MCOTAP test cases across uniform (TC1-1 to TC1-3) and random (TC2-1 to TC2-3) target distributions (problem scales: U3-T15, U4-T20, U5-T30). Evaluated using Hypervolume (HV), execution runtime, and non-parametric Wilcoxon rank-sum tests at a 0.05 significance level. Included a component ablation study comparing BCIA against Variant 1 (single population, no common subpopulation guidance), Variant 2 (random strategy selection without adaptive \\(P_{de}\\)), and Variant 3 (single strategy \\(ES_1\\)).

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
| Benchmark HV (ZDT5) | **0.80925** (BCIA) vs 0.75911 (NSGA-II) | Achieves best HV score on the ZDT5 benchmark problem. |
| Benchmark HV (mQAP) | **0.67457** (BCIA) vs 0.67287 (NSGA-II) | Outperforms all compared algorithms on mQAP. |
| Benchmark HV (MOTSP) | 0.86794 (BCIA) vs **0.86865** (NNCA) | Achieves sub-optimal rank, statistically comparable to NNCA. |
| Benchmark HV (MONRP) | 0.64305 (BCIA) vs **0.68363** (NNIA) | Achieves second place overall on MONRP. |
| MCOTAP HV (TC1-1: U3-T15, Uniform) | **0.52169** (BCIA) vs 0.51941 (NNCA) | Highest mean HV across 30 independent runs. |
| MCOTAP HV (TC1-3: U5-T30, Uniform) | **0.33686** (BCIA) vs 0.31829 (NNIA) | Significantly outperforms all baselines on large uniform cases. |
| MCOTAP HV (TC2-3: U5-T30, Random) | **0.33134** (BCIA) vs 0.29781 (NNCA) | Highest HV and superior box-plot stability on large random cases. |
| MCOTAP Solving Time (TC1-3) | 5.1037 s (BCIA) vs 13.6880 s (H-NSGAII-VNS) | Substantially faster than MOEA/D (9.02s) and H-NSGAII-VNS (13.69s). |
| Ablation HV (TC1-3) | **0.33686** (BCIA) vs 0.31899 (Var1), 0.31306 (Var2) | BCIA completely dominates all ablation variants on large-scale problems. |

- **Key findings:**
  - BCIA achieves optimal or sub-optimal Hypervolume performance on standard MCOP benchmarks and consistently obtains the highest mean HV across all six MCOTAP test problems.
  - Bi-subpopulation coevolution successfully maintains high population diversity while preventing search stagnation or premature convergence to local optima.
  - The \\(N \times N_T\\) 0-padded hybrid encoding allows unnecessary UAVs to remain idle, avoiding wasteful flight consumption when additional UAVs yield negligible completion time gains.
  - Component ablation confirms that bi-subpopulation guidance and adaptive strategy selection become increasingly vital as problem scale grows (TC1-3, TC2-3).
- **Best-performing method:** BCIA (Bi-subpopulation Coevolutionary Immune Algorithm).

## Strengths

- **Effective Bi-subpopulation Structure:** Combines cooperative evolution within elite antibodies (\\(E\\)) with guided evolution from common antibodies (\\(C\\)) toward elite antibodies, preserving diversity while accelerating search directionality.
- **Adaptive Stage-based Strategy Selection:** Smoothly transitions operator selection probabilities (\\(P_{de}\\)) from global exploration (\\(ES_1\\)) to localized exploitation (\\(ES_2, ES_3\\)), resolving the diversity-convergence trade-off.
- **Practical Idle-Aware Encoding:** Overcomes a widespread flaw in multi-UAV planners by natively supporting inactive UAVs via 0-padding, directly reducing unnecessary resource usage.
- **Rigorously Validated:** Thoroughly tested against 6 competitive baselines across 4 benchmark problems and 6 custom task allocation scenarios, supported by complete component ablation studies.

## Limitations & Threats to Validity

- **Static Task Environment:** Assumes fixed target coordinates, known reconnaissance durations, and static UAV parameters without handling real-time dynamic re-planning or unexpected pop-up targets.
- **Simplified Operational Constraints:** Models endurance, maximum speed, and temporal precedence, but omits complex constraints such as anti-access/area-denial (A2AD) threat zones, communication range limits, or sensor payload switching.
- **Computational Overhead vs. Lightweight Heuristics:** While significantly faster than MOEA/D, SPEA2, and H-NSGAII-VNS, BCIA is slightly slower than lightweight local search algorithms (NNIA, NNCA, C-MOPSO) due to the overhead of bi-subpopulation sorting and adaptive strategy evaluation.

## Relevance to Our Project

- **Which milestones it informs:** M2 (multi-objective model formulation), M4 (evolutionary mechanism design), M6 (coevolutionary immune algorithms + adaptive strategy selection).
- **Ideas it suggests:**
  - Implement the \\(N \times N_T\\) 0-padded hybrid chromosome encoding to allow dynamic swarm sizing and idle UAV retention.
  - Adopt a sigmoid-based adaptive operator selection probability curve (\\(P_{de}\\)) to automate the transition from exploration to exploitation.
  - Incorporate bi-subpopulation splitting (elite \\(E\\) vs common \\(C\\)) with guided crossover to elevate sub-optimal solutions toward the non-dominated front.
- **Can we reproduce or extend it?**
  - **Yes.** The mathematical formulation, objective functions, encoding structure, crossover operators (\\(ES_1, ES_2, ES_3\\)), and parameters are fully specified.
  - **Extension opportunities:** Extend MCOTAP to dynamic environments with online task insertion, expand to many-objective optimization (\\(M \ge 4\\)), or replace fixed sigmoid scheduling with multi-armed bandit / reinforcement learning strategy selection.

## Open Questions

- How well does BCIA scale to many-objective combinatorial task allocation (\\(M \ge 4\\) objectives, e.g., incorporating threat risk, communication bandwidth, and payload fatigue)?
- Can the bi-subpopulation coevolutionary structure be adapted for real-time online re-allocation when UAV hardware fails or targets move mid-mission?
- Could the static sigmoid parameters in \\(P_{de}\\) be dynamically driven by real-time population diversity metrics or Pareto front stagnation counters rather than fixed generation ratios?

## Keywords

coevolutionary algorithm, multi-objective immune algorithm, adaptive strategy selection, multi-UAV, task allocation

## Abstract (verbatim)

> With the development of Unmanned Aerial Vehicle (UAV) technology towards multi-UAV and UAV swarm, multi-UAV cooperative task allocation has more and more influence on the success or failure of UAV missions. From the operational research point of view, such problems belong to high-dimensional combinatorial optimization problems, which makes the solving process face many challenges. One is that the discrete and high-dimensional decision variables make the quality of the solution obtained with acceptable time not guaranteed. Second, the desired solution of real missions often needs to satisfy multiple objective functions, or a set of solutions for decision-making. Therefore, this paper constructs a Multi-objective Combinatorial Optimization in Multi-UAV Task Allocation Problem (MCOTAP) model, and proposes a Bi-subpopulation Coevolutionary Immune Algorithm (BCIA). The two coevolutionary mechanisms improve the lower limit of population diversity, and the evolutionary strategy pool integrating multiple strategies and the adaptive strategy selection mechanism enhance the local search ability in the late evolution. In the experiments, BCIA competes fairly with the mainstream multi-objective evolutionary algorithms (MOEAs), multi-objective immune algorithms (MOIAs) and the recently proposed multi-UAV mission planning algorithms. The experimental results on different test problems (including several multi-objective combinatorial optimization benchmark problems and the proposed MCOTAP model) show that BCIA has superior performance in solving multi-objective combinatorial optimization problems (MCOPs). At the same time, the effectiveness of each design component of BCIA has been comprehensively verified in the ablation study.