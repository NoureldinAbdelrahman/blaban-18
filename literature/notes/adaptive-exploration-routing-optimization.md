---
id: adaptive-exploration-routing-optimization
title: "Meta-heuristic Adaptive Exploration Strategy Through Routing Optimization"
authors: ["Ahd Mostafa", "Amr Hegazy", "Fathy Metwally", "Mohamed Wael", "Yousef Elbrolosy", "Ziad Abdelrahman", "Abdelrahman Y. Altaher", "Omar M. Shehata"]
year: null
tags: ["multi-robot", "exploration", "path-planning", "adaptive-selection"]
pdf: literature/papers/adaptive-exploration-routing-optimization.pdf
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# Meta-heuristic Adaptive Exploration Strategy Through Routing Optimization

> [!info] Citation
> Ahd Mostafa, Amr Hegazy, Fathy Metwally, Mohamed Wael, Yousef Elbrolosy, Ziad Abdelrahman, Abdelrahman Y. Altaher, Omar M. Shehata. *Meta-heuristic Adaptive Exploration Strategy Through Routing Optimization*. [PDF](../papers/adaptive-exploration-routing-optimization.pdf)

## TL;DR

_One or two sentences capturing the core contribution in your own words._

## Problem & Motivation

- **Problem addressed:**
- **Why it matters:**
- **Application domain:**

## Research Question / Objective

-

## Contributions

- [ ]
- [ ]

## Methodology

- **Problem formulation:** (decision variables, objective(s), constraints)
- **Algorithms / techniques:**
- **Baselines compared:**
- **Datasets / environments:**

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
|  |  |  |

- **Key findings:**
- **Best-performing method:**

## Strengths

-

## Limitations & Threats to Validity

-

## Relevance to Our Project

- **Which of our milestones it informs:** (formulation / SA / GA / swarm / novel algorithm)
- **Ideas it suggests for our problem:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Notable Quotes

> "..." (p. )

## Keywords

Multi-Robot Systems, Path Planning, Metaheuristics, Adaptive Selection, Connectivity Maintenance, Learning to Optimize

## Abstract (verbatim)

Efficient exploration of unknown environments by multi-robot teams requires a delicate balance between coverage maximization and the maintenance of communication connectivity. While various metaheuristic approaches such as Genetic Algorithms (GA), Ant Colony Optimization (ACO), Simulated Annealing (SA), and Artificial Bee Colony (ABC) have been applied to this problem, no single algorithm dominates across all environmental conditions. For connectivity-constrained scenarios with sparse initial robot configurations, constructive methods like ACO often excel, whereas perturbative methods like SA may offer superior computational efficiency in simpler scenarios. We introduce MAESTRO, a framework that integrates a learned router (Random Forest) to dynamically select the optimal planner based on extracted map features and connectivity/topology statistics. Our evaluation, performed on a dataset of 1,836 test scenarios, demonstrates that this adaptive approach achieves a classification accuracy of 94.99% in selecting the optimal solver. We further conduct a sensitivity analysis on GA population sizing, proving that adaptive routing outperforms even hyperparametertuned static solvers. Crucially, the system exhibits a fail-safe routing behavior: in our testing, it achieved zero critical errors, correctly avoiding the lightweight solver (SA) for complex instances requiring robust optimization (ACO), thereby minimizing mission failure risk while reducing computational overhead by approximately 34%.
