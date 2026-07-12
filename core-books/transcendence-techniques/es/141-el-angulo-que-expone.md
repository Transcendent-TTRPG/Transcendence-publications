---
title: "El Ángulo Que Expone"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, deflection, long-blades, short-blades, reactive, defense, vesper, deflect-and-window, attack-penalty]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-techniques/es/137-la-brecha-sin-ruido.md
---

# El Ángulo Que Expone

### Reactivo - Defensa

**Rango Novato**

*No paró el golpe. Usó el golpe.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | Individual | Permanente | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | T.I. | `5` | `2` |

## Requisitos

- Competencia de arma con acceso al perfil `Desvío`
- El agresor está dentro del alcance del arma del usuario

## Keywords

- `Desvío`
- `Hereda Efectos`

## Efecto

Cuando un enemigo declara un ataque físico contra el usuario, declara esta técnica antes de que el ataque resuelva. Realiza una T.A. reactiva con tu perfil de Desvío contra el agresor. Esta T.A. reemplaza tu T.D. contra ese ataque.

Compara tu T.A. con la T.A. del agresor:

- **Si tu T.A. es igual o mayor:** el ataque falla. Resuelve tu T.I. normalmente contra el agresor. Además, la próxima T.A. del agresor contra el usuario recibe una penalización igual a tu rango de competencia en la superficie de Desvío usada. Este efecto es `Permanente` hasta que el agresor realice su próxima T.A. contra el usuario, o hasta que el encuentro termine.

- **Si tu T.A. es menor:** el desvío falla. El ataque resuelve como si tu T.D. hubiera fallado.

Esta técnica no produce un segundo ataque adicional. La penalización no se acumula — si existe una penalización mayor, aplica la mayor.
