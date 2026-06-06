# Limpiar datos

tags: #python #datos

Limpiar datos significa preparar una tabla para que el análisis sea confiable.

## Script validado

```bash
python scripts/03_limpiar_datos.py
```

El script guarda una copia limpia en `outputs/ausentismo_limpio.csv`.

## Código básico

```python
import pandas as pd

datos = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
print(datos.isna().sum())
datos["area"] = datos["area"].str.strip()
datos["mes"] = datos["mes"].str.strip()
```

## Preguntas útiles

- ¿Hay valores vacíos?
- ¿Hay nombres escritos de formas distintas?
- ¿Las fechas tienen el mismo formato?
- ¿Estoy usando datos agregados y seguros?

## Relacionado

- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
