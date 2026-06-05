---
title: "Cerrar el Juicio"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, impacto, active, attack, sauri, break_validation, execution]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Cerrar el Juicio

### Activo - Ataque

**Rango Novato**

*La mandíbula cierra como veredicto — lo que no aguanta, cede.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `T.D.` | `T.I.` | `5` | `1` |

## Requisitos

- Perfil de arma: `Impacto`

## Keywords

- `Impacto`

## Efecto

Antes de tirar, declara un objetivo de ruptura que tu ataque pueda alcanzar: arma, escudo, pieza de armadura, objeto portado, ataque natural expuesto, extremidad, mandíbula, cuerno, borde de caparazón, u otro punto del cuerpo establecido.

Realiza un ataque con perfil `Impacto` contra ese objetivo. Si el ataque impacta, resuelve el daño normalmente.

Para este ataque, el resultado de `T.I.` necesario para validar una ruptura se reduce en 1 por cada rango de competencia:

| Rango de competencia | Reducción |
| --- | ---: |
| Novato | 1 |
| Adepto | 2 |
| Experto | 3 |
| Maestro | 4 |
| Consumado | 5 |
| Trascendente | 6 |

Si la `T.I.` cae dentro del rango, resuelve la validación de ruptura con la fórmula habitual: `Potencia Crítica > Durabilidad del objetivo`.

Esta técnica no aumenta la Potencia; solo amplía los resultados de `T.I.` que permiten intentar la ruptura.
