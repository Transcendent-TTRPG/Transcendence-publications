# AGENTS — Transcendence Corebook

This file instructs AI agents working specifically on corebook chapters.

## Chapter structure

Each chapter lives under a numbered directory matching its chapter number:

```text
08-conflict-and-combat/
  es/    Spanish prose files
  en/    English prose files
```

Every file in `es/` must have a corresponding file in `en/`. When you edit one, check the other for content drift and report any inconsistencies.

## Corebook-specific rules

- Chapter numbers in frontmatter must match the directory prefix (chapter 8 → directory `08-*`).
- Do not split content that belongs in the same section across multiple files without explicit instruction.
- Rules text must be in the `rule-clarifier` skill's constraints — especially: every rule needs an example or explicit reference to one.
- New corebook files must be created from a template, not from an empty file.
- New corebook files must declare `content_kind` and `writing_mode` immediately.
- If a corebook file mixes modes intentionally, keep `writing_mode` as the dominant mode and declare the divergent sections in `section_modes`.
- New corebook rules files should include `authority_refs` before moving beyond `draft`.
- In ES files, all system terms use their canonical Spanish form (see `../../canon/glossary.md`).
- In EN files, system terms that are marked "Do not translate" in the glossary remain in Spanish.

## Before writing any rules text

1. Read `../../canon/glossary.md` — confirm all terms are present before using them.
2. Read the relevant ADR from `Transcendence-design/docs/adr/` to confirm mechanical values.
3. Cross-check numeric values against `Transcendence-design/data/system/`.
4. Read `../../canon/corebook-writing-checklist.md`.
5. Add `authority_refs` if the file defines, explains, or updates mechanics.

## Before writing any prose

1. Read `../../canon/style-guide.md`.
2. Read `../../canon/voice-samples.md` — find a sample with similar purpose to the passage you are writing.
3. Read `../../canon/text-modes.md`.
4. Read `../../canon/corebook-writing-checklist.md`.
5. Run the indexer to find 2–5 related files for context:

   ```bash
   python3 ../../../../pipeline/scripts/index.py \
     --repo-path ../../../.. \
     --search '{"chapter": <N>, "language": "<lang>", "tags": [<tags>]}'
   ```

## Bilingual pairing checklist

Before marking any file `status: review`:

- [ ] Paired file in the other language exists and covers the same content
- [ ] Mechanical values match between ES and EN versions
- [ ] Canonical terms are spelled correctly in both versions
- [ ] Section structure (headings, order) is consistent between ES and EN
- [ ] `canon/corebook-writing-checklist.md` passes
- [ ] `./pipeline/scripts/editorial-check.sh` passes from workspace root
