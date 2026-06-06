# Generar informes

tags: #python #informes #ia #principiantes

Python puede calcular indicadores y la IA puede ayudar a convertirlos en un texto más claro. La parte importante es separar:

- hechos observados;
- hipótesis posibles;
- límites del análisis;
- preguntas pendientes;
- recomendaciones prudentes.

## Flujo recomendado

```text
Datos sintéticos → cálculo con Python → informe base → revisión con IA → validación humana
```

## Script validado

Ejecuta:

```bash
python scripts/04_generar_informe_base.py
```

En macOS:

```bash
python3 scripts/04_generar_informe_base.py
```

El script genera:

```text
outputs/informe_base.md
```

## Qué hace el script

1. Lee `ausentismo_ejemplo.csv`.
2. Lee `incidentes_ejemplo.csv`.
3. Calcula indicadores agregados.
4. Escribe un informe base en Markdown.
5. Incluye límites y preguntas para discutir.

## Código conceptual

```python
# Leer datos
ausentismo = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
incidentes = pd.read_csv("assets/datos/incidentes_ejemplo.csv")

# Calcular indicadores simples
total_dias = int(ausentismo["dias_ausencia"].sum())
total_incidentes = len(incidentes)

# Crear texto de informe
informe = f"""
Días totales de ausencia: {total_dias}
Incidentes registrados: {total_incidentes}
"""
```

## Cómo pedirle a la IA que mejore el informe

Primero abre `outputs/informe_base.md` y copia su contenido. Luego usa este prompt:

```text
Revisa este informe con datos sintéticos.
Mejora la claridad para estudiantes y profesionales de salud ocupacional.
Separa hechos observados, hipótesis posibles, límites del análisis y preguntas pendientes.
No inventes causas.
No hagas recomendaciones individualizadas.
No uses lenguaje sancionatorio.
```

## Cómo reemplazar los datos

Si tienes otro CSV seguro y agregado:

1. Guárdalo en `assets/datos/externos/`.
2. Revisa sus columnas.
3. Cambia las rutas en el script.
4. Ajusta los nombres de columnas usados para calcular indicadores.
5. Ejecuta el script.
6. Revisa el informe antes de compartir.

Prompt para pedir ayuda:

```text
Quiero adaptar este script de informe a un nuevo CSV.
Estas son las columnas del nuevo archivo: [pega columnas].
Propón indicadores agregados seguros.
Dime qué líneas debo cambiar y por qué.
No uses datos identificables ni hagas conclusiones causales.
```

## Plantilla de informe prudente

```text
# Informe base

## Datos usados
[explicar archivo, fecha y límites]

## Resultados observados
[hechos numéricos]

## Hipótesis posibles
[ideas que requieren validación]

## Límites
[qué no se puede concluir]

## Preguntas pendientes
[qué investigar antes de decidir]
```

## Relacionado

- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[05-mini-proyectos/generador-informes|Generador de informes]]
- [[06-recursos/prompts|Banco de prompts]]
