# Práctica 1: analizar ausentismo

tags: #practica #python #ausentismo #principiantes

En esta práctica vas a leer una tabla sintética de ausentismo, resumir días de ausencia por área y crear un gráfico simple.

No necesitas entender todo el código al inicio. La meta es comprender el proceso:

```text
tabla CSV → Python lee datos → Python agrupa → gráfico → preguntas profesionales
```

## Objetivo de aprendizaje

Al terminar podrás:

- ubicar un archivo CSV dentro del vault;
- ejecutar un script de Python;
- entender qué significa agrupar por área;
- leer un gráfico sin sacar conclusiones apresuradas;
- pedir a una IA una interpretación prudente.

## Tiempo sugerido

| Actividad | Tiempo |
|---|---:|
| Revisar datos | 5 min |
| Ejecutar script | 5 min |
| Leer gráfico | 5 min |
| Pedir interpretación a IA | 5-10 min |

## Antes de empezar

Asegúrate de haber revisado:

- [[00-empezar-aqui/reglas-de-privacidad|Reglas de privacidad]]
- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]

## Archivo de datos

Usa este archivo:

```text
assets/datos/ausentismo_ejemplo.csv
```

Es sintético. No contiene personas reales.

## Qué contiene el dataset

| Columna | Qué significa |
|---|---|
| `mes` | Mes del registro. |
| `area` | Área o servicio. |
| `dias_ausencia` | Total agregado de días de ausencia. |
| `eventos_ausencia` | Cantidad de eventos registrados. |
| `motivo_agregado` | Motivo agrupado, no diagnóstico individual. |
| `turno` | Turno asociado al registro agregado. |

## Pregunta profesional

> ¿En qué áreas se concentran más días de ausencia y qué preguntas deberíamos investigar antes de proponer acciones?

Observa que la pregunta no dice “cuál área tiene la culpa”. Dice “qué preguntas investigar”. Ese cambio es importante.

## Paso 1: abrir el CSV sin programar

1. Abre la carpeta del repositorio.
2. Entra a `assets/datos/`.
3. Abre `ausentismo_ejemplo.csv`.
4. Puedes abrirlo con Excel, Numbers, Google Sheets o un editor de texto.
5. Mira las columnas.
6. Revisa si entiendes qué representa cada fila.

Pregunta para pensar:

```text
¿Estoy viendo datos de personas individuales o datos agregados?
```

Respuesta esperada: datos agregados.

## Paso 2: validar que los archivos existen

Abre una consola en la carpeta del repositorio siguiendo [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]].

En Windows ejecuta:

```bash
python scripts/00_validar_datos.py
```

Si en Windows usas `py`:

```bash
py scripts/00_validar_datos.py
```

En macOS ejecuta:

```bash
python3 scripts/00_validar_datos.py
```

Resultado esperado:

```text
OK ausentismo_ejemplo.csv: 20 filas
```

## Paso 3: ejecutar el análisis

En Windows:

```bash
python scripts/01_analizar_ausentismo.py
```

Si usas `py`:

```bash
py scripts/01_analizar_ausentismo.py
```

En macOS:

```bash
python3 scripts/01_analizar_ausentismo.py
```

## Paso 4: revisar la salida

El script imprime algo parecido a:

```text
Días de ausencia por área:
area
Urgencias              87
Enfermeria             66
Servicios_generales    53
Laboratorio            32
Administracion         23
```

Esto significa que Python sumó los días de ausencia por cada área.

## Paso 5: revisar el gráfico

El gráfico se guarda en:

```text
assets/imagenes/ausentismo_por_area.png
```

Abre esa imagen.

Preguntas:

- ¿Qué área aparece con más días?
- ¿Qué área aparece con menos días?
- ¿Qué información falta antes de explicar por qué ocurre?
- ¿Podría haber diferencias por tamaño del equipo, turnos o forma de registrar ausencias?

## Código explicado

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

| Línea | Qué hace |
|---|---|
| `import pandas as pd` | Carga la herramienta para leer tablas. |
| `import matplotlib.pyplot as plt` | Carga la herramienta para graficar. |
| `pd.read_csv(...)` | Lee el archivo CSV. |
| `groupby("area")` | Agrupa filas por área. |
| `["dias_ausencia"].sum()` | Suma días de ausencia en cada área. |
| `sort_values(...)` | Ordena de mayor a menor. |
| `plot(kind="bar")` | Crea gráfico de barras. |

## Cómo pedirle ayuda a la IA

Prompt para entender el resultado:

```text
Actúa como docente de salud ocupacional.
Estoy viendo un resumen agregado de días de ausencia por área.
Ayúdame a separar hechos observables, hipótesis posibles y preguntas pendientes.
No inventes causas. No hagas recomendaciones individualizadas.
```

Prompt para explicar el código:

```text
Explícame este código línea por línea para una persona que sabe usar Excel pero está empezando con Python.
Usa ejemplos simples y no asumas conocimiento técnico.
```

## Cómo adaptar la práctica con otro archivo

Si quieres usar otro CSV seguro:

1. Guárdalo en `assets/datos/externos/`.
2. Revisa cómo se llaman las columnas.
3. Busca en el script esta línea:

```python
DATOS = ROOT / "assets" / "datos" / "ausentismo_ejemplo.csv"
```

4. Cámbiala por la nueva ruta.
5. Si las columnas no se llaman `area` y `dias_ausencia`, cambia también esas palabras en el script.

Prompt para pedir ayuda:

```text
Quiero adaptar el análisis de ausentismo a otro CSV.
La ruta es: assets/datos/externos/mi_archivo.csv.
Estas son sus columnas: [pega columnas].
Dime qué líneas debo cambiar para agrupar por área y sumar días.
Explícalo paso a paso.
```

## Qué NO concluir

No concluyas automáticamente:

- que un área “trabaja peor”;
- que una persona o grupo tiene responsabilidad;
- que existe una causa sin más evidencia;
- que el gráfico basta para decidir acciones.

## Producto final de esta práctica

Al finalizar deberías tener:

- resumen por área en consola;
- gráfico `ausentismo_por_area.png`;
- tres preguntas para investigar;
- una interpretación prudente escrita con ayuda de IA.

## Relacionado

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
