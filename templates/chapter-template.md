---
title: "Chapter Template"
type: template
content_kind: template
writing_mode: reference
language: both
status: draft
canonical: false
tags: [template, chapter, editorial]
related: []
---

# Chapter Template

Use this template to start a new chapter-level manuscript file.

## Purpose

Use for new corebook chapter files, chapter sections, or major rulebook units.

For real corebook files, fill these frontmatter fields before drafting:

- `type: corebook`
- `content_kind: ...`
- `writing_mode: ...`
- `related: ...`
- `authority_refs: ...` for rules-facing content

Before writing, read:

1. `canon/text-modes.md`
2. `canon/style-guide.md`
3. `canon/glossary.md`
4. `canon/voice-samples.md`
5. Relevant design docs / ADR / YAML if the chapter contains mechanics

## Mode Declaration

- Primary mode: `rules` / `description` / `reference` / `narrative`
- Secondary mode if needed: `example` / `flavor`
- Do not draft until the primary mode is explicit

## File Role

State in one sentence what this file is for.

Example:

`This file defines the action economy used during hostile scenes.`

## Reader Need

State what the reader must be able to do after reading the file.

Example:

`After reading this file, the reader should know what actions exist, what they cost, and when they can be used.`

## Recommended Structures

### If primary mode is `rules`

```md
## What This Section Covers

Short orientation. No atmosphere.

## Definition

Define the system element clearly.

## Procedure / Rule Logic

Explain sequence, cost, thresholds, and consequences.

## Edge Cases or Restrictions

State exceptions explicitly.

## Example

Optional but recommended when misreading is likely.
```

### If primary mode is `description`

```md
## What This Section Covers

Orient the reader to the subject.

## Observable State

What can be perceived directly.

## Stable Behaviors or Conditions

How the subject behaves over time.

## Operational Relevance

Why this matters to play, setting, or interpretation.
```

### If primary mode is `reference`

```md
## Quick Reference

Table, list, or condensed lookup block.

## Definitions

Only if required for lookup clarity.

## Notes

Keep brief. No rhetorical expansion.
```

## Writing Constraints

- One primary function per paragraph
- Rules and narrative do not mix in the same paragraph
- Examples stay concrete and brief
- Flavor is optional and never carries critical mechanics
- Use canonical terms exactly as in `canon/glossary.md`

## Bilingual Pairing

- Create the paired ES/EN file in the same work cycle
- Add the paired file to `related`
- Keep section order aligned between languages

## Draft Start

```md
# [Section Title]

## What This Section Covers

[State the scope of the section in 1–3 sentences.]
```
