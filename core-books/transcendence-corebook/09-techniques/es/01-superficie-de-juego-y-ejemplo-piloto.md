---
title: "Como Leer una Tecnica"
type: corebook
content_kind: rules
writing_mode: rules
language: es
chapter: 9
status: draft
canonical: false
tags: [techniques, cards, play-surface, publication, pilot]
authority_refs:
  - Transcendence-design/docs/system/technique-play-surface.md
  - Transcendence-design/docs/system/techniques.md
  - Transcendence-design/data/system/techniques.yaml
related:
  - core-books/transcendence-corebook/09-techniques/es/README.md
---

# Como Leer una Tecnica

Una **Tecnica** es una aplicacion entrenada y concreta de una competencia.

No es una accion generica ni una mejora pasiva indefinida. Una Tecnica dice:

- cuando puede usarse
- que costo tiene
- que condiciones reales del juego deben cumplirse
- y que efecto produce si resuelve

Cada Tecnica del juego deberia poder leerse con rapidez en mesa. Por eso, su
bloque final presenta siempre la misma clase de informacion:

- `Tipo - Categoria`
- `Nombre`
- `Rango de competencia`
- `Flavor text`
- `Rango`
- `Area`
- `Duracion`
- `Tirada principal`
- `Salvacion`, si existe una tirada separada que anule el efecto
- `Impacto`, si la Tecnica resuelve `I.R.` o un payload equivalente
- `Ritmo`
- `Desgaste`
- `Requisitos`
- `Keywords`
- `Efecto`

---

## Generalidades

### Tipo y categoria

El **tipo** indica como entra la Tecnica en la escena:

- `Activa`
- `Reaccion`
- `Pasiva`

La **categoria** resume su uso principal:

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

Si una condicion no es un mecanismo real del juego, normalmente no deberia
aparecer aqui.

### Keywords

Las **keywords** sirven para destacar informacion util que no este ya visible
en el resto del bloque.

No hace falta repetir:

- `Reaccion` si ya aparece en `Tipo`
- `Ataque` si ya aparece en `Categoria`

### Efecto

El **efecto** debe decir con claridad:

- que pasa cuando la Tecnica entra en juego
- que tirada se hace
- que pasa si funciona
- y que pasa si falla, cuando eso importe

---

## Lista actual

Las Tecnicas de esta seccion se presentan una por una con este formato.

Entrada piloto actual:

- `Cerrar la Línea`

Con el tiempo, esta lista deberia crecer por especie, perfil y dominio de uso,
pero todas las entradas deberian conservar la misma superficie de lectura.
