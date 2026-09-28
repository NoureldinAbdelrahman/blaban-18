---
id: coevolutionary-immune-multi-uav-task-allocation
title: "A bi-subpopulation coevolutionary immune algorithm for multi-objective combinatorial optimization in multi-UAV task allocation"
authors: ["Xi Chen", "Yu Wan", "Jingtao Qi", "Zipeng Zhao", "Yirun Ruan", "Jun Tang"]
year: 2025
venue: "Complex & Intelligent Systems"
doi: "10.1007/s40747-024-01720-9"
url: "https://doi.org/10.1007/s40747-024-01720-9"
pdf: null
tags: ["coevolution", "immune-algorithm", "multi-objective", "multi-uav", "task-allocation", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# A bi-subpopulation coevolutionary immune algorithm for multi-objective combinatorial optimization in multi-UAV task allocation

> [!info] Citation
> X. Chen, Y. Wan, J. Qi, Z. Zhao, Y. Ruan, and J. Tang, "A bi-subpopulation coevolutionary immune algorithm for multi-objective combinatorial optimization in multi-UAV task allocation," *Complex & Intelligent Systems*, vol. 11, no. 2, art. 149, 2025.
> **Access:** Open access (Springer, CC BY-NC-ND 4.0). Download at the DOI link.

## Why this paper (pre-selected)

- **Coevolutionary immune algorithm with adaptive strategy selection** — a less obvious evolutionary family than GWO/WOA, and an ideal M6 novelty path.
- **Multi-objective combinatorial model (MCOTAP)** with Pareto solution sets for decision support — feeds our multi-objective framing in M2.
- Includes an **ablation study** of each component, a good template for our own analysis.

## TL;DR

_One or two sentences in your own words._

## Problem & Motivation

- **Problem addressed:** High-dimensional, discrete multi-UAV cooperative task allocation as a multi-objective combinatorial optimization problem.
- **Why it matters:** Mission success depends on producing a set of trade-off solutions for decision-makers.
- **Application domain:** Multi-UAV / UAV-swarm mission planning.

## Research Question / Objective

-

## Contributions

- [ ] Multi-objective Combinatorial Optimization in Multi-UAV Task Allocation Problem (MCOTAP) model.
- [ ] Bi-subpopulation coevolutionary immune algorithm (BCIA) with an evolutionary strategy pool and adaptive strategy selection.

## Methodology

- **Problem formulation:** Multi-objective combinatorial optimization (permutation encoding).
- **Algorithm:** BCIA (elite/common antibody subpopulations, coevolution, adaptive strategy selection).
- **Baselines compared:** Mainstream MOEAs, multi-objective immune algorithms (MOIAs), recent multi-UAV planners.
- **Validation:** Benchmark MCOPs + two MCOTAP test sets, plus ablation study.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
|  |  |  |

- **Key findings:**
- **Best-performing method:** BCIA.

## Strengths

-

## Limitations & Threats to Validity

-

## Relevance to Our Project

- **Which milestones it informs:** M2 (multi-objective model), M4 (evolutionary mechanisms), M6 (immune/coevolution + adaptive strategy selection).
- **Ideas it suggests:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Keywords

coevolutionary algorithm, multi-objective immune algorithm, adaptive strategy selection, multi-UAV, task allocation

## Abstract (verbatim)

With the development of Unmanned Aerial Vehicle (UAV) technology towards multi-UAV and UAV swarm, multi-UAV cooperative task allocation has more and more influence on the success or failure of UAV missions. From the operational research point of view, such problems belong to high-dimensional combinatorial optimization problems, which makes the solving process face many challenges. One is that the discrete and high-dimensional decision variables make the quality of the solution obtained with acceptable time not guaranteed. Second, the desired solution of real missions often needs to satisfy multiple objective functions, or a set of solutions for decision-making. Therefore, this paper constructs a Multi-objective Combinatorial Optimization in Multi-UAV Task Allocation Problem (MCOTAP) model, and proposes a Bi-subpopulation Coevolutionary Immune Algorithm (BCIA). The two coevolutionary mechanisms improve the lower limit of population diversity, and the evolutionary strategy pool integrating multiple strategies and the adaptive strategy selection mechanism enhance the local search ability in the late evolution. In the experiments, BCIA competes fairly with the mainstream multi-objective evolutionary algorithms (MOEAs), multi-objective immune algorithms (MOIAs) and the recently proposed multi-UAV mission planning algorithms. The experimental results on different test problems (including several multi-objective combinatorial optimization benchmark problems and the proposed MCOTAP model) show that BCIA has superior performance in solving multi-objective combinatorial optimization problems (MCOPs). At the same time, the effectiveness of each design component of BCIA has been comprehensively verified in the ablation study.
