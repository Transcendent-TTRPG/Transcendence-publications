---
title: "Señal Química"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, innate, species, formix, active, utility, detection, chemical, tracking]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
  - core-books/transcendence-corebook/06-species/es/06-formix.md
---

# Señal Química

### Activo - Utilidad

**Rango Novato**

*Las antenas no preguntan. Distinguen.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Personal | Circular 10 m | Permanente | T.C. (Astucia) |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | `3` | `2` |

## Requisitos

- Especie: Formix.

## Keywords

- `Formix`
- `Detección`
- `Oculto`

## Efecto

Realiza una T.C. (Astucia) contra un umbral fijado por la saturación química del entorno:

| Condición del entorno | Dificultad | Umbral |
| --- | --- | --- |
| Neutro o limpio | Fundamentos | 5 + NR |
| Actividad química moderada (rastros de veneno, fuego reciente, materiales fuertes) | Desafiante | 8 + NR |
| Contaminación significativa (ácido activo, humo denso, veneno en el aire) | Rigurosa | 11 + NR |
| Saturación extrema (batalla química activa, área inundada de ácido o gas) | Exigente | 14 + NR |

Con éxito, el Formix enfoca su lectura química sobre el entorno inmediato y distingue lo siguiente dentro del área:

- **Criaturas vivas** — posición por firma metabólica, independientemente de visibilidad, cobertura o estado Oculto. Las criaturas dentro del área no pueden establecer ni mantener el estado Oculto contra el Formix.
- **Rastros recientes** — criaturas que pasaron por el área recientemente dejaron señal química detectable aunque ya no estén presentes. El Formix sabe por dónde se movieron.
- **Sustancias peligrosas** — venenos activos, ácidos, gases y otros agentes químicos; detecta su presencia y ubicación aproximada aunque no tengan fuente visible.

El estado termina si el Formix queda Inconsciente, si la saturación química del entorno sube al punto de hacer la tirada fallida, o si lo finaliza voluntariamente.