---
title: "Trabar el Gesto"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, flexible-weapons, reactive, attack, naghii, interruption, counter]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Trabar el Gesto

### Reacción - Ataque

**Rango Novato**

*El ataque abre lo mismo que promete cerrar.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `T.R. (Alteraciones)` | `T.I.` | `5` | `1` |

## Requisitos

- Arma con perfil `Interrupción`
- Ser el objetivo declarado del ataque y que el atacante este dentro de tu rango.

## Keywords

- `Interrupción`

## Efecto

Sustituye tu `T.D.` normal por una `T.A.` contra el atacante.

Si tu `T.A.` supera la del atacante, no recibes daño del ataque y resuelves `T.I.` normalmente contra el atacante. El atacante realiza entonces una `T.R.` de Resistencia a las Alteraciones. La severidad se determina según tu rango:

- Rangos 1-2: Menor
- Rangos 3-4: Moderado
- Rangos 5-6: Grave

Si falla la `T.R.`, el atacante queda `Impedido` a esa severidad. Si supera la `T.R.`, `Impedido` no se aplica.

Si tu `T.A.` no supera la del atacante, el contraataque falla y el ataque se resuelve normalmente contra ti.
