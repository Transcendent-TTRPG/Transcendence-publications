---
title: "La Base Que Falta"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, interrupcion, attack, reactive, drakkai, desequilibrado, alteracion, hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# La Base Que Falta

### Reactivo - Ataque

**Rango Novato**

*Cuando el pie busca apoyo, la garra ya lo está esperando.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| T.R. (Alteraciones) | T.I. | `6` | `2` |

## Requisitos

- Perfil de arma: `Interrupción`

## Keywords

- `Interrupción`
- `Desequilibrado`
- `Hereda Efectos`

## Efecto

Cuando un enemigo a tu alcance inicie una acción de ataque contra ti, te adelantas. 

Realiza una `T.A. reactiva` (Interrupción). El resultado reemplaza a tu `T.D.` contra ese ataque. 

Si tu `T.A.` iguala o supera a la del atacante, su acción falla antes de resolverse y tú conectas tu daño normalmente. Además, lo fuerzas a realizar una `T.R. (Alteraciones)` para resistir el estado `Desequilibrado`. 

| Rango de competencia | Severidad |
| --- | --- |
| 1 a 2 | Leve |
| 3 a 4 | Moderado |
| 5 a 6 | Grave |

Si su tirada falla, sufre el estado `Desequilibrado` con la severidad indicada. 

Si tu `T.A.` original es menor que la suya, recibes su ataque como si hubieras fallado tu Defensa normalmente.
