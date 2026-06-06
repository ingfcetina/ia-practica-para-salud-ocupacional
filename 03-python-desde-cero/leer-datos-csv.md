# Leer datos CSV

tags: #python #csv #principiantes

Un CSV es una tabla guardada como texto. Es parecido a una hoja de cálculo, pero se guarda en un formato simple que Python puede leer fácilmente.

En este vault vas a empezar con datos sintéticos ubicados en:

```text
assets/datos/
```

## Qué aprenderás

Al terminar esta nota podrás:

- ubicar un archivo CSV dentro del proyecto;
- leerlo con Python;
- ver sus primeras filas;
- revisar nombres de columnas;
- entender qué hacer si la ruta falla.

## Antes de empezar

1. Abre una terminal en la carpeta raíz del repositorio.
2. Verifica que ves estas carpetas:

```text
assets/
scripts/
03-python-desde-cero/
```

3. Instala dependencias si todavía no lo hiciste:

```bash
pip install -r requirements.txt
```

En macOS o Linux puede ser:

```bash
python3 -m pip install -r requirements.txt
```

Guía completa: [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]].

## Paso 1: validar que los datos existen

Ejecuta:

```bash
python scripts/00_validar_datos.py
```

Si usas macOS o Linux:

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

## Paso 2: leer un CSV con Python

Copia este código en un archivo nuevo o pruébalo en un notebook:

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

## Qué significa cada parte

| Código | Explicación |
|---|---|
| `import pandas as pd` | Carga pandas y le da el nombre corto `pd`. |
| `ruta = ...` | Guarda la ubicación del archivo. |
| `pd.read_csv(ruta)` | Lee el CSV. |
| `datos` | Variable donde queda guardada la tabla. |
| `datos.head()` | Muestra las primeras filas. |
| `datos.columns` | Muestra los nombres de columnas. |

## Paso 3: cambiar el archivo que quieres leer

Para leer otro CSV, cambia la ruta.

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

## Cómo pedirle a la IA que te ayude

Prompt recomendado:

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

## Errores comunes

| Error | Qué significa | Cómo resolverlo |
|---|---|---|
| `FileNotFoundError` | Python no encuentra el archivo. | Revisa la ruta y que estés en la carpeta raíz del repo. |
| `ModuleNotFoundError: pandas` | No está instalada la librería pandas. | Ejecuta `pip install -r requirements.txt`. |
| Columnas raras o vacías | El archivo puede tener otro separador o codificación. | Revisa el CSV o pide ayuda a la IA con el mensaje de error. |

## Relacionado

- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[06-recursos/datos-abiertos-colombia|Datos abiertos de Colombia]]
- [[03-python-desde-cero/limpiar-datos|Limpiar datos]]
- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]
