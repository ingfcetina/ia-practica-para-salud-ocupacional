# Limpiar datos

tags: #python #datos #principiantes

Limpiar datos significa preparar una tabla para que el análisis sea más confiable. No es “maquillar” datos ni borrar lo que incomoda. Es revisar problemas básicos antes de interpretar.

En esta nota vas a usar Python para revisar valores vacíos y limpiar espacios sobrantes en textos.

## Objetivo de aprendizaje

Al terminar podrás:

- explicar qué significa limpiar datos;
- revisar valores vacíos por columna;
- entender qué hace `.str.strip()`;
- ejecutar un script que guarda una copia limpia;
- abrir el archivo generado y compararlo con el original;
- pedir ayuda a la IA sin entregar datos sensibles.

## Tiempo sugerido

| Actividad | Tiempo |
|---|---:|
| Abrir datos originales | 5 min |
| Ejecutar script | 5 min |
| Revisar salida | 10 min |
| Leer código explicado | 10 min |
| Adaptar con cuidado | 10 min |

## Antes de empezar

Revisa:

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]

Debes tener abierta una consola o Terminal en la carpeta del repositorio.

## Archivo de datos

Archivo original:

```text
assets/datos/ausentismo_ejemplo.csv
```

Archivo que genera el script:

```text
outputs/ausentismo_limpio.csv
```

Ambos son archivos sintéticos.

## Qué contiene el dataset

| Columna | Qué significa |
|---|---|
| `mes` | Mes del registro. |
| `area` | Área o servicio. |
| `dias_ausencia` | Total agregado de días de ausencia. |
| `eventos_ausencia` | Cantidad agregada de eventos. |
| `motivo_agregado` | Motivo agrupado. |
| `turno` | Turno asociado. |

## Pregunta profesional

> ¿La tabla está suficientemente ordenada para analizarla sin confundir errores de formato con patrones reales?

## Paso 1: abrir el archivo original

1. Entra a `assets/datos/`.
2. Abre `ausentismo_ejemplo.csv`.
3. Mira si las columnas tienen sentido.
4. Revisa si hay espacios raros, celdas vacías o textos inconsistentes.

No necesitas corregir nada manualmente todavía.

## Paso 2: ejecutar el script de limpieza

### Windows

```bash
python scripts/03_limpiar_datos.py
```

Si usas `py`:

```bash
py scripts/03_limpiar_datos.py
```

### macOS

```bash
python3 scripts/03_limpiar_datos.py
```

## Paso 3: revisar la salida esperada

Deberías ver algo parecido a:

```text
Valores vacíos por columna:
mes                 0
area                0
dias_ausencia       0
eventos_ausencia    0
motivo_agregado     0
turno               0
Datos limpios guardados en outputs/ausentismo_limpio.csv
```

Si los acentos se ven raros en una consola de Windows, no significa necesariamente que el script falló. Revisa si el archivo de salida fue creado.

## Paso 4: abrir el archivo limpio

1. Entra a `outputs/`.
2. Abre `ausentismo_limpio.csv`.
3. Compáralo con `assets/datos/ausentismo_ejemplo.csv`.
4. Revisa si conserva las columnas principales.

Pregunta para pensar:

```text
¿El script modificó el archivo original o creó una copia limpia?
```

Respuesta esperada: creó una copia en `outputs/`.

## Código explicado

```python
# Cargamos herramientas necesarias.
from pathlib import Path
import pandas as pd

# Definimos rutas de entrada y salida.
ROOT = Path(".")
DATOS = ROOT / "assets" / "datos" / "ausentismo_ejemplo.csv"
SALIDA = ROOT / "outputs" / "ausentismo_limpio.csv"

# Leemos el archivo sintético de ausentismo.
datos = pd.read_csv(DATOS)

# Revisamos cuántos valores vacíos hay por columna.
print(datos.isna().sum())

# Quitamos espacios al inicio o al final del texto en columnas importantes.
for columna in ["area", "mes", "motivo_agregado", "turno"]:
    datos[columna] = datos[columna].astype(str).str.strip()

# Guardamos una copia limpia sin modificar el archivo original.
SALIDA.parent.mkdir(parents=True, exist_ok=True)
datos.to_csv(SALIDA, index=False)
print(f"Datos limpios guardados en {SALIDA.relative_to(ROOT)}")
```

## Qué significa cada línea

| Código | Explicación |
|---|---|
| `from pathlib import Path` | Permite construir rutas de archivos. |
| `import pandas as pd` | Carga pandas para trabajar con tablas. |
| `ROOT = Path(".")` | Indica que trabajamos desde la carpeta actual del repositorio. |
| `DATOS = ...` | Define dónde está el CSV original. |
| `SALIDA = ...` | Define dónde se guardará la copia limpia. |
| `pd.read_csv(DATOS)` | Lee el CSV original. |
| `datos.isna()` | Revisa qué celdas están vacías. |
| `.sum()` | Suma cuántos vacíos hay por columna. |
| `for columna in [...]` | Repite la limpieza en varias columnas de texto. |
| `datos[columna]` | Selecciona una columna cada vez. |
| `astype(str)` | Trata el valor como texto antes de limpiarlo. |
| `.str.strip()` | Quita espacios sobrantes al inicio o al final. |
| `SALIDA.parent.mkdir(...)` | Crea la carpeta `outputs/` si no existe. |
| `datos.to_csv(...)` | Guarda la tabla limpia como CSV. |
| `print(...)` | Muestra dónde quedó guardado el archivo. |

## Cómo reemplazar el archivo

Si quieres limpiar otro CSV seguro:

1. Guárdalo en `assets/datos/externos/`.
2. Cambia solo esta línea:

```python
datos = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
```

por algo como:

```python
datos = pd.read_csv("assets/datos/externos/mi_archivo.csv")
```

3. Revisa si las columnas se llaman igual.
4. Si no existe `area` o `mes`, cambia también estas líneas:

```python
datos["area"] = datos["area"].str.strip()
datos["mes"] = datos["mes"].str.strip()
```

5. Cambia una cosa a la vez y vuelve a ejecutar.

## Cómo pedirle ayuda a la IA

Prompt para entender limpieza:

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
No propongas borrar filas sin justificarlo.
```

## Qué NO hacer

- No borres filas solo porque tienen datos faltantes.
- No reemplaces valores faltantes sin explicar el criterio.
- No combines categorías si no entiendes su significado.
- No uses datos reales identificables con herramientas públicas de IA.
- No modifiques el archivo original sin guardar copia.

## Si algo falla

| Problema | Qué revisar |
|---|---|
| No aparece `outputs/ausentismo_limpio.csv` | Revisa si ejecutaste el comando desde la carpeta correcta. |
| Sale `FileNotFoundError` | Python no encuentra `assets/datos/ausentismo_ejemplo.csv`. |
| Sale `KeyError: 'area'` | La columna `area` no existe o tiene otro nombre. |
| Sale `ModuleNotFoundError: pandas` | Falta instalar dependencias. Vuelve a instalación. |

## Producto final

Al terminar deberías tener:

- archivo original revisado;
- script ejecutado;
- conteo de valores vacíos leído;
- archivo `outputs/ausentismo_limpio.csv` abierto;
- una explicación de qué limpió el script y qué no limpió.

## Relacionado

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[06-recursos/datos-abiertos-colombia|Datos abiertos de Colombia]]
