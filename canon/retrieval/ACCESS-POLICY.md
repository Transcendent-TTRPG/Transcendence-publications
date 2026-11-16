# Política de acceso canónico

## Orden de autoridad

1. El Corebook en español de `Transcendence-publications` es la fuente de verdad para
   reglas, lore, especies y cosmología.
2. Los registros de esta carpeta sólo localizan, condensan y enlazan esa verdad.
3. El Corebook en inglés es una traducción o espejo editorial; no resuelve conflictos.
4. `Transcendence-design` es histórico y de trabajo. No se lee como respaldo implícito
   ni puede resolver una ambigüedad del Corebook publicado.
5. Una cuestión que Publications no cubre es un **vacío de canon**. Debe registrarse y
   resolverse mediante una revisión editorial explícita.
6. Una decisión aprobada por el creador y aún no integrada al Corebook se registra en
   `canon/decisions/registry.yaml`. Es autoridad provisional trazable, no texto publicado.

## Reglas de consumo

- Un consumidor empieza siempre por un perfil de consulta, no por una búsqueda global.
- El perfil define un presupuesto de contexto y el orden de fuentes.
- El registro entrega resúmenes compactos y rutas; el consumidor abre texto largo sólo
  cuando el resumen no basta para una decisión concreta.
- Los módulos fuente y las ejecuciones narrativas guardan el commit de Publications y
  las fuentes que consultaron. Ese conjunto es su snapshot canónico.

## Reglas de mantenimiento

- Toda entrada de concepto debe citar una o más rutas primarias.
- Un cambio de texto canónico que invalide un resumen, etiqueta o relación debe actualizar
  el registro en el mismo cambio.
- No se duplican tablas extensas, capítulos ni prosa editorial en los YAML.
- Una entrada puede declarar `summary_status: pending` mientras su fuente ya sea útil.
  La ausencia de resumen no autoriza una inferencia libre.
- Una decisión canónica aprobada debe pasar al Corebook y actualizar su estado a
  `integrated` cuando la edición publicada ya la contenga.
