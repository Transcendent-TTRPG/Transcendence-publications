---
title: "Cerrar el Flanco"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, intercepcion, reactive, defense, sauri, interception, escort, hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Cerrar el Flanco

### Reactivo - Ataque

**Rango Novato**

*El flanco que el enemigo creyó abierto ya tenía la cola cruzándolo.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `—` | `T.I.` | `6` | `2` |

## Requisitos

- Perfil: `Intercepción`

## Keywords

- `Intercepción`
- `Hereda Efectos`

## Efecto

Cuando un enemigo dentro del alcance de tu arma ataca físicamente a un aliado o a ti mismo, puedes sustituir la `T.D.` del objetivo por una `T.A.` tuya contra el agresor (un aliado debe aceptar tu intervención).

- **Si tu `T.A.` es igual o mayor:** Bloqueas el ataque por completo y resuelves tu `T.I.` contra el agresor.
- **Si tu `T.A.` es menor:** El ataque enemigo impacta automáticamente a su objetivo original, sin posibilidad de otra `T.D.`

Solo aplica contra ataques físicos directos de un solo objetivo que puedas percibir y alcanzar físicamente.
