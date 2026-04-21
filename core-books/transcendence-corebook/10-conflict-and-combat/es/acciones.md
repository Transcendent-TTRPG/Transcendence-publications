---
title: "Acciones"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 10
status: draft
canonical: false
tags: [actions, combat, atb, active-actions, reactions, free-actions, movement, attack, techniques, attrition]
related:
  - core-books/transcendence-corebook/10-conflict-and-combat/en/actions.md
  - core-books/transcendence-corebook/10-conflict-and-combat/es/atb-linea-de-tiempo.md
  - core-books/transcendence-corebook/10-conflict-and-combat/es/desgaste-aguante-fatiga.md
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
  - heading: "Atacar"
    writing_mode: flavor
  - heading: "Interactuar"
    writing_mode: flavor
  - heading: "Especialización"
    writing_mode: flavor
  - heading: "Técnicas"
    writing_mode: flavor
  - heading: "Soltar"
    writing_mode: flavor
  - heading: "Hablar"
    writing_mode: flavor
  - heading: "Ejemplo"
    writing_mode: example
---

# Acciones

En combate y en escenas de alta presión, todo lo que un personaje hace tiene un lugar y un costo dentro del flujo temporal. No todas las acciones ocupan ese lugar de la misma manera.

Algunas exigen compromiso total y alteran el ritmo del personaje. Otras ocurren como respuesta a un peligro inmediato. Otras son tan breves que no justifican por sí solas un costo de tiempo o esfuerzo.

Las acciones se dividen en tres tipos:

- **Acciones Activas**
- **Reacciones**
- **Acciones Gratuitas**

Esta división no reemplaza al ATB. Existe para aclarar cómo entra cada tipo de acción dentro del flujo temporal del combate.

---

## Acciones Activas

Las Acciones Activas son aquellas que un personaje realiza de forma deliberada durante su activación normal en la línea de tiempo ATB. Representan lo que el personaje dedica su cuerpo, su atención o su intención principal en ese momento.

Una Acción Activa:

- ocurre durante la activación normal del personaje
- tiene un costo de ritmo que desplaza su ficha en la línea de tiempo
- puede generar Desgaste
- altera de forma clara la situación de la escena

Son la forma más común de actuar en combate y en escenas de alta presión.

---

## Reacciones

Las Reacciones son acciones permitidas por un disparador. No ocurren porque haya llegado la activación natural del personaje, sino porque algo en la escena ofrece — o exige — una respuesta inmediata.

Una Reacción puede usarse para:

- interrumpir una acción entrante
- protegerse o cubrir a otro personaje
- desviar un ataque
- aprovechar un error o una apertura del enemigo
- responder a una amenaza inminente

**Las Reacciones no son gratuitas.**

Aunque ocurran fuera de la activación natural del personaje, siguen formando parte del mismo sistema temporal. Por ello, una Reacción puede:

- tener costo de ritmo
- generar Desgaste
- modificar la posición futura del personaje en el ATB

---

## Acciones Gratuitas

Las Acciones Gratuitas son acciones tan breves que no justifican por sí solas un costo de ritmo ni de Desgaste.

Se usan para gestos mínimos, coordinación inmediata o detalles que permiten que la escena fluya sin convertir todo en una activación formal.

Ejemplos:

- soltar un objeto
- decir una frase breve sin intención táctica
- señalar una dirección
- asentir, negar o emitir una advertencia corta
- ajustar ligeramente la postura sin alterar la escena

### Importante

Una acción no es gratuita por parecer pequeña. Si una acción:

- cambia de forma importante la situación de la escena
- exige precisión real bajo presión
- sustituye algo que normalmente sería una Acción Activa
- se repite de forma abusiva para multiplicar efectos sin costo

el Narrador puede decidir que deja de ser gratuita y pasa a costar ritmo, Desgaste o ambos.

Las Acciones Gratuitas existen para mantener naturalidad y fluidez — no para multiplicar ventajas sin costo.

---

## Relación con el ATB

| Tipo | Cuándo ocurre | Efecto en el ATB |
| --- | --- | --- |
| Acción Activa | Durante la activación normal del personaje | Desplaza la ficha según su costo de ritmo |
| Reacción | Por disparador, fuera de la activación natural | También desplaza la ficha |
| Acción Gratuita | En cualquier momento razonable | No suele alterar la posición, salvo decisión del Narrador |

---

## Acciones Base

Las siguientes acciones están disponibles para cualquier personaje en una escena de combate o alta presión. Cada una indica su tipo, su costo de ritmo y su costo de Desgaste base.

---

### Movimiento

Un Movimiento representa el desplazamiento deliberado del personaje a través del espacio de combate. Correr hacia una posición de ventaja, retroceder ante una amenaza, flanquear a un enemigo, cruzar una zona peligrosa — cualquier cambio de posición con intención táctica es un Movimiento. La distancia que puede recorrer y las dificultades que encuentra dependen del tipo de terreno y de las circunstancias de la escena.

**Tipo:** Acción Activa  
**Costo de ritmo:** 5 (Estándar)  
**Desgaste:** 1

La distancia base proviene de los valores de velocidad de la especie del personaje. El terreno no altera el costo de ritmo: lo que cambia es cuánto avanza el personaje, si el trayecto requiere una tirada, o las consecuencias del desplazamiento.

| Condición | Efecto en la distancia |
| --- | --- |
| Terreno difícil | Velocidad a la mitad |
| Reptar | Velocidad a la mitad |
| Correr | Velocidad al doble |

Nadar, trepar y saltar exigen cada uno una Tirada de Especialización de su competencia correspondiente — Nadar, Trepar y Saltar. El Narrador la solicita antes o durante el Movimiento según lo que el trayecto requiera.

---

### Atacar

Atacar es el intento directo de infligir daño o presión física sobre un objetivo. La familia de ataque determina cómo se resuelve la acción y qué lugar ocupa en el ATB.

#### Armas Naturales

Las armas naturales son garras, mordida, cuernos, cola — cualquier elemento ofensivo que forme parte del cuerpo de la criatura. No requieren equipo, no pueden ser desarmadas, y están disponibles mientras el cuerpo del personaje funcione.

**Tipo:** Acción Activa  
**Costo de ritmo:** 5 (Estándar)  
**Desgaste:** 1

Se resuelve con una T.A. estándar usando la competencia y la característica asociada.

#### Arma a una mano

El ataque con arma a una mano cubre toda la familia de armas ofensivas que se sostienen y operan con una sola mano: espadas cortas, hachas, mazas, dagas de combate y similares. Es el ataque base más versátil: deja la otra mano libre y permite al personaje volver a actuar sin una demora significativa. Las diferencias entre las armas de esta familia no están en el ritmo base, sino en los efectos que causan, los rasgos que tienen y las Técnicas que cada una puede activar.

**Tipo:** Acción Activa  
**Costo de ritmo:** 5 (Estándar)  
**Desgaste:** 1

Se resuelve con una T.A. estándar.

#### Arma a dos manos

Algunas armas exigen el cuerpo entero — espadones, hachas de guerra, lanzas sostenidas con ambas manos, grandes mazas. Lo que ganan en alcance, masa o poder de amenaza tiene un precio: la ejecución es más lenta, la recuperación más larga, y los errores pueden dejar aberturas reales. Son armas que modifican el ritmo del combate tanto para quien las empuña como para quienes las enfrentan.

**Tipo:** Acción Activa  
**Costo de ritmo:** 7 (Pesado)  
**Desgaste:** 1

Se resuelve con una T.A. estándar. El personaje regresa al ATB más tarde que con cualquier otro ataque base.

#### Dos armas

Combatir con un arma en cada mano permite encadenar más golpes en una sola activación. La mano principal ataca sin penalización; lo que determina cuántos golpes adicionales conectan es la capacidad del personaje para sostener esa coordinación bajo presión. No es simplemente dos ataques — es una secuencia que puede colapsar si la habilidad no acompaña.

**Tipo:** Acción Activa  
**Costo de ritmo:** 7 (Pesado)  
**Desgaste:** 1

1. **T.A. inicial** con la mano principal, sin penalización.
2. **T.E. de combate con dos armas** contra la T.D. del objetivo. Si supera la T.D., el personaje puede declarar ataques adicionales.
3. **Ataques adicionales:** 1 por cada 2 puntos de Agilidad del personaje (mínimo 1). Los ataques alternan entre ambas manos.

La T.E. utiliza la especialización en combate con dos armas con Agilidad como característica asociada.

---

### Interactuar

Interactuar cubre las intervenciones físicas breves que no son ataques ni desplazamientos: tomar un objeto, abrir o cerrar algo, recoger algo del suelo, activar un mecanismo, ajustar el equipo. Son acciones que ocurren dentro del flujo del combate pero no se dirigen directamente a un adversario. Requieren presencia física y atención — por eso tienen costo de ritmo — pero no exigen el compromiso de un ataque ni el alcance de un desplazamiento.

**Tipo:** Acción Activa  
**Costo de ritmo:** 3 (Rápido)  
**Desgaste:** 1\*

**Cambio de arma:** Cambiar el arma en la mano requiere dos acciones de Interactuar — una para dejar el arma actual y otra para tomar la nueva. Si el personaje suelta primero (Acción Gratuita), solo necesita una acción de Interactuar para tomar la siguiente.

\* El Desgaste solo se genera cuando la interacción ocurre bajo presión real de la escena. Las interacciones triviales o sin presión activa no generan Desgaste.

---

### Especialización

Una Especialización representa el uso de cualquier habilidad entrenada en el contexto de una escena hostil: saltar un obstáculo, escalar bajo amenaza, nadar contra una corriente mientras el combate continúa, rastrear en movimiento, interpretar una inscripción antes de que el enemigo llegue, leer el lenguaje corporal de un adversario, fabricar algo bajo presión. La habilidad puede ser física, mental o social — la escena impone la misma presión sin importar cuál sea.

**Tipo:** Acción Activa  
**Costo de ritmo:** 5 (Estándar)  
**Desgaste:** 1

Una Especialización produce un efecto narrativo: el personaje salta el abismo, interpreta el código, detecta la trampa. Si ese resultado tiene consecuencias mecánicas directas, esos efectos se resuelven a través de las acciones que siguen o a través de una Técnica.

---

### Técnicas

Las Técnicas son el resultado de entrenamiento acumulado expresado en una acción concreta. Donde una Especialización produce un efecto narrativo, una Técnica añade un efecto mecánico definido en la misma activación — sin pasos adicionales, sin esperar a la siguiente acción. Esa capacidad de combinar lo que se hace con lo que se produce mecánicamente es lo que las distingue, y lo que justifica que solo sean accesibles a través de competencias.

**Tipo:** Variable  
**Costo de ritmo:** Definido por la Técnica  
**Desgaste:** Definido por la Técnica

La mayoría son Acciones Activas; algunas funcionan como Reacciones y pueden activarse fuera de la secuencia normal si su disparador lo permite.

El catálogo completo de Técnicas y sus condiciones de activación se encuentra en el capítulo de Competencias y Técnicas.

---

### Soltar

Hay momentos en que lo más útil es simplemente abrir la mano: dejar caer el arma secundaria para usar esa mano en otra cosa, soltar un objeto que ya no forma parte de la acción, liberar algo antes de que comience el siguiente movimiento. Cuando el objeto no está involucrado en ninguna maniobra activa, hacerlo no tiene costo.

**Tipo:** Acción Gratuita  
**Costo de ritmo:** 0  
**Desgaste:** 0

Esto cubre:

- soltar un arma de la mano no activa mientras la otra actúa
- dejar caer un objeto antes o después de la acción principal
- liberar algo que ya no forma parte de lo que el personaje está haciendo

Un objeto que es parte activa de un agarre o maniobra conjunta comprometida no puede soltarse de forma gratuita — eso requiere una acción de Interactuar (ritmo 3).

### Hablar

No todo lo que se dice requiere tiempo. Una advertencia, una señal, un nombre gritado al aliado más cercano — palabras que transmiten información sin interrumpir el flujo del personaje ni desplazar su ficha en el ATB.

**Tipo:** Acción Gratuita  
**Costo de ritmo:** 0  
**Desgaste:** 0

Esto cubre:

- una señal táctica o advertencia breve
- un comando de una palabra o frase corta dirigido a un aliado
- una exclamación involuntaria

Engañar, persuadir, negociar o ejercer presión social no es gratuito. La distinción no es de longitud sino de función: transmitir información es gratuito; intentar influir no lo es.

---

## Ejemplo

Un personaje sostiene un pasillo mientras un aliado se repliega. Puede gritar "¡Izquierda!" como Acción Gratuita porque esa frase solo transmite información inmediata. Si ese mismo personaje intenta calmar a un aliado en pánico, provocar a un enemigo o forzar una rendición, ya no es gratuito: la acción busca alterar el estado de decisión de otro participante y debe resolverse con la estructura de acción correspondiente.
