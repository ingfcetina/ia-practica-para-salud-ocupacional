# Graficar resultados

tags: #python #graficos #principiantes

Un gráfico ayuda a ver patrones sin perderse en una tabla. Pero un gráfico no prueba causas: solo muestra una forma de mirar los datos.

## Qué aprenderás

- contar registros por categoría;
- crear un gráfico de barras;
- guardar o mostrar el resultado;
- pedirle a la IA que explique el gráfico sin inventar causas.

## Script validado

Ejecuta:

```bash
python scripts/02_graficar_incidentes.py
```

En macOS:

```bash
python3 scripts/02_graficar_incidentes.py
```

El script guarda el gráfico en:

```text
assets/imagenes/incidentes_por_tipo.png
```

## Código explicado

```python
# pandas permite leer y resumir tablas.
import pandas as pd

# matplotlib permite crear gráficos.
import matplotlib.pyplot as plt

# Leemos datos sintéticos de incidentes.
datos = pd.read_csv("assets/datos/incidentes_ejemplo.csv")

# Contamos cuántas veces aparece cada tipo de incidente.
conteo = datos["tipo_incidente"].value_counts()

# Creamos un gráfico de barras.
conteo.plot(kind="bar", color="#27ae60")

# Agregamos título y nombres de ejes.
plt.title("Incidentes por tipo")
plt.xlabel("Tipo de incidente")
plt.ylabel("Cantidad")

# Ajustamos el diseño para que no se corten etiquetas.
plt.tight_layout()

# Mostramos el gráfico.
plt.show()
```

## Qué puedes cambiar

| Si quieres cambiar... | Línea a revisar |
|---|---|
| Archivo de datos | `pd.read_csv(...)` |
| Columna que se cuenta | `datos["tipo_incidente"]` |
| Tipo de gráfico | `kind="bar"` |
| Color | `color="#27ae60"` |
| Título | `plt.title(...)` |

## Ejemplo: graficar severidad

```python
conteo = datos["severidad"].value_counts()
conteo.plot(kind="bar", color="#f97316")
plt.title("Incidentes por severidad")
plt.xlabel("Severidad")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()
```

## Cómo pedirle ayuda a la IA

```text
Tengo una tabla CSV con estas columnas: [pega las columnas].
Quiero crear un gráfico de barras en Python.
Indícame qué columna conviene contar y dame código con comentarios para principiantes.
No interpretes causas, solo ayuda a visualizar datos.
```

Prompt para interpretar con cuidado:

```text
Este gráfico muestra conteos por categoría.
Ayúdame a separar hechos observables, preguntas pendientes y límites del análisis.
No inventes causas ni hagas recomendaciones individualizadas.
```

## Preguntas antes de interpretar

- ¿La muestra es suficiente?
- ¿Faltan registros?
- ¿Hay sesgos de reporte?
- ¿La categoría fue asignada de forma consistente?
- ¿Necesito revisar el contexto con una persona experta?

## Relacionado

- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[03-python-desde-cero/generar-informes|Generar informes]]
- [[06-recursos/datos-abiertos-colombia|Datos abiertos de Colombia]]
