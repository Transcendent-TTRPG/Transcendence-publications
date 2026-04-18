---
title: "Transcendence Style Guide"
type: canon
language: both
status: draft
canonical: true
tags: [style, voice, editorial, prose]
related: []
---

# Transcendence Style Guide

**Status: skeleton — needs voice content from project owner.**

This file is the primary editorial anchor for all Transcendence prose. Once populated, it governs every writing, revision, and AI-assisted editing task in this repository.

---

## Voice description

> **[Project owner: write a 1–3 sentence description of the Transcendence voice here.]**
>
> Example of the kind of entry this needs:
> *"The Transcendence voice is precise and unhurried. It describes mechanical systems as if they were living processes. It never explains more than necessary, and trusts the reader to follow."*

---

## Rhythm and sentence structure

> **[Project owner: describe sentence length patterns, paragraph length, use of short vs. long sentences, cadence preferences.]**

Placeholder notes (to be confirmed or replaced):

- Short declarative sentences are preferred for rules text.
- Longer sentences are acceptable in scene-setting prose when they build tension.
- Paragraphs should not exceed 4–5 sentences in rules text.

---

## Vocabulary

> **[Project owner: list preferred words and phrasing for common concepts.]**

Placeholder notes:

- Prefer active voice over passive.
- System terms always use their canonical Spanish names even in English text (Preparación, Desgaste, Aguante, ATB, Aflicciones).
- Numbers in rules text are written as numerals (not words): "3 Desgaste", not "three Desgaste".

---

## AI-patterns to avoid

These patterns make prose sound generated. **Any text exhibiting these patterns must be rewritten before it can advance past `status: draft`.**

### Generic transition phrases

Do not use:

- "In the world of Transcendence, ..."
- "It is important to note that ..."
- "Additionally, ..."
- "Furthermore, ..."
- "This means that ..."
- "As a result, ..."
- "In other words, ..."

### Filler qualifiers

Do not use:

- "very", "quite", "rather", "somewhat"
- "essentially", "basically", "generally", "typically"
- "in a sense", "in a way", "more or less"

### Hollow abstractions

Do not use phrases that describe a concept without actually explaining it:

- "The system is designed to reflect real-world complexity."
- "This mechanic captures the feeling of ..."
- "Combat feels more dynamic because ..."

Write the mechanism. Do not describe how the mechanism feels.

### Excessive hedging in rules text

Rules text must be declaritive. Do not write:

- "The Narrator may want to consider ..."
- "Players might find it useful to ..."
- "It can sometimes be helpful to ..."

Write: "The Narrator decides X." or "Players choose X."

### Over-explained obvious steps

Do not write sequences where every step is spelled out redundantly. Trust the reader.

---

## Formatting conventions

- H1 (`#`) — document title only (one per file)
- H2 (`##`) — major sections
- H3 (`###`) — subsections
- H4 (`####`) — named items within a subsection (sparingly)
- Bold (`**text**`) — canonical terms on first use in a section; important mechanical values
- Tables — for anything that would otherwise be a bulleted list of paired values
- Blockquotes (`>`) — designer's notes, examples, or in-world flavor text set apart from rules

---

## What to do if a passage sounds like AI

1. Read `canon/voice-samples.md` — find an approved paragraph with similar purpose.
2. Identify which AI-pattern above is present.
3. Rewrite from scratch using the voice sample as rhythm reference.
4. Do not try to "patch" AI prose — rewrite the paragraph.

---

## Sign-off requirements by status

| Status | Requirements |
| --- | --- |
| `draft` | No requirements — work in progress |
| `review` | No AI-patterns; terminology matches glossary; bilingual pair exists |
| `final` | `review` requirements + project owner approval |
| `locked` | `final` + explicit design decision on record |
