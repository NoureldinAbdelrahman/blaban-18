# Literature

Curated corpus of the 21 previous course publications provided in the CMS
archive, plus the tooling and templates used to review them.

## Contents

| Path | Purpose |
| --- | --- |
| `papers/` | Source PDFs, renamed to stable kebab-case ids (`<id>.pdf`). |
| `notes/` | One structured literature note per paper (`<id>.md`). |
| `reviews/` | Literature survey drafts and the review tracker. |
| `bibliography/catalog.json` | Canonical metadata (title, authors, tags, keywords, abstract). |
| `bibliography/references.bib` | BibTeX entries (key = `<id>`) for LaTeX. |
| `bibliography/references.md` | Human-readable reference list. |
| `bibliography/manifest.csv` | Mapping from original filenames to curated ids. |

## Reviewing a paper

1. Open the note in `notes/<id>.md`.
2. Fill in TL;DR, problem, contributions, methodology, results, strengths,
   limitations and relevance to our project.
3. Update the frontmatter: set `status: reviewed` and `relevance: 1–5`.
4. Update `reviews/review_tracker.md`.

The template is `docs/templates/literature_note_template.md`.

## Rebuilding

```bash
python scripts/build_bibliography.py            # skips existing notes
python scripts/build_bibliography.py --force    # overwrite all notes
```

Add a paper by appending an entry to `CURATED` in `scripts/build_bibliography.py`
(and dropping the PDF into `previous_publications/` or `literature/papers/`).
