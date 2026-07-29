---
title: "Cierre en el Umbral"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, intercepcion, defense, reactive, drakkai, impedido, alteracion, no-hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Cierre en el Umbral

### Reactivo - Ataque

**Rango Novato**

*Cuando el brazo llegó, ya lo estaba esperando.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| T.R. (Alteraciones) | — | `5` | `2` |

## Requisitos

- Perfil de arma: `Intercepción`

## Keywords

- `Intercepción`
- `Impedido`
- `No Hereda Efectos`

## Efecto

Cuando un enemigo a tu alcance realice un ataque físico contra ti, te defiendes atacando. 

Realiza una `T.A. reactiva` (Intercepción). El resultado de esta tirada reemplaza a tu `T.D.` contra el ataque. 

Si tu `T.A.` iguala o supera a la del atacante, su ataque falla automáticamente y lo fuerzas a realizar una `T.R. (Alteraciones)` para resistir el estado `Impedido`. 

| Rango de competencia | Severidad |
| --- | --- |
| 1 a 2 | Leve |
| 3 a 4 | Moderado |
| 5 a 6 | Grave |

Si su tirada falla, sufre el estado `Impedido` con la severidad indicada. 

Si tu `T.A.` es menor que la suya, recibes el ataque como si hubieras fallado tu Defensa normalmente.
