---
title: "El rastro ofrecido"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, bufoni, unpredictability, reactive, utility, concealment, false-location]
authority_refs:
  - Transcendence-design/data/system/techniques.yaml
  - Transcendence-design/docs/system/technique-el-rastro-ofrecido.md
  - Transcendence-design/docs/system/cover-visibility-concealment.md
related:
  - core-books/transcendence-techniques/en/164-the-offered-trail.md
  - core-books/transcendence-corebook/06-species/es/14-bufoni.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/07-cobertura-visibilidad-y-ocultacion.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-acciones.md
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
---

# El rastro ofrecido

### Reactivo - Utilidad

**Rango Novato**

*Las garras encuentran hojas.*

| Rango | Área | Duración | Tirada |
| --- | --- | --- | --- |
| Alcance del arma | 1 Criatura | Instantáneo | `T.A.` |

| Salvación | Impacto | Ritmo | Desgaste |
| --- | --- | --- | --- |
| — | — | `2` | `1` |

## Requisitos

- Competencia Novato o superior con el arma utilizada.
- Arma con perfil Impredecible.
- Estar Oculto respecto al detector.

## Palabras clave

- Impredecible
- Oculto

## Efecto

Cuando un enemigo vaya a resolver un intento de localizarte, puedes declarar esta técnica antes de conocer el resultado de su Percepción.

Elige una posición falsa distinta de la que ocupas, donde tu arma pueda producir una señal físicamente plausible para el sentido que utiliza el detector. El alcance de tu arma limita el punto de la señal, no la distancia al detector; este debe poder percibirla según las reglas normales de detección.

Realiza una `T.A.` con tu arma de Impredecible, enfrentada a la `T.E.` de Percepción del detector. Utiliza ese mismo resultado de Percepción para resolver su intento habitual de localizarte frente al valor activo de tu estado Oculto. No vuelves a tirar ni reemplazas ese valor, y el detector no realiza una segunda Percepción por esta técnica.

Si su Percepción supera tu valor de Oculto, localiza tu posición real, aunque tu `T.A.` sea superior.

Si su Percepción no supera tu valor de Oculto y tu `T.A.` supera su Percepción, recibe como pista la posición falsa que elegiste, en lugar de la determinada mediante 1d8. Si tu `T.A.` no supera su Percepción, la posición falsa se determina por el procedimiento normal de Ocultación.

La criatura decide qué hacer con la pista. Esta técnica no la obliga a moverse ni atacar, no modifica tu valor de Oculto y no impide futuras búsquedas. No borra información obtenida por otros sentidos ni anula una detección automática.

Cada uso afecta un solo intento de localización de un detector. Solo puedes intentar esta técnica una vez contra ese intento. Los demás observadores resuelven su detección normalmente; la señal puede comprometer tu ocultamiento frente a ellos según las reglas habituales.

Esta técnica no inflige impacto ni aplica efectos de tu arma, no concede ventaja de apertura y no te protege de áreas que cubran tu posición real.

Pagas Ritmo y Desgaste aunque no consigas dirigir la pista.

## Ejemplo

Tu valor activo de Oculto es 12. Declaras un punto de señal válido antes de resolver la detección. Obtienes `T.A.` 14 y el enemigo Percepción 10: recibe como pista el punto que elegiste. Si su Percepción fuera 13, localizaría tu posición real, aunque tu `T.A.` siguiera siendo 14. Si obtuvieras `T.A.` 10 frente a Percepción 10, no dirigirías la pista: se resolvería la posición falsa mediante el procedimiento normal. En todos los casos pagas Ritmo 2 y Desgaste 1.
