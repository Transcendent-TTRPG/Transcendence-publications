---
title: "Agravios"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 11
status: draft
canonical: false
tags: [ailments, agravios, alteraciones, aflicciones, venenos, infecciones, maldiciones, conditions, severity]
related:
  - core-books/transcendence-corebook/11-ailments/en/01-ailments.md
  - core-books/transcendence-corebook/11-ailments/es/02-alteraciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/02-desgaste-aguante-fatiga.md
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Agravios

Un **Agravio** es una condición perjudicial que se asienta sobre una criatura y altera la forma en que puede actuar, percibir, resistir o mantenerse funcional.

Los Agravios no describen simples molestias pasajeras. Representan estados que ya lograron imponerse sobre el cuerpo o la mente de una criatura. 

Mientras un Agravio permanezca activo, la criatura afectada debe tratar con sus consecuencias hasta que el estado se elimine, se alivie o termine por sus propias condiciones.

La fuente de un Agravio puede variar: una criatura, un arma, un veneno, una exposición prolongada, una escena peligrosa, un objeto, un lugar o una causa extranatural. Lo que define al Agravio no es de dónde viene, sino **qué tipo de daño funcional deja una vez existe sobre el objetivo**.

---

## Familias de Agravios

Cada Agravio pertenece a una familia. La familia indica qué parte de la criatura o de su relación con el mundo está siendo comprometida.

| Familia | Qué compromete |
| --- | --- |
| **Alteraciones** | El funcionamiento físico inmediato del cuerpo |
| **Aflicciones** | La mente, la percepción, la estabilidad interna o la relación con lo real |
| **Venenos** | El organismo mediante una sustancia tóxica introducida por una vía de administración |
| **Infecciones** | El cuerpo mediante agentes biológicos, contaminantes o procesos persistentes que pueden progresar o propagarse |
| **Maldiciones** | La exposición constante a fuentes extranaturales |

---

Las familias determinan qué tipo de resistencia se usa, qué clase de recuperación tiene sentido y cómo debe describirse el estado en la ficción.

## Severidad

Todos los Agravios usan tres niveles de severidad:

- **Leve**
- **Moderado**
- **Grave**

La severidad indica cuánto se ha asentado el Agravio y cuánta presión ejerce sobre la criatura afectada.

La estructura de tres niveles es común a todas las familias, pero cada Agravio define qué significa esa severidad en su propio caso. En algunos Agravios, una severidad mayor aumenta una penalización. En otros, activa restricciones adicionales o vuelve más difícil eliminar el estado.

La severidad no debe leerse siempre como “más número”. A veces significa que el Agravio es más profundo, más estable, más difícil de limpiar o más peligroso si se ignora.

### Umbrales de aplicación por defecto

Salvo que la entrada del Agravio indique otra cosa, los umbrales para aplicar o escalar un Agravio por severidad son:

| Severidad | Umbral base |
| --- | --- |
| Leve | `8 + NR` |
| Moderado | `13 + NR` |
| Grave | `17 + NR` |

Estos umbrales funcionan como referencia común. Técnicas, criaturas, escenas o Agravios específicos pueden reemplazarlos si su entrada lo indica.

### Penalizaciones numéricas y severidad

Cuando el efecto principal de un Agravio es una **penalización numérica**, esa penalización normalmente proviene del **bonificador de rango de la fuente** que lo aplicó, no de la severidad por sí misma.

En esos casos, la severidad determina otros aspectos del estado: qué restricciones adicionales aparecen, cuánto cuesta eliminarlo, qué tan difícil es resistirlo o cuánto persiste bajo presión.

Los Agravios estructurales — como ceguera, parálisis, derribo o inmovilización completa — usan la severidad principalmente para medir presión de aplicación, dificultad de recuperación y persistencia. No todos necesitan escalar mediante penalizaciones numéricas.

---

## Duración

Los Agravios no se miden por rondas. En lugar de eso, usan modelos de duración ligados a la ficción, la fuente que los sostiene o la forma en que pueden eliminarse.

| Modelo | Significado |
| --- | --- |
| `hasta_eliminar` | Persiste hasta que una acción, tratamiento, técnica o condición específica lo elimina |
| `hasta_desencadenante` | Termina cuando ocurre el desencadenante indicado por el Agravio |
| `mientras_persista_la_condición` | Persiste mientras la condición ficticia que lo justifica siga presente |

La **duración** indica cuánto tiempo puede permanecer el Agravio.  
La **recuperación** indica qué debe hacerse para eliminarlo, aliviarlo o impedir que escale.

Son dos cosas distintas. Un Agravio puede durar hasta ser eliminado, pero requerir una acción específica para limpiarlo. Otro puede terminar con la escena, aunque no haya sido tratado directamente.

---

## Regla de condición más fuerte

Los Agravios siguen la regla de **condición más fuerte**.

Cuando una criatura recibe varias aplicaciones del mismo Agravio o de un efecto equivalente:

- los efectos iguales no se apilan en paralelo;
- una aplicación más fuerte reemplaza a una más débil;
- una aplicación igual puede refrescar, reiniciar o extender la existente si su duración es mayor o si resulta más difícil de eliminar.

---

## Fórmulas de Tirada de Resistencia

Cada familia de Agravio indica qué tipo de resistencia se usa para impedir sus efectos.

Una `T.R.` combina tres elementos:

1. una **característica base**, que representa qué parte de la criatura responde al peligro;
2. el **nivel de competencia en la Resistencia correspondiente**, que representa experiencia acumulada frente a ese tipo de Agravio;
3. cualquier **bonificador adicional** otorgado por técnicas, equipo, preparación, condiciones de escena u otras reglas.

| Familia | Fórmula de `T.R.` |
| --- | --- |
| Alteraciones | `1d10 + Resiliencia + nivel de competencia en Resistencia a Alteraciones + bonificadores adicionales` |
| Aflicciones | `1d10 + Compostura + nivel de competencia en Resistencia a Aflicciones + bonificadores adicionales` |
| Maldiciones | `1d10 + Compostura + nivel de competencia en Resistencia a Maldiciones + bonificadores adicionales` |
| Venenos | `1d10 + Tenacidad + nivel de competencia en Resistencia a Venenos + bonificadores adicionales` |
| Infecciones | `1d10 + Tenacidad + nivel de competencia en Resistencia a Infecciones + bonificadores adicionales` |

---
