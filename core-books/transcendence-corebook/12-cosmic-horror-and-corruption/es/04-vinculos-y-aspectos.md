---
title: "Vínculos y Aspectos"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 12
status: draft
canonical: false
tags: [limbo, vínculo, aspectos, caminos, convergencia, eco, cordura, disonancia, horror-cósmico]
related:
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/01-el-limbo.md
  - core-books/transcendence-corebook/12-cosmic-horror-and-corruption/es/02-el-descubrimiento.md
  - core-books/transcendence-corebook/11-ailments/es/03-aflicciones.md
  - core-books/transcendence-corebook/08-conflict-and-combat/es/02-desgaste-aguante-fatiga.md
authority_refs:
  - Transcendence-design/docs/system/limbo-entities.md
  - Transcendence-design/docs/system/attrition-fatigue.md
  - Transcendence-design/data/system/attrition-fatigue.yaml
---

# Vínculos y Aspectos

El vínculo reorganiza al portador, no lo amplía. Sus competencias siguen siendo suyas — el daño viene de sus armas, la resistencia de su constitución — pero el vínculo estructura cómo todo eso se expresa. La entidad aporta la forma, no la fuerza.

---

## Aspectos

Los **Aspectos** son las expresiones concretas de un vínculo — lo que el portador puede hacer mientras la conexión está activa. No son habilidades independientes: están definidas por la naturaleza de la entidad, el sentido vinculado y la etapa del camino activa en ese momento.

Cada Aspecto tiene un coste de **Eco** definido en su propia entrada, de la misma forma en que cada acción tiene su coste de Desgaste. El coste depende de lo que el Aspecto hace — no hay una escala universal. Un Aspecto que altera el entorno de forma menor cuesta menos que uno que reestructura cómo el portador se mueve en el espacio durante toda una escena.

---

## Caminos

Cada sentido vinculado a un vínculo corresponde a un **camino** — una línea de escalado con su propia temática dentro de la identidad central del vínculo. Los caminos son completamente independientes: acceder a uno no requiere canal activo en los otros.

Cada camino tiene tres etapas, acumulativas, determinadas por la severidad de la Aflicción del portador en ese sentido:

| Severidad de Aflicción | Acceso al camino |
| --- | --- |
| **Leve** | Primera expresión — limitada pero real |
| **Moderado** | El efecto se expande: más alcance, duración, control o precisión |
| **Grave** | La expresión máxima — la versión más extrema de lo que ese sentido hace posible |

Si la Aflicción del portador en el sentido vinculado baja de umbral — por recuperación — el acceso al camino retrocede a la etapa correspondiente.

Ningún vínculo tiene más poder que otro. La escala de lo que un vínculo puede hacer no viene de la entidad sino de las Aflicciones del portador: cuanto más profundo el canal, más profunda la expresión.

---

## Convergencia

Cuando un vínculo está vinculado a más de un sentido y el portador ha descubierto todos sus caminos, se desbloquea la **convergencia**: el efecto que ningún camino produce por separado, la síntesis de ambos operando al mismo tiempo.

La potencia de la convergencia usa la **severidad mínima** entre todos los sentidos activos del vínculo. Un portador con Aflicción Grave en Vista y Aflicción Leve en Tacto accede a la convergencia en etapa Leve — no en la máxima.

La convergencia no es automática ni siempre activa. Es una activación propia con su propio coste de Eco.

---

## Eco, Cordura y Disonancia

El uso de vínculos opera en un track psíquico paralelo al track físico de Desgaste y Fatiga. Los dos acumulan de forma independiente — la Fatiga no afecta al Eco y la Disonancia no afecta al Desgaste. Pero el overflow en cualquiera de los dos deja al personaje **Inconsciente**: no es un AND, es un OR.

| | Track físico | Track psíquico |
| --- | --- | --- |
| Acumulado | Desgaste | **Eco** |
| Reserva | Aguante | **Cordura** |
| Consecuencia asentada | Fatiga | **Disonancia** |
| Overflow | Inconsciente | Inconsciente |

### Eco

El **Eco** es la carga psíquica acumulada que genera cada activación de un Aspecto. No representa daño — representa el residuo del vínculo presionando la realidad perceptual del portador. El Eco se proyecta durante la escena y se asienta cuando termina, igual que el Desgaste.

### Cordura

La **Cordura** es cuánta carga psíquica puede absorber el personaje antes de sufrir Disonancia.

```text
Cordura = 3 + (Compostura × 2)
```

Valor mínimo: `3`.

### Disonancia

La **Disonancia** es el deterioro progresivo de la coherencia perceptual cuando el Eco supera lo que la Cordura puede sostener. No surge de una sola activación — surge de acumulación. A medida que el Eco crece, la mente pierde precisión en lo que percibe a través del vínculo: primero lo más fino del procesamiento cognitivo, luego el acceso a las profundidades mayores, finalmente la capacidad de sostener múltiples canales a la vez.

#### Umbrales

| Nivel | Condición |
| --- | --- |
| Disonancia 0 | Eco < Cordura |
| Disonancia 1 | Eco ≥ Cordura |
| Disonancia 2 | Eco ≥ 2 × Cordura |
| Disonancia 3 | Eco ≥ 3 × Cordura |
| Disonancia 4 | Eco ≥ 4 × Cordura |
| Disonancia 5 | Eco ≥ 5 × Cordura |

#### Efectos

Los efectos son acumulativos — cada nivel añade algo distinto al anterior.

| Nivel | Efecto |
| --- | --- |
| **Disonancia 1** | Las T.E. de categoría mental y de saberes requieren una T.R. de Compostura previa. Si falla, la T.E. se pierde. |
| **Disonancia 2** | Los Aspectos de etapa Grave no están disponibles, independientemente de la severidad de Aflicción. |
| **Disonancia 3** | Todas las activaciones de Aspecto cuestan +1 Eco adicional. |
| **Disonancia 4** | Los vínculos con más de un camino quedan completamente inutilizables. Solo los vínculos de camino único siguen disponibles. |
| **Disonancia 5** | Los Aspectos solo resuelven su etapa Leve. Los efectos de etapa Moderado y Grave no se activan. El vínculo sigue respondiendo, pero la mente no puede procesar la percepción profunda en acción. |
| **Overflow** | **Inconsciente** — el cerebro activa el corte automático. El personaje pierde consciencia. Todos los vínculos quedan suspendidos hasta descansar o recibir ayuda. Las Aflicciones acumuladas durante el proceso permanecen. |

---

## Requisitos de acceso

Para activar un Aspecto de un vínculo, el portador debe cumplir dos condiciones simultáneas:

**NR mínimo** según el nivel de la entidad:

| Nivel de entidad | NR mínimo |
| --- | --- |
| Fragmento | 1 |
| Entidad | 3 |
| Soberano | 5 |
| Abismal | condición narrativa — sin NR que lo haga accesible |

El NR es el promedio de los rangos de todas las competencias del personaje. Es el umbral de capacidad necesario para sostener la conexión.

**Aflicción activa** en el sentido vinculado, con la severidad mínima especificada por la entrada del vínculo. El NR es la capacidad de sostener la conexión. La Aflicción es la llave que la abre.

Sin una de las dos condiciones, el vínculo no puede activarse.

---

## Aflicciones durante el uso

La Aflicción de un portador de vínculo crece durante el descubrimiento, no durante el uso. Esa es la diferencia central con los vestigos:

- **Vestigo**: cada uso puede aumentar la Aflicción del portador en el sentido vinculado.
- **Vínculo**: el uso acumula Eco. La Aflicción no aumenta por el uso.

El canal se construyó durante el descubrimiento — ese proceso dejó las Aflicciones que determinan a qué etapas de los caminos tiene acceso el portador. Una vez completo, activar Aspectos no lo desgasta perceptualmente. Lo que desgasta es el Eco que el vínculo presiona sobre la mente mientras la conexión está activa.

Las Aflicciones del portador pueden seguir cambiando — por otros vestigos, por exposición ambiental, por recuperación — y esos cambios afectan qué etapas de los caminos están disponibles. Pero el uso del vínculo no los genera.