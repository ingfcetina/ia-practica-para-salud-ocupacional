# Limpiar datos

tags: #python #datos #principiantes

Limpiar datos significa preparar una tabla para que el análisis sea más confiable. No es “maquillar” datos: es revisar problemas básicos antes de interpretar.

## Qué revisar primero

Antes de calcular o graficar, pregunta:

- ¿faltan valores?
- ¿los nombres de áreas están escritos igual?
- ¿las fechas tienen el mismo formato?
- ¿las columnas significan lo que creo?
- ¿los datos son sintéticos, agregados o seguros?

## Script validado

Puedes ejecutar:

```bash
python scripts/03_limpiar_datos.py
```

En macOS o Linux:

```bash
python3 scripts/03_limpiar_datos.py
```

El script guarda una copia limpia en:

```text
outputs/ausentismo_limpio.csv
```

## Código explicado

```python
# Cargamos pandas para trabajar con tablas.
import pandas as pd

# Leemos el archivo sintético de ausentismo.
datos = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")

# Revisamos cuántos valores vacíos hay por columna.
print(datos.isna().sum())

# Quitamos espacios al inicio o al final del texto en columnas importantes.
datos["area"] = datos["area"].str.strip()
datos["mes"] = datos["mes"].str.strip()
```

## Qué significa cada línea

| Código | Explicación |
|---|---|
| `datos.isna().sum()` | Cuenta valores vacíos por columna. |
| `.str.strip()` | Quita espacios sobrantes al inicio o al final. |
| `datos["area"]` | Selecciona la columna `area`. |

## Cómo reemplazar el archivo

Si quieres limpiar otro CSV:

1. Guarda el nuevo archivo en `assets/datos/externos/`.
2. Cambia solo esta línea:

```python
datos = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
```

por algo como:

```python
datos = pd.read_csv("assets/datos/externos/mi_archivo.csv")
```

3. Revisa si las columnas se llaman igual.
4. Si no existe `area` o `mes`, debes cambiar también estas líneas:

```python
datos["area"] = datos["area"].str.strip()
datos["mes"] = datos["mes"].str.strip()
```

## Cómo pedirle ayuda a la IA

```text
Tengo un CSV y quiero limpiarlo con Python.
Estas son sus columnas: [pega aquí la lista de columnas].
Ayúdame a revisar valores vacíos, espacios sobrantes y formatos de fecha.
Explícame cada línea para principiantes.
No elimines datos sin explicar el criterio.
```

Prompt si aparece un error:

```text
Este código me dio el siguiente error: [pega el error].
Explícalo en lenguaje simple.
Dime qué línea debo revisar primero y propón una corrección mínima.
```

## Cuidado con datos reales

Si usas datos reales, limpiar datos no elimina automáticamente riesgos de privacidad. Antes de usar IA o publicar resultados, revisa [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]].

## Relacionado

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[06-recursos/datos-abiertos-colombia|Datos abiertos de Colombia]]
