# Leer datos CSV

tags: #python #csv #principiantes

En esta nota vas a aprender a abrir una tabla CSV y a leerla con Python. Un CSV es parecido a una hoja de cálculo, pero guardada como texto simple.

No necesitas entender todo el código al inicio. La idea es reconocer este flujo:

```text
archivo CSV → Python lo lee → Python muestra filas y columnas → tú revisas si tiene sentido
```

## Objetivo de aprendizaje

Al terminar podrás:

- ubicar un archivo CSV dentro del vault;
- abrirlo sin programar;
- validar que los datos del proyecto existen;
- leer un CSV con Python;
- ver las primeras filas y los nombres de columnas;
- pedir ayuda a la IA cuando una ruta falla.

## Tiempo sugerido

| Actividad | Tiempo |
|---|---:|
| Abrir el CSV sin programar | 5 min |
| Validar archivos | 5 min |
| Leer código explicado | 10 min |
| Probar o adaptar ruta | 10 min |

## Antes de empezar

Revisa:

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[00-empezar-aqui/reglas-de-privacidad|Reglas de privacidad]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]

Abre una consola o Terminal en la carpeta raíz del repositorio. Debes estar en la carpeta donde ves:

```text
README.md
assets/
scripts/
03-python-desde-cero/
```

Si no ves esas carpetas, todavía no estás en el lugar correcto.

## Archivo de datos

Usa:

```text
assets/datos/ausentismo_ejemplo.csv
```

Este archivo es sintético. No contiene personas reales.

## Qué contiene el dataset

| Columna | Qué significa |
|---|---|
| `mes` | Mes del registro. |
| `area` | Área o servicio. |
| `dias_ausencia` | Total agregado de días de ausencia. |
| `eventos_ausencia` | Cantidad agregada de eventos. |
| `motivo_agregado` | Motivo agrupado, no diagnóstico individual. |
| `turno` | Turno asociado al registro agregado. |

## Pregunta profesional

> ¿Qué información trae esta tabla y qué columnas podrían servir para un análisis de ausentismo?

Antes de calcular, primero hay que entender la tabla.

## Paso 1: abrir el CSV sin programar

1. Abre la carpeta del repositorio.
2. Entra a `assets/datos/`.
3. Abre `ausentismo_ejemplo.csv`.
4. Puedes usar Excel, Numbers, Google Sheets o un editor de texto.
5. Mira los nombres de columnas.
6. Revisa si entiendes qué representa cada fila.

Pregunta para pensar:

```text
¿Esta tabla contiene nombres, documentos o diagnósticos individuales?
```

Respuesta esperada: no.

## Paso 2: instalar dependencias si hace falta

Si todavía no instalaste librerías, ejecuta esto desde la carpeta del repositorio.

### Windows

```bash
python -m pip install -r requirements.txt
```

Si `python` no funciona:

```bash
py -m pip install -r requirements.txt
```

### macOS

```bash
python3 -m pip install -r requirements.txt
```

## Paso 3: validar que los datos existen

### Windows

```bash
python scripts/00_validar_datos.py
```

Si usas `py`:

```bash
py scripts/00_validar_datos.py
```

### macOS

```bash
python3 scripts/00_validar_datos.py
```

Resultado esperado:

```text
OK ausentismo_ejemplo.csv: 20 filas
OK incidentes_ejemplo.csv: 12 filas
OK checklist_inspeccion_ejemplo.csv: 7 filas
OK indicadores_dashboard_ejemplo.csv: 12 filas
OK checklist_interactivo.html
```

Si esto falla, no sigas todavía. Revisa:

- que estés en la carpeta correcta;
- que exista `assets/datos/`;
- que no hayas movido los archivos CSV.

## Paso 4: leer un CSV con Python

Puedes probar este código en un notebook o pedir a Claude Code/Codex que lo ejecute en un archivo temporal. Si estás empezando, primero léelo sin modificarlo.

```python
# Importamos pandas, una librería para trabajar con tablas.
import pandas as pd

# Esta es la ruta del archivo que queremos leer.
ruta = "assets/datos/ausentismo_ejemplo.csv"

# read_csv lee el archivo y lo convierte en una tabla de Python.
datos = pd.read_csv(ruta)

# head muestra las primeras filas.
print(datos.head())

# columns muestra los nombres de las columnas.
print(datos.columns)
```

## Qué deberías observar

`datos.head()` muestra las primeras filas de la tabla.

`datos.columns` muestra algo parecido a:

```text
Index(['mes', 'area', 'dias_ausencia', 'eventos_ausencia', 'motivo_agregado', 'turno'], dtype='object')
```

No importa si el formato se ve un poco distinto. Lo importante es reconocer los nombres de columnas.

## Código explicado

| Código | Explicación |
|---|---|
| `import pandas as pd` | Carga pandas y le da el nombre corto `pd`. |
| `ruta = ...` | Guarda la ubicación del archivo. |
| `pd.read_csv(ruta)` | Lee el CSV. |
| `datos` | Variable donde queda guardada la tabla. |
| `datos.head()` | Muestra las primeras filas. |
| `datos.columns` | Muestra los nombres de columnas. |

## Paso 5: cambiar el archivo que quieres leer

Para leer otro CSV, cambia solo la ruta.

Ejemplo con incidentes:

```python
ruta = "assets/datos/incidentes_ejemplo.csv"
datos = pd.read_csv(ruta)
print(datos.head())
```

Ejemplo con checklist:

```python
ruta = "assets/datos/checklist_inspeccion_ejemplo.csv"
datos = pd.read_csv(ruta)
print(datos.head())
```

## Cómo pedirle ayuda a la IA

Prompt para entender el código:

```text
Estoy aprendiendo Python desde cero.
Tengo un archivo CSV en esta ruta: assets/datos/ausentismo_ejemplo.csv.
Explícame cómo leerlo con pandas, cómo ver las primeras filas y cómo revisar los nombres de columnas.
Explica cada línea como si yo supiera usar Excel pero no programación.
```

Prompt si quieres reemplazar el archivo:

```text
Quiero adaptar este código para leer otro archivo CSV.
La nueva ruta es: [pega aquí la ruta].
Indícame exactamente qué línea debo reemplazar y por qué.
No cambies el resto del código si no es necesario.
```

Prompt si aparece error:

```text
Estoy empezando con Python.
Este código me dio este error: [pega el error].
Explícame qué significa en lenguaje simple.
Dime qué debo revisar primero: carpeta, ruta, instalación o nombre de columna.
```

## Qué NO hacer

- No pegues datos reales identificables en una IA pública.
- No cambies varias líneas a la vez si estás aprendiendo.
- No borres archivos originales para “probar”.
- No interpretes resultados antes de entender qué columnas tienes.

## Errores comunes

| Error | Qué significa | Cómo resolverlo |
|---|---|---|
| `FileNotFoundError` | Python no encuentra el archivo. | Revisa la ruta y que estés en la carpeta raíz del repositorio. |
| `ModuleNotFoundError: pandas` | No está instalada la librería pandas. | Instala dependencias con el comando de Windows o macOS. |
| Columnas raras o vacías | El archivo puede tener otro separador o codificación. | Revisa el CSV o pide ayuda a la IA con el mensaje de error. |
| No sabes dónde está la consola | Falta abrir la carpeta correcta. | Vuelve a [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]. |

## Producto final

Al terminar deberías tener:

- el CSV abierto sin programar;
- validación de datos ejecutada;
- nombres de columnas identificados;
- una explicación básica de `read_csv`, `head` y `columns`;
- un prompt listo para pedir ayuda si falla la ruta.

## Relacionado

- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[06-recursos/datos-abiertos-colombia|Datos abiertos de Colombia]]
- [[03-python-desde-cero/limpiar-datos|Limpiar datos]]
- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
