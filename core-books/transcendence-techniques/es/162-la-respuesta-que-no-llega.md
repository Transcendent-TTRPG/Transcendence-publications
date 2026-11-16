---
title: "La respuesta que no llega"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, bufoni, interrupcion, reactive, utility, entorpecido, reaction-cancel]
authority_refs:
  - Transcendence-design/data/system/techniques.yaml
  - Transcendence-design/docs/system/technique-la-respuesta-que-no-llega.md
related:
  - core-books/transcendence-techniques/en/162-the-response-that-never-comes.md
  - core-books/transcendence-corebook/06-species/es/14-bufoni.md
  - core-books/transcendence-corebook/11-ailments/es/04-venenos.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-acciones.md
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
---

# La respuesta que no llega

### Reactivo - Utilidad

**Rango Novato**

*La mano todavía intenta llegar.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | `4` | `1` |

## Requisitos

- Competencia Novato o superior con el arma utilizada.
- Arma con perfil `Interrupción`.
- El objetivo debe tener activo el Veneno `Entorpecido`, de severidad Leve, Moderada o Grave. No es necesario que tú lo hayas aplicado.

## Palabras clave

- `Interrupción`
- `Entorpecido`

## Efecto

Cuando un objetivo dentro del alcance de tu arma declare una `Reacción` que incluya un ataque físico o un desplazamiento, puedes declarar esta técnica antes de que esa Reacción comience a resolverse. Realiza una `T.A.` con tu arma, enfrentada a la `T.D.` del objetivo. Puedes intervenir aunque su Reacción responda a la acción de otra criatura.

Si tu `T.A.` supera su `T.D.`, cancelas esa Reacción completa. El objetivo conserva los costes de Ritmo y Desgaste correspondientes a la Reacción cancelada. Si no superas su `T.D.`, la Reacción se resuelve normalmente. Esta técnica no inflige daño, no aplica el efecto del arma ni modifica Entorpecido.

Solo puedes intentar esta técnica una vez contra cada Reacción declarada. No puedes utilizarla contra una ejecución de esta misma técnica, contra una Acción Activa ni contra una `T.D.` ordinaria.

## Ejemplo

Un enemigo con Entorpecido Leve declara una Reacción de ataque contra tu compañero. Está dentro del alcance de tu arma con Interrupción. Declaras esta técnica antes de que resuelva su Reacción. Tu `T.A.` obtiene 12 y su `T.D.` obtiene 10: su Reacción se cancela, conserva sus costes y no recibe daño de esta técnica. Si ambas tiradas obtuvieran 10, su Reacción continuaría normalmente.

Entorpecido es el Veneno definido en el capítulo 11, **Venenos**. Otros agravios, heridas o Fatiga no sustituyen este requisito.
