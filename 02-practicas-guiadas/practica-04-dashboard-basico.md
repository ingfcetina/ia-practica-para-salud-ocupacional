# Práctica 4: dashboard básico

tags: #practica #dashboard #python #principiantes

En esta práctica vas a diseñar un dashboard básico con indicadores agregados. Un dashboard no es solo “poner gráficos”: debe responder preguntas claras.

## Objetivo de aprendizaje

Al terminar podrás:

- elegir indicadores simples;
- relacionar cada gráfico con una pregunta;
- evitar exceso de información;
- incluir advertencias de interpretación;
- pedir a la IA ayuda para diseñar visualizaciones.

## Qué es un dashboard

Un dashboard es una pantalla o página que reúne indicadores para facilitar una conversación.

Ejemplo de pregunta:

```text
¿Qué áreas o temas conviene revisar primero?
```

No debe convertirse en:

```text
¿A quién culpamos?
```

## Datos sugeridos

Usa:

```text
assets/datos/indicadores_dashboard_ejemplo.csv
```

También puedes usar gráficos generados por:

```bash
python scripts/01_analizar_ausentismo.py
python scripts/02_graficar_incidentes.py
```

## Paso 1: revisar indicadores disponibles

Abre `indicadores_dashboard_ejemplo.csv`.

Columnas:

| Columna | Qué significa |
|---|---|
| `mes` | Mes del indicador. |
| `indicador` | Nombre del indicador. |
| `valor` | Valor numérico. |
| `unidad` | Cómo se interpreta el valor. |

## Paso 2: elegir preguntas

Antes de elegir gráficos, escribe preguntas.

| Pregunta | Indicador útil | Visualización sugerida |
|---|---|---|
| ¿Cómo cambia el ausentismo por mes? | `dias_ausencia` | Línea o barras. |
| ¿Cuántos incidentes se reportan por mes? | `incidentes_reportados` | Línea. |
| ¿Cómo cambia el cumplimiento del checklist? | `cumplimiento_checklist` | Línea o tarjeta. |

## Paso 3: pedir propuesta a la IA

```text
Ayúdame a diseñar un dashboard básico para una reunión de salud ocupacional.
Tengo indicadores agregados por mes: días de ausencia, incidentes reportados y cumplimiento de checklist.
Propón 3 visualizaciones.
Para cada una indica: pregunta que responde, gráfico sugerido, advertencia de interpretación y qué dato faltaría.
No inventes causas.
```

## Paso 4: revisar gráficos existentes

Abre:

```text
assets/imagenes/ausentismo_por_area.png
assets/imagenes/incidentes_por_tipo.png
```

Preguntas:

- ¿El título es claro?
- ¿Los ejes se entienden?
- ¿La audiencia sabrá qué significa el gráfico?
- ¿Hace falta una advertencia?

## Paso 5: ejemplo de advertencia

Incluye una nota como:

```text
Estos datos son sintéticos y agregados. Los gráficos muestran patrones para discusión, no prueban causas ni justifican decisiones individuales.
```

## Paso 6: estructura mínima del dashboard

```text
Título: Indicadores sintéticos de salud ocupacional

Bloque 1: Ausentismo por área
Pregunta: ¿dónde se concentran días de ausencia?
Advertencia: no interpreta causas.

Bloque 2: Incidentes por tipo
Pregunta: ¿qué categorías aparecen más?
Advertencia: puede haber sesgo de reporte.

Bloque 3: Cumplimiento de checklist
Pregunta: ¿qué temas requieren revisión preventiva?
Advertencia: requiere observación y diálogo.
```

## Cómo hacerlo más robusto

Puedes pedir a la IA:

```text
Convierte esta estructura de dashboard en una página HTML sencilla.
Debe tener tres secciones, una advertencia de privacidad y espacio para imágenes.
No uses librerías externas.
Explica qué textos puedo reemplazar.
```

O puedes pedir:

```text
Ayúdame a crear un notebook que lea indicadores_dashboard_ejemplo.csv y genere un gráfico por indicador.
Explica cada celda para principiantes.
```

## Qué NO hacer

- No pongas demasiados gráficos.
- No mezcles indicadores sin explicar unidades.
- No presentes hipótesis como hechos.
- No uses datos identificables.
- No uses colores tipo rojo para señalar culpables.

## Producto final

Al terminar deberías tener:

- tres preguntas para el dashboard;
- tres visualizaciones sugeridas;
- una advertencia de interpretación;
- idea de cómo presentarlo en reunión o clase.

## Relacionado

- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
- [[05-mini-proyectos/generador-informes|Generador de informes]]
- [[06-recursos/diagramas-mermaid|Diagramas Mermaid]]
