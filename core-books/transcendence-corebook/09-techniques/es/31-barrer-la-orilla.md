---
title: "Barrer la Orilla"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, impacto, active, attack, sauri, desequilibrado, disruption]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Barrer la Orilla

### Activo - Ataque

**Rango Novato**

*El cuerpo recordó demasiado tarde que estaba parado en la orilla.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `T.R.` (Alteraciones) | `T.I.` | `5` | `2` |

## Requisitos

- Perfil de arma: `Impacto`

## Keywords

- `Impacto`

## Efecto

Realiza un ataque con perfil `Impacto` contra el objetivo. Si el ataque impacta, resuelve el daño normalmente.

Tras resolver el daño, el objetivo realiza una `T.R. (Alteraciones)` contra `Desequilibrado`. La severidad depende de tu rango de competencia:

| Rango de competencia | Severidad |
| --- | ---: |
| Novato | Menor |
| Adepto | Menor |
| Experto | Moderado |
| Maestro | Moderado |
| Consumado | Severo |
| Trascendente | Severo |

Si falla la `T.R.`, el objetivo gana `Desequilibrado` a esa severidad. Si tiene éxito, `Desequilibrado` no se aplica, pero el daño del ataque resuelve igualmente si el golpe impactó.
