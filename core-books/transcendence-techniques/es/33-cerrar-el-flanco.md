---
title: "Cerrar el Flanco"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, intercepcion, reactive, defense, sauri, interception, escort, hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Cerrar el Flanco

### Reactivo - Ataque

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
- `Hereda Efectos`

## Efecto

Cuando un enemigo ataque físicamente a un aliado (que acepte tu intervención) o a ti mismo dentro del alcance de tu arma, sustituye la `T.D.` del objetivo original por tu propia `T.A.` contra el atacante.

- **Éxito (T.A. igual o mayor):** Bloqueas su ataque por completo y resuelves inmediatamente tu `T.I.` contra el atacante.
- **Fallo:** Su ataque impacta automáticamente al objetivo original.
