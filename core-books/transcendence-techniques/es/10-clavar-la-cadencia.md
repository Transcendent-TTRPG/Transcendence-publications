---
title: "Clavar la Cadencia"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, ranged-weapons, reactive, attack, naghii, volley, movement-control, hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
---

# Clavar la Cadencia

### Reacción - Ataque

**Rango Novato**

*No hace falta detener el avance; basta con romperle el ritmo.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| `T.D.` | `T.I.` | `4` | `1` |

## Requisitos

- Arma con perfil `Cadencia`
- Una criatura dentro de tu línea de tiro declara o inicia un movimiento

## Keywords

- `Cadencia`
- `Hereda Efectos`

## Efecto

Cuando una criatura dentro de tu línea de tiro declara o inicia un desplazamiento, puedes interrumpirlo para realizar una `T.A.`.

Si aciertas, resuelves `T.I.` normalmente. El fuego de supresión rompe la inercia del objetivo: la distancia total que puede recorrer con este desplazamiento se reduce a la mitad.

Además, si el objetivo decide continuar moviéndose bajo este fuego de supresión, debe pagar un costo de Ritmo adicional. Este sobrecargo aumenta según tu rango de competencia:

- Rangos 1-2: `+1` Ritmo
- Rangos 3-4: `+2` Ritmo
- Rangos 5-6: `+3` Ritmo

Si el objetivo no puede o no quiere pagar el costo adicional, su acción de movimiento termina inmediatamente en la casilla donde recibió el impacto. Si fallas la `T.A.`, el desplazamiento del objetivo continúa normalmente.
