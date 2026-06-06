# Leer datos CSV

tags: #python #csv #principiantes

Un CSV es una tabla guardada como texto. Python puede leerlo con `pandas`.

## Instalación mínima

```bash
pip install pandas matplotlib
```

> Si no puedes instalar estas dependencias ahora, lee el código y observa qué intenta hacer. Puedes volver a la instalación después.

## Validar datos antes de empezar

```bash
python scripts/00_validar_datos.py
```

## Código

```python
import pandas as pd

datos = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
print(datos.head())
print(datos.columns)
```

## Qué observar

- `head()` muestra las primeras filas.
- `columns` muestra nombres de columnas.
- Si falla, revisa ruta, separador y codificación.

## Relacionado

- [[03-python-desde-cero/limpiar-datos|Limpiar datos]]
- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
