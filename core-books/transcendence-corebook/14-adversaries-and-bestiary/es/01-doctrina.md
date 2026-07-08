---
title: "Doctrina, Naturaleza, Categoría y Rol"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 14
status: draft
canonical: false
tags: [criaturas, adversarios, naturaleza, categoría, rol, doctrina, mortal, anomalía, primordial]
related:
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/02-zonas.md
  - core-books/transcendence-corebook/14-adversaries-and-bestiary/es/03-rasgos.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/
authority_refs:
  - Transcendence-design/docs/system/creatures.md
---

# Doctrina, Naturaleza, Categoría y Rol

Cada criatura es un sistema biológico diseñado para matar o sobrevivir, y cada comportamiento letal tiene una anatomía que lo hace posible.

---

## El cuerpo explica el comportamiento

Una criatura que respira hielo tiene un órgano que produce ese frío. Una que regenera tejido tiene una glándula que lo impulsa. Una que barre con la cola tiene una cola que existe porque ese barrido existe.

El punto de partida siempre son los comportamientos: qué hace la criatura, cómo ataca, cómo responde, cómo presiona el campo de batalla. Las zonas — las partes del cuerpo que el sistema registra — son consecuencia de esos comportamientos, no su origen.

**Si un comportamiento no tiene zona, no es un comportamiento: es una abstracción. Las abstracciones no pertenecen al diseño de criaturas.**

Cuando una zona colapsa, el comportamiento vinculado a ella se detiene. Los jugadores que apuntan a zonas desmantelan a la criatura parte por parte: cuando una zona colapsa, el comportamiento que sostenía muere con ella. La pregunta táctica no es cuánto daño hacer en general, sino qué órgano mutilar primero, y cómo responderá la criatura al dolor y a la pérdida.

---

## Naturaleza

La naturaleza describe la composición biológica de la criatura y su relación con el Tauma. El peligro viene del NR — una Mortal puede ser tan letal como una Anomalía; la naturaleza describe qué es la criatura, no cuánto daña.

### Mortal

Carne, hueso, ácido y quitina. Sin Tauma en su composición ni en sus procesos internos. La resistencia a daño elemental es biológica — pieles gruesas, conchas, densidad, masa — y se expresa a través de los valores de Bloqueo en las zonas relevantes.

### Anomalía

Organismos mutados donde el Tauma se ha integrado parasíticamente a sus procesos biológicos. El Tauma es parte indisoluble de su metabolismo, no una habilidad que activa o controla.

- **Afinidad elemental:** 50% de reducción de daño del elemento afiliado.
- **Vulnerabilidad elemental:** +50% de daño del elemento opuesto.

### Primordial

Anomalías sin estructura biológica convencional. Entidades compuestas enteramente de la distorsión del Limbo.

- **Afinidad elemental:** 100% de reducción de daño del elemento afiliado.
- **Vulnerabilidad elemental:** +100% de daño del elemento opuesto.

Para los Primordiales, los ataques que alcanzan zonas sin relación con su lógica estructural causan 0 de daño. El daño significativo requiere que los jugadores comprendan la composición de la criatura lo suficiente como para identificar qué atacar.

---

## Categoría

La categoría define el tipo de presencia que tiene la criatura en el mundo y en un encuentro: su rol en el ecosistema y el alcance de sus ciclos autónomos. El poder lo determina el NR.

### Común

Representa la población general de una especie. Sin rol organizativo especial. Sus ciclos autónomos son estrictamente biológicos: expresan la propia fisiología de la criatura — cómo carga una habilidad elemental, cómo recupera su cuerpo, cómo cambia de postura entre ataques.

### Campeón

Un individuo poderoso que comanda o coordina a un grupo. Sus ciclos autónomos incluyen ciclos biológicos y ciclos de coordinación de aliados — habilidades que funcionan porque otras criaturas están presentes y que modifican el comportamiento de esas aliadas (Preparación, acceso a tácticas, Bloqueo, posicionamiento).

### Elite

Un individuo excepcional, más allá de cualquier otro miembro de su especie. Sus ciclos autónomos incluyen ciclos biológicos y ciclos ambientales — procesos que cambian el propio campo de batalla: visibilidad, terreno, condiciones elementales, estabilidad espacial.

Una criatura Elite no es un Común o un Campeón con más potencia — es un encuentro que modifica el espacio mismo donde están los jugadores.

Las criaturas Elite tienen además:

**Metamorfosis** — El colapso de órganos principales desencadena respuestas biológicas de supervivencia catastrófica. Cada fase modifica a la bestia, alterando los comportamientos disponibles, los ciclos y el entorno de forma impredecible. Las fases no están telegrafiadas; los jugadores las sufren a medida que desmantelan a la criatura.

**Apoteosis** — El organismo llevado más allá de su límite evolutivo; el pico de adrenalina o inestabilidad antes del colapso total. Se activa después de completar todas las fases de Metamorfosis. Concede a la criatura +3 a todas las tiradas de ataque. Reduce en 1 el rango de amenaza crítica para los jugadores que la atacan.

**Golpe Final** — La acción coordinada específica que pone fin a la criatura durante la Apoteosis. Se define por criatura. Requiere daño umbral entregado a través de un ataque coordinado declarado. Hasta que se ejecute el Golpe Final, la criatura en Apoteosis no puede reducirse por debajo de 1 PV en ninguna zona.

---

## Características y Estadísticas Base

A diferencia de versiones anteriores de diseño abstracto, las criaturas de *Transcendence* están ancladas al mismo motor simulacionista que los jugadores. Toda bestia, sin importar su intelecto, posee las 9 características base: **Fuerza, Agilidad, Tenacidad, Astucia, Intelecto, Sabiduría, Aura, Presencia y Compostura**.

A partir de estas características, se derivan sus atributos de supervivencia de la misma forma que un personaje jugador:
- **Preparación:** `(Agilidad + Astucia + Compostura) / 3` (redondeado hacia arriba). Puede recibir bonificadores pasivos si la bestia es un depredador de emboscada.
- **Resiliencia:** `(Tenacidad + Sabiduría + Compostura) / 3` (redondeado hacia arriba).

### Nivel Base y Tiradas de Combate

Las criaturas no tienen "Niveles de Especialización" genéricos en armas como un jugador. En su lugar, el juego les asigna un **Nivel Base** dictado por su letalidad biológica:
`Nivel Base = NR + Rango` *(donde el Rango es 1 para NR 1-2, R2 para NR 3-4, R3 para NR 5-6)*.

Este Nivel Base se suma a la Característica relevante de la criatura para calcular las resoluciones de combate, logrando una asimetría matemática real:

- **Tirada de Ataque (T.A):** Característica (según el arma natural) + Nivel Base
- **Tirada de Defensa (T.D):** Agilidad + Nivel Base
- **Tirada de Reacción (T.R):** Tenacidad + Nivel Base
- **Tirada de Contención (T.C):** Compostura + Nivel Base
- **Tirada de Impacto (Daño Fijo):** `(Rango)d(Dado de arma) + (NR × Grado) + Característica` asociada al ataque.

*(Nota: En la ficha de la criatura, estos valores se entregan pre-calculados en el bloque de combate para agilizar el juego en la mesa).*

### Especializaciones (T.E) Biológicas

Las criaturas no reciben bonificadores genéricos a sus Tiradas de Especialización. Para reflejar su biología e instintos, el bloque de estadísticas lista únicamente las **Especializaciones** que la bestia posee realmente (elegidas estrictamente del Catálogo, como *Percepción, Acrobacias, Rastreo o Supervivencia*). Si una criatura es forzada a tirar una especialización que no posee en su lista, tira exclusivamente con su Característica (sin sumar Nivel Base).

## Rol

El rol define la función táctica de la criatura en el ecosistema de combate. Bajo este sistema anclado en características, el rol ya no otorga bonificadores numéricos a las tiradas; su función mecánica es dictar el multiplicador base de los Puntos de Vida (PV) al momento de construir sus zonas anatómicas, y guiar su comportamiento de IA en mesa.

| Rol | Multiplicador de PV | Función |
| --- | --- | --- |
| Protector | × 3 | Absorbe ataques; protege a Comunes; prioriza Bloqueo |
| Golpeador | × 2 | Fuente de daño principal; ataques agresivos y emboscadas |
| Soporte | × 1,5 | Coordina aliados; aplica condiciones; rastrea o debilita |
| Lanzador | × 1 | Ataques a distancia o biológicos; se mantiene lejos del daño |
