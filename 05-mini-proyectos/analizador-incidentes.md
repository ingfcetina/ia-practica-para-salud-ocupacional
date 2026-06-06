# Analizador de incidentes

tags: #mini-proyecto #incidentes #ia #python

Objetivo: tomar descripciones sintéticas de incidentes y organizarlas para detectar patrones preventivos.

Este proyecto no busca encontrar culpables. Busca aprender a clasificar información, hacer preguntas y pensar acciones preventivas prudentes.

## Datos base

Usa:

```text
assets/datos/incidentes_ejemplo.csv
```

Columnas principales:

| Columna | Uso |
|---|---|
| `fecha` | Ubicar el evento en el tiempo. |
| `area` | Agrupar por área. |
| `descripcion` | Leer el texto del incidente. |
| `tipo_incidente` | Clasificar preventivamente. |
| `severidad` | Revisar gravedad simple. |
| `accion_inicial` | Ver una acción inicial sugerida. |

## Salida esperada

Una tabla con:

- descripción;
- categoría preventiva;
- severidad estimada;
- acción preventiva sugerida;
- dudas para revisar con una persona competente.

## Paso a paso sin programar mucho

1. Abre `assets/datos/incidentes_ejemplo.csv` en Excel, Google Sheets o un editor.
2. Lee 3 descripciones.
3. Pregunta: ¿qué tipo de riesgo aparece?
4. Compara tu clasificación con `tipo_incidente`.
5. Revisa si falta contexto.
6. Pide a una IA que proponga preguntas, no conclusiones.

## Paso a paso con Python

Ejecuta:

```bash
python scripts/02_graficar_incidentes.py
```

Esto genera:

```text
assets/imagenes/incidentes_por_tipo.png
```

Luego revisa:

- ¿qué categoría aparece más?
- ¿cuántos registros hay?
- ¿la muestra es suficiente?
- ¿hay categorías ambiguas?

## Cómo reemplazar los datos

Si quieres usar otro archivo:

1. Crea una copia del CSV nuevo en `assets/datos/externos/`.
2. Asegúrate de tener una columna de descripción.
3. No incluyas nombres, documentos, cargos únicos ni datos clínicos.
4. Cambia la ruta en el código o pide a la IA que la cambie.
5. Revisa las columnas antes de graficar.

## Prompt para la IA

```text
Tengo descripciones sintéticas de incidentes de salud ocupacional.
Clasifícalas en categorías preventivas.
Devuelve una tabla con descripcion, categoria, nivel_confianza, pregunta_de_seguimiento y comentario.
Si una descripción es ambigua, marca nivel_confianza bajo.
No identifiques responsables individuales.
No hagas recomendaciones disciplinarias.
```

## Prompt para adaptar el script

```text
Quiero adaptar scripts/02_graficar_incidentes.py para otro CSV.
La nueva ruta es: assets/datos/externos/incidentes_nuevos.csv.
Las columnas son: [pega aquí columnas].
Dime qué línea debo cambiar para contar incidentes por categoría.
Explica el cambio para principiantes.
```

## Más robusto: agregar revisión de calidad

Puedes pedirle a la IA que agregue un paso para revisar:

- valores vacíos;
- categorías repetidas con nombres diferentes;
- descripciones demasiado cortas;
- severidad faltante.

Prompt:

```text
Agrega al análisis una revisión de calidad de datos.
Quiero saber cuántos valores vacíos hay, cuántas categorías únicas existen y qué descripciones son muy cortas.
Mantén el código simple y comentado.
```

## Validación antes de presentar

- [ ] Los datos son sintéticos; si son datos reales, fueron anonimizados y revisados según políticas institucionales.
- [ ] La clasificación se presenta como apoyo, no como verdad final.
- [ ] Las recomendaciones son preventivas y no punitivas.
- [ ] Se explican límites y preguntas pendientes.

## Relacionado

- [[02-practicas-guiadas/practica-02-clasificar-incidentes|Práctica 2: clasificar incidentes]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
