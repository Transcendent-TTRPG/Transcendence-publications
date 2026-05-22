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

Las heridas definen qué ocurre cuando un ataque supera la defensa y alcanza el cuerpo, equipo o estructura del objetivo.

No reemplazan la Tirada de Ataque ni la Tirada de Impacto. Entran después, cuando ya existe contacto efectivo y la escena necesita determinar qué consecuencia deja ese golpe.

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

La defensa decide si el golpe conecta. El Bloqueo decide cuánto de esa presión llega realmente al cuerpo, pieza o parte golpeada.

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

Un **Impacto Crítico** ocurre cuando el dado crítico designado de la Tirada de Impacto muestra su valor máximo.

Si la Tirada de Impacto usa varios dados, el atacante debe designar uno antes de tirar. En mesa, se recomienda usar un dado de color distinto. En digital, el dado puede marcarse con una etiqueta equivalente.

Solo ese dado valida el Impacto Crítico. Los demás dados suman Impacto de forma normal.

| Dado de Impacto | Resultado crítico |
| --- | ---: |
| d4 | 4 |
| d6 | 6 |
| d8 | 8 |
| d10 | 10 |
| d12 | 12 |

Las armas con dados pequeños generan críticos con más frecuencia. Las armas con dados grandes generan críticos menos frecuentes, pero suelen transmitir más Impacto.

Subir de rango aumenta el Impacto total, pero no aumenta por sí mismo la probabilidad crítica, porque solo el dado designado puede validarla.

Un Impacto Crítico puede permitir:

- aplicar daño crítico contra un PNJ si su modelo lo define
- intentar romper una parte, pieza de equipo o protección
- activar una Técnica que requiera Impacto Crítico
- aplicar una consecuencia física si el ataque o el objetivo la declaran

Un Impacto Crítico no concede una lista universal de efectos. El arma, la Técnica, el objetivo o la escena definen qué opciones están disponibles.

---

## Potencia Crítica

La **Potencia Crítica** mide la capacidad del arma para romper, deformar, abrir o inutilizar una estructura resistente durante un Impacto Crítico.

```text
Potencia Crítica = Potencia base × Multiplicador de Potencia del arma
```

Si el resultado produce fracciones o decimales, redondea hacia arriba salvo que una regla específica indique lo contrario.

La Potencia base proviene del material, construcción o perfil del arma. El multiplicador depende del tipo de arma y expresa cómo esa arma transmite fuerza durante un crítico.

| Tipo de arma | Multiplicador | Uso ideal |
| --- | ---: | --- |
| Lanzas | 80% | Perforar puntos pequeños y atravesar protecciones ligeras |
| Hachas | 120% | Abrir material y partir superficies rígidas |
| Mazas | 150% | Romper armaduras pesadas y aplastar estructuras resistentes |
| Hojas largas | 100% | Cortes amplios contra superficies de resistencia media |
| Dagas | 50% | Críticos frecuentes contra zonas vulnerables o desprotegidas |
| Hojas cortas | 75% | Ataques rápidos con potencia moderada |
| Armas arrojadizas | 40% | Impactos precisos a distancia con baja ruptura estructural |
| Armas a distancia | 60% | Perforación o impacto desde lejos |
| Armas flexibles | 30% | Control, restricción y desbalance |

El material no cambia necesariamente el dado de daño de un arma. Un khopesh de hierro y uno de adamantium pueden usar el mismo daño base. La diferencia aparece en Potencia y Durabilidad: el primero puede cortar igual, pero el segundo rompe mejor y resiste más.

---

## Romper partes

**Romper Partes** es una opción estratégica disponible cuando un ataque logra un Impacto Crítico y existe un objetivo rompible declarado.

El objetivo debe ser algo que el ataque pueda alcanzar y afectar de forma creíble:

- arma
- escudo
- pieza de armadura
- extremidad
- mandíbula
- cuerno
- caparazón
- cola
- ala
- articulación
- punto vital
- parte destructible definida por el encuentro

Para resolver la ruptura, compara Potencia Crítica contra Durabilidad.

```text
Potencia Crítica >= Durabilidad del objetivo
```

| Comparación | Resultado |
| --- | --- |
| Potencia Crítica >= Durabilidad | La parte se rompe, se deshabilita o queda inutilizada |
| Potencia Crítica < Durabilidad | La parte no se rompe y pierde 1 punto de Durabilidad |

La pérdida de Durabilidad solo ocurre durante un intento válido de ruptura:

- por Impacto Crítico
- por una Técnica que permita romper sin crítico
- por una regla específica del ataque

Los ataques normales no reducen Durabilidad por defecto.

Si una pieza rota aportaba Bloqueo, deja de aportar Bloqueo hasta ser reparada o reemplazada. La pérdida de Durabilidad no reduce Bloqueo por sí misma; la pieza funciona hasta romperse, salvo que una regla indique lo contrario.

Romper una parte puede:

- deshabilitar una opción de ataque
- reducir defensa
- destruir equipo
- impedir una Técnica dependiente de esa parte
- reducir movilidad
- alterar un patrón de comportamiento
- abrir un punto vulnerable
- cambiar una fase del encuentro

---

## Bloqueo

Cuando un golpe conecta contra una zona protegida, esa zona aporta **Bloqueo**.

```text
Bloqueo = BC + BM + CD + CO
```

| Componente | Significado |
| --- | --- |
| BC | Bloqueo base por categoría de armadura |
| BM | Bono de material |
| CD | Competencia Defensiva con la armadura de la zona |
| CO | Calidad o grado de la pieza |

| Armadura | BC |
| --- | ---: |
| Ligera | 2 |
| Intermedia | 4 |
| Pesada | 6 |

```text
BM = floor(Durabilidad / 10)
```

La Competencia Defensiva equivale al nivel de competencia en el tipo de armadura que protege la zona golpeada.

Solo se usa si esa armadura participa realmente en absorber el Impacto.

Una zona sin armadura no aporta Bloqueo de armadura.

---

## Umbral de Herida

Para convertir Impacto en Herida contra personajes jugadores, usa el **Umbral de Herida** de la zona.

```text
Umbral de Herida = max(Bloqueo, 1)
```

Este mínimo evita que una zona sin Bloqueo convierta cualquier golpe en Herida Crítica automática.

El Bloqueo sigue funcionando como protección normal. El Umbral de Herida solo sirve para determinar la gravedad de la Herida cuando el ataque ya conectó.

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

Cuando un PNJ golpea a un personaje jugador, no se usa HP general. El golpe se registra como una Herida en la zona impactada.

El orden de resolución es:

1. Determinar la zona golpeada.
2. Identificar la armadura de esa zona.
3. Resolver la Tirada de Defensa usando la Evasión aplicable y la Agilidad aplicable según la armadura de la zona.
4. Si el ataque conecta, tirar Impacto.
5. Calcular el Bloqueo de la zona.
6. Calcular el Umbral de Herida.
7. Comparar Impacto contra el Umbral de Herida.
8. Registrar la Herida si corresponde.

| Relación | Resultado | Ranuras |
| --- | --- | ---: |
| Impacto <= Umbral de Herida | Sin Herida | 0 |
| Impacto > Umbral de Herida y <= 2 × Umbral de Herida | Herida Leve | 1 |
| Impacto > 2 × Umbral de Herida y <= 3 × Umbral de Herida | Herida Grave | 2 |
| Impacto > 3 × Umbral de Herida | Herida Crítica | 3 |

Una Herida Crítica no fuerza una Tirada de Resistencia por defecto. Ya ocupa 3 ranuras y puede saturar o colapsar una zona por sí misma.

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
| Funcional | La zona tiene al menos 1 ranura libre | No aplica penalizador de zona por sí misma |
| Saturada | La zona llegó exactamente a su máximo de ranuras | Aplica Penalizador de Saturación |
| Colapsada | Una Herida no cupo completa o una zona Saturada recibió otra Herida | Aplica el efecto de Colapso de esa zona |

---

## Ejemplo

Un personaje tiene el Torso con 4 de 5 ranuras ocupadas.

Recibe una Herida Grave en el Torso, que debería ocupar 2 ranuras.

Solo queda 1 ranura libre, así que marca esa ranura y la otra produce Desbordamiento.

El Torso queda Colapsado.

---

## Penalizador de Saturación

Cuando una zona está Saturada, su penalizador base es igual a la cantidad de ranuras ocupadas en esa zona.

```text
Penalizador de Saturación = ranuras ocupadas en la zona
```

| Zona Saturada | Penalizador base |
| --- | ---: |
| Cabeza | -3 |
| Torso | -5 |
| Brazos | -4 |
| Piernas | -4 |
| Pies | -3 |

Este penalizador solo se aplica a tiradas y acciones que dependan claramente de esa zona.

No es un penalizador universal al personaje.

---

## Saturación y Colapso por zona

| Zona | Saturada | Colapsada |
| --- | --- | --- |
| Cabeza | Penalizador de Saturación a Tiradas de Especialización mentales y de percepción visual o auditiva. Penalizador de Saturación a Preparación. | Aplica Aturdido. Debe superar una Tirada de Resistencia de Alteración contra la severidad de la Herida que causó el Colapso o queda Inconsciente. |
| Torso | Penalizador de Saturación a Tolerancia, acciones físicas exigentes, defensas pesadas, mantener postura bajo Impacto y Técnicas que comprometan el torso. | Queda Incapacitado hasta estabilizarse. Si la Herida que causó el Colapso fue Crítica, también entra en Agonía. |
| Brazos | Penalizador de Saturación a Tiradas de Ataque, Tiradas de Impacto y Tiradas de Especialización físicas que dependan de brazos, agarre, escudo, armas o manipulación. | Un brazo, agarre o línea de ejecución queda inutilizado. No puede usar armas a dos manos, escudo o Técnicas ligadas a esa extremidad si dependen de la parte colapsada. Puede aplicar Impedido. |
| Piernas | Movimiento reducido a la mitad. Penalizador de Saturación a Tiradas de Especialización físicas de Fuerza o Tenacidad que dependan de piernas. | No puede caminar de forma funcional sin apoyo o ayuda. No puede cargar, correr ni saltar. |
| Pies | No puede correr. Penalizador de Saturación a Tiradas de Especialización físicas de Agilidad que dependan de apoyo fino. | Puede moverse solo con apoyo, ayuda o una Tirada de Especialización apropiada. Si intenta moverse bajo presión sin apoyo y falla, queda Derribado. |

La dificultad sugerida para la Tirada de Resistencia por Colapso depende de la Herida que causó el Desbordamiento.

| Herida que causó Colapso | Dificultad |
| --- | --- |
| Leve | Desafiante |
| Grave | Rigurosa |
| Crítica | Exigente |

---

## Estados Corporales

Los Estados Corporales describen la condición general de una criatura cuando el daño deja de ser solo local.

| Estado | Significado |
| --- | --- |
| Operativo | Puede actuar con los penalizadores que tenga por zona, Agravio, Fatiga o Desgaste |
| Incapacitado | No puede realizar acciones significativas. Puede hablar, arrastrarse, sostener algo o reaccionar débilmente si la ficción lo permite |
| Inconsciente | No puede actuar ni percibir de forma útil. No puede defenderse de forma activa |
| Agonía | Está en riesgo de morir si no recibe estabilización. No puede actuar de forma significativa |
| Muerto | La criatura deja de ser recuperable por medios normales de escena |

Si una zona ya Colapsada recibe otra Herida, se aplica o refresca el efecto de Colapso.

Si la zona es Cabeza o Torso, el personaje debe superar una Tirada de Resistencia de Alteración contra la severidad de la nueva Herida.

Si falla:

- Cabeza escala hacia Inconsciente
- Torso escala hacia Agonía

Si un personaje en Agonía recibe otra Herida Crítica en Cabeza o Torso, muere salvo que una regla específica, Técnica, intervención inmediata o decisión de mesa establezca otra salida.

---

## Zonas y localización

Para ataques de PNJs contra jugadores, la localización se determina antes de resolver la defensa. Esto evita que el Narrador elija siempre la zona más castigada.

| 1d100 | Zona |
| --- | --- |
| 01–04 | Cabeza |
| 05–10 | Pies |
| 11–45 | Torso |
| 46–65 | Brazos |
| 66–100 | Piernas |

Los ataques de jugadores contra PNJs no usan esta tabla por defecto. El jugador declara objetivo, intención, Técnica o punto vulnerable según lo permita la escena y la información disponible.

---

## Estabilizar, Tratar y Curar

Transcendence separa tres pasos de recuperación.

| Paso | Función | Libera ranuras |
| --- | --- | ---: |
| Estabilizar | Detiene deterioro inmediato, shock activo, sangrado abierto o Colapso que sigue empeorando | No |
| Tratar | Atiende una zona durante un Descanso Completo para preparar recuperación | No por sí mismo |
| Curar | Libera ranuras ocupadas como resultado de Descanso Completo con tratamiento exitoso | Sí |

Medicina cubre estabilizar, tratar y curar daño corporal.

Herboristería, alquimia, objetos, Técnicas y artefactos pueden modificar estas reglas desde sus propias secciones.

Cuando una Técnica no crea una Herida más severa sino un problema de tratamiento
o limpieza, la respuesta inmediata en combate suele resolverse con **Interactuar**
o **Usar Especialización** según exija o no diagnóstico y manejo entrenado. Eso
no sustituye **Estabilizar**, **Tratar** o **Curar**: solo resuelve el paso
previo que permite volver a ellos en condiciones limpias.

---

## Estabilización

Para estabilizar una Herida, un personaje realiza una Tirada de Especialización de Medicina con Sabiduría.

| Herida | Dificultad | Kit requerido | Tiempo |
| --- | --- | --- | --- |
| Leve | Desafiante | Básico | 30 minutos |
| Grave | Rigurosa | Avanzado | 60 minutos |
| Crítica | Exigente | Especializado | Descanso Completo |

En un éxito, la Herida queda estabilizada. Sus efectos inmediatos dejan de empeorar.

En un fallo, la Herida sigue activa y el intento puede consumir tiempo, recursos o abrir una complicación si la escena sigue bajo presión.

---

## Tratamiento y curación

Las Heridas deben estar estabilizadas antes de liberar ranuras. Una Herida activa primero debe estabilizarse.

| Descanso | Puede estabilizar | Puede tratar | Puede liberar ranuras |
| --- | --- | --- | ---: |
| 30 minutos | Herida Leve | No | 0 |
| 60 minutos | Herida Grave | No | 0 |
| Descanso Completo | Herida Crítica o cualquier Herida estabilizada | Sí, con Medicina | 1 ranura por personaje tratado |

Al tratar una zona durante un Descanso Completo, el personaje que atiende al paciente realiza una Tirada de Especialización de Medicina con Sabiduría.

La dificultad base y el kit dependen de la ranura más severa que todavía esté ocupada en esa zona.

| Ranura ocupada más severa | Dificultad | Kit requerido |
| --- | --- | --- |
| Leve | Desafiante | Básico |
| Grave | Rigurosa | Avanzado |
| Crítica | Exigente | Especializado |

Después, aumenta el Nivel de Referencia según cuántas ranuras estén ocupadas en la misma zona al inicio del Descanso Completo.

| Ranuras ocupadas en la zona | Ajuste |
| ---: | --- |
| 1 | Sin ajuste |
| 2–3 | +1 Nivel de Referencia |
| 4–5 | +2 Nivel de Referencia |
| Zona Colapsada | +1 Nivel de Referencia adicional |

En un éxito, el paciente libera 1 ranura ocupada de esa zona.

La ranura liberada debe pertenecer a una Herida estabilizada.

En un fallo, la zona no libera ranuras.

Cuando hay varias Heridas estabilizadas en la misma zona, quien realiza el tratamiento declara qué ranura intenta liberar antes de tirar.

El Narrador puede exigir que primero se libere una ranura de la Herida más severa si esa lesión mantiene Agonía, Colapso o una pérdida funcional dominante.

---

## Ejemplos de progresión

Una Herida Leve ocupa 1 ranura. Si está estabilizada y recibe tratamiento exitoso durante un Descanso Completo, libera esa ranura y desaparece.

Una Herida Grave ocupa 2 ranuras. Después de un Descanso Completo con tratamiento exitoso, libera 1 ranura y queda como Herida Leve. Necesita otro Descanso Completo con tratamiento exitoso para desaparecer.

Una Herida Crítica ocupa 3 ranuras. Después de un Descanso Completo con tratamiento exitoso, libera 1 ranura y queda como Grave. Después de otro Descanso Completo con tratamiento exitoso, queda como Leve. Después de otro, desaparece.

---

## Partes de criatura y enemigos

Los enemigos no tienen que usar las mismas zonas anatómicas que un personaje jugador. Una criatura importante usa las zonas que su anatomía y diseño de encuentro necesiten.

Por defecto, una criatura importante debería organizarse en cinco lugares principales para mantener lectura en mesa.

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
