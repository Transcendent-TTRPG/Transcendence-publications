---
title: "Cerrar el Juicio"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, impacto, active, attack, sauri, break_validation, execution, hereda-efectos]
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
- `Hereda Efectos`

## Efecto

Antes de tirar, declara un objetivo de ruptura que tu ataque pueda alcanzar (arma, escudo, pieza de armadura, objeto portado, extremidad, mandíbula, cuerno, u otro punto establecido del cuerpo).

Realiza un ataque con perfil `Impacto` contra tu objetivo. Si aciertas, resuelves el daño normalmente.

Para este ataque, el resultado de `T.I.` necesario para validar una ruptura se reduce en un valor igual a tu rango de competencia.

Si logras que la `T.I.` caiga dentro del rango, resuelves la validación de ruptura con la fórmula habitual: `Potencia Crítica > Durabilidad del objetivo`.

Esta técnica no aumenta tu Potencia Crítica; solo amplía los resultados de `T.I.` que te permiten intentar la ruptura.
