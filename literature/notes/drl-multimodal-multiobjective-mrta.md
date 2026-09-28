---
id: drl-multimodal-multiobjective-mrta
title: "A deep reinforcement learning-assisted multimodal multiobjective bilevel optimization method for multirobot task allocation"
authors: ["Yuanyuan Yu", "Qirong Tang", "Qingchao Jiang", "Qinqin Fan"]
year: 2025
venue: "IEEE Transactions on Evolutionary Computation"
doi: "10.1109/TEVC.2025.3535954"
url: "https://doi.org/10.1109/TEVC.2025.3535954"
pdf: null
tags: ["multimodal-multiobjective", "bilevel", "reinforcement-learning", "large-neighborhood-search", "mrta", "review-2026"]
status: unread
relevance: 0
reviewed_by: ""
reviewed_date: ""
---

# A deep reinforcement learning-assisted multimodal multiobjective bilevel optimization method for multirobot task allocation

> [!info] Citation
> Y. Yu, Q. Tang, Q. Jiang, and Q. Fan, "A deep reinforcement learning-assisted multimodal multiobjective bilevel optimization method for multirobot task allocation," *IEEE Transactions on Evolutionary Computation*, vol. 29, no. 3, pp. 574–588, 2025.
> **Access:** IEEE Xplore (paywalled). Use the DOI via the university library.

## Why this paper (pre-selected)

- **Multi-objective + bilevel framing** of MRTA (allocation on top, routing below) — a modern problem formulation we can borrow for Milestone 2.
- **MMOEA + LNS + deep RL** hybrid; the "equivalent solutions" idea gives robustness and connects to the optional ML bonus.
- Published in a top-tier evolutionary-computation venue, so citing it strengthens the report.

## TL;DR

_One or two sentences in your own words._

## Problem & Motivation

- **Problem addressed:** Multirobot task allocation as a multimodal multi-objective bi-level problem in uncertain/dynamic environments.
- **Why it matters:**
- **Application domain:** Multi-robot cooperative systems.

## Research Question / Objective

-

## Contributions

- [ ] Multimodal multiobjective evolutionary algorithm (MMOEA) for the upper-level allocation.
- [ ] DRL + large neighborhood search for the lower-level routing/TSP.
- [ ] Produces many equivalent schemes to cope with dynamic or unforeseen conditions.

## Methodology

- **Problem formulation:** Bi-level; upper level = task allocation, lower level = TSP routing.
- **Algorithm:** MMOEA-DL (MMOEA + DRL + LNS).
- **Baselines compared:**
- **Validation:** 16 simulation scenarios + 2 real MRTA scenarios.

## Experimental Setup & Results

| Metric | Value | Notes |
| --- | --- | --- |
|  |  |  |

- **Key findings:**
- **Best-performing method:** MMOEA-DL.

## Strengths

-

## Limitations & Threats to Validity

-

## Relevance to Our Project

- **Which milestones it informs:** M2 (multi-objective/bilevel formulation), M6 (hybrid evolutionary + LNS + RL), optional ML bonus.
- **Ideas it suggests:**
- **Can we reproduce or extend it?**

## Open Questions

-

## Keywords

multimodal multi-objective optimization, bi-level optimization, multirobot task allocation, deep reinforcement learning, large neighborhood search

## Abstract (verbatim)

Multirobot task allocation (MRTA) is a challenging bi-level problem in the multirobot cooperative systems (MRCSs) and offers an effective method for addressing complex tasks. However, dynamic/uncertain environments can easily invalidate original schemes in practical MRTA decision-makings. Further, a nested structure in MRTA problems makes computational expensive. Therefore, the two main tasks are 1) finding a sufficient number of equivalent schemes for MRTA problems to adapt to task environments and 2) improving algorithm search efficiency in bi-level optimization problems. In this study, a multimodal multiobjective evolutionary algorithm (MMOEA) based on deep reinforcement learning (DRL) and large neighborhood search (LNS), called MMOEA-DL, is proposed to solve MRTA problems. In the MMOEA-DL, the task allocation problem, which is considered as the upper-level optimization problem, is solved using an improved MMOEA. The traveling salesman problem (TSP) regarded as the lower-level optimization problem is addressed via end-to-end method (i.e., DRL) and LNS. By leveraging the end-to-end method to obtain the results of the lower-level optimization, the bi-level optimization problem is effectively transformed into a single-level optimization problem. To demonstrate the performance of the proposed algorithm, 16 MRTA simulation scenarios and two actual MRTA scenarios with evenly and unevenly distributed task points are introduced in the present study. The simulation results verify that the MMOEA-DL not only provides decision-makers with expanded equivalent optimal schemes to address dynamic environments or unforeseen circumstances, but also offers a novel approach to solve the multimodal multiobjective bi-level optimization problem while saving computational costs.
