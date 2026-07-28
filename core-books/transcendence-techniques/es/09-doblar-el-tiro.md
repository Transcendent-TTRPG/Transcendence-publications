---
title: "Doblar el Tiro"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, ranged-weapons, active, attack, naghii, ricochet, geometry, hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Doblar el Tiro

### Activo - Ataque

**Rango Novato**

*El ángulo que no miran es el que cobra.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `T.D.` | `T.I.` | `4` | `1` |

## Requisitos

- Arma con perfil `Desvío`
- Superficie útil de rebote o desvío

## Keywords

- `Desvío`
- `Hereda Efectos`

## Efecto

Declara una línea indirecta usando superficies de rebote o desvío y realiza una `T.A.` a través de ella. Si aciertas, resuelves `T.I.` normalmente.

Debido a lo impredecible de la trayectoria, este ataque reduce tanto la `T.D.` como el `Bloqueo` del objetivo en un valor igual a tu rango de competencia. Además, el objetivo no puede beneficiarse de bonificadores por Cobertura direccional.

La técnica no atraviesa barreras selladas, no curva libremente en aire abierto y no busca objetivos cuya posición no puedas localizar de forma razonable.
