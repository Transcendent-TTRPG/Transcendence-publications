---
title: "Cerrar el Flanco"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, intercepcion, reactive, defense, sauri, interception, escort]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

### Reactivo - Ataque

# Cerrar el Flanco

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

## Efecto

Cuando un enemigo dentro de tu alcance realiza un ataque físico contra ti o contra una criatura u objeto dentro de ese mismo alcance, puedes reemplazar tu propia `T.D.` o la del objetivo protegido contra ese ataque. Si el objetivo protegido es una criatura capaz de defenderse, debe aceptarlo antes de la tirada.

Realiza `T.A.` contra el atacante y compárala con su `T.A.`:

- **Si tu `T.A.` es igual o superior:** el ataque no alcanza al objetivo protegido, resuelves tu daño normalmente contra el atacante, y cualquier efecto secundario del ataque desencadenante no afecta al objetivo protegido salvo que una regla específica indique lo contrario.

- **Si tu `T.A.` es inferior:** el ataque resuelve contra el objetivo protegido como si su `T.D.` hubiera fallado. El objetivo no realiza una `T.D.` separada contra ese ataque.

Esta técnica no detiene el movimiento del enemigo ni aplica condiciones. No puede usarse contra ataques de área, efectos no físicos, ni líneas de ataque que no puedas percibir o alcanzar físicamente.