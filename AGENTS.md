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
- **ATB** is never translated — use the initialism in both languages.
- All other system terms use their EN equivalent in EN files (see `canon/glossary.md`). Do not use the Spanish form in EN prose.

## What good prose looks like

See `canon/voice-samples.md` for approved paragraphs. The Transcendence voice:

> Precise, restrained, and perceptive. It describes systems as processes unfolding in real time, not as static rules. It prioritizes what can be observed or experienced, and avoids explaining more than necessary. When describing the world, it focuses on specific, limited sensory anchors rather than broad abstraction.

## Bilingual consistency

Every corebook section must exist in both ES and EN. When editing one language version, check the paired file in the sibling directory and flag any content drift.

Paired file paths follow the pattern:

```text
08-conflict-and-combat/es/<file>.md   ←→   08-conflict-and-combat/en/<file>.md
```


## GitHub Connector Workflow

When working through ChatGPT's GitHub connector:

- Treat `Transcendence-design` as the source of truth for mechanics and canon.
- Treat `Transcendence-publications` as the reader-facing manuscript layer.
- If repository search is unavailable or not indexed, fetch files by known path.
- For mechanical changes, check both:
  - `Transcendence-design/data/system/*.yaml`
  - `Transcendence-design/docs/system/*.md`
- Then update the paired ES/EN manuscript files in `Transcendence-publications`.
- If a term changes, update `Transcendence-publications/canon/glossary.md`.