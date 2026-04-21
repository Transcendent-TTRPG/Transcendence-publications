---
title: "Manuscript Template"
type: template
content_kind: template
writing_mode: reference
language: both
status: draft
canonical: false
tags: [template, manuscript, editorial]
related: []
---

# Manuscript Template

Use this template to start a new long-form publication manuscript.

## Purpose

Use for a full publication unit: novel, supplement, guide, or long-form outward-facing manuscript.

Before writing, read:

1. `canon/text-modes.md`
2. `canon/style-guide.md`
3. `canon/glossary.md`
4. `canon/fiction-guide.md` if the manuscript is story-facing
5. Relevant canon / design docs for the manuscript domain

## Manuscript Identity

- Product type: `corebook` / `novel` / `supplement`
- Primary modes expected in this manuscript
- Audience: player / Narrator / reader / mixed
- Canon sensitivity: low / medium / high

## Scope Statement

Describe in 2–4 sentences:

- what this manuscript is
- what it is not
- what reader need it serves
- what kinds of text should dominate it

## Structural Outline

```md
# [Manuscript Title]

## Purpose

[What the manuscript does.]

## Reader Contract

[What the reader should expect from tone, structure, and content.]

## Sections

### [Section A]

- Primary mode:
- Reader need:
- Required canon inputs:

### [Section B]

- Primary mode:
- Reader need:
- Required canon inputs:
```

## Mode Planning

For each planned section, declare:

- primary mode
- optional secondary mode
- whether examples are required
- whether bilingual mirroring is required

## Writing Constraints

- Do not let the manuscript drift between teaching text and fiction without an explicit section break
- `rules` and `reference` dominate technical products
- `narrative` and `description` dominate fiction products
- `flavor` supports tone but should not carry core information

## Continuity Checklist

- Terms checked against glossary
- Cross-repo mechanics checked against design YAML / ADR when relevant
- Bilingual strategy decided before drafting at scale
- Related files added in frontmatter once companion files exist
