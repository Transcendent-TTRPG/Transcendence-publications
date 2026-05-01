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

El combate y las escenas de alta tensión no solo ponen en riesgo la vida de un personaje: también desgastan su cuerpo, su mente y su compostura. Actuar bajo presión tiene un costo. Ese costo se registra mediante el sistema de Desgaste, Aguante y Fatiga.

Este sistema no reemplaza al daño ni al orden de activación. Registra cuánto esfuerzo puede seguir sosteniendo un personaje antes de empezar a deteriorarse.

El Desgaste representa la carga acumulada de actuar bajo presión.
El Aguante representa cuánto de esa carga puede soportar un personaje.
La Fatiga representa el deterioro que aparece cuando el Desgaste supera sus límites.

Un personaje puede seguir luchando, analizando, resistiendo y reaccionando durante un tiempo — pero no indefinidamente.

---

## Desgaste

El Desgaste es la carga acumulada que un personaje soporta al ejecutar acciones significativas en una escena hostil.

No representa daño físico directo. Tampoco es una medida exclusiva de cansancio muscular. El Desgaste incluye todo aquello que obliga al personaje a seguir rindiendo bajo tensión: esfuerzo corporal, concentración, lectura táctica, control emocional y respuesta inmediata ante el peligro.

Un personaje puede acumular Desgaste por:

- atacar, defenderse o moverse en combate
- reaccionar a amenazas repentinas
- analizar una criatura bajo presión
- sostener una maniobra exigente
- imponer presión mental o social en medio de una escena conflictiva
- actuar mientras sufre condiciones adversas o presión ambiental

No toda acción genera Desgaste. Solo lo hacen aquellas que exigen un esfuerzo real y que tienen peso dentro de la escena.

---

## Aguante

El Aguante representa la capacidad del personaje para seguir funcionando antes de empezar a sufrir Fatiga.

Todo personaje posee una reserva mínima de funcionamiento en tres planos fundamentales del conflicto:

- el **cuerpo**, que sostiene esfuerzo, impacto y movimiento
- la **mente**, que sostiene atención, lectura e interpretación
- la **compostura**, que sostiene control, intención y claridad bajo tensión

Todo personaje cuenta con una Reserva Base de Aguante de 3. A esa base se le suma la resistencia corporal final del personaje, expresada en su Tenacidad.

### Fórmula de Aguante

**Aguante** = 3 + (Tenacidad × 2)

El Aguante depende de dos cosas:

- capacidad natural para soportar esfuerzo (Tenacidad)
- una reserva mínima universal que representa la continuidad operativa en cuerpo, mente y compostura

### Ejemplo

Un personaje con Tenacidad final 2 tras aplicar su Sinapsis inicial de Tenacidad tiene:

Aguante = 3 + (2 × 2) = 7

---

Todo personaje comienza con una especialización inicial de Tenacidad en Nivel 1 / Rango 1: Marcha, Aclimatación o Tolerancia. Operar bajo cualquier presión seria exige alguna forma básica de resistencia entrenada, pero no una única manifestación idéntica para todos.

---

## Fatiga

La Fatiga es el deterioro progresivo que aparece cuando el personaje acumula más Desgaste del que puede sostener.

No surge por una sola acción aislada, sino por acumulación. A medida que el Desgaste aumenta, el personaje empieza a perder eficacia. Le cuesta más mantener precisión, sostener el ritmo, conservar la claridad o responder con la misma firmeza.

La Fatiga no representa solo agotamiento físico. También puede reflejar:

- saturación corporal
- sobrecarga mental
- pérdida de compostura
- dificultad para sostener el mismo nivel de rendimiento

### Fatiga proyectada y Fatiga asentada

Durante una escena hostil, el personaje puede seguir actuando aunque ya haya acumulado bastante Desgaste. Por eso, el sistema distingue entre dos momentos distintos:

#### Fatiga proyectada

Mientras el combate o la situación de peligro sigue activa, el jugador registra cuánto Desgaste lleva acumulado y puede ver qué nivel de Fatiga sufriría si la escena terminara en ese momento.

Esto no significa que la penalización completa se aplique inmediatamente. Significa que el personaje ya está forzando su margen y que, si continúa así, saldrá de la escena en peor estado.

#### Fatiga asentada

Cuando la escena hostil termina o desciende claramente de intensidad, la adrenalina deja de sostener artificialmente el rendimiento. En ese momento, la Fatiga proyectada se convierte en Fatiga real y se aplican sus efectos.

- Durante el combate, la Fatiga se proyecta.
- Al terminar el combate, la Fatiga se asienta.

### Umbrales de Fatiga

La Fatiga se determina comparando el Desgaste acumulado con el Aguante del personaje.

| Nivel | Condición |
| --- | --- |
| Fatiga 0 | el Desgaste es menor que el Aguante |
| Fatiga 1 | el Desgaste es igual o mayor al Aguante |
| Fatiga 2 | el Desgaste es igual o mayor a 2 × Aguante |
| Fatiga 3 | el Desgaste es igual o mayor a 3 × Aguante |
| Fatiga 4 | el Desgaste es igual o mayor a 4 × Aguante |
| Fatiga 5 | el Desgaste es igual o mayor a 5 × Aguante |

### Ejemplo de umbrales

Si un personaje tiene Aguante 7:

- Desgaste 0 a 6 → sin Fatiga
- Desgaste 7 a 13 → Fatiga 1
- Desgaste 14 a 20 → Fatiga 2
- Desgaste 21 a 27 → Fatiga 3
- Desgaste 28 a 34 → Fatiga 4
- Desgaste 35 o más → Fatiga 5

La escala base no supera Fatiga 5. Si una regla vuelve a añadir Fatiga cuando el personaje ya está en Fatiga 5, el personaje queda Incapacitado por agotamiento.

Un personaje Incapacitado por agotamiento no puede realizar Acciones Activas, Reacciones ni Técnicas. Debe iniciar descanso en cuanto la escena lo permita. Si el entorno impide descansar, necesita ayuda, refugio, transporte o una regla específica para no quedar fuera de acción.

Fatiga 5 no es un margen táctico que pueda sostenerse voluntariamente. Es el último punto antes del colapso operativo.

---

## Capacidad de Carga

La carga sostenida no usa Desgaste de escena cuando se mide como esfuerzo prolongado de viaje, exploración, transporte o trabajo físico. En ese caso, genera Fatiga directamente por tiempo.

La capacidad de carga depende del tamaño de la criatura, Fuerza y Tenacidad.

Para evitar que un personaje con Fuerza 0 o Tenacidad 0 tenga capacidad 0, usa valores efectivos mínimos:

```text
Fuerza efectiva = mínimo 1
Tenacidad efectiva = mínimo 1
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

El tipo de carga se determina por el porcentaje usado de esa capacidad.

| Tipo de carga | Peso transportado | Fatiga por carga sostenida |
| --- | --- | --- |
| Carga Ligera | Hasta 50% de la capacidad | No genera Fatiga automática. |
| Carga Media | Más de 50% y hasta 75% | +1 nivel de Fatiga por cada 2 horas. |
| Carga Pesada | Más de 75% y hasta 100% | +1 nivel de Fatiga por cada 1 hora. |

Una carga que supera el 100% de la capacidad no puede transportarse de forma funcional sin ayuda, equipo, Técnica, criatura de carga o una regla específica.

La Fatiga por carga sostenida no revisa umbrales de Desgaste. Se añade directamente por tiempo. Si una nueva aplicación de carga sostenida empujaría al personaje más allá de Fatiga 5, queda Incapacitado por agotamiento y debe descansar o recibir ayuda.

---

## Costos de Desgaste

Las acciones no generan todas el mismo nivel de carga. Para reflejarlo, el sistema usa una escala simple de costos.

### Escala de Desgaste

| Costo | Tipo de acción |
| --- | --- |
| 0 | acción sin exigencia real |
| 1 | acción significativa estándar |
| 2 | acción de alta exigencia |
| 3 | acción extrema o de sobreextensión |

### 0 Desgaste

Acciones triviales o puramente narrativas que no exigen esfuerzo real dentro de la escena.

Ejemplos:

- una observación evidente
- una frase breve sin peso táctico
- una acción menor sin amenaza inmediata

### 1 Desgaste

Acciones significativas normales.

Ejemplos:

- un ataque estándar
- una defensa sencilla
- un desplazamiento importante bajo presión
- una observación activa del enemigo
- una lectura básica del comportamiento de una criatura

### 2 Desgaste

Acciones de alta exigencia.

Ejemplos:

- interceptar una carga
- proteger a otro personaje absorbiendo presión
- analizar en profundidad a un enemigo durante el combate
- ejecutar una maniobra que altere de verdad el ritmo de la escena
- usar una acción mental o social que quite una ventaja importante

### 3 Desgaste

Acciones extremas o de sobreextensión.

Ejemplos:

- un esfuerzo límite cuando el personaje ya está muy presionado
- una intervención heroica por encima del margen seguro
- una maniobra especialmente exigente que fuerce al personaje más allá de su ritmo normal

---

## Acciones físicas, mentales y sociales

El Desgaste no depende del tipo de atributo utilizado, sino de la exigencia real de la acción.

Una acción mental o social genera Desgaste si:

- exige foco real bajo amenaza
- altera la situación táctica
- compite con otras acciones importantes del combate
- obliga al personaje a sostener lectura, control o presión en medio del caos

No toda acción mental o social genera Desgaste. Lo generan aquellas que aportan una ventaja real o imponen una carga significativa bajo presión.

Leer a una criatura, quebrar su patrón, forzar una reacción o desestabilizar su conducta puede costar tanto como atacar o defenderse, cuando la situación lo justifica.

---

## Reacciones y Desgaste

Las reacciones no son costosas por ser reacciones, sino por la exigencia que suelen implicar.

Responder fuera del ritmo natural del personaje suele requerir más precisión, tensión y rapidez. Por ello, una reacción puede costar más o menos Desgaste según lo difícil que resulte ejecutarla.

- una reacción simple puede costar 1
- una reacción exigente puede costar 2
- una reacción límite puede costar 3

Lo importante no es su categoría, sino su intensidad dentro de la escena.
