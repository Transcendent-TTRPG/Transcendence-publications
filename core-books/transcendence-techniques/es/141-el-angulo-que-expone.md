---
title: "El Ángulo Que Expone"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, deflection, long-blades, short-blades, reactive, defense, vesper, deflect-and-window, attack-penalty]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-techniques/es/137-la-brecha-sin-ruido.md
---

# El Ángulo Que Expone

### Reactivo - Defensa

**Rango Novato**

*No paró el golpe. Usó el golpe.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | Individual | Permanente | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | T.I. | `5` | `2` |

## Requisitos

- Competencia de arma con acceso al perfil `Desvío`
- El agresor está dentro del alcance del arma del usuario

## Keywords

- `Desvío`
- `Hereda Efectos`

## Efecto

Cuando un enemigo declare un ataque físico contra ti, puedes declarar esta técnica. Realiza una `T.A.` reactiva con tu perfil de `Desvío` contra el agresor. Esta tirada reemplaza tu `T.D.` para este ataque.

Compara tu `T.A.` contra la `T.A.` del agresor:

- **Si tu T.A. es Igual o Mayor:** El ataque enemigo falla. Resuelves tu `T.I.` normalmente contra el agresor. Además, la próxima `T.A.` que ese agresor intente realizar contra ti sufre una penalización igual a tu rango en `Desvío`. Este efecto es Permanente hasta aplicarse.
- **Si tu T.A. es Menor:** El desvío fracasa y recibes el ataque como si tu `T.D.` hubiera fallado.

La penalización a la `T.A.` enemiga no se acumula.
