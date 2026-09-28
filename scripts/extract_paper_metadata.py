#!/usr/bin/env python3
"""Extract paper metadata from PDFs into a bibliographic catalog.

Usage:
    python scripts/extract_paper_metadata.py [SOURCE_DIR] [OUTPUT_JSON]

Defaults:
    SOURCE_DIR  literature/papers
    OUTPUT_JSON literature/bibliography/catalog.raw.json

The extractor is heuristic: it reads the first page in reading order and
pulls out the title, author line and abstract. Review the generated catalog
and correct any mis-parsed fields before relying on it.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = REPO_ROOT / "literature" / "papers"
DEFAULT_OUTPUT = REPO_ROOT / "literature" / "bibliography" / "catalog.raw.json"

STOP_MARKERS = (
    "Abstract",
    "ABSTRACT",
)

SECTION_MARKERS = (
    "Index Terms",
    "I. INTRODUCTION",
    "I. I NTRODUCTION",
    "INTRODUCTION",
    "Keywords",
    "1. INTRODUCTION",
)

AFFILIATION_HINTS = (
    "Department",
    "University",
    "Faculty",
    "Egypt",
    "Email",
    "Research Group",
    "Research Lab",
    "Cairo",
    "gmail",
    "student.guc",
    "@guc",
    "@student",
    "Media Engineering",
    "Mechatronics",
)


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return re.sub(r"-{2,}", "-", text)


def pdf_text(path: Path, first_page_only: bool = True) -> str:
    cmd = ["pdftotext"]
    if first_page_only:
        cmd += ["-f", "1", "-l", "1"]
    cmd += [str(path), "-"]
    try:
        out = subprocess.run(cmd, capture_output=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""
    return out.decode("utf-8", errors="replace")


def extract_title(lines: list[str]) -> str:
    title_parts: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if title_parts:
                break
            continue
        if any(stripped.startswith(marker) for marker in STOP_MARKERS):
            break
        if re.search(r"@|Department|University|Faculty", stripped):
            break
        title_parts.append(stripped)
        if len(title_parts) >= 4:
            break
    title = " ".join(title_parts)
    title = re.sub(r"\s{2,}", " ", title).strip()
    return title


def extract_authors(lines: list[str], title: str) -> str:
    title_tokens = title.split()
    idx = 0
    for i, line in enumerate(lines):
        if title_tokens and title_tokens[0] in line and title_tokens[-1] in line:
            idx = i + 1
            break
    author_lines: list[str] = []
    for line in lines[idx:]:
        stripped = line.strip()
        if not stripped:
            if author_lines:
                break
            continue
        if any(stripped.startswith(marker) for marker in STOP_MARKERS):
            break
        if any(hint in stripped for hint in AFFILIATION_HINTS):
            if author_lines:
                break
            continue
        if re.fullmatch(r"[\d\s,†‡∗*]+", stripped):
            continue
        author_lines.append(stripped)
        if len(author_lines) >= 3:
            break
    authors = " ".join(author_lines)
    authors = re.sub(r"[\d\s]*[,]\s*(?=[A-Z])", ", ", authors)
    authors = re.sub(r"\s{2,}", " ", authors).strip(" ,")
    return authors


def extract_abstract(text: str) -> str:
    match = None
    for marker in ("Abstract—", "Abstract -", "Abstract—", "Abstract"):
        pos = text.find(marker)
        if pos != -1:
            match = pos + len(marker)
            break
    if match is None:
        return ""
    tail = text[match:]
    end = len(tail)
    for marker in SECTION_MARKERS:
        pos = tail.find(marker)
        if pos != -1:
            end = min(end, pos)
    abstract = tail[:end]
    abstract = abstract.replace("-\n", "")
    abstract = re.sub(r"\s+", " ", abstract).strip()
    return abstract


def extract_year(full_text: str, default: str | None = None) -> str | None:
    years = re.findall(r"\b(20(?:1[89]|2[0-6]))\b", full_text)
    if years:
        return max(set(years), key=years.count)
    return default


def extract_keywords(text: str) -> list[str]:
    for marker in ("Index Terms—", "Index Terms -", "Keywords—", "Keywords -", "Index Terms"):
        pos = text.find(marker)
        if pos != -1:
            tail = text[pos + len(marker):]
            stop = len(tail)
            for end_marker in ("\n\n", "I. I", "I. I NTRODUCTION", "1. INTRODUCTION", "INTRODUCTION"):
                p = tail.find(end_marker)
                if p != -1:
                    stop = min(stop, p)
            block = tail[:stop]
            block = re.sub(r"[\n\r]+", " ", block)
            parts = re.split(r"[;,]", block)
            return [p.strip(" .").strip() for p in parts if p.strip(" .")]
    return []


def build_entry(path: Path) -> dict:
    first_page = pdf_text(path, first_page_only=True)
    full_text = pdf_text(path, first_page_only=False)
    lines = first_page.splitlines()
    title = extract_title(lines)
    authors = extract_authors(lines, title)
    abstract = extract_abstract(first_page)
    year = extract_year(full_text)
    keywords = extract_keywords(first_page)
    return {
        "id": slugify(title)[:80] or slugify(path.stem),
        "title": title,
        "authors": authors,
        "year": year,
        "venue": None,
        "doi": None,
        "url": None,
        "keywords": keywords,
        "abstract": abstract,
        "source_file": path.name,
    }


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SOURCE
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT
    if not source.is_dir():
        print(f"source directory not found: {source}", file=sys.stderr)
        return 1
    entries = [build_entry(p) for p in sorted(source.glob("*.pdf"))]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {len(entries)} entries to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
