---
title: "El Ángulo Que Falla"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, desvio, attack, reactive, drakkai, natural_weapon, seguimiento, no-hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# El Ángulo Que Falla

### Reactivo - Ataque

**Rango Novato**

*El golpe encontró aire. La mandíbula encontró al golpe.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| T.D. | T.I. | `6` | `2` |

## Requisitos

- Perfil de arma: `Desvío`
- Una arma natural distinta disponible para el seguimiento

## Keywords

- `Desvío`
- `No Hereda Efectos`

## Efecto

Cuando un enemigo a tu alcance realice un ataque físico contra ti, te defiendes atacando. 

Realiza una `T.A. reactiva` (Desvío). El resultado reemplaza tu `T.D.` contra el ataque. 

Si tu `T.A.` iguala o supera a la del atacante, su ataque falla automáticamente y tú resuelves tu daño. Además, puedes realizar de inmediato una segunda `T.A.` usando una arma natural distinta a la que usaste para defenderte, sumando tu **rango de competencia** como bonificador a esta segunda tirada.

Si tu `T.A.` original es menor que la del atacante, recibes su ataque como si hubieras fallado tu Defensa normalmente.
