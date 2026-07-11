---
title: "Guardar el Pulso"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, tolerancia, reactive, utility, sauri, mitigation, survival_window, exploration]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Guardar el Pulso

### Reactivo - Utilidad

**Rango Novato**

*La vasija lleva lo que no puede derramarse, aunque ya esté resquebrajada.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Personal | Tú | Instantáneo | `T.E. (Tolerancia)` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `—` | `—` | `0` | `1+` |

## Requisitos

- Especialización: `Tolerancia`

## Keywords

- `Tolerancia`

## Efecto

Cuando estás a punto de resolver una acción física, mantener una tarea sostenida o completar un tramo de exploración mientras ya sufres un estado físico que penalizaría o interrumpiría esa función, activa esta técnica sin coste de Ritmo.

Paga el Desgaste base de `1` y realiza `T.E. (Tolerancia)` contra la dificultad correspondiente a la severidad de la Alteración que intentas superar:

| Severidad | Dificultad |
| --- | --- |
| Leve | Fundamental |
| Moderada | Desafiante |
| Grave | Rigurosa |

Si fallas, el Desgaste se pierde y el efecto no se produce. Si tienes éxito, elige un estado físico concreto que ya te afecta. Antes de resolver, puedes pagar Desgaste adicional — hasta un máximo igual a tu rango de Tolerancia. Cada punto de Desgaste adicional aumenta la mitigación en `1`, en proporción estricta de `1:1`.

Para esta resolución, elige uno de los siguientes efectos:

- **Reducir severidad:** si el estado usa pasos de severidad, reduce esa severidad en `1` más el Desgaste adicional pagado, hasta un mínimo de ninguno.
- **Ignorar penalización:** si el estado no usa pasos de severidad, ignora hasta `1` más el Desgaste adicional pagado puntos de su penalización concreta para esta resolución.
- **Prevenir interrupción:** impide que ese estado interrumpa una acción física ya declarada, siempre que la acción siga siendo físicamente posible.
- **Mantener tarea sostenida:** mantén una función continua hasta tu próxima activación — cargar un cuerpo, sujetar una compuerta, conservar el agarre, permanecer en pie, o completar un tramo corto de movimiento forzado.

Esta técnica aplica únicamente a Alteraciones.

Esta técnica no elimina el estado. Cuando la función preservada resuelve, todas las heridas, Fatiga, Aflicciones, penalizaciones y consecuencias continúan normalmente.
