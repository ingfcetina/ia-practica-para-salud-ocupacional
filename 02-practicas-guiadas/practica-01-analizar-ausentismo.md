# Práctica 1: analizar ausentismo

tags: #practica #python #ausentismo

Objetivo: leer una tabla sintética de ausentismo y crear un resumen por área.

## Archivo de datos

Usa `assets/datos/ausentismo_ejemplo.csv`. Es sintético y no contiene personas reales.

## Pregunta profesional

> ¿En qué áreas se concentran más días de ausencia y qué preguntas deberíamos investigar antes de proponer acciones?

## Script validado

Puedes ejecutar el ejemplo completo desde:

```bash
python scripts/01_analizar_ausentismo.py
```

El script imprime el resumen y guarda el gráfico en `assets/imagenes/ausentismo_por_area.png`.

## Código Python

```python
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
resumen = datos.groupby("area")["dias_ausencia"].sum().sort_values(ascending=False)
print(resumen)

resumen.plot(kind="bar", color="#2f80ed")
plt.title("Días de ausencia por área")
plt.xlabel("Área")
plt.ylabel("Días de ausencia")
plt.tight_layout()
plt.show()
```

## Prompt para interpretar

```text
Actúa como analista de salud ocupacional.
Estos son resultados agregados por área, sin datos personales.
Separa hechos observables, hipótesis posibles y preguntas antes de recomendar acciones.
No inventes causas.
```

## Relacionado

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
