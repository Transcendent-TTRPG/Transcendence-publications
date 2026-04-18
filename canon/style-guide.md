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

This file is the primary editorial anchor for all Transcendence prose. It governs every writing, revision, and AI-assisted editing task in this repository.

---

## Voice description

The Transcendence voice is precise, restrained, and perceptive. It describes systems as processes unfolding in real time, not as static rules. It prioritizes what can be observed or experienced, and avoids explaining more than necessary. When describing the world, it focuses on specific, limited sensory anchors rather than broad abstraction.

---

## Text intent

- Rules text exists to enable decisions.
- Narrative text exists to guide perception.
- Example text exists to bridge both — concrete situation, no atmosphere.

---

## Rhythm and sentence structure

- Rules text favors short to medium declarative sentences.
- Each sentence should introduce a single idea or consequence.
- Paragraphs in rules text are compact (2–4 sentences).
- Narrative text may use longer sentences, but only when they build a clear sensory or temporal progression.
- Each paragraph should center on a single perceptual anomaly or interaction.
- Avoid chaining multiple metaphors or concepts within the same sentence.
- Prefer sequence over density: one idea, then the next.

---

## Vocabulary

The glossary is authoritative. If a term appears in `canon/glossary.md`, it must be used exactly as defined — same spelling, same capitalization, no synonyms.

- Prefer concrete, physical language over abstract descriptors.
  Write: "the ground gives underfoot"
  Avoid: "the environment feels unstable"
- Canonical system terms remain in Spanish in all contexts:
  Preparación, Desgaste, Aguante, ATB, Aflicciones.
- Avoid synonyms for canonical terms.
  A concept must always be named the same way.
- Prefer verbs over adjectives.
  Write: "the sound arrives late"
  Avoid: "the sound is strange and unnatural"
- Avoid emotional labeling.
  Do not write: "it feels unsettling"
  Show why it is unsettling through perception.

---

## Perception rules

- Each narrative passage should be anchored in one primary sensory channel.
- A secondary sensory detail may be added if it reinforces the same phenomenon.

- Do not distribute attention across multiple unrelated sensory inputs.

- Every passage should present a perceivable anomaly:
  something that behaves differently than expected.

- If a detail cannot be physically perceived, it should not be described directly.

---

## Narrative vs Rules boundary

- Narrative text shows. It does not explain underlying systems.
- Rules text defines. It does not attempt to evoke atmosphere.

- When both are required, separate them explicitly:
  rules first, then example or flavor text.

---

## AI-patterns to avoid

These rules are filters, not templates. Apply them to eliminate AI-generated patterns — not to produce uniformity. Intentional variation in rhythm, sentence length, and structure is expected.

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

Rules text must be declarative. Do not write:

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
