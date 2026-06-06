# Datos abiertos de Colombia

tags: #datos-abiertos #colombia #csv #api #principiantes

Esta guía explica cómo buscar, descargar y usar datos del portal oficial de Datos Abiertos Colombia con cuidado ético y técnico.

Portal oficial:

- <https://www.datos.gov.co/>

Guías del portal:

- <http://herramientas.datos.gov.co/>
- <http://herramientas.datos.gov.co/herramientas/usar-los-datos>
- <http://herramientas.datos.gov.co/herramientas/preguntas-frecuentes>

## Antes de descargar datos reales

Aunque los datos sean públicos, no significa que puedas interpretarlos sin contexto. Para este taller:

- usa primero los datos sintéticos de [[06-recursos/datasets-ejemplo|Datasets de ejemplo]];
- descarga datos reales solo para aprender el proceso técnico;
- revisa diccionario de datos, fecha de actualización y entidad responsable;
- no hagas conclusiones sobre personas o instituciones sin validación profesional;
- no mezcles datos públicos con datos internos o identificables.

## Cómo buscar un conjunto de datos

1. Entra a <https://www.datos.gov.co/>.
2. Usa el buscador.
3. Prueba palabras como:
   - `salud`;
   - `seguridad y salud en el trabajo`;
   - `inspección`;
   - `licencias`;
   - `hospital`;
   - `accidentes`.
4. Abre un conjunto de datos.
5. Revisa:
   - nombre;
   - entidad publicadora;
   - fecha de actualización;
   - columnas;
   - licencia;
   - opciones de descarga.

## Ejemplos útiles para practicar

| Dataset | Enlace | Uso didáctico |
|---|---|---|
| Resoluciones de licencias en seguridad y salud en el trabajo persona natural | <https://www.datos.gov.co/Salud-y-Protecci-n-Social/Resoluciones-de-licencias-en-seguridad-y-salud-en-/5k89-zfk7> | Practicar descarga, lectura de columnas y conteos por categoría o fecha. |
| POT - Salud | <https://www.datos.gov.co/dataset/POT-Salud/rr8q-xvjs> | Practicar lectura de datos públicos de salud territorial. |
| Portal general de datos | <https://www.datos.gov.co/> | Buscar otros datasets según el interés del grupo. |

## Descargar manualmente como CSV

En muchos datasets puedes usar la interfaz del portal:

1. Abre el dataset.
2. Busca opciones como **Exportar**, **Download** o **Descargar**.
3. Elige formato **CSV**.
4. Guarda el archivo dentro de una carpeta como:

```text
assets/datos/externos/
```

> Recomendación: no reemplaces los CSV sintéticos originales. Guarda los datos externos en una carpeta separada.

## Descargar con URL CSV

Datos Abiertos Colombia usa tecnología Socrata. Muchos datasets permiten una URL de descarga directa con este patrón:

```text
https://www.datos.gov.co/resource/IDENTIFICADOR.csv?$limit=5000
```

Ejemplo con el dataset de licencias:

```text
https://www.datos.gov.co/resource/5k89-zfk7.csv?$limit=5000
```

Ejemplo con POT - Salud:

```text
https://www.datos.gov.co/resource/rr8q-xvjs.csv?$limit=5000
```

Documentación de la API Socrata:

- <https://dev.socrata.com/>

## Leer un CSV público con Python

Ejemplo didáctico:

```python
import pandas as pd

url = "https://www.datos.gov.co/resource/5k89-zfk7.csv?$limit=5000"
datos = pd.read_csv(url)

print(datos.head())
print(datos.columns)
print(datos.shape)
```

Qué hace cada línea:

- `import pandas as pd`: carga la librería para trabajar con tablas.
- `url = ...`: guarda la dirección del CSV.
- `pd.read_csv(url)`: descarga y lee el CSV.
- `head()`: muestra las primeras filas.
- `columns`: muestra los nombres de columnas.
- `shape`: muestra cuántas filas y columnas hay.

## Guardar una copia local

Después de descargar, guarda una copia para trabajar sin depender de internet:

```python
from pathlib import Path
import pandas as pd

url = "https://www.datos.gov.co/resource/5k89-zfk7.csv?$limit=5000"
datos = pd.read_csv(url)

carpeta = Path("assets/datos/externos")
carpeta.mkdir(parents=True, exist_ok=True)

datos.to_csv(carpeta / "licencias_sst_colombia.csv", index=False)
```

## Pedirle ayuda a la IA

Prompt para explorar un dataset público:

```text
Estoy usando un dataset público de Datos Abiertos Colombia.
Quiero entender sus columnas antes de hacer análisis.
No hagas conclusiones todavía.
Ayúdame a crear una lista de preguntas: qué significa cada columna, qué calidad de datos debo revisar y qué límites tendría cualquier análisis.
```

Prompt para pedir código:

```text
Ayúdame a escribir código Python para leer un CSV desde una URL de Datos Abiertos Colombia.
Quiero ver primeras filas, nombres de columnas, cantidad de filas y valores vacíos por columna.
Explica cada línea para una persona que está empezando.
No hagas análisis causal ni recomendaciones profesionales.
```

Prompt para cuidar interpretación:

```text
Con estos resultados agregados de un dataset público, separa hechos observables, preguntas pendientes y límites del análisis.
No inventes causas. No hagas recomendaciones sobre personas o instituciones específicas.
```

## Ejercicio guiado

1. Abre un dataset en <https://www.datos.gov.co/>.
2. Copia el identificador de la URL. Suele aparecer al final, por ejemplo `5k89-zfk7`.
3. Construye la URL CSV:

```text
https://www.datos.gov.co/resource/5k89-zfk7.csv?$limit=5000
```

4. Lee la URL con `pandas`.
5. Revisa columnas y tamaño.
6. Guarda una copia local en `assets/datos/externos/`.
7. Escribe tres preguntas de calidad de datos antes de analizar.

## Advertencia importante

Un dataset público puede estar incompleto, desactualizado o requerir conocimiento normativo. Descargarlo no significa que ya puedas hacer recomendaciones. Primero revisa contexto, fuente, diccionario, limitaciones y propósito del análisis.

## Relacionado

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/limpiar-datos|Limpiar datos]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
