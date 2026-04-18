# Transcendence Publications — Claude Context

This repository contains all prose content for the Transcendence TTRPG project:

- A bilingual corebook (ES + EN) for a tabletop RPG system
- A bilingual light novel series set in the same universe

## Repository structure

```text
canon/                          Canonical references (style, glossary, voice)
core-books/
  transcendence-corebook/
    00-introduction/
    01-getting-started/
    ...
    10-conflict-and-combat/
      es/                       Spanish prose
      en/                       English prose
light-novels/
  volume-01/
    es/
    en/
templates/                      Reusable file templates
98-layout-export/               Layout-ready PDFs (tracked, do not regenerate)
99-release/                     Final release artifacts
```

## Editorial pipeline

The pipeline lives in the workspace-level `pipeline/` directory (outside this repo).

Before editing any prose file:

1. Run the indexer to find related context files:

   ```bash
   python3 ../pipeline/scripts/index.py \
     --repo-path . \
     --search '{"tags": ["combat"], "chapter": 10, "language": "es"}'
   ```

2. Load the mandatory context listed in `../pipeline/SKILLS.md` for the relevant skill.
3. Edit following the constraints in `SKILLS.md`.

## Metadata

Every `.md` file (except files in `canon/`, `templates/`, AGENTS.md, CLAUDE.md, README.md) must have YAML frontmatter conforming to `../pipeline/schemas/metadata.yaml`.

Fields: `title`, `type`, `language`, `chapter` (optional), `section` (optional), `status`, `canonical`, `tags`, `related`.

## Language conventions

- ES files: written entirely in Spanish. Do not mix languages.
- EN files: written entirely in English. Do not mix languages.
- Canon files: `language: both` — language-neutral references.

## What NOT to change without explicit instruction

- Files with `status: locked` or `canonical: true` — require an explicit design decision.
- Numbers (costs, formulas, thresholds) — must match `Transcendence-design/data/system/`.
- Canonical terms — spelling and capitalization must match `canon/glossary.md`.

## Canonical terms cheat sheet

| ES | EN | Notes |
| --- | --- | --- |
| Preparación | Preparación | Derived stat — do not translate the term |
| Desgaste | Desgaste | Strain/attrition — do not translate |
| Aguante | Aguante | Endurance — do not translate |
| ATB | ATB | Active Time Battle — keep initialism |
| Narrador | Narrator | GM equivalent |
| Aflicciones | Aflicciones | Conditions — do not translate |

Full glossary: `canon/glossary.md`
