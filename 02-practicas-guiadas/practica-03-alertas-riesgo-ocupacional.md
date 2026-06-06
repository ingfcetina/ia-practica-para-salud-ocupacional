# Práctica 3: alertas de riesgo ocupacional

tags: #practica #riesgo #alertas #principiantes

En esta práctica vas a diseñar reglas simples de alerta preventiva usando datos sintéticos. Una alerta no es una decisión automática: es una señal para revisar mejor.

## Objetivo de aprendizaje

Al terminar podrás:

- explicar qué es una alerta preventiva;
- crear una regla simple y revisable;
- diferenciar alerta de sanción;
- pedir a una IA que convierta una regla en pasos lógicos;
- reconocer límites antes de actuar.

## Idea central

Una alerta debe responder:

```text
¿Dónde conviene mirar con más atención?
```

No debe responder:

```text
¿A quién culpamos?
```

## Datos sugeridos

Puedes usar:

```text
assets/datos/incidentes_ejemplo.csv
assets/datos/indicadores_dashboard_ejemplo.csv
```

## Ejemplo de regla

```text
Si un área tiene más de 3 incidentes leves en un mes o cualquier incidente severo,
marcarla para revisión preventiva.
```

Esta regla es didáctica. No es una norma institucional.

## Paso 1: escribir la regla en lenguaje humano

Antes de programar, escribe una regla clara.

Ejemplo:

```text
Si una categoría de incidente aparece varias veces, quiero revisarla.
```

Mejor versión:

```text
Si un tipo de incidente aparece 2 o más veces en los datos sintéticos,
lo marco para discusión preventiva.
```

## Paso 2: convertir la regla en pasos

```text
1. Leer datos de incidentes.
2. Contar cuántas veces aparece cada tipo de incidente.
3. Comparar cada conteo con un umbral.
4. Marcar las categorías que superan el umbral.
5. Escribir preguntas de seguimiento.
```

## Paso 3: pedir ayuda a la IA

```text
Convierte esta regla preventiva en pasos lógicos fáciles de revisar:
"Si un tipo de incidente aparece 2 o más veces, marcarlo para discusión preventiva".
No propongas sanciones.
No tomes decisiones sobre personas.
Incluye preguntas de seguimiento para salud ocupacional.
```

## Paso 4: ejemplo con Python

```python
import pandas as pd

datos = pd.read_csv("assets/datos/incidentes_ejemplo.csv")
conteo = datos["tipo_incidente"].value_counts()

umbral = 2
alertas = conteo[conteo >= umbral]

print(alertas)
```

## Qué significa cada línea

| Línea | Explicación |
|---|---|
| `pd.read_csv(...)` | Lee el CSV de incidentes. |
| `value_counts()` | Cuenta incidentes por tipo. |
| `umbral = 2` | Define cuándo se marca alerta. |
| `conteo >= umbral` | Revisa qué categorías cumplen la regla. |
| `print(alertas)` | Muestra las categorías marcadas. |

## Paso 5: convertir alertas en preguntas

Si aparece una alerta, no escribas “hay un problema confirmado”. Escribe preguntas:

| Alerta | Preguntas prudentes |
|---|---|
| Exposición química repetida | ¿Hay capacitación reciente? ¿El EPP es suficiente? ¿Hay cambios en productos o procesos? |
| Sobreesfuerzo repetido | ¿Hay ayudas mecánicas? ¿Se revisaron pesos y posturas? ¿Hay turnos con mayor carga? |
| Caídas al mismo nivel | ¿Hay pisos húmedos? ¿Señalización temporal? ¿Calzado adecuado? |

## Cómo adaptar la regla

Puedes cambiar:

| Elemento | Ejemplo |
|---|---|
| Umbral | `2`, `3`, `5` eventos. |
| Columna | `tipo_incidente`, `area`, `severidad`. |
| Acción | revisión, conversación, inspección, capacitación. |

Prompt para IA:

```text
Quiero ajustar una regla de alerta preventiva.
Tengo estas columnas: [pega columnas].
Propón 3 reglas simples, explícame qué datos necesita cada una y qué riesgo tendría interpretarla mal.
```

## Cuidado ético

Una alerta no debe convertirse en:

- castigo automático;
- señalamiento individual;
- conclusión causal;
- decisión clínica u ocupacional definitiva.

Debe activar:

- conversación;
- revisión de condiciones;
- búsqueda de causas;
- mejora preventiva.

## Producto final

Al terminar deberías tener:

- una regla escrita en lenguaje claro;
- una versión en pasos lógicos;
- una lista de alertas sintéticas;
- preguntas de seguimiento;
- límites de interpretación.

## Relacionado

- [[02-practicas-guiadas/practica-02-clasificar-incidentes|Práctica 2: clasificar incidentes]]
- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
- [[05-mini-proyectos/analizador-incidentes|Analizador de incidentes]]
