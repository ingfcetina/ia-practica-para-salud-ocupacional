# Práctica 2: clasificar incidentes

tags: #practica #incidentes #ia #principiantes

En esta práctica vas a organizar descripciones sintéticas de incidentes en categorías preventivas. La idea no es sancionar ni señalar personas, sino aprender a ordenar información para conversar sobre prevención.

## Objetivo de aprendizaje

Al terminar podrás:

- leer descripciones breves de incidentes;
- distinguir descripción, categoría y severidad;
- contar incidentes por tipo;
- pedir a una IA una clasificación prudente;
- revisar por qué la clasificación automática necesita criterio humano.

## Tiempo sugerido

| Actividad | Tiempo |
|---|---:|
| Leer el CSV | 5 min |
| Clasificar 3 ejemplos manualmente | 5 min |
| Ejecutar gráfico | 5 min |
| Pedir clasificación a IA | 10 min |
| Comparar y discutir | 10 min |

## Archivo de datos

Usa:

```text
assets/datos/incidentes_ejemplo.csv
```

Es un archivo sintético. Las descripciones son inventadas.

## Qué contiene el dataset

| Columna | Qué significa |
|---|---|
| `fecha` | Fecha sintética del evento. |
| `area` | Área donde se reporta el evento. |
| `descripcion` | Texto breve del incidente. |
| `tipo_incidente` | Categoría preventiva. |
| `severidad` | Nivel simple: leve o moderada. |
| `accion_inicial` | Acción inicial sugerida en el ejemplo. |

## Paso 1: leer tres incidentes sin IA

Abre el CSV y lee estas columnas:

```text
descripcion
tipo_incidente
severidad
```

Elige tres filas y pregúntate:

- ¿Qué pasó?
- ¿Qué riesgo aparece?
- ¿Qué dato falta?
- ¿La severidad parece clara o discutible?

## Paso 2: revisar categorías sugeridas

Categorías usadas en el ejemplo:

- caída al mismo nivel;
- corte o punción;
- sobreesfuerzo;
- exposición química;
- riesgo biológico;
- golpe o atrapamiento;
- ergonomía;
- otro.

Estas categorías no son universales. Son categorías didácticas para practicar.

## Paso 3: ejecutar el gráfico

En Windows:

```bash
python scripts/02_graficar_incidentes.py
```

Si usas `py`:

```bash
py scripts/02_graficar_incidentes.py
```

En macOS:

```bash
python3 scripts/02_graficar_incidentes.py
```

El gráfico se guarda en:

```text
assets/imagenes/incidentes_por_tipo.png
```

## Paso 4: interpretar el gráfico

Abre la imagen y responde:

- ¿Qué tipo de incidente aparece más?
- ¿Cuántos registros hay en total?
- ¿La muestra es suficientemente grande?
- ¿Podría haber subregistro?
- ¿Las categorías fueron asignadas con el mismo criterio?

## Paso 5: pedir ayuda a la IA

Copia algunas descripciones sintéticas y usa este prompt:

```text
Actúa como profesional de salud ocupacional.
Clasifica estas descripciones sintéticas de incidentes en categorías preventivas.
Devuelve una tabla con descripcion, categoria, nivel_confianza y pregunta_de_seguimiento.
Si la descripción es ambigua, marca nivel_confianza bajo.
No identifiques responsables individuales.
No propongas sanciones.
```

## Paso 6: comparar IA vs revisión humana

Crea una tabla simple:

| Descripción | Categoría del CSV | Categoría sugerida por IA | ¿Coinciden? | Pregunta pendiente |
|---|---|---|---|---|
| ... | ... | ... | Sí/No | ... |

La pregunta importante no es “quién tiene razón”, sino:

> ¿Qué información falta para clasificar mejor?

## Código explicado

```python
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("assets/datos/incidentes_ejemplo.csv")
conteo = datos["tipo_incidente"].value_counts()

conteo.plot(kind="bar", color="#27ae60")
plt.title("Incidentes por tipo")
plt.xlabel("Tipo de incidente")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()
```

| Línea | Qué hace |
|---|---|
| `pd.read_csv(...)` | Lee el CSV de incidentes. |
| `datos["tipo_incidente"]` | Selecciona la columna de categoría. |
| `value_counts()` | Cuenta cuántas veces aparece cada categoría. |
| `plot(kind="bar")` | Crea un gráfico de barras. |

## Cómo adaptar la práctica

Si tienes otro CSV seguro:

1. Guarda el archivo en `assets/datos/externos/`.
2. Revisa si tiene una columna de descripción.
3. Revisa si tiene una columna de categoría.
4. Cambia la ruta del archivo en el script.
5. Cambia `tipo_incidente` por el nombre real de tu columna.

Prompt para pedir ayuda:

```text
Quiero adaptar el análisis de incidentes a otro CSV.
La ruta es: assets/datos/externos/incidentes.csv.
Estas son sus columnas: [pega columnas].
Dime qué columna puedo usar para categorizar y qué línea del código debo cambiar.
Explica paso a paso para una persona principiante.
```

## Qué NO concluir

No concluyas automáticamente:

- que un área es insegura solo por tener más reportes;
- que una persona es responsable;
- que la categoría asignada por IA es verdad final;
- que una acción preventiva aplica sin revisar contexto.

## Producto final

Al terminar deberías tener:

- gráfico `incidentes_por_tipo.png`;
- una tabla comparando clasificación humana e IA;
- preguntas pendientes;
- una explicación de límites del análisis.

## Relacionado

- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[05-mini-proyectos/analizador-incidentes|Analizador de incidentes]]
- [[06-recursos/prompts|Banco de prompts]]
