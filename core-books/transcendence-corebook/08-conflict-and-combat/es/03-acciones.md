---
title: "Acciones"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [actions, combat, atb, active-actions, reactions, free-actions, movement, attack, techniques, attrition]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/03-actions.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-atb-flujo-temporal.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/02-desgaste-aguante-fatiga.md
authority_refs:
  - Transcendence-design/docs/system/atb-reference.md
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/docs/system/specializations.md
  - Transcendence-design/docs/adr/combat-atb-rhythm-costs.md
  - Transcendence-design/docs/adr/combat-atb-timeline.md
  - Transcendence-design/data/system/atb-combat.yaml
  - Transcendence-design/data/system/attrition-fatigue.yaml
  - Transcendence-design/data/system/specializations.yaml
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
---

# Acciones

En combate y en escenas de alta presión, cada acción tiene un lugar dentro del flujo temporal. Algunas acciones consumen la activación normal de una criatura. Otras ocurren como respuesta a un disparador. Otras son tan breves que no necesitan costo propio.

Las acciones se dividen en tres tipos:

- **Acciones Activas**
- **Reacciones**
- **Acciones Gratuitas**

Esta división no reemplaza la línea de tiempo **ATB**. Indica cómo entra cada acción en ese sistema.

---

## Tipos de acción

| Tipo | Cuándo ocurre | Efecto en el ATB |
| --- | --- | --- |
| Acción Activa | Durante la activación normal de la criatura | Desplaza la ficha según su costo de ritmo |
| Reacción | Cuando un disparador permite responder fuera de la activación normal | Desplaza la ficha si la reacción tiene costo de ritmo |
| Acción Gratuita | En un momento razonable de la escena | No suele desplazar la ficha |

---

## Acciones Activas

Una **Acción Activa** es una acción deliberada realizada durante la activación normal de una criatura en la línea de tiempo ATB.

Una Acción Activa:

- ocurre durante la activación normal de la criatura
- tiene costo de ritmo
- puede generar Desgaste
- modifica la situación de la escena de forma clara

Atacar, moverse, ocultarse, interactuar bajo presión o usar una especialización en combate suelen ser Acciones Activas.

---

## Reacciones

Una **Reacción** es una acción permitida por un disparador.

No ocurre porque la criatura haya llegado a su activación normal, sino porque algo en la escena permite o exige una respuesta inmediata.

Una Reacción puede usarse para:

- responder a una amenaza entrante
- protegerse
- cubrir a otra criatura
- interrumpir una acción
- desviar un ataque
- aprovechar una apertura
- activar una Técnica con disparador reactivo

Las Reacciones no son gratuitas. Si una Reacción tiene costo de ritmo, desplaza la ficha de la criatura en el ATB. Si genera Desgaste, ese Desgaste se acumula normalmente.

Una criatura solo puede usar una Reacción cuando una regla, Técnica, maniobra, rasgo o situación específica lo permita.

---

## Acciones Gratuitas

Una **Acción Gratuita** es una acción breve que no justifica por sí sola costo de ritmo ni Desgaste.

Se usa para gestos mínimos, coordinación inmediata o detalles que permiten que la escena fluya sin convertir todo en una activación formal.

Ejemplos:

- soltar un objeto
- decir una frase breve
- señalar una dirección
- asentir o negar
- emitir una advertencia corta
- ajustar la postura sin cambiar la situación

Una acción no es gratuita solo porque parece pequeña. Si cambia la escena de forma importante, exige precisión bajo presión, sustituye una Acción Activa o se repite para generar ventajas sin costo, el Narrador puede asignarle costo de ritmo, Desgaste o ambos.

Las Acciones Gratuitas existen para mantener fluidez, no para multiplicar efectos sin costo.

---

## Costos de ritmo

Los costos de ritmo indican cuánto se desplaza la ficha de la criatura en la línea de tiempo ATB después de actuar.

| Categoría | Costo de ritmo |
| --- | --- |
| Gratuita | 0 |
| Rápida | 3 |
| Estándar | 5 |
| Pesada | 7 |
| Variable | Definido por la regla, Técnica o efecto |

El costo de ritmo no siempre mide duración física. También mide recuperación, exposición, compromiso y pérdida de oportunidad dentro del combate.

Algunas acciones y Técnicas también pueden usar valores intermedios como `6` u
`8` cuando realmente caen entre dos anclas de sensación de juego.

---

## Acciones base

Estas acciones están disponibles para cualquier personaje en combate o en una escena de alta presión.

| Acción | Tipo | Ritmo | Desgaste base |
| --- | --- | --- | --- |
| Movimiento | Acción Activa | 5 | 1 |
| Ataque con arma natural | Acción Activa | 6 | 1 |
| Ataque con arma a una mano | Acción Activa | 6 | 1 |
| Ataque con arma a dos manos | Acción Activa | 7 | 1 |
| Ataque con dos armas | Acción Activa | 8 | 1 |
| Interactuar | Acción Activa | 3 | 0 o 1 |
| Ocultarse | Acción Activa | 6 | 1 |
| Usar Especialización | Acción Activa | 4 | 1 |
| Usar Técnica | Variable | Variable | Variable |
| Soltar | Acción Gratuita | 0 | 0 |
| Hablar brevemente | Acción Gratuita | 0 | 0 |

El Desgaste indicado es el costo base. Algunas reglas, condiciones, Técnicas o circunstancias pueden modificarlo.

---

## Movimiento

Un **Movimiento** representa un desplazamiento deliberado dentro de una escena de combate o alta presión.

Puede usarse para:

- avanzar hacia una posición
- retroceder
- flanquear
- cruzar una zona peligrosa
- alcanzar cobertura
- separarse de una amenaza

**Tipo:** Acción Activa  
**Costo de ritmo:** 5  
**Desgaste:** 1

La distancia base proviene de la velocidad de la especie del personaje. El terreno no cambia el costo de ritmo. Cambia cuánto avanza el personaje, si el trayecto requiere una tirada o qué consecuencias produce.

| Condición | Efecto en la distancia |
| --- | --- |
| Terreno difícil | Velocidad a la mitad |
| Reptar | Velocidad a la mitad |
| Correr | Velocidad al doble |

Nadar, trepar y saltar forman parte del Movimiento cuando se usan para desplazarse. Cada uno puede requerir una Tirada de Especialización apropiada: **Nadar**, **Trepar** o **Saltar**.

El Narrador solicita la tirada antes o durante el Movimiento según el riesgo del trayecto.

---

## Atacar

Atacar es el intento directo de causar daño o presión física sobre un objetivo.

Todo ataque se resuelve con una **Tirada de Ataque** (**T.A.**) salvo que una regla específica indique otro procedimiento. La familia de ataque determina el costo de ritmo, el Desgaste y cualquier procedimiento adicional.

---

### Armas naturales

Las armas naturales son partes ofensivas del cuerpo de una criatura: garras, mordida, cuernos, cola, pinzas, aguijones u otras estructuras similares.

No requieren equipo y no pueden ser desarmadas mientras el cuerpo de la criatura pueda usarlas.

**Tipo:** Acción Activa  
**Costo de ritmo:** 6  
**Desgaste:** 1

Se resuelve con una T.A. estándar usando la competencia y la característica asociada.

---

### Arma a una mano

Un ataque con arma a una mano usa un arma que puede sostenerse y manejarse con una sola mano: espada corta, hacha, maza, daga de combate u otra equivalente.

Este ataque deja la otra mano libre.

**Tipo:** Acción Activa  
**Costo de ritmo:** 6  
**Desgaste:** 1

Se resuelve con una T.A. estándar.

---

### Arma a dos manos

Un ataque con arma a dos manos usa un arma que exige compromiso corporal completo: espadón, hacha de guerra, lanza sostenida con ambas manos, gran maza u otra equivalente.

Estas armas suelen tener más alcance, masa o amenaza, pero retrasan la siguiente intervención de quien las usa.

**Tipo:** Acción Activa  
**Costo de ritmo:** 7  
**Desgaste:** 1

Se resuelve con una T.A. estándar.

El personaje regresa al ATB más tarde que con otros ataques base.

---

### Dos armas

Combatir con dos armas permite encadenar ataques dentro de una misma activación. La mano principal realiza el ataque inicial. Los ataques adicionales dependen de la coordinación del personaje bajo presión.

**Tipo:** Acción Activa  
**Costo de ritmo:** 8  
**Desgaste:** 1

Procedimiento:

1. Realiza una **T.A. inicial** con la mano principal, sin penalización.
2. Realiza una **T.E. de combate con dos armas** contra la T.D. del objetivo.
3. Si la T.E. supera la T.D., puedes declarar ataques adicionales.
4. Los ataques adicionales alternan entre ambas manos.

La T.E. usa la especialización **Combate con dos armas** y **Agilidad** como característica asociada.

El personaje obtiene `1` ataque adicional por cada `2` puntos de Agilidad, con mínimo `1`.

---

## Interactuar

**Interactuar** cubre intervenciones físicas breves que no son ataques ni desplazamientos.

Puede usarse para:

- tomar un objeto
- recoger algo del suelo
- abrir o cerrar algo
- activar un mecanismo
- ajustar equipo
- guardar o sacar un objeto accesible
- limpiar, retirar, desenredar o acomodar rápidamente algo que estorba la función inmediata

**Tipo:** Acción Activa  
**Costo de ritmo:** 3  
**Desgaste:** 1 bajo presión real

El Desgaste solo se genera cuando la interacción ocurre bajo presión activa de la escena. Una interacción trivial o sin riesgo inmediato no genera Desgaste.

### Respuestas procedurales breves

Algunas Técnicas, condiciones o peligros no se responden con daño directo sino con un
paso práctico: limpiar una herida, arrancar residuo, soltar una línea atrapada,
retirar un irritante, despejar un mecanismo o volver una parte del cuerpo a un
estado utilizable.

Cuando la respuesta es principalmente física, breve y no exige diagnóstico
entrenado, suele resolverse como **Interactuar**.

Costo orientativo bajo presión activa:

- **Respuesta rápida propia:** `Ritmo 3 / Desgaste 1`

Esto no reemplaza reglas más específicas. Si la situación exige diagnóstico,
tratamiento técnico o una tirada entrenada, pasa a **Usar Especialización**.

### Cambio de arma

Cambiar el arma que el personaje tiene en la mano requiere dos acciones de Interactuar:

1. dejar o guardar el arma actual
2. tomar la nueva arma

Si el personaje primero suelta el arma actual como Acción Gratuita, solo necesita una acción de Interactuar para tomar la nueva.

---

## Ocultarse

**Ocultarse** es el intento deliberado de salir de la localización precisa de los enemigos.

No vuelve invisible al personaje. No borra sus rastros. Crea duda sobre dónde está exactamente y desde dónde puede actuar.

**Tipo:** Acción Activa  
**Costo de ritmo:** 6  
**Desgaste:** 1

Para ocultarse, el personaje necesita una oportunidad real. Debe cumplir al menos una de estas condiciones:

- tener Cobertura Media o Total
- estar fuera del rango visual efectivo
- aprovechar Visibilidad reducida
- usar una distracción suficiente
- contar con una Técnica, rasgo, artefacto o preparación que permita ocultarse

No se puede desaparecer a simple vista mientras un enemigo relevante mantiene al personaje localizado con claridad mediante un sentido aplicable. Si alguien lo ve, oye, huele o percibe sin obstrucción, primero debe romper esa localización.

Ocultarse se resuelve con una Tirada de Especialización apropiada a la ficción, como **Sigilo**, **Supervivencia** u otra autorizada por una Técnica.

La tirada se compara contra la dificultad del entorno o la Percepción enemiga. Si tiene éxito, el personaje obtiene el estado **`Oculto`** contra los enemigos afectados.

Las reglas completas del estado `Oculto`, posición aproximada y detección se encuentran en **Cobertura, Visibilidad y Ocultación**.

---

## Usar Especialización

Usar una **Especialización** representa aplicar una habilidad entrenada dentro de una escena hostil o bajo presión.

Puede cubrir acciones como:

- saltar un obstáculo
- escalar bajo amenaza
- nadar contra una corriente
- rastrear en movimiento
- interpretar una inscripción antes de que el enemigo llegue
- leer el lenguaje corporal de un adversario
- fabricar o ajustar algo bajo presión
- identificar un residuo, señal, afección o alteración antes de responder
- aplicar tratamiento técnico, limpieza entrenada o contención bajo presión

**Tipo:** Acción Activa  
**Costo de ritmo:** 4  
**Desgaste:** 1

Una Especialización produce un resultado narrativo o práctico: el personaje salta el abismo, interpreta el código, detecta la trampa o alcanza una posición.

Si ese resultado tiene una consecuencia mecánica directa, esa consecuencia debe provenir de una regla específica, una acción posterior o una Técnica.

### Respuestas procedurales entrenadas

Cuando una Técnica o condición crea un problema que no se resuelve solo con
quitar algo de encima, la respuesta apropiada suele ser **Usar Especialización**.

Ejemplos frecuentes:

- leer qué clase de contaminación o señal está presente
- decidir cómo tratar una herida ensuciada
- contener un derrame peligroso antes de que empeore
- desenredar una restricción sin agravarla

Costos orientativos bajo presión activa:

- **Identificación rápida:** `Ritmo 3 / Desgaste 1`
- **Tratamiento asistido o técnico:** `Ritmo 6 / Desgaste 1`

La Especialización concreta depende de la ficción: **Medicina**, **Contención**,
**Destreza**, **Rastreo**, **Agarre** u otra si una Técnica o regla lo autoriza.

---

## Usar Técnica

Una **Técnica** es una aplicación entrenada que produce una consecuencia mecánica definida.

Donde una Especialización abre una posibilidad, una Técnica convierte esa posibilidad en efecto inmediato.

**Tipo:** Variable  
**Costo de ritmo:** Definido por la Técnica  
**Desgaste:** Definido por la Técnica

La mayoría de las Técnicas son Acciones Activas. Algunas funcionan como Reacciones si tienen un disparador que lo permite.

El catálogo completo de Técnicas y sus condiciones de activación se encuentra en el capítulo **Técnicas**.

---

## Soltar

**Soltar** cubre dejar caer un objeto que el personaje sostiene y que no está comprometido en una maniobra activa.

**Tipo:** Acción Gratuita  
**Costo de ritmo:** 0  
**Desgaste:** 0

Esto cubre:

- soltar un arma de la mano no activa
- dejar caer un objeto antes o después de la acción principal
- liberar algo que ya no forma parte de lo que el personaje está haciendo

Un objeto que forma parte activa de un agarre, forcejeo, bloqueo, maniobra conjunta o situación comprometida no puede soltarse gratuitamente. En ese caso, requiere una acción de Interactuar.

---

## Hablar

**Hablar** cubre una comunicación breve que no busca alterar la voluntad, emoción o decisión de otra criatura.

**Tipo:** Acción Gratuita  
**Costo de ritmo:** 0  
**Desgaste:** 0

Esto cubre:

- una advertencia breve
- una señal táctica
- un comando corto dirigido a un aliado
- una exclamación involuntaria
- una frase que transmite información inmediata

Engañar, persuadir, negociar, intimidar, calmar o provocar no es gratuito. La distinción no depende solo de la longitud de la frase, sino de su función.

Transmitir información inmediata puede ser gratuito. Intentar influir sobre otro participante requiere una acción apropiada.

---

## Ejemplo

Un personaje sostiene un pasillo mientras un aliado se repliega.

Puede gritar “¡Izquierda!” como Acción Gratuita porque la frase solo transmite información inmediata.

Si ese mismo personaje intenta calmar a un aliado en pánico, provocar a un enemigo o forzar una rendición, ya no es gratuito. La acción busca alterar el estado de decisión de otro participante y debe resolverse con la estructura de acción correspondiente.
