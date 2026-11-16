# Capa de acceso canónico

**Estado:** base operativa verificada; ampliar de forma incremental por dominio.

Esta carpeta permite que las herramientas, módulos de campaña y el motor narrativo
consulten el Corebook canónico en español sin leer el repositorio entero. No sustituye
los textos editoriales ni crea una segunda versión del canon.

## Fuente de verdad

La fuente primaria es el Corebook en español bajo
`core-books/transcendence-corebook/**/es/`. La versión inglesa es un espejo editorial.
`Transcendence-design` no es una fuente de consulta automática: si una cuestión no se
puede resolver desde Publications, se registra como un vacío de canon.

## Flujo de consulta

```text
perfil de trabajo + dominio
        ↓
retrieval-profiles.yaml
        ↓
concept-registry.yaml + source-manifest.yaml
        ↓
paquete de contexto mínimo y trazable
        ↓
fragmentos exactos de las fuentes primarias, sólo si son necesarios
```

## Resolver local y pruebas

El resolvedor devuelve un conjunto mínimo, ordenado y trazable de referencias. No
lee ni resume capítulos: el consumidor abre sólo las rutas que devuelve.

```text
ruby canon/retrieval/resolve.rb --profile campaign_species_foundation --concept consagrado --verify
ruby canon/retrieval/resolve.rb --profile campaign_cosmology_and_horror --concept vestige --verify
ruby canon/retrieval/test-resolver.rb
```

- Un perfil aporta sus `baseline_concepts`.
- `--concept` añade una pregunta concreta.
- Las decisiones provisionales aprobadas sólo aparecen si declaran un concepto
  relacionado con la consulta.
- `--verify` comprueba rutas del manifiesto y la forma mínima de las decisiones.

Los casos en `test-cases.yaml` fijan consultas representativas. Al añadir una
fuente, concepto o decisión, se debe añadir o ajustar un caso que demuestre que
la consulta carga lo necesario y no material ajeno.

## Archivos

- `source-manifest.yaml`: rutas canónicas, dominio, audiencia y relaciones.
- `concept-registry.yaml`: conceptos compactos que apuntan a sus fuentes; no resume
  capítulos enteros.
- `retrieval-profiles.yaml`: rutas de consulta con presupuesto de contexto por tipo de
  trabajo.
- `ACCESS-POLICY.md`: reglas de autoridad, versionado y tratamiento de vacíos.

## Límites

- No indexar todo el Corebook en una primera pasada.
- No copiar reglas o lore completos en el registro.
- No usar búsqueda semántica ni embeddings antes de estabilizar los conceptos y fuentes.
- Todo resumen futuro debe enlazar sus fuentes y mantenerse en el mismo cambio que las
  modifica.
