---
title: "Afflictions"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 11
status: draft
canonical: false
tags: [ailments, aflicciones, afflictions, conditions, progression, vínculo, vestigio]
related:
  - core-books/transcendence-corebook/11-ailments/es/03-aflicciones.md
  - core-books/transcendence-corebook/11-ailments/en/01-ailments.md
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/en/
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Afflictions

**Afflictions** are mental, perceptual, or inner-state disruptions. Unlike Alterations — which are direct physiological disruptions of the body — Afflictions compromise the being's internal stability: judgment, perception, emotional regulation, cognitive integrity.

An Affliction may originate from psychic exposure, contact with vestiges or vínculos, sustained trauma, horror presence, or extranatural infusion. What defines it is that the result is an inner-state disruption that does not resolve like an ordinary physical injury.

**Resistance Roll:** `1d10 + Composure + Affliction Resistance level + additional bonuses`

---

## Intensity and Progression

Afflictions do not have a fixed duration. Instead, they have an **Intensity** — a value that rises or falls based on how the character carries their state, their exposure to certain elements, and their access to recovery.

An Affliction begins at **Minor Intensity** (5 points) and can progress across three thresholds:

| Severity | Intensity Threshold |
| --- | --- |
| **Minor** | 5 |
| **Moderate** | 10 |
| **Severe** | 15 |

The Intensity threshold also determines the difficulty of relevant rolls during the worsening and recovery process.

When an Affliction's Intensity rises enough to cross the next threshold, the Affliction advances to that severity. When it falls below the current threshold, it retreats.

---

## Worsening Factors

The following factors increase the Intensity of an active Affliction:

| Factor | Modifier |
| --- | --- |
| Night without full rest | `+1` |
| Interaction with a vestige — using or discovering it | `+1` |
| Interaction with a vínculo — discovering it | `+1` |

Each factor applies once per relevant event or period.

---

## Treatment Factors

The following factors reduce the Intensity of an active Affliction:

| Factor | Modifier |
| --- | --- |
| Night of good rest | `−1` |
| Effective session of Deep Meditation | `−1` |

If Intensity falls below 5, the Affliction is considered resolved and ends.

---

## New Affliction Rule

Once an Affliction has progressed to **Severe Intensity**, the character can no longer worsen that individual Affliction further. Instead, the next time they receive an Affliction — the same one or a different one — they receive a **new, separate Affliction** that begins at Minor Intensity.

Parallel active Afflictions are distinct states. Each carries its own threshold and responds to its own worsening and treatment factors independently.

---

## Catalog

### Vision

#### Paranoid Schizophrenia

*Paranoid disruption of threat judgment. The character interprets neutral or ambiguous presences as sources of imminent danger. Intent reading is contaminated.*

**Trigger:** when perceiving a creature in a context of uncertainty, social ambiguity, or unconfirmed potential threat.

**S.R.:** Cunning against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to Cunning S.R.s related to intent, social reading, or threat detection. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Cunning S.R.; on fail → Terrified Minor for the rest of the scene. |
| **Severe** | Moderate, plus: on fail → also becomes Trapped Minor for the rest of the scene. |

**Extranatural Channel:** can genuinely detect hidden threats, concealed intentions, and entities presenting themselves as benign presences.

---

#### Visual Agnosia

*Loss of functional recognition. The character sees objects and creatures but cognition fails when trying to identify them or assign them function.*

**Trigger:** when attempting to deliberately interact with an object, or when attempting to recognize a specific creature.

**S.R.:** Identification (Intellect) against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to Identification S.R.s. |
| **Moderate** | Minor, plus: when the trigger activates on an object, must pass an Identification S.R.; on fail → the interaction does not resolve that activation. |
| **Severe** | Moderate, plus: the trigger also applies to recognizing creatures; on fail → cannot distinguish the creature from its surroundings or direct actions against it specifically that activation. |

**Extranatural Channel:** sees hidden symbols, extranatural inscriptions, and impossible geometries in objects in the environment.

---

#### Visual Hallucinations

*Overlay of false images on real perception. The character receives visual stimuli with no correlate in the physical world.*

**Trigger:** at the start of each of the character's activations, or when the Narrator determines it during a scene of high visual load or extranatural presence.

**S.R.:** Perception (Wisdom) against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to visual Perception S.R.s. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Perception S.R.; on fail → Confused Minor for the rest of the scene. |
| **Severe** | Moderate, plus: on fail → also becomes Disoriented Minor for the rest of the scene. |

**Extranatural Channel:** perceives overlapping realities, echoes, and traces of extranatural presences that have already left or have not yet arrived.

---

### Hearing

#### Tinnitus

*Persistent ringing or tone that interferes with auditory Perception and sustained concentration.*

**Trigger:** when performing an action that requires sustained concentration or active auditory Perception.

**S.R.:** Perception (Wisdom) against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to auditory Perception S.R.s. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Perception S.R.; on fail → Impeded Minor for the rest of the scene. |
| **Severe** | Moderate, plus: on fail → Overwhelmed Minor for the rest of the scene instead of Impeded Minor. |

**Extranatural Channel:** hears hidden whispers, extranatural frequencies, and communications between entities imperceptible to others.

---

#### Hyperacusis

*Hypersensitivity to sound. Sudden or sustained auditory stimuli produce a disproportionate collapse response.*

**Trigger:** when exposed to sudden, sustained, or high-intensity sounds.

**S.R.:** Focus (Composure) against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to Composure S.R.s. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Focus S.R.; on fail → Stunned Minor for the rest of the scene. |
| **Severe** | Moderate, plus: on fail → Deafened Minor for the rest of the scene instead of Stunned Minor. |

**Extranatural Channel:** perceives subtle non-acoustic vibrations: emotional tensions, hidden presences, movements in the adjacent plane.

---

#### Persistent Echo

*The inner ear registers echoes with no real correlate. The vestibular system, linked to the ear, is compromised, affecting balance and spatial orientation.*

**Trigger:** when attempting to orient, move precisely, or maintain balance in demanding terrain.

**S.R.:** Balance (Agility) against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to auditory Perception S.R.s and Orientation S.R.s. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Balance S.R.; on fail → Unbalanced Minor for the rest of the scene. |
| **Severe** | Moderate, plus: on fail → Paralyzed Minor for the rest of the scene instead of Unbalanced Minor. |

**Extranatural Channel:** hears echoes from other realities and perceives movements of presences in the adjacent plane.

---

### Smell

#### Phantosmia

*Olfactory perception of odors with no physical origin. Phantom stimuli saturate and destabilize internal regulation.*

**Trigger:** when in a scene of high tension or confirmed or suspected extranatural proximity.

**S.R.:** Containment (Composure) against the current Intensity. Does not apply to C.R.s.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to Composure S.R.s. Does not apply to C.R.s. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Containment S.R.; on fail → Overwhelmed Minor for the rest of the scene. |
| **Severe** | Moderate, plus: on fail → Overwhelmed Moderate for the rest of the scene instead of Overwhelmed Minor. |

**Extranatural Channel:** detects traces of corruption and Tauma; perceives extranatural entities by scent before detecting them by other means.

---

#### Hyperosmia

*Olfactory hypersensitivity. Environmental odors become invasive and incapacitating.*

**Trigger:** when exposed to intense, concentrated, or active odors in the environment.

**S.R.:** Focus (Composure) against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to Focus S.R.s. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Focus S.R.; on fail → Stunned Minor for the rest of the scene. |
| **Severe** | Moderate, plus: the character's Preparation is reduced to 0; on fail → also becomes Overwhelmed Minor for the rest of the scene. |

**Extranatural Channel:** can track invisible creatures by scent; detects active extranatural presences in the area.

---

### Taste

#### Dysgeusia

*Persistent taste distortion. Any ingestion is repulsive or alien, interfering with rest and recovery.*

**Trigger:** when attempting to eat or drink during rest.

**S.R.:** Containment (Composure) against the current Intensity.

| Intensity | Effect on fail |
| --- | --- |
| **Minor** | Loses 1 level of Fatigue recovery during that rest. |
| **Moderate** | Loses 2 levels of Fatigue recovery and cannot perform additional activities during that rest. |
| **Severe** | Does not recover Fatigue and does not reduce the Intensity of any active Affliction during that rest. |

**Extranatural Channel:** detects corrupted, poisoned, or extranatural-impregnated substances by tasting them or being in direct proximity to them.

---

#### Alimentary Compulsion

*Irresistible urge to consume matter after high-intensity hostile situations. The compulsion escalates with Intensity toward increasingly dangerous consumables.*

**Trigger:** when a hostile scene ends or when corpses, remains, or accessible organic tissue are encountered.

**S.R.:** Containment (Composure) against the current Intensity.

| Intensity | Effect on fail |
| --- | --- |
| **Minor** | Must consume inert matter — earth, dust, refuse, insects. Receives Unbalanced Minor. |
| **Moderate** | Must consume contaminated organic matter — dead tissue, fluids, creature remains. Receives Infection Minor. |
| **Severe** | Must consume toxic or caustic material — poisoned flesh, active fluids, corrosive material. Receives Infection Minor and Poison Minor. |

**Extranatural Channel:** receives fragments of vision or residual memory from the consumed material — images, emotions, instants from the past of the organism or entity.

---

### Touch

#### Formication

*Persistent sensation of movement beneath the skin: tingling, pressure, or contact with no external origin. Action cost expands as Intensity increases.*

**Passive effect:** no activation S.R. required.

| Intensity | Effect |
| --- | --- |
| **Minor** | Direct physical contact actions cost +1 additional Rhythm. |
| **Moderate** | Physical Techniques and Focus S.R.s cost +1 additional Rhythm. |
| **Severe** | All actions cost +1 additional Rhythm. |

**Extranatural Channel:** perceives incorporeal entities and traces of the adjacent plane through direct physical contact.

---

#### Partial Anesthesia

*Partial loss of sensation from external damage. The body does not correctly register danger signals, and resistance defenses are reduced.*

**Passive effect:** no activation S.R. required.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to R.R.s against Alterations. |
| **Moderate** | −1 penalty to R.R.s against Alterations and Infections. |
| **Severe** | −1 penalty to R.R.s against Alterations, Infections, and Poisons. |

**Extranatural Channel:** perceives the intangible plane; detects presences without physical form in the immediate area.

---

#### Hypertouch

*Tactile hypersensitivity. Contact with objects or creatures produces disproportionate stimuli that destabilize internal regulation.*

**Trigger:** when deliberately touching an object or a creature.

**S.R.:** Focus (Composure) against the current Intensity.

| Intensity | Effect |
| --- | --- |
| **Minor** | −1 penalty to Focus S.R.s when touching objects or creatures. |
| **Moderate** | Minor, plus: when the trigger activates, must pass a Focus S.R.; on fail → Overwhelmed Minor for the rest of the scene. |
| **Severe** | Moderate, plus: on fail → Impeded Minor for the rest of the scene instead of Overwhelmed Minor. |

**Extranatural Channel:** feels energy currents in objects; detects hidden properties and extranatural origins through direct contact.
