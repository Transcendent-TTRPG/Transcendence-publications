---
title: "La Presa del Oso"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, innate, species, ursari, active, attack, atrapado, garras, grapple, permanent, no-hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
  - core-books/transcendence-corebook/06-species/es/11-ursari.md
---

# La Presa del Oso

### Activo - Ataque

**Rango Novato**

*Una vez que las garras lo encuentran, soltar es una decisión suya, no de la presa.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Personal | 1 Criatura | Permanente | T.A. |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| T.R. (Alteraciones) | T.I. | `4` | `2` |

## Requisitos

- Especie: Ursari.

## Keywords

- `Ursari`
- `Garras`
- `Atrapado`
- `No Hereda Efectos`

## Efecto

Realiza una `T.A.` con tus garras contra un objetivo dentro de tu alcance cuerpo a cuerpo. Si impactas, resuelves el daño normalmente. 

Inmediatamente después, el objetivo debe realizar una `T.R.` (Alteraciones). Si falla, queda bajo el estado `Atrapado`, con una severidad que depende de tu Rango de Competencia en la habilidad base de tu ataque:

| Rango de Competencia | Severidad del Estado |
| :---: | :--- |
| **1 – 2 (Novato/Aprendiz)** | Leve |
| **3 – 4 (Competente/Diestro)** | Moderado |
| **5 – 6 (Experto/Maestro)** | Grave |

Mientras mantengas al objetivo `Atrapado`:
- En cada una de tus activaciones, puedes pagar **1 de Desgaste** adicional para aplicarle automáticamente el impacto de tus garras sin necesidad de realizar una nueva `T.A.`
- Tu movilidad se reduce a cero (no puedes desplazarte mientras mantienes el agarre).

El objetivo puede intentar liberarse durante su propia activación realizando una prueba enfrentada contra tu `T.C.` (Fuerza). Si tiene éxito, el agarre se rompe y el efecto termina. Por tu parte, si fallas voluntariamente esta prueba resistida o simplemente decides soltar a tu presa en cualquier momento, el efecto también termina de inmediato.
