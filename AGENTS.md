# AGENTS — Transcendence Publications

This file instructs AI agents working in this repository on how to approach editorial tasks.

## Before every task

1. Read `canon/style-guide.md` — voice, rhythm, AI-patterns to avoid.
2. Read `canon/glossary.md` — canonical terms and their exact spelling.
3. Use the pipeline indexer to find related files:

   ```bash
   python3 ../pipeline/scripts/index.py --repo-path . --search '<json-query>'
   ```

4. Follow the skill definition in `../pipeline/SKILLS.md` that matches the task type.

## Task types and their skill

| Task | Skill | Key constraint |
| --- | --- | --- |
| Write or revise prose | `prose-editor` | Must not trigger any pattern in style-guide §AI-patterns-to-avoid |
| Clarify or fix a rules passage | `rule-clarifier` | Numbers must match `Transcendence-design/data/system/` YAML |
| Validate a file before marking it final | `continuity-checker` | All canonical terms must match glossary exactly |

## Hard rules

- Do not introduce terminology that does not appear in `canon/glossary.md`. If a new term is needed, propose it and wait for approval.
- Do not change `status: final` or `status: locked` files without explicit instruction.
- Do not change `canonical: true` files without explicit instruction.
- Numbers (Desgaste values, rhythm costs, thresholds) must match the design YAML — never invent values.
- ES files are written entirely in Spanish. EN files entirely in English. Do not mix.
- The term **Preparación**, **Desgaste**, **Aguante**, **ATB**, **Aflicciones** are never translated.

## What good prose looks like

See `canon/voice-samples.md` for approved paragraphs. The short description of the Transcendence voice:

> **[To be filled by project owner — see canon/voice-samples.md]**

## Bilingual consistency

Every corebook section must exist in both ES and EN. When editing one language version, check the paired file in the sibling directory and flag any content drift.

Paired file paths follow the pattern:

```text
10-conflict-and-combat/es/<file>.md   ←→   10-conflict-and-combat/en/<file>.md
```
