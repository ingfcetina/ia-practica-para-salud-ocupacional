# Graficar resultados

tags: #python #graficos #principiantes

Un gráfico ayuda a ver patrones sin perderse en una tabla. Pero un gráfico no prueba causas: solo muestra una forma de mirar los datos.

En esta nota vas a contar incidentes por tipo y guardar una imagen de barras.

## Objetivo de aprendizaje

Al terminar podrás:

- abrir un CSV de incidentes;
- contar registros por categoría;
- ejecutar un script que guarda un gráfico;
- abrir la imagen generada;
- explicar qué hace `value_counts()`;
- interpretar un gráfico con cuidado.

## Tiempo sugerido

| Actividad | Tiempo |
|---|---:|
| Abrir CSV de incidentes | 5 min |
| Ejecutar script | 5 min |
| Revisar imagen | 5 min |
| Leer código explicado | 10 min |
| Adaptar gráfico | 10 min |

## Antes de empezar

Revisa:

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[02-practicas-guiadas/practica-02-clasificar-incidentes|Práctica 2: clasificar incidentes]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]

## Archivo de datos

Usa:

```text
assets/datos/incidentes_ejemplo.csv
```

El gráfico se guarda en:

```text
assets/imagenes/incidentes_por_tipo.png
```

## Qué contiene el dataset

| Columna | Qué significa |
|---|---|
| `fecha` | Fecha sintética del evento. |
| `area` | Área donde se reporta el evento. |
| `descripcion` | Texto breve del incidente. |
| `tipo_incidente` | Categoría preventiva. |
| `severidad` | Nivel simple: leve o moderada. |
| `accion_inicial` | Acción inicial sugerida en el ejemplo. |

## Pregunta profesional

> ¿Qué tipos de incidentes aparecen con más frecuencia en estos datos sintéticos?

La pregunta no busca culpables. Busca temas para revisar.

## Paso 1: abrir el CSV sin programar

1. Entra a `assets/datos/`.
2. Abre `incidentes_ejemplo.csv`.
3. Busca la columna `tipo_incidente`.
4. Observa si algunas categorías se repiten.

Pregunta para pensar:

```text
¿Estoy contando incidentes por categoría o explicando sus causas?
```

Respuesta esperada: solo estás contando categorías.

## Paso 2: ejecutar el script

### Windows

```bash
python scripts/02_graficar_incidentes.py
```

Si usas `py`:

```bash
py scripts/02_graficar_incidentes.py
```

### macOS

```bash
python3 scripts/02_graficar_incidentes.py
```

## Paso 3: revisar salida esperada

Deberías ver algo parecido a:

```text
Incidentes por tipo:
tipo_incidente
exposicion_quimica    2
caida_mismo_nivel     2
sobreesfuerzo         2
corte_puncion         2
golpe_atrapamiento    2
ergonomia             1
riesgo_biologico      1
Gráfico guardado en assets/imagenes/incidentes_por_tipo.png
```

## Paso 4: abrir la imagen

1. Entra a `assets/imagenes/`.
2. Abre `incidentes_por_tipo.png`.
3. Mira el título.
4. Mira el eje horizontal.
5. Mira el eje vertical.
6. Pregunta qué categorías aparecen más.

## Código explicado

Este ejemplo está alineado con el script, que guarda la imagen en archivo.

```python
# pandas permite leer y resumir tablas.
import pandas as pd

# matplotlib permite crear gráficos.
import matplotlib.pyplot as plt

# Leemos datos sintéticos de incidentes.
datos = pd.read_csv("assets/datos/incidentes_ejemplo.csv")

# Contamos cuántas veces aparece cada tipo de incidente.
conteo = datos["tipo_incidente"].value_counts()

# Creamos un gráfico de barras.
conteo.plot(kind="bar", color="#27ae60")

# Agregamos título y nombres de ejes.
plt.title("Incidentes por tipo")
plt.xlabel("Tipo de incidente")
plt.ylabel("Cantidad")

# Ajustamos el diseño para que no se corten etiquetas.
plt.tight_layout()

# Guardamos el gráfico como imagen.
plt.savefig("assets/imagenes/incidentes_por_tipo.png", dpi=160)
plt.close()
```

## Qué significa cada línea

| Código | Explicación |
|---|---|
| `pd.read_csv(...)` | Lee el CSV de incidentes. |
| `datos["tipo_incidente"]` | Selecciona la columna que se va a contar. |
| `value_counts()` | Cuenta cuántas veces aparece cada categoría. |
| `plot(kind="bar")` | Crea un gráfico de barras. |
| `plt.title(...)` | Agrega título. |
| `plt.xlabel(...)` | Nombra el eje horizontal. |
| `plt.ylabel(...)` | Nombra el eje vertical. |
| `plt.savefig(...)` | Guarda la imagen. |
| `plt.close()` | Cierra el gráfico en memoria. |

## Qué puedes cambiar

| Si quieres cambiar... | Línea a revisar |
|---|---|
| Archivo de datos | `pd.read_csv(...)` |
| Columna que se cuenta | `datos["tipo_incidente"]` |
| Tipo de gráfico | `kind="bar"` |
| Color | `color="#27ae60"` |
| Título | `plt.title(...)` |
| Archivo de salida | `plt.savefig(...)` |

## Ejemplo: graficar severidad

Este ejemplo reutiliza las líneas anteriores de `import pandas`, `import matplotlib.pyplot` y `pd.read_csv(...)`. Solo cambia la columna que se cuenta y el nombre del archivo de salida.

```python
conteo = datos["severidad"].value_counts()
conteo.plot(kind="bar", color="#f97316")
plt.title("Incidentes por severidad")
plt.xlabel("Severidad")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig("assets/imagenes/incidentes_por_severidad.png", dpi=160)
plt.close()
```

## Cómo pedirle ayuda a la IA

Prompt para crear un gráfico:

```text
Tengo una tabla CSV con estas columnas: [pega las columnas].
Quiero crear un gráfico de barras en Python.
Indícame qué columna conviene contar y dame código con comentarios para principiantes.
El gráfico debe guardarse como archivo PNG.
No interpretes causas, solo ayuda a visualizar datos.
```

Prompt para interpretar con cuidado:

```text
Este gráfico muestra conteos por categoría.
Ayúdame a separar hechos observables, preguntas pendientes y límites del análisis.
No inventes causas ni hagas recomendaciones individualizadas.
```

## Preguntas antes de interpretar

- ¿La muestra es suficiente?
- ¿Faltan registros?
- ¿Hay sesgos de reporte?
- ¿La categoría fue asignada de forma consistente?
- ¿Necesito revisar el contexto con una persona experta?

## Qué NO concluir

No concluyas automáticamente:

- que una categoría tiene una causa confirmada;
- que un área o persona es responsable;
- que el gráfico muestra todos los incidentes reales;
- que el conteo basta para decidir acciones.

## Si algo falla

| Problema | Qué revisar |
|---|---|
| No aparece la imagen | Revisa si existe `assets/imagenes/` y si ejecutaste desde la carpeta correcta. |
| Sale `KeyError: 'tipo_incidente'` | La columna no existe o está escrita distinto. |
| El gráfico se ve cortado | Revisa `plt.tight_layout()` o aumenta el tamaño en el script. |
| Sale `ModuleNotFoundError: matplotlib` | Falta instalar dependencias. |

## Producto final

Al terminar deberías tener:

- CSV de incidentes revisado;
- script ejecutado;
- conteo por tipo leído en consola;
- imagen `assets/imagenes/incidentes_por_tipo.png` abierta;
- una interpretación prudente con límites.

## Relacionado

- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[03-python-desde-cero/generar-informes|Generar informes]]
- [[06-recursos/datos-abiertos-colombia|Datos abiertos de Colombia]]
