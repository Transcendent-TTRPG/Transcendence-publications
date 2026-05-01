---
title: "Corebook Writing Checklist"
type: canon
language: both
status: draft
canonical: true
tags: [corebook, writing, checklist, rules, editorial]
related:
  - canon/style-guide.md
  - canon/publication-visual-style.md
  - canon/text-modes.md
  - canon/voice-samples.md
  - canon/glossary.md
  - canon/world-facts.md
---

# Corebook Writing Checklist

This file defines the minimum writing gate for any new or revised `corebook` content.

Its purpose is simple:

- ensure corebook prose uses the defined pipeline
- prevent style drift
- stop rule text from shipping without the basic teaching and continuity checks

Use this checklist before changing a file to `review`, `final`, or `locked`.

---

## Mandatory context before writing

Read these files first:

1. `canon/text-modes.md`
2. `canon/style-guide.md`
3. `canon/publication-visual-style.md` when changing layout, CSS, printable artifacts, tables, cards, sheets, or PDF export styling
4. `canon/glossary.md`
5. `canon/voice-samples.md`
6. `canon/world-facts.md` when the file touches setting, atmosphere, religion, cosmology, or extranatural phenomena

Also load:

- the target file
- the bilingual pair
- 2–5 related files from the manifest
- relevant ADR / YAML if the file defines or explains mechanics

---

## Before drafting

- [ ] The file has a clear `content_kind`
- [ ] The primary text mode is explicit (`rules`, `description`, `narrative`, `reference`, etc.)
- [ ] The correct workflow is chosen:
  `rule-clarifier` for mechanics,
  `prose-editor` for prose polish,
  `continuity-checker` before finalization,
  `fiction-writer` only if the corebook deliberately contains scene text
- [ ] The bilingual pair is identified

---

## Rules-writing gate

Apply when the file's primary function is mechanical explanation.

- [ ] Rules text is declarative, not atmospheric
- [ ] The passage does not mix `rules` and `narrative` in the same paragraph
- [ ] At least one example exists in the file or the file explicitly points to one
- [ ] Numbers match design authority
- [ ] Terms match glossary spelling exactly
- [ ] Edge cases are handled or deferred explicitly

---

## Prose and voice gate

- [ ] The text does not use banned transition phrases from `style-guide.md`
- [ ] The text does not rely on hollow abstractions
- [ ] The text does not use emotional labeling without physical grounding
- [ ] If the passage is narrative, it follows the mode rules in `text-modes.md`
- [ ] If the passage is description, it presents observable state rather than hidden explanation

---

## Continuity gate

- [ ] The file does not contradict `world-facts.md`
- [ ] The file does not treat theology as neutral mechanical certainty
- [ ] The file does not treat the Limbo and the Void as synonyms
- [ ] Extranatural phenomena are described by origin, not only by spectacle

---

## Bilingual gate

- [ ] ES and EN versions cover the same section logic
- [ ] Mechanical values match
- [ ] Canonical terms match glossary policy in both languages
- [ ] Headings and section order remain aligned unless divergence is intentional and documented

---

## Status gate

Before `review`:

- [ ] All previous sections pass

Before `final`:

- [ ] `continuity-checker` completed
- [ ] Project owner sign-off

Before `locked`:

- [ ] The content is stable enough to function as canon or canon-adjacent authority
- [ ] Any design dependency has an ADR or explicit authority source
