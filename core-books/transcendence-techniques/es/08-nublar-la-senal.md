---
title: "Nublar la Señal"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, ranged-weapons, active, utility, naghii, corrosion, residue]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Nublar la Señal

### Activo - Utilidad

**Rango Novato**

*No hace falta cegar: basta ensuciar el canal que decide.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Arma | 1 Criatura | Permanente | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `T.D.` | `—` | `4` | `2` |

## Requisitos

- Arma con perfil `Corrosión`
- `Kit de Munición`
- Canal sensorial identificado

## Keywords

- `Corrosión`
- `Kit de Munición`

## Efecto

Declara un canal sensorial o punto de lectura expuesto del objetivo. Realiza una `T.A.` con `-2` contra su `T.D.` para fijar el residuo en ese punto.

Si no superas su `T.D.`, el residuo no se aplica.

Si la técnica resuelve con éxito, el residuo nubla ese canal. Mientras permanezca, el objetivo pierde cualquier ventaja sensorial que dependa exclusivamente de ese canal y sufre una **Alteración** basada en el canal obstruido:

- **Vista:** `Cegado`
- **Oído:** `Ensordecido`
- **Olfato, tacto u otros canales:** `Desorientado`

La severidad de la alteración es igual a tu Rango de competencia (1-2: Leve, 3-4: Moderado, 5-6: Grave).

El objetivo puede gastar la acción `Interactuar` para limpiar el residuo y eliminar la alteración asociada. El residuo también desaparece si una condición ambiental apropiada lo lava o remueve.
