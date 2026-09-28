#!/usr/bin/env python3
"""Build the literature corpus from a curated catalog.

This script:
  1. moves the source PDFs into literature/papers/<id>.pdf (flat, stable names),
  2. writes literature/bibliography/catalog.json (canonical metadata),
  3. writes literature/bibliography/references.bib and references.md,
  4. writes literature/bibliography/manifest.csv (source -> curated mapping),
  5. renders one literature note per paper from the note template.

The CURATED table below is the source of truth for title, authors, tags and
keywords. Abstracts are extracted from the PDFs unless overridden.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from pathlib import Path

import extract_paper_metadata as epm

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = REPO_ROOT / "previous_publications"
PAPERS_DIR = REPO_ROOT / "literature" / "papers"
BIB_DIR = REPO_ROOT / "literature" / "bibliography"
NOTES_DIR = REPO_ROOT / "literature" / "notes"
TEMPLATE = REPO_ROOT / "docs" / "templates" / "literature_note_template.md"

CURATED = [
    {
        "source_file": "a138-ghoneim final.pdf",
        "id": "multi-agv-path-planning-search-rescue",
        "title": "Metaheuristic Optimization for Multi-AGV Path Planning in Search and Rescue Missions",
        "authors": ["Arwa H. Ghoneim", "Ahmed M. Elsoda", "Heba A. Abdelmawla", "Khaled Elbadawy", "Linah Tamer", "Lobna Tarek", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["agv", "search-and-rescue", "path-planning", "metaheuristics"],
    },
    {
        "source_file": "a27-alfarrash final.pdf",
        "id": "vehicle-routing-v2g-scheduling",
        "title": "Metaheuristic Optimization for Vehicle Routing and V2G Scheduling in Electrical Vehicle Fleet Network",
        "authors": ["Rahaf M. Alfarrash", "Arwa H. Khattab", "Roba Hesham", "Hana Elmalah", "Menna Wahba", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["vehicle-routing", "electric-vehicles", "v2g", "scheduling", "metaheuristics"],
    },
    {
        "source_file": "a28-elmaghraby final.pdf",
        "id": "multi-uav-task-assignment-firefighting",
        "title": "Optimizing Multi-UAV Cooperative Task Assignment for Fire Extinguishing Missions",
        "authors": ["Ziad Elmaghraby", "Refat Tamer", "Mohamed Wazery", "Abdelrahman Zakzouk", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["uav", "task-assignment", "firefighting", "metaheuristics"],
    },
    {
        "source_file": "a33-ehab final.pdf",
        "id": "comparative-metaheuristics-multi-robot-sar",
        "title": "Comparative Analysis of Meta-Heuristic Algorithms for Multi-Robot Search and Rescue",
        "authors": ["Nada Ehab", "Farah Khaled", "Martin Morcos", "Ibrahim Abdelaty", "Abdelrahman Y. Altaher", "Omar M. Shehata"],
        "tags": ["multi-robot", "search-and-rescue", "path-planning", "comparative-study"],
    },
    {
        "source_file": "a38-abbas final.pdf",
        "id": "heterogeneous-fleet-navigation-optimization",
        "title": "Metaheuristic-Based Navigation Optimization for Heterogeneous Autonomous Vehicle Fleets",
        "authors": ["Seifeldin Abbas", "Rasheed Atia", "Yassin Otifa", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["vehicle-routing", "heterogeneous-fleet", "navigation", "metaheuristics"],
    },
    {
        "source_file": "a39-elharridy final.pdf",
        "id": "weather-adaptive-task-allocation-disaster",
        "title": "Weather-Adaptive Task Allocation for Vehicle Fleets in Disaster Relief Operations: A Multi-Scenario Optimization Framework",
        "authors": ["Omar ElHarridy", "Mohamed Elmenshawy", "Ahmed Gasser", "Mahmoud Hebishy", "Abdelrahman Sayed", "Aly Ibrahim", "Jessica Magdy", "Omar Shehata"],
        "tags": ["vehicle-fleet", "task-allocation", "disaster-relief", "multi-scenario"],
    },
    {
        "source_file": "a42-abdallah final.pdf",
        "id": "multi-robot-delivery-smart-hotels",
        "title": "Optimizing Multi-Robot Delivery in Smart Hotels: A Multi-Objective Metaheuristic Approach",
        "authors": ["Seif Abdallah", "Yahia Abdelraheem", "Nour Eldin Daoud", "Abdelrahman Mohamed Wael", "Ahmed Elkot", "Youssef Maged", "Jessica Magdy", "Omar Shehata"],
        "tags": ["multi-robot", "task-allocation", "delivery", "multi-objective"],
    },
    {
        "source_file": "a50-mostafa final.pdf",
        "id": "adaptive-exploration-routing-optimization",
        "title": "Meta-heuristic Adaptive Exploration Strategy Through Routing Optimization",
        "authors": ["Ahd Mostafa", "Amr Hegazy", "Fathy Metwally", "Mohamed Wael", "Yousef Elbrolosy", "Ziad Abdelrahman", "Abdelrahman Y. Altaher", "Omar M. Shehata"],
        "tags": ["multi-robot", "exploration", "path-planning", "adaptive-selection"],
    },
    {
        "source_file": "a62-mahdi final.pdf",
        "id": "hybrid-energy-system-planning",
        "title": "Hybrid Energy System Planning: Optimizing Solar and Wind Power for Maximum Efficiency and Cost Reduction",
        "authors": ["Seif Mahdi", "Abdulrahman Yasser", "Omar Hashem", "Ahmed Hatem", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["energy", "renewable", "solar", "wind", "cost-optimization"],
        "keywords": ["hybrid renewable energy", "solar PV", "wind power", "cost optimization", "metaheuristics"],
    },
    {
        "source_file": "a94-ahmed final.pdf",
        "id": "waste-collection-ugv-optimization",
        "title": "Route to Clean Cities: Waste Collection Optimization with UGVs",
        "authors": ["Farah Ahmed", "Hoor Amr", "Marwan Khalil", "Maryam Mohamed", "Youssef Amir", "Ziad Yasser", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["ugv", "waste-collection", "routing", "metaheuristics"],
    },
    {
        "source_file": "Development_and_Evaluation_of_Various_Optimization_Techniques_for_Multi_Robot_Task_Allocation_and_Routing_in_Warehouse_Settings.pdf",
        "id": "warehouse-tlbo-task-allocation-routing",
        "title": "Development and Evaluation of Various Optimization Techniques for Multi-Robot Task Allocation and Routing in Warehouse Settings",
        "authors": ["Rana M. Talaat", "Sama Tamer", "Menna Walaa", "Aya Walid", "Dalia M. Mahfouz", "Omar M. Shehata"],
        "tags": ["warehouse", "task-allocation", "routing", "tlbo"],
    },
    {
        "source_file": "Final_Draft.pdf",
        "id": "rsu-placement-reinforcement-learning",
        "title": "Reinforcement Learning Based Optimization Technique for Road-Side-Units (RSUs) Placement along a Highway",
        "authors": ["Mohamed Sabry", "Mohammed Saeed", "Shaheer Sherif", "Mariam Fathi", "Lina Ghonim", "Youssef Mahran", "Mohamed Ibrahim", "Omar M. Shehata"],
        "tags": ["vanet", "rsu-placement", "reinforcement-learning", "transportation"],
        "keywords": ["VANET", "RSU placement", "reinforcement learning", "DDPG", "TD3", "metaheuristics"],
    },
    {
        "source_file": "ICEENG_IPCS_overleaf.pdf",
        "id": "coordinated-defense-target-attacker-defender",
        "title": "Coordinated Defense via Multiagent Optimization in Distributed Target-Attacker-Defender Games",
        "authors": ["Ahmed Y. Gado", "Yousef Y. Mohamed", "Abdelrahman M. M. Mohammed", "Mohamed O. Abdelal", "Youssef A. Abdelaziz", "Abdelrahman A. Zidan", "Mohamed A. Ibrahim", "Omar M. Shehata"],
        "tags": ["multi-agent", "defense", "game-theory", "uav"],
    },
    {
        "source_file": "Metaheuristic_Optimization_for_Efficient_Food_Production_Scheduling (1).pdf",
        "id": "food-production-scheduling-optimization",
        "title": "Metaheuristic Optimization for Efficient Food Production Scheduling",
        "authors": ["Aseel Abdelkareem", "Rawan Hegazy", "Ganna Moahmed", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["scheduling", "manufacturing", "food-production", "metaheuristics"],
        "keywords": ["production scheduling", "food industry", "energy consumption", "labor cost", "metaheuristics"],
    },
    {
        "source_file": "Multi_Robot_Exploration___Mapping__Search_And_Rescue__final.pdf",
        "id": "multi-robot-sar-scaling-exploration",
        "title": "Scaling Multi-Robot Search and Rescue: A Comparative Study of Metaheuristic Exploration Methods",
        "authors": ["Diana Elzeftawy", "Ethar Hany", "Jana Saad", "Mariam Gafar", "Mennah M. Shaker", "Nabila Ataby", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["multi-robot", "search-and-rescue", "exploration", "comparative-study"],
    },
    {
        "source_file": "Multi_UAV_Trajectory_Planning_and_Task_Allocation_for_Disaster_Rescue_Operations_Final.pdf",
        "id": "multi-uav-trajectory-task-allocation-disaster",
        "title": "Multi-UAV Trajectory Planning and Task Allocation for Disaster Rescue Operations",
        "authors": ["Yousra M. Aljifri", "Sarah H. Shaaban", "Farida B. El-Saadawy", "Yousef H. Ali", "Youssof M. Awad", "Youssef M. El-Khawanky", "Dalia M. Mahfouz", "Omar M. Shehata"],
        "tags": ["uav", "trajectory-planning", "task-allocation", "disaster-relief"],
        "keywords": ["multi-UAV", "trajectory planning", "task allocation", "disaster rescue", "VRPTW", "endurance"],
    },
    {
        "source_file": "Optimization_Akher_Wahda-1.pdf",
        "id": "multi-agent-racing-tire-wear",
        "title": "Multi-Agent Racing Trajectory Optimization with Tire Wear Awareness: A Comparison of Reinforcement Learning and Metaheuristic Methods",
        "authors": ["Farida Gamal", "Sara Alajmy", "Salma Elhabashy", "Ziad ElGendy", "Farah Eltaher", "Omar Ayoub", "Mohamed A. Ibrahim", "Omar M. Shehata"],
        "tags": ["multi-agent", "racing", "trajectory-optimization", "reinforcement-learning"],
    },
    {
        "source_file": "Optimization of Multi-AGV Scheduling for Airport Baggage Handling.pdf",
        "id": "multi-agv-airport-baggage-scheduling",
        "title": "Optimization of Multi-AGV Scheduling for Airport Baggage Handling",
        "authors": ["Abdallah Ahmed Hassan", "Abdelrahman Ewida", "Haidy Ehab Elkenawy", "Abdulrahman Bassem Bahy", "Karim Mohamed Fathy", "Dalia M. Mahfouz", "Omar M. Shehata"],
        "tags": ["agv", "scheduling", "airport-logistics", "metaheuristics"],
    },
    {
        "source_file": "PA044-10.4.pdf",
        "id": "wind-farm-layout-optimization",
        "title": "Advancing Sustainable Energy: Analyzing Stochastic Algorithms and Q-Learning for Wind Farm Layout Optimization",
        "authors": ["Mohamed Elsheikh", "Amr Yonis", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["energy", "wind-farm", "layout-optimization", "reinforcement-learning"],
    },
    {
        "source_file": "paper ID 552.pdf",
        "id": "autonomous-intersection-management-aimp",
        "title": "Autonomous Intersection Management Platform (AIMP): Metaheuristic Optimization for Traffic Scheduling",
        "authors": ["Ahmed Mostafa", "Hazim Ashraf", "Gasser Emara", "Michael Hany", "Kirolous Magdy", "Mazen Amr", "Dalia M. Mahfouz", "Omar M. Shehata"],
        "tags": ["traffic", "intersection-management", "scheduling", "metaheuristics"],
        "keywords": ["autonomous intersection management", "traffic scheduling", "metaheuristics"],
    },
    {
        "source_file": "Performance_Evaluation_of_Meta_Heuristic_Algorithms_for_Multi_Robot_Task_Allocation.pdf",
        "id": "mrta-metaheuristic-performance-evaluation",
        "title": "Performance Evaluation of Meta-Heuristic Algorithms for Multi-Robot Task Allocation",
        "authors": ["Mohammed Hany", "Karim Hassan", "Jessica Magdy", "Omar M. Shehata"],
        "tags": ["multi-robot", "task-allocation", "comparative-study", "metaheuristics"],
        "abstract": (
            "Multi-Robot Task Allocation (MRTA) is a nondeterministic polynomial-time (NP)-hard "
            "optimization problem that requires assigning tasks to multiple robots while minimizing travel "
            "cost, maximizing task coverage, and maintaining workload balance. This paper evaluates four "
            "meta-heuristic algorithms, Simulated Annealing (SA), Genetic Algorithm (GA), Grey Wolf "
            "Optimizer (GWO), and the Bee Algorithm (BA), for solving MRTA using a unified multi-objective "
            "formulation based on distance minimization, task maximization, and Jain's Fairness Index. Each "
            "method is tested under multiple parameter settings to analyze convergence behavior, solution "
            "quality, and computational efficiency. Simulation results show that the Genetic Algorithm "
            "achieves the best overall performance, providing the highest task coverage and fastest "
            "convergence while preserving balanced task distribution among robots. Although BA and GWO offer "
            "stable and fair solutions and SA produces energy-efficient routes, GA consistently outperforms "
            "the other methods in both solution quality and runtime. These results highlight GA as the most "
            "suitable choice for scalable and efficient MRTA applications."
        ),
    },
]


def detect_copyright_year(full_text: str) -> str | None:
    patterns = [
        r"©\s*(20[0-9]{2})",
        r"Copyright\s*(?:\(c\)|©)?\s*(20[0-9]{2})",
        r"\(c\)\s*(20[0-9]{2})",
    ]
    for pattern in patterns:
        match = re.search(pattern, full_text)
        if match:
            return match.group(1)
    return None


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(str(i), ensure_ascii=False) for i in items) + "]"


def render_template(template: str, entry: dict, keywords: list[str]) -> str:
    year = entry.get("year")
    replacements = {
        "{{id}}": entry["id"],
        "{{title}}": entry["title"].replace('"', "'"),
        "{{authors_yaml}}": yaml_list(entry["authors"]),
        "{{tags_yaml}}": yaml_list(entry["tags"]),
        "{{year}}": str(year) if year else "null",
        "{{pdf_path}}": f"literature/papers/{entry['id']}.pdf",
        "{{pdf_relative_from_note}}": f"../papers/{entry['id']}.pdf",
        "{{authors_inline}}": ", ".join(entry["authors"]),
        "{{year_inline}}": f", {year}" if year else "",
        "{{keywords_inline}}": ", ".join(keywords) if keywords else "_none extracted_",
        "{{abstract}}": entry.get("abstract") or "_Abstract not extracted; paste from PDF._",
    }
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(key, value)
    return rendered


def build(make_notes: bool, force: bool, move_pdfs: bool) -> None:
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    BIB_DIR.mkdir(parents=True, exist_ok=True)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    template_text = TEMPLATE.read_text(encoding="utf-8") if make_notes else ""

    catalog = []
    manifest_rows = []
    for entry in CURATED:
        source = SOURCE_DIR / entry["source_file"]
        target = PAPERS_DIR / f"{entry['id']}.pdf"
        if move_pdfs:
            if source.exists() and not target.exists():
                shutil.move(str(source), str(target))
            elif source.exists() and target.exists():
                source.unlink()
        if not target.exists():
            print(f"warning: missing PDF for {entry['id']} ({entry['source_file']})")

        first_page = epm.pdf_text(target) if target.exists() else ""
        full_text = epm.pdf_text(target, first_page_only=False) if target.exists() else ""
        abstract = entry.get("abstract") or epm.extract_abstract(first_page)
        keywords = entry.get("keywords") or epm.extract_keywords(first_page)
        year = detect_copyright_year(full_text)

        record = {
            "id": entry["id"],
            "title": entry["title"],
            "authors": entry["authors"],
            "year": year,
            "venue": None,
            "doi": None,
            "url": None,
            "tags": entry["tags"],
            "keywords": keywords,
            "abstract": abstract,
            "source_file": entry["source_file"],
            "pdf": f"literature/papers/{entry['id']}.pdf",
        }
        catalog.append(record)
        manifest_rows.append(
            {
                "id": entry["id"],
                "curated_file": f"literature/papers/{entry['id']}.pdf",
                "original_file": entry["source_file"],
                "title": entry["title"],
                "authors": "; ".join(entry["authors"]),
                "year": year or "",
                "tags": "; ".join(entry["tags"]),
            }
        )

        if make_notes:
            note_path = NOTES_DIR / f"{entry['id']}.md"
            if note_path.exists() and not force:
                continue
            note_path.write_text(render_template(template_text, record, keywords), encoding="utf-8")

    (BIB_DIR / "catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    with (BIB_DIR / "manifest.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest_rows[0].keys()))
        writer.writeheader()
        writer.writerows(manifest_rows)

    bib_entries = []
    for record in catalog:
        fields = [
            f"  title        = {{{record['title']}}}",
            f"  author       = {{{' and '.join(record['authors'])}}}",
        ]
        if record["year"]:
            fields.append(f"  year         = {{{record['year']}}}")
        if record["keywords"]:
            fields.append(f"  keywords     = {{{', '.join(record['keywords'])}}}")
        fields.append("  howpublished = {GUC MCTR 1021 course publication archive (Winter 2026)}")
        fields.append("  note         = {Venue and year unverified; confirm on the course CMS}")
        bib_entries.append(f"@misc{{{record['id']},\n" + ",\n".join(fields) + "\n}")
    (BIB_DIR / "references.bib").write_text("\n\n".join(bib_entries) + "\n", encoding="utf-8")

    lines = ["# Curated References", "", f"Total papers: {len(catalog)}", ""]
    for index, record in enumerate(catalog, start=1):
        year = record["year"] or "n.d."
        authors = ", ".join(record["authors"])
        lines.append(f"{index}. {authors}. *{record['title']}*. {year}. "
                     f"`{record['id']}` · [PDF](../papers/{record['id']}.pdf)")
        lines.append(f"   - Tags: {', '.join(record['tags'])}")
    (BIB_DIR / "references.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"catalogued {len(catalog)} papers")
    print(f"  {BIB_DIR / 'catalog.json'}")
    print(f"  {BIB_DIR / 'references.bib'}")
    print(f"  {BIB_DIR / 'references.md'}")
    print(f"  {BIB_DIR / 'manifest.csv'}")
    if make_notes:
        print(f"  notes in {NOTES_DIR}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-notes", action="store_true", help="skip literature note generation")
    parser.add_argument("--force", action="store_true", help="overwrite existing literature notes")
    parser.add_argument("--keep-sources", action="store_true", help="copy PDFs instead of moving them")
    args = parser.parse_args()
    build(make_notes=not args.no_notes, force=args.force, move_pdfs=not args.keep_sources)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
