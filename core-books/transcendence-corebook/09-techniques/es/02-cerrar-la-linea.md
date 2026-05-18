---
title: "Cerrar la Línea"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, spear, reactive, attack, naghii, line-control]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

### Reaccion - Ataque

# Cerrar la Línea

**Rango Novato**

*La punta llega donde el cruce tiene que pagarse.*

| Rango | Area | Duracion | Tirada |
| --- | --- | --- | --- |
| Arma | 1 criatura | Instantaneo | `A.R.` |

| Impacto | Ritmo | Desgaste |
| --- | --- | --- |
| `I.R.` | `4` | `1` |

## Requisitos

- Arma con perfil `Control de Linea`
- Un enemigo en movimiento entra en el rango de tu arma

## Keywords

- `Control de Linea`

## Efecto

Cuando un enemigo realiza cualquier accion que involucre movimiento y alcanza
una casilla dentro del rango de tu arma, antes de continuar esa accion haces
una `A.R.`. Si aciertas, resuelves `I.R.` normalmente y el enemigo debe
detener su movimiento en esa casilla. Si fallas, el enemigo continua su accion
normalmente.
