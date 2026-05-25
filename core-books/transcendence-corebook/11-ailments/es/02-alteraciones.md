---
title: "Alteraciones"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 11
status: draft
canonical: false
tags: [ailments, alteraciones, alterations, conditions, catalog, combat]
related:
  - core-books/transcendence-corebook/11-ailments/en/02-alterations.md
  - core-books/transcendence-corebook/11-ailments/es/01-agravios.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/03-acciones.md
  - core-books/transcendence-corebook/09-techniques/es/01-superficie-de-juego-y-ejemplo-piloto.md
authority_refs:
  - Transcendence-design/docs/system/ailments.md
  - Transcendence-design/data/system/ailments.yaml
---

# Alteraciones

Las **Alteraciones** son disrupciones fisiológicas que comprometen directamente la función del cuerpo. Son la capa principal de estados de combate del sistema.

Una Alteración puede tener origen físico, ambiental, mental, por criatura o anómalo — lo que la define es que el resultado es una disrupción operativa directa del cuerpo durante el juego.

**Tirada de Resistencia:** `1d10 + Resiliencia + nivel de competencia en Resistencia a Alteraciones + bonificadores adicionales`

Los efectos de cada Alteración son **acumulativos por severidad**: Moderado incluye todo lo de Leve, Grave incluye todo lo de Moderado.

---

## Asfixiado

*El objetivo no puede respirar correctamente y lucha por mantenerse operativo.*

**Aplicación:** Asfixia, ahogamiento, inhalación de humo, presión aplastante u otra fuente que impida la respiración de forma creíble.

**Duración:** Mientras persista la fuente.

**Recuperación:** Termina cuando la fuente que impide la respiración deja de actuar. La penalización acumulativa se reinicia al terminar el estado.

| Severidad | Efectos |
| --- | --- |
| **Leve** | Al inicio de cada activación, `T.E.` de Tolerancia contra la severidad original o queda incapacitado esa activación. Penalización acumulativa de `−1` a todas las tiradas por cada activación transcurrida bajo Asfixiado. |
| **Moderado** | Leve, más: `Preparación` se convierte en `0`. No puede correr, gritar con fuerza, mantener esfuerzo prolongado ni usar acciones claramente dependientes de la respiración sin superar primero la `T.E.` de Tolerancia. |
| **Grave** | Moderado, más: si falla la `T.E.` de Tolerancia al inicio de la activación, queda Incapacitado. |

---

## Aterrorizado

*El cuerpo y el juicio operativo inmediato del objetivo son tomados por terror agudo.*

**Aplicación:** Una criatura, Técnica, revelación de escena, presencia hostil, exhibición grotesca, amenaza de contaminación o presencia de depredador que crea una línea de terror inmediata que el cuerpo trata como peligro urgente.

**Duración:** Mientras persista la condición.

**Recuperación:** Termina cuando la línea de terror es materialmente rota, desmentida, eliminada o deja de ser funcionalmente relevante; o cuando supera una `T.E.` de Contención contra la severidad original para recuperar suficiente control interno.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.A.`, `T.D.`, `T.C.` y `T.E.` que se oponen directamente, se acercan, manejan o comprometen hacia la fuente temida sufren una penalización igual al bonificador de rango de la fuente que aplicó Aterrorizado. |
| **Moderado** | Leve, más: no puede reducir voluntariamente la distancia a la fuente temida ni comprometerse deliberadamente sin superar primero una `T.E.` de Contención contra la severidad original. |
| **Grave** | Moderado, más: para realizar cualquier acción, debe superar primero una `T.E.` de Contención contra la severidad original; si falla, la acción no se resuelve. |

---

## Atrapado

*El cuerpo está físicamente retenido o estructuralmente impedido de moverse con libertad.*

**Aplicación:** Agarre o sujeción de criatura, red o mecanismo de restricción, peligro adhesivo, superficie en colapso u otra fuente que retiene físicamente al objetivo de forma creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Termina cuando el objetivo se libera, es soltado o la fuente deja de retenerlo. La recuperación preferida es una `T.E.` de Agarre contra una sujeción viva, u otra `T.E.` de Agilidad si la ficción trata más de deslizarse o desenredarse que de superar un contacto.

| Severidad | Efectos |
| --- | --- |
| **Leve** | Movimiento `0`. `T.A.`, `T.I.`, `T.D.` y `T.E.` de Agilidad sufren penalización igual al bonificador de rango de la fuente que aplicó Atrapado. |
| **Moderado** | Leve, más: no puede usar acciones con costo de ritmo superior a 4 sin superar primero una `T.E.` de Agarre contra la severidad original. |
| **Grave** | Moderado, más: para realizar cualquier acción, debe superar primero esa `T.E.` de Agarre; si falla, la acción no se resuelve. |

---

## Aturdido

*El objetivo está aturdido lo suficiente para perder su próxima activación significativa.*

**Aplicación:** Impacto, shock neural, fuerza de concusión, sobrecarga u otra fuente que brevemente cierra la acción limpia de forma creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Leve termina tras consumir la primera activación perdida. Moderado y Grave terminan con una `T.E.` de Tolerancia exitosa contra la severidad original después de una activación perdida, o cuando el tratamiento o eliminación de la fuente restaura la continuidad operativa.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.R.` y `T.C.` sufren penalización igual al bonificador de rango de la fuente que aplicó Aturdido. La próxima activación del objetivo se pierde. |
| **Moderado** | Leve, más: mientras Aturdido permanezca activo, `Preparación` se convierte en `0`. Tras cada activación perdida consumida, debe superar una `T.E.` de Tolerancia contra la severidad original o Aturdido permanece activo y consume la siguiente activación también. |
| **Grave** | Moderado, más: mientras Aturdido permanezca activo, no puede usar reacciones voluntariamente sin superar primero esa `T.E.` de Tolerancia. |

---

## Cegado

*El objetivo no puede ver.*

**Aplicación:** Luz, trauma, escombros, oscuridad impuesta como estado del cuerpo, daño ocular u otra fuente que elimina funcionalmente la visión. Usar Cegado solo cuando la visión deja de ser un sentido primario utilizable; si una fuente solo ensucia una línea ocular, un punto de lectura o un canal visual acotado, usar un estado procedimental en su lugar.

**Duración:** Hasta eliminar.

**Recuperación:** Termina cuando la fuente de ceguera se disipa, es eliminada o la visión es restaurada. Cuando se necesita restauración corporal real, `T.E.` de Medicina es la recuperación preferida.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `−5` a todas las `T.A.`, `T.D.`, `T.C.` y `T.E.` |
| **Moderado** | `−5` a todas las `T.A.`, `T.D.`, `T.C.` y `T.E.` |
| **Grave** | `−5` a todas las `T.A.`, `T.D.`, `T.C.` y `T.E.` |

*La severidad gobierna principalmente la presión de aplicación y la dificultad de recuperación, no el tamaño de la penalización.*

---

## Confundido

*El objetivo pierde el juicio limpio y no puede distinguir con fiabilidad aliados, enemigos o intención en la escena inmediata.*

**Aplicación:** Shock corporal, sobrecarga sensorial, disrupción neural, concusión, toxinas u otra fuente que desestabiliza el juicio operativo inmediato de forma creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Termina con una `T.E.` de Enfoque exitosa contra la severidad original una vez que regresa suficiente claridad operativa. `Medicina` o la eliminación de la fuente desestabilizadora también pueden terminarlo si la ficción lo justifica.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.A.`, `T.I.` y `T.E.` de Intelecto o Compostura que requieren discriminación, identificación de objetivo o lectura de intención sufren penalización igual al bonificador de rango de la fuente que aplicó Confundido. |
| **Moderado** | Leve, más: antes de poder elegir deliberadamente una criatura, bando o línea operativa específica en una escena concurrida, ambigua o cambiante, debe superar primero una `T.E.` de Enfoque contra la severidad original. |
| **Grave** | Moderado, más: para elegir deliberadamente una criatura, debe superar primero esa `T.E.` de Enfoque; si falla, el objetivo será la criatura más próxima, aun si es un aliado. |

---

## Congelado

*El frío se ha asentado en el cuerpo lo suficiente como para comprometer la temperatura, la respuesta motora y el movimiento ágil.*

**Aplicación:** Exposición prolongada a congelación, efecto hostil basado en hielo u otra fuente que deteriora funcionalmente el cuerpo por frío de forma creíble.

**Duración:** Mientras persista la condición.

**Recuperación:** Termina cuando la temperatura corporal sube y el objetivo ya no está funcionalmente deteriorado por el frío. Si la fuente de frío ya no impone activamente el estado, una `T.E.` de Aclimatación exitosa contra la severidad original suele terminar la Alteración; `Medicina` puede asistir cuando el tratamiento forma parte de la ficción.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.C.` de Agilidad y `T.E.` de Agilidad sufren penalización igual al bonificador de rango de la fuente que aplicó Congelado. Movimiento reducido a la mitad. |
| **Moderado** | Leve, más: no puede correr, saltar, trepar ni usar tecnicas que otorguen movimiento adicional sin superar primero una `T.E.` de Aclimatación contra la severidad original. |
| **Grave** | Moderado, más: al inicio de su activación, debe superar la `T.E.` de Aclimatación contra la severidad original; si falla, pierde la activación. |

---

## Conmocionado

*Un golpe o shock desestabilizador ha comprometido la claridad del objetivo, su estabilidad mental y su continuidad cognitiva.*

**Aplicación:** Impacto, shock interno, fuerza de explosión, colisión u otra fuente que produce una desestabilización similar a una conmoción de forma creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Termina cuando el objetivo recupera suficiente estabilidad interna para restaurar la claridad. La recuperación preferida es una `T.E.` de Contención contra la severidad original; `Medicina` también puede terminar el estado, y el descanso completo puede eliminarlo entre escenas si la ficción lo justifica.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.C.` y `T.E.` de Compostura e Intelecto sufren penalización igual al bonificador de rango de la fuente que aplicó Conmocionado. |
| **Moderado** | Leve, más: `Preparación` se convierte en `0`. |
| **Grave** | Moderado, más: para usar `T.C.` o `T.E.` basada en Compostura o Intelecto, debe superar primero una `T.E.` de Contención contra la severidad original; si falla, la acción no se resuelve. |

---

## Derribado

*El objetivo pierde el equilibrio o la postura corporal estable y cae al suelo.*

**Aplicación:** Impacto, barrido, transferencia de fuerza, colapso de terreno, colisión u otra causa creíble que tira al objetivo al suelo.

**Duración:** Hasta eliminar.

**Recuperación:** Termina cuando el objetivo se levanta, usando su primera acción de movimiento para ponerse en pie.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `−3` a todas las tiradas. La primera acción de movimiento se gasta levantándose. |
| **Moderado** | `−3` a todas las tiradas. La primera acción de movimiento se gasta levantándose. |
| **Grave** | `−3` a todas las tiradas. La primera acción de movimiento se gasta levantándose. |

*La severidad gobierna principalmente la dificultad de resistir o evitar el derribo, no la intensidad del estado una vez que el objetivo ya está en el suelo.*

---

## Desequilibrado

*La postura y la estabilidad corporal del objetivo están comprometidas.*

**Aplicación:** Pérdida de equilibrio o impulso, shock corporal, suelo inestable u otra fuente que compromete el movimiento estable y la defensa de forma creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Termina con una `T.E.` de Equilibrio exitosa contra la severidad original.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.D.` y `T.E.` de Agilidad sufren penalización igual al bonificador de rango de la fuente que aplicó Desequilibrado. |
| **Moderado** | Leve, más: para correr, usar reacciones, ó `T.E.` de Fuerza o Agilidad, debe superar primero una `T.E.` de Equilibrio contra la severidad original; si falla, la `T.E.` no se resuelve. |
| **Grave** | Moderado, más: si falla esa `T.E.` de Equilibrio, queda inmediatamente Derribado en lugar de simplemente perder el intento. |

---

## Desorientado

*El objetivo pierde la certeza direccional y la orientación mental.*

**Aplicación:** Disrupción espacial, saturación sensorial, mareos, perspectiva inestable u otra fuente que rompe el sentido de dirección del objetivo de forma creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Termina con una `T.E.` de Orientación exitosa contra la severidad original.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.E.` de Intelecto o Compostura sufren penalización igual al bonificador de rango de la fuente que aplicó Desorientado. |
| **Moderado** | Leve, más: `Preparación` se convierte en `0`. |
| **Grave** | Moderado, más: para usar una acción que requiera `T.E.` de Intelecto o Compostura, debe superar primero una `T.E.` de Orientación contra la severidad original; si falla, la `T.E.` no se resuelve. |

---

## Electrizado

*La disrupción eléctrica causa pérdida de continuidad muscular, respuesta de descarga involuntaria y ejecución física degradada.*

**Aplicación:** Descarga eléctrica significativa, exposición conductora prolongada u otra fuente de shock corporal creíble.

**Duración:** Mientras persista la condición.

**Recuperación:** Termina cuando la descarga se neutraliza o se interrumpe el tiempo suficiente para que el cuerpo recupere la continuidad. Una `T.E.` de Tolerancia exitosa contra la severidad original suele terminar el estado una vez que la fuente ya no está activa.

| Severidad | Efectos |
| --- | --- |
| **Leve** | Ataques, movimiento y Técnicas vinculadas a ataque o movimiento cuestan Ritmo adicional igual al bonificador de rango de la fuente. `T.E.` de Agilidad sufren esa misma penalización. |
| **Moderado** | Leve, más: no puede usar Reacciones sin superar primero una `T.E.` de Tolerancia contra la severidad original. |
| **Grave** | Moderado, más: para realizar cualquier acción, debe superar primero esa `T.E.` de Tolerancia; si falla, la acción no se resuelve. |

---

## Ensordecido

*La audición del objetivo está funcionalmente deteriorada o perdida.*

**Aplicación:** Trauma sónico, shock de presión interna, fuerza de explosión, sobrecarga ambiental u otra fuente que disrumpe la función auditiva lo suficiente para que el oído deje de ser un sentido primario utilizable. Usar Ensordecido solo cuando la audición ya no es utilizable; si una fuente solo ensucia una línea auditiva, un oído, un eco o un canal acotado, usar un estado procedimental en su lugar.

**Duración:** Hasta eliminar.

**Recuperación:** Termina cuando la función auditiva regresa o el objetivo ya no está funcionalmente ensordecido. Si la fuente ya no está activa, una `T.E.` de Medicina es la vía preferida; de lo contrario, el estado persiste hasta que el tiempo, el tratamiento o la eliminación de la fuente lo hagan creíble.

| Severidad | Efectos |
| --- | --- |
| **Leve** | No puede realizar `T.C.` o `T.E.` que requieran audición. No puede apoyarse en señales auditivas para responder a amenazas que no vio. |
| **Moderado** | No puede realizar `T.C.` o `T.E.` que requieran audición. No puede apoyarse en señales auditivas para responder a amenazas que no vio. |
| **Grave** | No puede realizar `T.C.` o `T.E.` que requieran audición. No puede apoyarse en señales auditivas para responder a amenazas que no vio. |

*La severidad gobierna principalmente la presión de aplicación y la dificultad de recuperación.*

---

## Impedido

*El objetivo no puede ejecutar Técnicas de arma con limpieza.*

**Aplicación:** Disrupción corporal, interferencia neural, bloqueo por dolor, agarre inestable u otra fuente que impide la ejecución de técnicas de arma sin paralizar completamente al objetivo.

**Duración:** Hasta eliminar.

**Recuperación:** Termina con una `T.E.` de Enfoque exitosa contra la severidad original una vez que el objetivo puede restablecer la ejecución, o cuando la fuente que impide la ejecución ya no aplica.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.A.`, `T.I.` basadas en arma y `T.E.` de Agilidad sufren penalización igual al bonificador de rango de la fuente que aplicó Impedido. |
| **Moderado** | Leve, más: para realizar un ataque con arma, interceptar, recargar o re-preparar, debe superar primero una `T.E.` de Enfoque contra la severidad original; si falla, la acción no se resuelve. |
| **Grave** | Moderado, más: no puede usar Técnicas vinculadas a competencias de arma. |

---

## Lacerado

*El objetivo ha sido desgarrado, cortado o herido de un modo que hace más lenta la ejecución física exigente porque el movimiento debe proteger, compensar o empujar a través del tejido dañado.*

**Aplicación:** Corte profundo o laceración, mordedura o zarpazo desgarrador, contacto con arma con gancho o sierra, herida abierta bajo presión física u otra fuente de disrupción de tejido dolorosa y creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Termina cuando el objetivo dedica una acción apropiada a vendar, apuntalar, cerrar, endurecer o estabilizar la presión de la herida. `Medicina` puede terminar el estado cuando el tratamiento forma parte de la ficción.

| Severidad | Efectos |
| --- | --- |
| **Leve** | Técnicas de ataque o movimiento y `T.E.` de Fuerza o Agilidad cuestan Ritmo adicional igual al bonificador de rango de la fuente que aplicó Lacerado. |
| **Moderado** | Leve, más: para usar Técnicas de ataque o movimiento o `T.E.` de Fuerza o Agilidad, debe superar primero una `T.E.` de Tolerancia contra la severidad original; si falla, la acción no se resuelve. |
| **Grave** | Moderado, más: para realizar cualquier acción, debe superar primero esa `T.E.` de Tolerancia; si falla, la acción no se resuelve. |

---

## Paralizado

*El cuerpo pierde la capacidad de ejecutar acciones significativas por cierre neuromuscular, bloqueo rígido o arresto corporal equivalente.*

**Aplicación:** Electricidad, veneno, bloqueo por frío, shock corporal, supresión forzada u otra fuente que detiene de forma creíble la acción significativa.

**Duración:** Hasta eliminar.

**Recuperación:** Termina cuando el control corporal regresa. La recuperación preferida es una `T.E.` de Tolerancia contra la severidad original una vez que la fuente ya no bloquea completamente el cuerpo; algunas fuentes pueden requerir su propia condición de liberación antes de que sea posible cualquier tirada.

| Severidad | Efectos |
| --- | --- |
| **Leve** | El objetivo no puede realizar acciones. |
| **Moderado** | El objetivo no puede realizar acciones. |
| **Grave** | El objetivo no puede realizar acciones. |

*La severidad gobierna principalmente la dificultad de aplicar, resistir o romper el estado. Usar Paralizado solo cuando la acción corporal significativa está realmente detenida; usar Atrapado para retención, Aturdido para activación perdida, e Impedido para ruptura de ejecución que deja al cuerpo aún activo.*

---

## Sobrecargado

*El objetivo está desbordado por presión sensorial, neural o interna excesiva.*

**Aplicación:** Saturación sensorial, sobrecarga interna, desbordamiento psíquico expresado a través del cuerpo u otra fuente que rompe la regulación funcional de forma creíble.

**Duración:** Hasta eliminar.

**Recuperación:** Termina con una `T.E.` de Contención exitosa contra la severidad original, o cuando la fuente de sobrecarga termina y el objetivo recupera suficiente regulación interna.

| Severidad | Efectos |
| --- | --- |
| **Leve** | `T.R.` sufren penalización igual al bonificador de rango de la fuente que aplicó Sobrecargado. |
| **Moderado** | Leve, más: no puede usar voluntariamente `T.E.` de Aura o Compostura sin superar primero una `T.E.` de Contención contra la severidad original. |
| **Grave** | Moderado, más: para realizar cualquier `T.E.`, debe superar primero esa `T.E.` de Contención; si falla, la `T.E.` no se resuelve. |
