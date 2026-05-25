---
title: "Alterations"
type: corebook
content_kind: rules
writing_mode: rules
language: en
chapter: 11
status: draft
canonical: false
tags: [ailments, alteraciones, alterations, conditions, catalog, combat]
related:
  - core-books/transcendence-corebook/11-ailments/es/02-alteraciones.md
  - core-books/transcendence-corebook/11-ailments/en/01-ailments.md
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-actions.md
  - core-books/transcendence-corebook/09-techniques/en/01-play-surface-and-pilot-example.md
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Alterations

**Alterations** are physiological disruptions that directly compromise the body's function. They are the primary layer of combat conditions in the system.

An Alteration may originate from physical, environmental, mental, creature, or anomalous sources — what defines it is that the result is a direct operational disruption of the body during play.

**Resistance Roll:** `1d10 + Resilience + Alteration Resistance level + additional bonuses`

The effects of each Alteration are **cumulative by severity**: Moderate includes everything from Minor, Severe includes everything from Moderate.

---

## Blinded

*The target cannot see.*

**Application:** Light, trauma, debris, darkness imposed as a body state, eye damage, or any other source that functionally eliminates vision. Apply Blinded only when sight is no longer a usable primary sense; if a source merely obscures a single visual line, a reading point, or a bounded visual channel, use a procedural state instead.

**Duration:** `until_removed`

**Recovery:** Ends when the source of blindness dissipates, is eliminated, or vision is restored. When true physical restoration is needed, a `S.R.` of Medicine is the preferred recovery path.

| Severity | Effects |
| --- | --- |
| **Minor** | `−5` to all `A.R.`, `D.R.`, `C.R.`, and `S.R.` |
| **Moderate** | `−5` to all `A.R.`, `D.R.`, `C.R.`, and `S.R.` |
| **Severe** | `−5` to all `A.R.`, `D.R.`, `C.R.`, and `S.R.` |

*Severity governs primarily application pressure and recovery difficulty, not the size of the penalty.*

---

## Concussed

*The hit landed. Clarity will take a while to return.*

**Application:** Impact, internal shock, blast force, collision, or any other source that produces a concussion-like destabilization in a credible way.

**Duration:** `until_removed`

**Recovery:** Ends when the target recovers enough internal stability to restore clarity. The preferred recovery is a `S.R.` of Containment against the original severity; Medicine can also end the state, and full rest may clear it between scenes if the fiction justifies it.

| Severity | Effects |
| --- | --- |
| **Minor** | `C.R.` and `S.R.` based on Composure or Intellect suffer a penalty equal to the rank bonus of the source that applied Concussed. |
| **Moderate** | Minor, plus: `Preparation` becomes `0`. |
| **Severe** | Moderate, plus: to use a `C.R.` or `S.R.` based on Composure or Intellect, the target must first pass a `S.R.` of Containment against the original severity; if it fails, the action does not resolve. |

---

## Confused

*The target loses clean judgment and cannot reliably distinguish allies, enemies, or intent in the immediate scene.*

**Application:** Body shock, sensory overload, neural disruption, concussion, toxins, or any other source that destabilizes immediate operational judgment in a credible way.

**Duration:** `until_removed`

**Recovery:** Ends with a successful `S.R.` of Focus against the original severity once enough operational clarity returns. Medicine or elimination of the destabilizing source may also end it if the fiction justifies it.

| Severity | Effects |
| --- | --- |
| **Minor** | `A.R.`, `I.R.`, and `S.R.` based on Intellect or Composure that require ally-enemy discrimination, target identification, or intent reading suffer a penalty equal to the rank bonus of the source that applied Confused. |
| **Moderate** | Minor, plus: before deliberately choosing a specific creature, side, or operational line in a crowded, ambiguous, or shifting scene, the target must first pass a `S.R.` of Focus against the original severity. |
| **Severe** | Moderate, plus: to deliberately choose a specific creature, side, or operational line, the target must first pass that `S.R.` of Focus; if it fails, the target is the nearest creature, even if an ally. |

---

## Deafened

*The sound came in too hard. Now it does not come at all.*

**Application:** Sonic trauma, internal pressure shock, blast force, environmental overload, or any other source that disrupts auditory function enough that hearing is no longer a usable primary sense. Apply Deafened only when hearing is no longer usable; if a source merely obscures a single auditory line, one ear, an echo, or a bounded channel, use a procedural state instead.

**Duration:** `until_removed`

**Recovery:** Ends when auditory function returns or the target is no longer functionally deafened. If the source is no longer active, a `S.R.` of Medicine is the preferred path; otherwise the state persists until time, treatment, or elimination of the source makes it credible.

| Severity | Effects |
| --- | --- |
| **Minor** | Cannot perform `C.R.` or `S.R.` that require hearing. Cannot rely on auditory cues to respond to threats not seen. |
| **Moderate** | Cannot perform `C.R.` or `S.R.` that require hearing. Cannot rely on auditory cues to respond to threats not seen. |
| **Severe** | Cannot perform `C.R.` or `S.R.` that require hearing. Cannot rely on auditory cues to respond to threats not seen. |

*Severity governs primarily application pressure and recovery difficulty.*

---

## Disoriented

*Direction is gone. The body moves, but without bearing.*

**Application:** Spatial disruption, sensory saturation, dizziness, unstable perspective, or any other source that breaks the target's sense of direction in a credible way.

**Duration:** `until_removed`

**Recovery:** Ends with a successful `S.R.` of Orientation against the original severity.

| Severity | Effects |
| --- | --- |
| **Minor** | `S.R.` based on Intellect or Composure suffer a penalty equal to the rank bonus of the source that applied Disoriented. |
| **Moderate** | Minor, plus: `Preparation` becomes `0`. |
| **Severe** | Moderate, plus: to use an action that requires an `S.R.` based on Intellect or Composure, the target must first pass a `S.R.` of Orientation against the original severity; if it fails, the `S.R.` does not resolve. |

---

## Electrified

*The discharge passed. The muscles have not finished believing it.*

**Application:** Significant electrical discharge, prolonged conductive exposure, or any other source of credible body shock.

**Duration:** `while_condition_persists`

**Recovery:** Ends when the discharge is neutralized or interrupted long enough for the body to recover continuity. A successful `S.R.` of Tolerance against the original severity usually ends the state once the source is no longer active.

| Severity | Effects |
| --- | --- |
| **Minor** | Attacks, movement, and Techniques tied to attack or movement cost additional Rhythm equal to the rank bonus of the source. `S.R.` based on Agility suffer that same penalty. |
| **Moderate** | Minor, plus: cannot use movement or interception Reactions without first passing a `S.R.` of Tolerance against the original severity. |
| **Severe** | Moderate, plus: to take any action, the target must first pass that `S.R.` of Tolerance; if it fails, the action does not resolve. |

---

## Frozen

*The muscles respond late. The cold already has the lead.*

**Application:** Prolonged exposure to freezing, a hostile ice-based effect, or any other source that functionally deteriorates the body through cold in a credible way.

**Duration:** `while_condition_persists`

**Recovery:** Ends when body temperature rises and the target is no longer functionally impaired by cold. If the cold source is no longer actively imposing the state, a successful `S.R.` of Acclimatization against the original severity usually ends the Alteration; Medicine can assist when treatment is part of the fiction.

| Severity | Effects |
| --- | --- |
| **Minor** | `C.R.` of Agility and `S.R.` of Agility suffer a penalty equal to the rank bonus of the source that applied Frozen. Movement reduced to half. |
| **Moderate** | Minor, plus: cannot run, jump, climb, or use any other explosive movement without first passing a `S.R.` of Acclimatization against the original severity. |
| **Severe** | Moderate, plus: at the start of its activation, the target must pass the `S.R.` of Acclimatization against the original severity; if it fails, it loses the activation. |

---

## Impeded

*The weapon stays in the hand. Control over it, not entirely.*

**Application:** Body disruption, neural interference, pain-based blocking, unstable grip, or any other source that prevents clean weapon technique execution without fully paralysing the target.

**Duration:** `until_removed`

**Recovery:** Ends with a successful `S.R.` of Focus against the original severity once the target can re-establish execution, or when the source blocking execution no longer applies.

| Severity | Effects |
| --- | --- |
| **Minor** | Weapon-based `A.R.`, `I.R.`, and `S.R.` based on Agility suffer a penalty equal to the rank bonus of the source that applied Impeded. |
| **Moderate** | Minor, plus: to perform a weapon attack, interception, reload, or re-preparation, the target must first pass a `S.R.` of Focus against the original severity; if it fails, the action does not resolve. |
| **Severe** | Moderate, plus: cannot use Techniques tied to weapon competencies. |

---

## Knocked Down

*Posture gives. The ground wins.*

**Application:** Impact, sweep, force transfer, terrain collapse, collision, or any other credible cause that brings the target to the ground.

**Duration:** `until_removed`

**Recovery:** Ends when the target stands up, spending its first movement action to rise.

| Severity | Effects |
| --- | --- |
| **Minor** | `−3` to all rolls. The first movement action is spent standing up. |
| **Moderate** | `−3` to all rolls. The first movement action is spent standing up. |
| **Severe** | `−3` to all rolls. The first movement action is spent standing up. |

*Severity governs primarily the difficulty of resisting or avoiding the knockdown, not the intensity of the state once the target is already on the ground.*

---

## Lacerated

*Moving costs. The wound remembers exactly how much.*

**Application:** Deep cut or laceration, tearing bite or slash, contact with a hooked or serrated weapon, open wound under physical pressure, or any other source of painful and credible tissue disruption.

**Duration:** `until_removed`

**Recovery:** Ends when the target dedicates an appropriate action to bandaging, bracing, closing, hardening, or stabilising pressure on the wound. Medicine can end the state when treatment is part of the fiction.

| Severity | Effects |
| --- | --- |
| **Minor** | Attack or movement Techniques and `S.R.` based on Strength or Agility cost additional Rhythm equal to the rank bonus of the source that applied Lacerated. |
| **Moderate** | Minor, plus: to use attack or movement Techniques or `S.R.` based on Strength or Agility, the target must first pass a `S.R.` of Tolerance against the original severity; if it fails, the action does not resolve. |
| **Severe** | Moderate, plus: to take any action, the target must first pass that `S.R.` of Tolerance; if it fails, the action does not resolve. |

---

## Off-Balance

*The center no longer responds — moving costs not falling.*

**Application:** Loss of balance or momentum, body shock, unstable ground, or any other source that compromises stable movement and defense in a credible way.

**Duration:** `until_removed`

**Recovery:** Ends with a successful `S.R.` of Balance against the original severity.

| Severity | Effects |
| --- | --- |
| **Minor** | `D.R.` and `S.R.` based on Agility suffer a penalty equal to the rank bonus of the source that applied Off-Balance. |
| **Moderate** | Minor, plus: to use `S.R.` based on Strength or Agility, the target must first pass a `S.R.` of Balance against the original severity; if it fails, the `S.R.` does not resolve. |
| **Severe** | Moderate, plus: if the target fails that `S.R.` of Balance when using `S.R.` based on Strength or Agility, it immediately becomes Knocked Down instead of simply losing the attempt. |

---

## Overwhelmed

*Too much at once. The system cannot find a way out.*

**Application:** Sensory saturation, internal overload, psychic overflow expressed through the body, or any other source that breaks functional regulation in a credible way.

**Duration:** `until_removed`

**Recovery:** Ends with a successful `S.R.` of Containment against the original severity, or when the source of overload ends and the target recovers enough internal regulation.

| Severity | Effects |
| --- | --- |
| **Minor** | `R.R.` suffer a penalty equal to the rank bonus of the source that applied Overwhelmed. |
| **Moderate** | Minor, plus: cannot voluntarily use `S.R.` based on Aura or Composure without first passing a `S.R.` of Containment against the original severity. |
| **Severe** | Moderate, plus: to use any `S.R.`, the target must first pass that `S.R.` of Containment; if it fails, the `S.R.` does not resolve. |

---

## Paralyzed

*The signal arrives. The body does not execute it.*

**Application:** Electricity, poison, cold blocking, body shock, forced suppression, or any other source that credibly halts significant action.

**Duration:** `until_removed`

**Recovery:** Ends when body control returns. The preferred recovery is a `S.R.` of Tolerance against the original severity once the source no longer fully blocks the body; some sources may require their own release condition before any roll is possible.

| Severity | Effects |
| --- | --- |
| **Minor** | The target cannot take significant actions. |
| **Moderate** | The target cannot take significant actions. |
| **Severe** | The target cannot take significant actions. |

*Severity governs primarily the difficulty of applying, resisting, or breaking the state. Apply Paralyzed only when significant body action is truly halted; use Restrained for physical retention, Stunned for lost activation, and Impeded for execution breakdown that leaves the body still active.*

---

## Restrained

*The body is physically held or structurally prevented from moving freely.*

**Application:** Creature grab or hold, net or restraining mechanism, adhesive hazard, collapsing surface, or any other source that physically retains the target in a credible way.

**Duration:** `until_removed`

**Recovery:** Ends when the target breaks free, is released, or the source stops retaining it. The preferred recovery is a `S.R.` of Grappling against a live hold, or another `S.R.` based on Agility if the fiction is more about slipping free or untangling than overcoming direct contact.

| Severity | Effects |
| --- | --- |
| **Minor** | Movement `0`. `A.R.`, `I.R.`, `D.R.`, and `S.R.` based on Agility suffer a penalty equal to the rank bonus of the source that applied Restrained when those rolls are made against the active retention. |
| **Moderate** | Minor, plus: cannot use actions costing more than 4 Rhythm, full-extension, or heavy-leverage actions without first passing a `S.R.` of Grappling against the original severity. |
| **Severe** | Moderate, plus: to take any action, the target must first pass that `S.R.` of Grappling; if it fails, the action does not resolve. |

---

## Stunned

*The hit does not just land — it leaves the action without an owner.*

**Application:** Impact, neural shock, concussive force, overload, or any other source that briefly shuts down clean action in a credible way.

**Duration:** `until_removed`

**Recovery:** Minor ends after the first lost activation is consumed. Moderate and Severe end with a successful `S.R.` of Tolerance against the original severity after one lost activation, or when treatment or elimination of the source restores operational continuity.

| Severity | Effects |
| --- | --- |
| **Minor** | `R.R.` and `C.R.` suffer a penalty equal to the rank bonus of the source that applied Stunned. The target's next significant activation is lost — it may only take free actions. |
| **Moderate** | Minor, plus: while Stunned remains active, `Preparation` becomes `0`. After each consumed lost activation, the target must pass a `S.R.` of Tolerance against the original severity or Stunned stays active and consumes the next activation as well. |
| **Severe** | Moderate, plus: while Stunned remains active, the target cannot voluntarily use Reactions without first passing that `S.R.` of Tolerance. |

---

## Suffocating

*The air falls short. Each action starts collecting its debt from inside.*

**Application:** Asphyxiation, drowning, smoke inhalation, crushing pressure, or any other source that prevents breathing in a credible way.

**Duration:** `while_source_persists`

**Recovery:** Ends when the source preventing breathing stops acting. The cumulative penalty resets when the state ends.

| Severity | Effects |
| --- | --- |
| **Minor** | At the start of each activation, `S.R.` of Tolerance against the original severity or the target is incapacitated for that activation. Cumulative `−1` penalty to all rolls for each activation spent under Suffocating. |
| **Moderate** | Minor, plus: `Preparation` becomes `0`. Cannot run, shout forcefully, sustain prolonged effort, or use actions clearly dependent on breathing without first passing the `S.R.` of Tolerance. |
| **Severe** | Moderate, plus: if the `S.R.` of Tolerance is failed at the start of an activation, the target becomes Incapacitated. |

---

## Terrified

*Danger occupies the body before the will can argue.*

**Application:** A creature, Technique, scene revelation, hostile presence, grotesque display, contamination threat, or predator presence that creates an immediate terror line the body treats as urgent danger.

**Duration:** `while_condition_persists`

**Recovery:** Ends when the terror line is materially broken, disproved, eliminated, or ceases to be functionally relevant; or when the target passes a `S.R.` of Containment against the original severity to recover enough internal control.

| Severity | Effects |
| --- | --- |
| **Minor** | `A.R.`, `D.R.`, `C.R.`, and `S.R.` that directly oppose, approach, handle, or commit toward the feared source suffer a penalty equal to the rank bonus of the source that applied Terrified. |
| **Moderate** | Minor, plus: cannot voluntarily close distance to the feared source or deliberately commit against it without first passing a `S.R.` of Containment against the original severity. |
| **Severe** | Moderate, plus: to take any action, the target must first pass a `S.R.` of Containment against the original severity; if it fails, the action does not resolve. |
