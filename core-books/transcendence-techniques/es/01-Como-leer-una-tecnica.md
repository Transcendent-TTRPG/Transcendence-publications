---
title: "Cómo Leer una Técnica"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, cards, play-surface, publication, pilot, no-hereda-efectos]
authority_refs:
  - Transcendence-design/docs/system/technique-play-surface.md
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/README.md
---

# Cómo Leer una Técnica

Una **Técnica** es una aplicación entrenada y concreta de una competencia.

No es una acción genérica ni una mejora pasiva indefinida. Una Técnica dice:

- cuándo puede usarse
- qué costo tiene
- qué condiciones reales del juego deben cumplirse
- qué efecto produce si resuelve

El bloque de cada Técnica presenta siempre la misma información:

- `Tipo - Categoría`
- `Nombre`
- `Rango de competencia`
- `Texto de ambientación`
- `Rango`
- `Área`
- `Duración`
- `Tirada principal`
- `Salvación`, si existe una tirada separada que anule el efecto
- `Impacto`, si la Técnica resuelve una `T.I.` o efecto de daño equivalente
- `Ritmo`
- `Desgaste`
- `Requisitos`
- `Keywords`
- `Efecto`

---

## Generalidades

### Tipo y categoría

El **tipo** indica cómo entra la Técnica en la escena:

- `Activa`
- `Reacción`
- `Pasiva`

La **categoría** resume su uso principal:

- `Ataque`
- `Utilidad`

### Requisitos

Los requisitos deben decir solo condiciones reales del juego.

Buenos requisitos:

- perfil de arma
- objetivo en movimiento
- objetivo en rango
- equipo requerido
- estado requerido

### Keywords

Las **keywords** sirven para destacar información útil que no esté ya visible en el resto del bloque.

### Efecto

El **efecto** determina:

- qué pasa cuando la Técnica entra en juego
- qué tirada se hace
- qué pasa si funciona
- qué pasa si falla

### Técnicas y armas

Cuando una Técnica se resuelve mediante un **ataque** usando un arma fabricada o un arma natural, puede que herede o no los efectos y bonificadores pasivos de esa arma, dependiendo de cómo se estructure la técnica.

Existen dos categorías de resolución para las técnicas de ataque:

#### 1. Resolución Normal (Hereda)

La Técnica es, en su núcleo, un ataque normal. Puede que permita un reposicionamiento después, un estado extra o un contraataque, pero el flujo del impacto sigue las físicas de tu arma. 

Se reconoce porque la técnica usa explícitamente esta frase (o una variación muy similar):
> *"Si impacta, resuelve la T.I. normalmente. Este ataque conserva los efectos y bonificadores inherentes del arma usada."*

En esta categoría, tu arma **aplica todos sus bonos pasivos** (ej: ignorar Bloqueo, +1 a Impacto). Si usas un arma natural (o un arma con efecto por umbral) y superas la Tirada de Defensa enemiga por 3 o más, detonas el efecto especial de tu arma **además** de cualquier cosa que haga la técnica.

#### 2. Resolución Propia (No Hereda)

La técnica usa el alcance o el perfil de tu arma, pero su ejecución es anormal o hiper-específica. (Por ejemplo: golpear el suelo para levantar escombros, o forzar la hoja en un ángulo letal garantizado). La técnica secuestra la física del arma y la sustituye por una rutina completamente nueva.

Se reconoce porque la técnica no habla de daño normal, o porque usa explícitamente esta cláusula de protección:
> *"Esta técnica utiliza el perfil de tu arma, pero su ejecución es una resolución propia. No hereda ni dispara los efectos y bonificadores inherentes del arma usada."*

En esta categoría, el arma es solo un implemento. No suma bonificadores pasivos ni detona estados de arma natural, sin importar qué tan alto ruedes. Solo ocurre el efecto explícito descrito por la técnica.

### Armas naturales y armas fabricadas

Las armas fabricadas y las armas naturales siguen esta misma lógica binaria. 

- Las **armas fabricadas** tienden a tener bonificadores numéricos pasivos que brillan siempre en las Técnicas de Resolución Normal.
- Las **armas naturales** tienden a aplicar estados letales (Veneno, Lacerado). Son más raras de detonar porque exigen superar la T.D. por un gran margen, pero si lo logras durante una Técnica de Resolución Normal, obtienes un apilamiento masivo de efectos que recompensa tu maestría.

### Duración

La duración de una Técnica describe cuánto tiempo permanece activo su efecto.

- `Instantáneo`: el efecto ocurre y termina en el mismo momento en que la Técnica resuelve. No hay nada que mantener ni rastrear.
- `Permanente`: el efecto persiste hasta que se cumpla una condición de fin descrita en el propio texto de la Técnica. Siempre hay al menos una condición explícita.

**Toda Técnica con duración `Permanente` termina automáticamente cuando el combate concluye**, salvo que su efecto sea claramente relevante fuera de él. La adrenalina cesa, el cuerpo recupera su estado basal y los estados sostenidos por la activación dejan de mantenerse. Las condiciones de fin adicionales descritas en el texto de cada Técnica aplican también durante el combate.
