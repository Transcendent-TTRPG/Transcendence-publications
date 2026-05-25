---
title: "Desgaste, Aguante y Fatiga"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [attrition, endurance, fatigue, combat, strain, fatigue-thresholds]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-attrition-endurance-fatigue.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/04-descanso.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-acciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/05-heridas-y-dano.md
  - core-books/transcendence-corebook/04-skills-and-proficiencies/es/01-especializaciones.md
authority_refs:
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/docs/system/mechanics-overview.md
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/data/system/attrition-fatigue.yaml
  - Transcendence-design/data/system/specializations.yaml
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
  - heading: "Ejemplo de umbrales"
    writing_mode: example
---

# Desgaste, Aguante y Fatiga

El combate y las escenas de alta presión no solo amenazan la vida de un personaje. También desgastan su cuerpo, su mente y su compostura.

Este sistema usa tres valores:

| Valor | Qué representa |
| --- | --- |
| **Desgaste** | La carga acumulada por actuar bajo presión |
| **Aguante** | Cuánto Desgaste puede sostener el personaje antes de deteriorarse |
| **Fatiga** | El deterioro que aparece cuando el Desgaste supera el Aguante |

El Desgaste no reemplaza al daño. Tampoco reemplaza el orden de activación. Registra cuánto esfuerzo puede seguir sosteniendo un personaje antes de que su rendimiento empiece a quebrarse.

---

## Desgaste

El **Desgaste** es la carga acumulada que un personaje soporta al ejecutar acciones significativas en una escena hostil o de alta tensión.

No representa daño físico directo. También incluye esfuerzo corporal, concentración, lectura táctica, control emocional y respuesta inmediata al peligro.

Un personaje puede acumular Desgaste por:

- atacar, defenderse o moverse en combate
- reaccionar a amenazas repentinas
- sostener una maniobra exigente
- analizar una criatura bajo presión
- imponer presión mental o social en una escena conflictiva
- actuar mientras sufre condiciones adversas o presión ambiental

No toda acción genera Desgaste. Solo lo hacen aquellas que exigen esfuerzo real y tienen peso dentro de la escena.

---

## Costos de Desgaste

Las acciones usan una escala simple de costos.

| Costo | Tipo de acción |
| ---: | --- |
| 0 | Acción sin exigencia real |
| 1 | Acción significativa estándar |
| 2 | Acción de alta exigencia |
| 3 | Acción extrema o de sobreextensión |

---

### 0 Desgaste

Acciones triviales o puramente narrativas que no exigen esfuerzo real dentro de la escena.

Ejemplos:

- una observación evidente
- una frase breve sin peso táctico
- una acción menor sin amenaza inmediata

---

### 1 Desgaste

Acciones significativas normales.

Ejemplos:

- un ataque estándar
- una defensa sencilla
- un desplazamiento importante bajo presión
- una observación activa del enemigo
- una lectura básica del comportamiento de una criatura

---

### 2 Desgaste

Acciones de alta exigencia.

Ejemplos:

- interceptar una carga
- proteger a otro personaje absorbiendo presión
- analizar en profundidad a un enemigo durante el combate
- ejecutar una maniobra que altere el ritmo de la escena
- usar una acción mental o social que quite una ventaja importante

---

### 3 Desgaste

Acciones extremas o de sobreextensión.

Ejemplos:

- un esfuerzo límite cuando el personaje ya está muy presionado
- una intervención heroica por encima del margen seguro
- una maniobra especialmente exigente que fuerza al personaje más allá de su ritmo normal

---

## Acciones físicas, mentales y sociales

El Desgaste no depende del tipo de característica usada. Depende de la exigencia real de la acción.

Una acción mental o social puede generar Desgaste si:

- exige foco real bajo amenaza
- altera la situación táctica
- compite con otras acciones importantes del combate
- obliga al personaje a sostener lectura, control o presión en medio del caos

No toda acción mental o social genera Desgaste. Lo generan aquellas que aportan una ventaja real o imponen una carga significativa bajo presión.

Leer a una criatura, quebrar su patrón, forzar una reacción o desestabilizar su conducta puede costar tanto como atacar o defenderse, si la situación lo justifica.

---

## Reacciones y Desgaste

Las Reacciones no son costosas por ser Reacciones. Son costosas por la exigencia que implican.

Responder fuera del ritmo natural del personaje suele requerir precisión, tensión y rapidez. Por eso una Reacción puede costar más o menos Desgaste según la dificultad de ejecutarla.

| Tipo de Reacción | Desgaste sugerido |
| --- | ---: |
| Reacción simple | 1 |
| Reacción exigente | 2 |
| Reacción límite | 3 |

Lo importante no es la categoría de la acción, sino su intensidad dentro de la escena.

---

## Aguante

El **Aguante** representa cuánta carga acumulada puede sostener un personaje antes de empezar a sufrir Fatiga.

Todo personaje posee una reserva mínima de funcionamiento. Esa reserva cubre tres planos del conflicto:

- el **cuerpo**, que sostiene esfuerzo, impacto y movimiento
- la **mente**, que sostiene atención, lectura e interpretación
- la **compostura**, que sostiene control, intención y claridad bajo tensión

Todo personaje cuenta con una reserva base de Aguante de `3`. A esa base se suma la resistencia corporal final del personaje, expresada en su Tenacidad.

```text
Aguante = 3 + (Tenacidad × 2)
```

La Tenacidad usada en esta fórmula es la Tenacidad final del personaje, después de aplicar especie y Sinapsis.

Todo personaje comienza con una especialización inicial de Tenacidad en nivel 1, rango Novato: **Marcha**, **Aclimatación** o **Tolerancia**. Esa especialización ya está incluida indirectamente en el Aguante porque aumenta Tenacidad mediante Sinapsis durante la creación.

---

## Ejemplo

Un personaje termina la creación con Tenacidad `2`.

```text
Aguante = 3 + (2 × 2)
Aguante = 7
```

Ese personaje tiene Aguante `7`.

---

## Fatiga

La **Fatiga** es el deterioro progresivo que aparece cuando el personaje acumula más Desgaste del que puede sostener.

No surge por una sola acción aislada. Surge por acumulación.

A medida que el Desgaste aumenta, al personaje le cuesta más mantener precisión, sostener el ritmo, conservar claridad o responder con firmeza.

La Fatiga puede reflejar:

- saturación corporal
- sobrecarga mental
- pérdida de compostura
- dificultad para sostener el mismo rendimiento
- deterioro general después de una escena exigente

---

## Fatiga proyectada y Fatiga asentada

La Fatiga se maneja en dos momentos: mientras la escena sigue activa y cuando la escena termina.

---

### Fatiga proyectada

Durante una escena hostil, el personaje registra el Desgaste acumulado y calcula qué nivel de Fatiga tendría si la escena terminara en ese momento.

Esa Fatiga todavía está **proyectada**.

Esto significa que el personaje está forzando su margen, pero la penalización completa no se asienta mientras la adrenalina, la urgencia o el peligro inmediato sigan sosteniendo su rendimiento.

Durante el combate, la Fatiga se proyecta.

---

### Fatiga asentada

Cuando la escena hostil termina o desciende claramente de intensidad, la Fatiga proyectada se convierte en Fatiga real.

En ese momento:

1. Revisa el Desgaste acumulado.
2. Determina el nivel de Fatiga alcanzado.
3. Aplica ese nivel como Fatiga asentada.
4. Elimina el Desgaste acumulado de esa escena, salvo que una regla específica indique lo contrario.

Al terminar el combate, la Fatiga se asienta.

---

## Umbrales de Fatiga

La Fatiga se determina comparando el Desgaste acumulado con el Aguante del personaje.

| Nivel | Condición |
| --- | --- |
| Fatiga 0 | El Desgaste es menor que el Aguante |
| Fatiga 1 | El Desgaste es igual o mayor al Aguante |
| Fatiga 2 | El Desgaste es igual o mayor a 2 × Aguante |
| Fatiga 3 | El Desgaste es igual o mayor a 3 × Aguante |
| Fatiga 4 | El Desgaste es igual o mayor a 4 × Aguante |
| Fatiga 5 | El Desgaste es igual o mayor a 5 × Aguante |

La escala base no supera Fatiga 5.

Si una mecánica vuelve a añadir Fatiga cuando el personaje ya está en Fatiga 5, el personaje queda **Incapacitado por agotamiento**.

---

## Ejemplo de umbrales

Si un personaje tiene Aguante `7`:

| Desgaste acumulado | Fatiga proyectada o asentada |
| ---: | ---: |
| 0–6 | Fatiga 0 |
| 7–13 | Fatiga 1 |
| 14–20 | Fatiga 2 |
| 21–27 | Fatiga 3 |
| 28–34 | Fatiga 4 |
| 35 o más | Fatiga 5 |

Fatiga 5 no es un margen táctico que pueda sostenerse voluntariamente. Es el último punto antes del colapso operativo.

---

## Efectos de Fatiga

Los efectos de Fatiga son **acumulativos**. Llegar a Fatiga 3 significa que el personaje carga simultáneamente con los efectos de Fatiga 1, 2 y 3. Cada nivel cierra o encarece algo distinto — no es más del mismo modificador.

| Nivel | Efecto |
| --- | --- |
| **Fatiga 1** | Las `T.E.` físicas requieren una `T.R.` de Tenacidad antes de ejecutarse. Si falla, la `T.E.` se pierde. |
| **Fatiga 2** | Las acciones de ritmo `5` o mayor no están disponibles. |
| **Fatiga 3** | Todas las acciones no gratuitas cuestan `+1` Desgaste adicional. |
| **Fatiga 4** | Las Reacciones no están disponibles. Solo se pueden usar Acciones Activas. |
| **Fatiga 5** | Las Técnicas solo resuelven su efecto primario (`T.A.`, `T.I.` o efecto de utilidad base). El reposicionamiento gratuito, las Alteraciones aplicadas y el control de posición no se activan. |

Si una mecánica añade Fatiga cuando el personaje ya está en Fatiga 5, queda **Incapacitado**.

---

## Incapacitado por agotamiento

Un personaje **Incapacitado por agotamiento** no puede realizar:

- Acciones Activas
- Reacciones
- Técnicas

Debe iniciar descanso en cuanto la escena lo permita.

Si el entorno impide descansar, necesita ayuda, refugio, transporte o una regla específica para no quedar fuera de acción.

---

## Capacidad de carga

La carga sostenida no usa Desgaste de escena cuando se mide como esfuerzo prolongado de viaje, exploración, transporte o trabajo físico.

En esos casos, genera Fatiga directamente por tiempo.

La capacidad de carga depende de tres factores:

- tamaño de la criatura
- Fuerza
- Tenacidad

Para evitar que un personaje con Fuerza `0` o Tenacidad `0` tenga capacidad `0`, usa valores efectivos mínimos.

```text
Fuerza efectiva = máximo(Fuerza, 1)
Tenacidad efectiva = máximo(Tenacidad, 1)
Capacidad de carga = Fuerza efectiva × Tenacidad efectiva × multiplicador de tamaño
```

| Tamaño | Capacidad de carga |
| --- | --- |
| Diminuto | Fuerza efectiva × Tenacidad efectiva × 1 kg |
| Pequeño | Fuerza efectiva × Tenacidad efectiva × 15 kg |
| Mediano | Fuerza efectiva × Tenacidad efectiva × 35 kg |
| Grande | Fuerza efectiva × Tenacidad efectiva × 80 kg |
| Enorme | Fuerza efectiva × Tenacidad efectiva × 200 kg |
| Gigantesco | Fuerza efectiva × Tenacidad efectiva × 800 kg |

---

## Tipo de carga

El tipo de carga se determina por el porcentaje usado de la capacidad total.

| Tipo de carga | Peso transportado | Fatiga por carga sostenida |
| --- | --- | --- |
| Carga Ligera | Hasta 50% de la capacidad | No genera Fatiga automática |
| Carga Media | Más de 50% y hasta 75% | +1 nivel de Fatiga por cada 2 horas |
| Carga Pesada | Más de 75% y hasta 100% | +1 nivel de Fatiga por cada 1 hora |

Una carga que supera el `100%` de la capacidad no puede transportarse de forma funcional sin ayuda, equipo, Técnica, criatura de carga o una regla específica.

La Fatiga por carga sostenida no revisa umbrales de Desgaste. Se añade directamente por tiempo.

Si una nueva aplicación de Fatiga por carga sostenida empujaría al personaje más allá de Fatiga 5, queda **Incapacitado por agotamiento**.

---

## Resumen rápido

| Elemento | Regla |
| --- | --- |
| Desgaste | Se acumula por acciones significativas bajo presión |
| Aguante | `3 + (Tenacidad × 2)` |
| Fatiga proyectada | Se calcula durante la escena, pero no se asienta todavía |
| Fatiga asentada | Se aplica cuando termina la escena hostil o baja la intensidad |
| Fatiga 1 | Desgaste igual o mayor al Aguante |
| Fatiga 5 | Máximo nivel base de Fatiga |
| Más allá de Fatiga 5 | Incapacitado por agotamiento |
| Carga sostenida | Añade Fatiga directamente por tiempo, no por umbrales de Desgaste |

---

## Ejemplo de combate

Una criatura con Aguante `7` participa en un combate largo.

Durante la escena acumula `15` puntos de Desgaste. Mientras el combate sigue activo, esa Fatiga está proyectada.

```text
Aguante = 7
Desgaste acumulado = 15
Fatiga proyectada = 2
```

El personaje sigue actuando mientras la escena continúa, salvo que otra regla indique lo contrario.

Cuando el combate termina, la Fatiga se asienta. El personaje recibe Fatiga 2 y elimina el Desgaste acumulado de esa escena.

Si más adelante descansa, podrá reducir Fatiga según las reglas de Descanso.
