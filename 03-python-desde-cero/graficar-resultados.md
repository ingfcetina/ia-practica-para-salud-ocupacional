# Graficar resultados

tags: #python #graficos

Un gráfico sencillo ayuda a conversar sobre patrones sin perderse en una tabla.

## Script validado

```bash
python scripts/02_graficar_incidentes.py
```

El script guarda el gráfico en `assets/imagenes/incidentes_por_tipo.png`.

## Código

```python
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("assets/datos/incidentes_ejemplo.csv")
conteo = datos["tipo_incidente"].value_counts()

conteo.plot(kind="bar", color="#27ae60")
plt.title("Incidentes por tipo")
plt.xlabel("Tipo de incidente")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()
```

## Consejo

Antes de interpretar, pregunta: ¿la muestra es suficiente?, ¿faltan registros?, ¿hay sesgos de reporte?

## Relacionado

- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[03-python-desde-cero/generar-informes|Generar informes]]
