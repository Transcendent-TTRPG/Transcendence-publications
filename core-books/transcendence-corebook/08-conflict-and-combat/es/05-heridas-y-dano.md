---
title: "Heridas y Daño"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 8
status: draft
canonical: false
tags: [wounds, damage, impact, block, critical-impact, injury, combat]
related:
  - core-books/transcendence-corebook/08-conflict-and-combat/en/05-wounds-and-damage.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/06-impacto-critico-y-romper-partes.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/01-acciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/04-descanso.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-desgaste-aguante-fatiga.md
  - core-books/transcendence-corebook/03-core-rules/es/02-rolling-system-and-competencies.md
authority_refs:
  - Transcendence-design/docs/system/wounds-and-damage.md
  - Transcendence-design/data/system/wounds-and-damage.yaml
  - Transcendence-design/docs/system/roll-types.md
  - Transcendence-design/docs/system/equipment-overview.md
  - Transcendence-design/docs/system/ailments.md
section_modes:
  - heading: "Ejemplo"
    writing_mode: example
  - heading: "Ejemplos de progresión"
    writing_mode: example
---

# Heridas y Daño

En Transcendence, la carne de los exploradores y la de los monstruos no se rige por las mismas leyes. Los Primordiales y adversarios son masas biológicas que debes abatir (usan HP y Partes rompibles). Tu personaje, en cambio, es un organismo que lucha por sobrevivir; no tienes una "barra de vida". Si un ataque supera tu defensa y tu armadura, tu cuerpo se rompe.

Las heridas definen la brutalidad de esa ruptura. Entran en juego después de la Tirada de Ataque y de Impacto, determinando qué consecuencia física, anatómica o estructural deja el golpe.

Transcendence usa dos modelos de daño:

| Caso | Modelo usado |
| --- | --- |
| PJ contra PNJ, criatura, monstruo o adversario | El modelo de daño del objetivo |
| PNJ contra PJ | Heridas localizadas por zona |

Esta separación permite que los enemigos usen HP, zonas, fases, partes rompibles o puntos vitales propios, mientras que los personajes jugadores no dependen de una barra general de vida.

Un golpe contra un personaje jugador deja una marca física. Esa marca ocupa ranuras, limita función y puede saturar o colapsar una zona.

---

## Flujo de ataque

Un ataque físico sigue esta secuencia:

1. El atacante declara el ataque.
2. Se determina el objetivo o zona, si corresponde.
3. Se resuelve la Tirada de Ataque contra la Tirada de Defensa del objetivo.
4. Si la Tirada de Ataque no supera la Tirada de Defensa, el ataque no conecta de forma efectiva.
5. Si el ataque conecta, el atacante realiza la Tirada de Impacto.
6. Se determina el Bloqueo aplicable.
7. El resultado se convierte en daño, herida, ruptura o efecto según el modelo del objetivo.

La Tirada de Impacto no se realiza si el ataque no encuentra una entrada.

La defensa decide si el golpe conecta. El Bloqueo decide cuánto de esa presión llega al cuerpo, pieza o parte golpeada.

---

## Tirada de Impacto

La Tirada de Impacto mide la presión que el ataque transmite después de superar la defensa.

```text
Impacto = (Rango de Competencia × Daño del arma) + (Característica asociada × Grado del arma)
```

El Impacto no representa solo fuerza bruta. También incluye masa, ángulo, ejecución, calidad del arma, punto de contacto y capacidad del atacante para convertir una apertura en consecuencia.

---

## Dados adicionales de Impacto

Algunas Técnicas añaden dados adicionales a la Tirada de Impacto.

Estos dados suman al Impacto total de forma normal. No modifican el dado crítico designado ni modifican la probabilidad de Impacto Crítico.

El atacante designa el dado crítico antes de tirar, como siempre. Los dados adicionales se tiran junto con la Tirada de Impacto y su resultado se suma al total. La probabilidad crítica no cambia.

Si una Técnica dice `+Xd2` al Impacto, esos dados se suman a la tirada de esa ronda. No sustituyen ningún dado ni mueven el umbral de crítico.

---

## Impacto Crítico

Cuando el dado crítico designado de la Tirada de Impacto muestra su valor máximo, el ataque produce **Impacto Crítico**. Solo ese dado puede validarlo — los demás dados suman Impacto de forma normal.

Las reglas completas de Impacto Crítico, Potencia Crítica y Romper Partes se encuentran en el capítulo **Impacto Crítico y Romper Partes**.

---

## Bloqueo

Cuando un golpe conecta contra una zona protegida, esa zona aporta **Bloqueo**.

El Bloqueo representa cuánta presión absorbe la armadura antes de que el cuerpo reciba daño real. No es solo grosor: también cuenta cómo estás entrenado para recibir golpes, cómo redistribuyes el impacto con el movimiento del cuerpo y qué tan denso es el material que cubre esa zona.

**Categoría.** La clase de armadura define el piso de protección. Una armadura pesada está construida para contener impactos sostenidos; una ligera prioriza la libertad de movimiento sobre la absorción pura.

| Categoría | Bloqueo base |
| --- | ---: |
| Ligera | 2 |
| Intermedia | 4 |
| Pesada | 6 |

**Material.** No toda armadura de la misma categoría protege igual. Divide la Durabilidad de la pieza entre seis y redondea hacia abajo: ese es el aporte del material. Un cuero estándar (Durabilidad 10) aporta 1. Un hierro estándar (Durabilidad 14) aporta 2. Un acero forjado (Durabilidad 20) aporta 3. Los materiales exóticos como el titanio, con Durabilidad 32, aportan 5 incluso dentro de una categoría ligera.

**Competencia.** Llevar una armadura no es lo mismo que saber usarla. Un guerrero entrenado sabe cómo moverse dentro de ella para recibir el impacto donde el material aguanta más, anular ángulos y reducir el pico de daño que llega al cuerpo. Tu nivel de competencia en el tipo de armadura que protege la zona golpeada suma directamente al Bloqueo.

El Bloqueo total de la zona es la suma de los tres.

Una zona sin armadura no aporta Bloqueo de armadura.

---

## Jugadores contra PNJs

Cuando un personaje jugador golpea a un PNJ, criatura, monstruo o adversario, el ataque usa el modelo de daño del objetivo.

```text
Daño efectivo = Impacto - Bloqueo del objetivo
```

Si el resultado es menor que `0`, trátalo como `0`.

Ese daño se aplica al HP, reserva, zona, punto vital, fase o subsistema que el enemigo tenga definido.

Un enemigo común puede usar HP simple. Una criatura importante puede tener zonas con valores propios. Un campeón puede usar puntos vitales, partes rompibles y fases que cambian cuando una estructura cae.

El Impacto Crítico se resuelve contra ese modelo. No todos los enemigos necesitan partes rompibles, pero los enemigos que las tengan deben indicar qué ocurre cuando una parte se rompe.

---

## PNJs contra jugadores

Cuando la bestia te alcanza, no "pierdes puntos de vida". La garra fractura tu hueso, perfora tu pulmón o destroza tu rodilla. El golpe se registra como una **Herida física** que satura, desangra o colapsa de forma realista la zona anatómica impactada.

El orden de resolución es:

1. Determinar la zona golpeada.
2. Identificar la armadura de esa zona.
3. Resolver la Tirada de Defensa usando la Evasión aplicable y la Agilidad aplicable según la armadura de la zona.
4. Si el ataque conecta, tirar Impacto.
5. Calcular el Bloqueo de la zona.
6. Comparar Impacto contra el Bloqueo.
7. Registrar la Herida si corresponde.

| Relación | Resultado | Ranuras |
| --- | --- | ---: |
| Impacto <= Bloqueo | Sin Herida | 0 |
| Impacto > Bloqueo y <= Bloqueo × 2 | Herida Leve | 1 |
| Impacto > Bloqueo × 2 y <= Bloqueo × 3 | Herida Grave | 2 |
| Impacto > Bloqueo × 3 | Herida Crítica | 3 |

Una Herida Crítica no fuerza una Tirada de Resistencia por defecto. Por sí sola puede llenar o colapsar una zona.

La Tirada de Resistencia solo se fuerza si:

- la Herida Crítica causa Colapso en una zona vital, como Cabeza o Torso
- el ataque, PNJ o Técnica lo dice
- el Agravio asociado exige una Tirada de Resistencia
- el Narrador lo declara por una circunstancia extrema de la escena

La Tirada de Resistencia usada por Colapso vital es de Alteración. Representa shock corporal, pérdida funcional, trauma interno o interrupción física del cuerpo.

---

## Ranuras de Herida

Cada zona del personaje tiene una cantidad de ranuras de Herida.

| Zona | Ranuras |
| --- | ---: |
| Cabeza | 3 |
| Torso | 5 |
| Brazos | 4 |
| Piernas | 4 |
| Pies | 3 |

Una Herida siempre intenta ocupar sus ranuras completas en la zona golpeada.

Si la zona tiene suficientes ranuras libres, se marcan normalmente.

Si no tiene suficientes ranuras libres, se marcan las ranuras restantes y el exceso produce **Desbordamiento**.

| Estado de zona | Condición | Efecto |
| --- | --- | --- |
| Sin heridas | 0 ranuras ocupadas | Sin penalizador |
| Con heridas | 1 o más ranuras ocupadas | Penalizador de Herida = ranuras ocupadas |
| Colapsada | Una Herida no cupo completa | Aplica el efecto de Colapso de esa zona |

---

## Ejemplo

Un personaje tiene el Torso con 4 de 5 ranuras ocupadas.

Recibe una Herida Grave en el Torso, que debería ocupar 2 ranuras.

Solo queda 1 ranura libre, así que marca esa ranura y la otra produce Desbordamiento.

El Torso queda Colapsado.

---

## Penalizador de Herida

Cada ranura de herida ocupada en una zona impone un penalizador inmediato a las tiradas de ese dominio. El malestar no espera a que la zona se llene: una sola herida ya limita la función.

```text
Penalizador de Herida = ranuras actualmente ocupadas en la zona
```

| Zona | Penalizador máximo (zona llena) |
| --- | ---: |
| Cabeza | −3 |
| Torso | −5 |
| Brazos | −4 |
| Piernas | −4 |
| Pies | −3 |

Este penalizador aplica a tiradas y acciones que dependan claramente de esa zona. No es un penalizador universal al personaje.

---

## Heridas y Colapso por zona

Cada zona aplica su penalizador a un dominio exclusivo de tiradas. Los penalizadores de diferentes zonas no se acumulan sobre una misma tirada — si una acción pertenece claramente al dominio de una zona, solo ese penalizador aplica.

| Zona | Penalizador por ranura activa | Colapsada |
| --- | --- | --- |
| Cabeza | −1 a T.E. y T.C. de Sabiduría, Intelecto, Compostura, Presencia y Astucia; −1 a Preparación | T.R. de Alteración contra la severidad de la Herida que causó el Colapso o queda Inconsciente. |
| Torso | −1 a T.E. y T.C. de Tenacidad; −1 a T.R. de todo tipo | T.R. de Alteración contra la severidad de la Herida que causó el Colapso o queda Debilitado. Si la Herida fue Crítica, entra en Agonía independientemente del resultado. |
| Brazos | −1 a T.A. | Un brazo queda inutilizado. No puede usar armas a dos manos, escudo o Técnicas que requieran coordinación de ambos brazos. Puede aplicar Impedido. |
| Piernas | −1 a T.E. y T.C. de Fuerza | Movimiento reducido a la mitad. No puede usar Técnicas que combinen movimiento y ataque en la misma activación. |
| Pies | −1 a T.E. y T.C. de Agilidad | Queda Derribado. Movimiento reducido a la mitad (solo arrastrándose). No puede realizar T.E. ni T.C. de Agilidad sin apoyo. |

La dificultad para la T.R. de Alteración por Colapso depende de la Herida que causó el Desbordamiento.

| Herida que causó Colapso | Dificultad | Valor Base |
| --- | --- | --- |
| Leve | Desafiante | 8 + NR |
| Grave | Rigurosa | 11 + NR |
| Crítica | Exigente | 13 + NR |

---

## Estados Corporales

Los Estados Corporales describen la condición general de una criatura cuando el daño deja de ser solo local.

| Estado | Significado |
| --- | --- |
| Operativo | Puede actuar con los penalizadores que tenga por zona, Agravio, Fatiga o Desgaste |
| Debilitado | No puede realizar acciones con ritmo mayor a 3. Puede hablar, arrastrarse, sostener algo o reaccionar débilmente si la ficción lo permite |
| Incapacitado | Queda Derribado y no puede realizar acciones declaradas. Está consciente — puede percibir y hablar con dificultad — pero el dolor o la lesión impiden toda ejecución activa |
| Inconsciente | No puede actuar ni percibir de forma útil. No puede defenderse de forma activa |
| Agonía | Está en riesgo de morir si no recibe estabilización. Queda Incapacitado |
| Muerto | La criatura deja de ser recuperable por medios normales |

Si una zona ya Colapsada recibe otra Herida, se aplica o refresca el efecto de Colapso.

Si la zona es Cabeza o Torso, el personaje debe superar una Tirada de Resistencia de Alteración contra la severidad de la nueva Herida.

Si falla:

- Si la herida fue en la cabeza, la criatura queda Inconsciente
- Si la herida fue en el torso, la criatura agoniza

Si un personaje en Agonía recibe otra Herida Crítica en Cabeza o Torso, muere salvo que una regla específica, Técnica, intervención inmediata o decisión de mesa establezca otra salida.

---

## Zonas y localización

Para ataques de PNJs contra jugadores, la localización se determina antes de resolver la defensa.

| 1d100 | Zona |
| --- | --- |
| 01–10 | Cabeza |
| 11–15 | Pies |
| 16–55 | Torso |
| 56–75 | Brazos |
| 76–100 | Piernas |

Los ataques de jugadores contra PNJs no usan esta tabla por defecto. El jugador declara objetivo, intención, Técnica o punto vulnerable según lo permita la escena y la información disponible.

---

## Daño por Caída

Las caídas no utilizan la tirada de ataque ni aplican el Bloqueo de armadura (el metal pesado no mitiga la desaceleración contra el suelo, e incluso puede agravarla). En su lugar, toda caída superior a 2 metros utiliza su propio cálculo de Impacto y un Umbral físico bruto.

### Umbral y Cálculo de Impacto
```text
Umbral de Caída = 5 + Tenacidad
```
*(No se suma BC, BM ni CD, a menos que un equipo o rasgo específico mencione absorción de caídas).*

El impacto se tira con dados d6 dependiendo de la distancia de la caída y la categoría de **Tamaño** de la criatura (basado en la masa y la tensión estructural bípeda):

| Tamaño | Impacto de Caída |
| --- | --- |
| Pequeño | `1d6` por cada `3 metros` completos |
| Mediano | `1d6` por cada `2 metros` completos |
| Grande | `1d6` por cada `1 metro` completo |

*Ejemplo: Una criatura Mediana que cae 10 metros tira `5d6` de Impacto contra su Umbral de Caída. Una criatura Grande que cae 4 metros tira `4d6`.*

### Zonas Afectadas y Control de Caída
La severidad de la herida se calcula con la misma tabla de Relación Impacto / Bloqueo (reemplazando Bloqueo por Umbral de Caída). Sin embargo, la zona afectada depende de si la criatura logró controlar su descenso:

- **Caída Controlada:** Si la criatura salta voluntariamente o supera una `T.E. de Acrobacias` al caer, aterriza de pie. La herida se aplica íntegramente a las **Piernas**.
- **Caída Descontrolada:** Si la criatura es empujada por sorpresa, lanzada por un enemigo, está inconsciente o falla su tirada para controlar el descenso, la herida se aplica directamente al **Torso**.

### Caídas Letales (Colapso Masivo)
Si el Impacto de Caída supera **4 veces** el Umbral de Caída, el daño estructural es devastador. Se aplica una Herida Crítica de forma simultánea tanto en las **Piernas** como en el **Torso**. Esto lleva inmediatamente a la criatura al estado de `Agonía`, independientemente de si la caída fue controlada o no.

---

## Estabilizar y Tratar

Existen dos pasos de recuperación.

| Paso | Función | Libera ranuras |
| --- | --- | ---: |
| Estabilizar | Medicina de campo. Detiene sangrados, cauteriza o aplica torniquetes para evitar que el paciente muera de shock mientras el peligro continúa. | No |
| Tratar | Cirugía de subsistencia en el Interludio. Consiste en extraer la esquirla, esterilizar el tejido y suturar durante un Descanso Completo para recuperar la zona. | Sí, con éxito |

Medicina cubre estabilizar y tratar daño corporal.

Herboristería, alquimia, objetos, Técnicas y artefactos pueden modificar estas reglas desde sus propias secciones.

Cuando una Técnica no crea una Herida más severa sino un problema de tratamiento
o limpieza, la respuesta inmediata en combate suele resolverse con **Interactuar**
o **Usar Especialización** según exija o no diagnóstico y manejo entrenado. Eso
no sustituye **Estabilizar** o **Tratar**: solo resuelve el paso previo que
permite volver a ellos en condiciones limpias.

---

## Estabilización

Para estabilizar una zona, un personaje realiza una Tirada de Especialización de Medicina con Sabiduría.

| Ranuras ocupadas en la zona | Dificultad | Kit requerido | Tiempo |
| --- | --- | --- | --- |
| 1–2 | Fundamentos | Básico | 30 minutos |
| 3–4 | Desafiante | Avanzado | 60 minutos |
| 5 / Colapsada | Rigurosa | Especializado | Descanso Completo |

En un éxito, la zona queda estabilizada. Sus efectos inmediatos dejan de empeorar.

En un fallo, la zona sigue activa y el intento puede consumir tiempo, recursos o abrir una complicación si la escena sigue bajo presión.

---

## Tratamiento

Las zonas deben estar estabilizadas antes de liberar ranuras. Una zona activa primero debe estabilizarse.

Al tratar una zona durante un Descanso Completo, el personaje que atiende al paciente realiza una Tirada de Especialización de Medicina con Sabiduría.

| Ranuras ocupadas en la zona | Dificultad | Kit requerido |
| --- | --- | --- |
| 1–2 | Desafiante | Básico |
| 3–4 | Rigurosa | Avanzado |
| 5 / Colapsada | Exigente | Especializado |

En un éxito, el paciente libera 1 ranura ocupada de esa zona.

En un fallo, la zona no libera ranuras.

---

## Ejemplos de progresión

Un golpe que produce una Herida Leve llena 1 ranura. Una vez estabilizada la zona, un tratamiento exitoso la vacía.

Un golpe que produce una Herida Grave llena 2 ranuras. Dos tratamientos exitosos para vaciarlas. La dificultad al tratar baja de Rigurosa a Desafiante cuando queda 1 ranura.

Un golpe que produce una Herida Crítica llena 3 ranuras. Tres tratamientos exitosos para vaciarlas. La dificultad baja de Exigente a Rigurosa al llegar a 2 ranuras, y a Desafiante al llegar a 1.

---

## Partes de criatura y enemigos

Los enemigos no tienen que usar las mismas zonas anatómicas que un personaje jugador. Una criatura importante usa las zonas que su anatomía y diseño de encuentro necesiten.

Por defecto, una criatura importante se organiza en cinco partes principales.

Estos lugares pueden ser:

- cráneo
- mandíbula
- torso
- patas
- cola
- núcleo
- placas dorsales
- extremidades
- alas
- cualquier distribución equivalente

Cada parte de criatura puede tener:

| Campo | Uso |
| --- | --- |
| Tirada de Defensa | Defensa o dificultad para golpear esa parte |
| HP | Reserva de daño normal de la parte |
| Bloqueo | Reducción de Impacto mientras la parte esté funcional |
| Potencia | Capacidad ofensiva o estructural si esa parte ataca o rompe |
| Durabilidad | Resistencia de la parte contra ruptura |
| Habilidades vinculadas | Ataques, Técnicas, rasgos o fases que dependen de la parte |

Romper una parte de criatura sirve para limitar opciones del enemigo.

Si un lobo de hielo tiene Aliento Helado vinculado a su mandíbula, romper la mandíbula impide usar esa habilidad hasta que el bloque del enemigo diga lo contrario.

Las reglas de extracción de recursos se resuelven en su propia sección. Aquí solo importa si la parte sigue funcional, si aporta Bloqueo y qué opciones del enemigo deja disponibles.
