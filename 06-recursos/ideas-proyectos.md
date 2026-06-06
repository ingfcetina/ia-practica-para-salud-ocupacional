# Ideas de ampliación y proyectos

tags: #proyectos #ideas #practica #salud-ocupacional

Estas ideas sirven para continuar después del taller. Todas deben hacerse con **datos sintéticos, agregados o anonimizados**.

## Cómo convertir una idea en proyecto

Usa esta secuencia:

```text
1. Problema profesional
2. Datos seguros disponibles
3. Resultado esperado
4. Primer prototipo pequeño
5. Validación humana
6. Mejora iterativa
```

Antes de pedir código a una IA, escribe:

- qué problema quieres resolver;
- quién usará el resultado;
- qué datos usarás;
- qué datos no debes usar;
- cómo sabrás si el resultado es útil.

## Proyecto 1: tablero de ausentismo sintético

### Objetivo

Crear un tablero simple con días de ausencia por área, mes y motivo agregado.

### Datos sugeridos

- `assets/datos/ausentismo_ejemplo.csv`
- `assets/datos/indicadores_dashboard_ejemplo.csv`

### Cómo hacerlo

1. Lee los datos con Python.
2. Agrupa por `area` y `mes`.
3. Crea gráficos de barras y líneas.
4. Escribe tres preguntas para investigar antes de decidir.
5. Pide a una IA que convierta los resultados en un resumen prudente.

### Prompt sugerido

```text
Quiero crear un dashboard básico con datos sintéticos de ausentismo.
Usa Python, pandas y matplotlib.
Necesito gráficos simples, comentarios para principiantes y una advertencia de que no se pueden inferir causas sin más evidencia.
```

## Proyecto 2: clasificador de incidentes sintéticos

### Objetivo

Clasificar descripciones breves de incidentes en categorías preventivas.

### Datos sugeridos

- `assets/datos/incidentes_ejemplo.csv`

### Cómo hacerlo

1. Lee el CSV.
2. Cuenta incidentes por `tipo_incidente`.
3. Revisa severidad por categoría.
4. Pide a una IA que proponga categorías alternativas.
5. Compara la propuesta de IA con revisión humana.

### Prompt sugerido

```text
Tengo descripciones sintéticas de incidentes de salud ocupacional.
Ayúdame a clasificarlas en categorías preventivas.
Devuelve una tabla con categoria, nivel_confianza y comentario.
Si una descripción es ambigua, dilo claramente.
```

## Proyecto 3: checklist interactivo para capacitación

### Objetivo

Adaptar `assets/checklist_interactivo.html` para una capacitación específica.

### Datos sugeridos

- `assets/datos/checklist_inspeccion_ejemplo.csv`
- `assets/checklist_interactivo.html`

### Cómo hacerlo

1. Elige un tema: ergonomía, emergencias, laboratorio, EPP u orden y aseo.
2. Define 5 a 8 preguntas.
3. Mantén respuestas simples: sí, no, parcial.
4. Agrega recomendaciones no punitivas.
5. Prueba el archivo con doble clic en el navegador.

### Prompt sugerido para Codex o Claude Code

```text
Modifica assets/checklist_interactivo.html para una capacitación de ergonomía.
Mantén un solo archivo HTML, sin dependencias externas.
Agrega comentarios simples para estudiantes y recomendaciones no punitivas.
No uses datos reales.
```

## Proyecto 4: informe ejecutivo asistido por IA

### Objetivo

Convertir indicadores agregados en un informe claro y prudente.

### Datos sugeridos

- `outputs/informe_base.md`
- `assets/datos/ausentismo_ejemplo.csv`
- `assets/datos/incidentes_ejemplo.csv`

### Cómo hacerlo

1. Ejecuta `scripts/04_generar_informe_base.py`.
2. Lee `outputs/informe_base.md`.
3. Pide a una IA que mejore claridad y estructura.
4. Exige separar hechos, hipótesis, límites y preguntas.
5. Revisa que no invente causas.

### Prompt sugerido

```text
Revisa este informe con datos sintéticos.
Mejora la claridad para una reunión de salud ocupacional.
Separa hechos observados, hipótesis posibles, límites y preguntas pendientes.
No inventes causas ni hagas recomendaciones individualizadas.
```

## Proyecto 5: guía de preguntas para inspección

### Objetivo

Crear una guía de preguntas para una inspección o conversación preventiva.

### Datos sugeridos

- `assets/datos/checklist_inspeccion_ejemplo.csv`

### Cómo hacerlo

1. Revisa los ítems con respuesta `no` o `parcial`.
2. Convierte cada hallazgo en una pregunta abierta.
3. Evita lenguaje sancionatorio.
4. Pide a la IA alternativas más claras.

### Prompt sugerido

```text
Convierte estos hallazgos sintéticos de checklist en preguntas abiertas para una conversación preventiva.
Evita lenguaje punitivo.
Incluye una pregunta de seguimiento por cada hallazgo.
```

## Proyecto 6: presentación web interactiva

### Objetivo

Crear una página web simple para presentar una actividad o resultado.

### Datos sugeridos

- `assets/checklist_interactivo.html`
- gráficos en `assets/imagenes/`

### Cómo hacerlo

1. Define el objetivo de la presentación.
2. Agrega un título, instrucciones y una actividad corta.
3. Incluye un gráfico o checklist.
4. Mantén todo en un solo archivo HTML.
5. Abre el archivo en el navegador.

### Prompt sugerido

```text
Crea una página HTML de un solo archivo para una presentación de 10 minutos.
Tema: uso responsable de IA en salud ocupacional.
Incluye una actividad interactiva, lenguaje claro y advertencias de privacidad.
No uses librerías externas.
```

## Proyecto 7: glosario interactivo

### Objetivo

Convertir términos del glosario en tarjetas de estudio.

### Datos sugeridos

- [[06-recursos/glosario|Glosario]]

### Cómo hacerlo

1. Elige 10 términos.
2. Crea tarjetas con término, explicación y ejemplo.
3. Agrega un botón para mostrar/ocultar respuesta.
4. Prueba en navegador.

### Prompt sugerido

```text
Crea un HTML de un solo archivo con tarjetas de estudio para 10 términos del glosario.
Cada tarjeta debe tener término, explicación simple y ejemplo.
Agrega interacción para mostrar u ocultar la respuesta.
```

## Reglas para todos los proyectos

- Usa datos sintéticos.
- Empieza pequeño.
- Pide primero un plan antes de pedir código.
- Valida resultados con criterio humano.
- No conviertas resultados de IA en decisiones profesionales automáticas.
- Documenta qué hace el proyecto y qué límites tiene.

## Relacionado

- [[04-herramientas-ia/claude-code-y-codex|Usar este vault con Claude Code y Codex]]
- [[06-recursos/prompts|Banco de prompts]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[05-mini-proyectos/mini-proyectos-moc|Mini proyectos]]
