# Datasets de ejemplo

tags: #datos #recursos #csv

Los datos de este vault son **sintéticos**. Sirven para practicar análisis, clasificación, visualización e informes sin exponer información real de pacientes, trabajadores, empresas o instituciones.

Todos los archivos están en:

```text
assets/datos/
```

## Resumen rápido

| Archivo | Filas | Para qué se usa |
|---|---:|---|
| `assets/datos/ausentismo_ejemplo.csv` | 20 | Analizar días de ausencia por área, mes, turno y motivo agregado. |
| `assets/datos/incidentes_ejemplo.csv` | 12 | Clasificar incidentes sintéticos y graficar tipos de evento. |
| `assets/datos/checklist_inspeccion_ejemplo.csv` | 7 | Practicar revisión de cumplimiento de una inspección. |
| `assets/datos/indicadores_dashboard_ejemplo.csv` | 12 | Diseñar un dashboard básico con indicadores agregados. |

## 1. `ausentismo_ejemplo.csv`

Este archivo simula registros agregados de ausentismo por mes y área. No contiene nombres ni información individual.

### Columnas

| Columna | Qué significa | Ejemplo |
|---|---|---|
| `mes` | Mes del registro en formato año-mes. | `2026-01` |
| `area` | Área o servicio agregado. | `Enfermeria` |
| `dias_ausencia` | Total de días de ausencia en ese grupo. | `18` |
| `eventos_ausencia` | Cantidad de eventos de ausencia registrados. | `6` |
| `motivo_agregado` | Motivo agrupado, no diagnóstico individual. | `respiratorio` |
| `turno` | Turno agregado asociado al registro. | `manana` |

### Preguntas que permite practicar

- ¿Qué áreas concentran más días de ausencia?
- ¿Qué meses muestran mayor carga?
- ¿Qué motivos agregados aparecen con más frecuencia?
- ¿Qué preguntas faltan antes de proponer acciones?

### Notas relacionadas

- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/limpiar-datos|Limpiar datos]]

## 2. `incidentes_ejemplo.csv`

Este archivo simula descripciones breves de incidentes o condiciones de seguridad ocupacional. Las descripciones son inventadas.

### Columnas

| Columna | Qué significa | Ejemplo |
|---|---|---|
| `fecha` | Fecha sintética del registro. | `2026-01-05` |
| `area` | Área donde ocurrió o se reportó el evento. | `Laboratorio` |
| `descripcion` | Descripción breve y ficticia. | `Salpicadura menor durante preparacion de solucion` |
| `tipo_incidente` | Categoría preventiva asignada. | `exposicion_quimica` |
| `severidad` | Nivel simple para practicar clasificación. | `leve` |
| `accion_inicial` | Acción inicial sugerida en el ejemplo. | `Lavado inmediato y reporte` |

### Preguntas que permite practicar

- ¿Qué tipos de incidentes son más frecuentes?
- ¿Qué categorías se pueden usar para prevención?
- ¿Qué descripciones son ambiguas?
- ¿Qué necesita revisión humana antes de tomar decisiones?

### Notas relacionadas

- [[02-practicas-guiadas/practica-02-clasificar-incidentes|Práctica 2: clasificar incidentes]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[05-mini-proyectos/analizador-incidentes|Analizador de incidentes]]

## 3. `checklist_inspeccion_ejemplo.csv`

Este archivo simula una inspección básica de seguridad ocupacional. Sirve para practicar lectura de tablas y revisión de cumplimiento.

### Columnas

| Columna | Qué significa | Ejemplo |
|---|---|---|
| `item` | Punto revisado en la inspección. | `Ruta de evacuacion despejada` |
| `categoria` | Tema preventivo asociado. | `emergencias` |
| `respuesta` | Resultado de la revisión. | `si`, `no` o `parcial` |
| `observacion_sintetica` | Comentario inventado para práctica. | `Caja temporal bloquea salida secundaria` |

### Preguntas que permite practicar

- ¿Qué porcentaje de puntos cumple?
- ¿Qué categorías necesitan seguimiento?
- ¿Cómo convertir una revisión en recomendaciones no punitivas?
- ¿Cómo adaptar un checklist a otra situación?

### Notas relacionadas

- [[05-mini-proyectos/checklist-inteligente|Checklist inteligente]]
- [[02-practicas-guiadas/practica-05-presentacion-web-interactiva|Práctica 5: presentación web interactiva]]

## 4. `indicadores_dashboard_ejemplo.csv`

Este archivo contiene indicadores agregados por mes para practicar diseño de dashboard.

### Columnas

| Columna | Qué significa | Ejemplo |
|---|---|---|
| `mes` | Mes del indicador. | `2026-01` |
| `indicador` | Nombre del indicador agregado. | `dias_ausencia` |
| `valor` | Valor numérico del indicador. | `55` |
| `unidad` | Unidad de interpretación. | `dias`, `eventos`, `porcentaje` |

### Preguntas que permite practicar

- ¿Qué indicador conviene mostrar primero?
- ¿Qué visualizaciones serían más claras para una reunión?
- ¿Qué advertencias deben acompañar un dashboard?
- ¿Qué información adicional falta para tomar decisiones?

### Notas relacionadas

- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[05-mini-proyectos/generador-informes|Generador de informes]]

## Cómo validar los datasets

Primero instala lo necesario siguiendo [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]. Luego ejecuta:

```bash
python scripts/00_validar_datos.py
```

Resultado esperado:

```text
OK ausentismo_ejemplo.csv: 20 filas
OK incidentes_ejemplo.csv: 12 filas
OK checklist_inspeccion_ejemplo.csv: 7 filas
OK indicadores_dashboard_ejemplo.csv: 12 filas
OK checklist_interactivo.html
```

## Regla para datos reales

Si vas a reemplazar estos archivos por datos propios:

1. elimina nombres, documentos, teléfonos, correos y direcciones;
2. evita diagnósticos individuales o historias clínicas;
3. agrupa datos por área, mes o categoría;
4. revisa políticas institucionales antes de subir archivos a herramientas de IA;
5. valida todo con criterio profesional.

## Relacionado

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
- [[scripts/README|Scripts de ejemplo]]
