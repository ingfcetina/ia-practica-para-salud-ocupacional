# Generar informes

tags: #python #informes #ia #principiantes

Python puede calcular indicadores y la IA puede ayudar a convertirlos en un texto más claro. La parte importante es separar hechos observados, hipótesis posibles, límites del análisis y preguntas pendientes.

En esta nota vas a generar un informe base con datos sintéticos y luego aprenderás cómo pedir a la IA que lo mejore sin inventar causas.

## Objetivo de aprendizaje

Al terminar podrás:

- ejecutar un script que calcula indicadores agregados;
- abrir un informe Markdown generado por Python;
- diferenciar hechos, hipótesis y límites;
- pedir a la IA que mejore redacción sin cambiar el sentido;
- revisar el informe antes de compartirlo.

## Tiempo sugerido

| Actividad | Tiempo |
|---|---:|
| Abrir datos base | 5 min |
| Ejecutar script | 5 min |
| Leer informe generado | 10 min |
| Mejorar con IA | 10 min |
| Validar informe | 10 min |

## Flujo recomendado

```text
Datos sintéticos → cálculo con Python → informe base → revisión con IA → validación humana
```

## Antes de empezar

Revisa:

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]

## Archivos de datos

El script usa:

```text
assets/datos/ausentismo_ejemplo.csv
assets/datos/incidentes_ejemplo.csv
```

El informe se genera en:

```text
outputs/informe_base.md
```

Todos son archivos sintéticos o generados desde datos sintéticos.

## Qué contienen los datasets

### Ausentismo

| Columna | Qué significa |
|---|---|
| `mes` | Mes del registro. |
| `area` | Área o servicio. |
| `dias_ausencia` | Total agregado de días de ausencia. |
| `eventos_ausencia` | Cantidad agregada de eventos. |
| `motivo_agregado` | Motivo agrupado. |
| `turno` | Turno asociado. |

### Incidentes

| Columna | Qué significa |
|---|---|
| `fecha` | Fecha sintética del evento. |
| `area` | Área donde se reporta el evento. |
| `descripcion` | Texto breve del incidente. |
| `tipo_incidente` | Categoría preventiva. |
| `severidad` | Nivel simple: leve o moderada. |
| `accion_inicial` | Acción inicial sugerida en el ejemplo. |

## Pregunta profesional

> ¿Cómo podemos convertir indicadores agregados en un informe prudente para discusión, sin inventar causas ni señalar personas?

## Paso 1: abrir los datos base

1. Entra a `assets/datos/`.
2. Abre `ausentismo_ejemplo.csv`.
3. Abre `incidentes_ejemplo.csv`.
4. Revisa qué columnas trae cada uno.
5. Confirma que no hay nombres ni documentos reales.

## Paso 2: ejecutar el script

### Windows

```bash
python scripts/04_generar_informe_base.py
```

Si usas `py`:

```bash
py scripts/04_generar_informe_base.py
```

### macOS

```bash
python3 scripts/04_generar_informe_base.py
```

## Paso 3: revisar salida esperada

Deberías ver:

```text
Informe guardado en outputs/informe_base.md
```

Si el mensaje aparece, Python creó o actualizó el informe.

## Paso 4: abrir el informe generado

1. Entra a `outputs/`.
2. Abre `informe_base.md`.
3. Lee el título.
4. Busca los indicadores numéricos.
5. Busca la sección de límites.
6. Busca las preguntas para discusión.

Pregunta para pensar:

```text
¿El informe dice hechos observados o afirma causas definitivas?
```

Respuesta esperada: debe quedarse en hechos, límites y preguntas.

## Qué hace el script

1. Lee `ausentismo_ejemplo.csv`.
2. Lee `incidentes_ejemplo.csv`.
3. Calcula indicadores agregados.
4. Escribe un informe base en Markdown.
5. Incluye límites y preguntas para discutir.

## Código conceptual explicado

```python
# Leer datos
ausentismo = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
incidentes = pd.read_csv("assets/datos/incidentes_ejemplo.csv")

# Calcular indicadores simples
total_dias = int(ausentismo["dias_ausencia"].sum())
total_incidentes = len(incidentes)

# Crear texto de informe
informe = f"""
Días totales de ausencia: {total_dias}
Incidentes registrados: {total_incidentes}
"""
```

| Código | Explicación |
|---|---|
| `pd.read_csv(...)` | Lee cada CSV. |
| `ausentismo["dias_ausencia"].sum()` | Suma días de ausencia. |
| `len(incidentes)` | Cuenta filas de incidentes. |
| `int(...)` | Convierte el resultado a número entero. |
| `f"""..."""` | Crea texto usando valores calculados. |

## Paso 5: mejorar el informe con IA

Primero abre `outputs/informe_base.md` y copia su contenido. Luego usa este prompt:

```text
Revisa este informe con datos sintéticos.
Mejora la claridad para estudiantes y profesionales de salud ocupacional.
Separa hechos observados, hipótesis posibles, límites del análisis y preguntas pendientes.
No inventes causas.
No hagas recomendaciones individualizadas.
No uses lenguaje sancionatorio.
Mantén una advertencia clara de privacidad.
```

## Paso 6: revisar antes de compartir

Marca esta lista:

- [ ] El informe dice que usa datos sintéticos o agregados.
- [ ] No hay nombres de personas.
- [ ] No hay nombres de instituciones reales.
- [ ] Los números coinciden con los resultados del script.
- [ ] Las hipótesis están escritas como hipótesis, no como verdades.
- [ ] Las recomendaciones son prudentes.
- [ ] El texto no culpa a personas o áreas.

## Cómo reemplazar los datos

Si tienes otro CSV seguro y agregado:

1. Guárdalo en `assets/datos/externos/`.
2. Revisa sus columnas.
3. Cambia las rutas en el script.
4. Ajusta los nombres de columnas usados para calcular indicadores.
5. Ejecuta el script.
6. Revisa el informe antes de compartir.

Prompt para pedir ayuda:

```text
Quiero adaptar este script de informe a un nuevo CSV.
Estas son las columnas del nuevo archivo: [pega columnas].
Propón indicadores agregados seguros.
Dime qué líneas debo cambiar y por qué.
No uses datos identificables ni hagas conclusiones causales.
```

## Plantilla de informe prudente

```text
# Informe base

## Datos usados
[explicar archivo, fecha y límites]

## Resultados observados
[hechos numéricos]

## Hipótesis posibles
[ideas que requieren validación]

## Límites
[qué no se puede concluir]

## Preguntas pendientes
[qué investigar antes de decidir]
```

## Qué NO hacer

- No publiques un informe con datos reales identificables.
- No cambies hipótesis por conclusiones definitivas.
- No agregues recomendaciones clínicas, ocupacionales o legales generadas por IA sin revisión profesional.
- No uses el informe para señalar personas o áreas.

## Si algo falla

| Problema | Qué revisar |
|---|---|
| No aparece `outputs/informe_base.md` | Revisa si ejecutaste desde la carpeta correcta. |
| Sale `FileNotFoundError` | Falta un CSV o la ruta cambió. |
| Sale `KeyError` | Una columna usada por el script no existe. |
| La IA inventa causas | Repite el prompt y exige separar hechos, hipótesis y límites. |

## Producto final

Al terminar deberías tener:

- informe base generado en `outputs/informe_base.md`;
- contenido revisado con criterios de privacidad;
- versión mejorada con IA, si corresponde;
- lista de límites y preguntas pendientes.

## Relacionado

- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[05-mini-proyectos/generador-informes|Generador de informes]]
- [[06-recursos/prompts|Banco de prompts]]
