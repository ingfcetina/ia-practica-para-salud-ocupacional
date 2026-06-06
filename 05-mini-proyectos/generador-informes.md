# Generador de informes

tags: #mini-proyecto #informes #ia #python

Objetivo: convertir indicadores agregados en un informe ejecutivo breve, claro y prudente.

Este proyecto combina Python e IA:

- Python calcula indicadores.
- La IA ayuda a redactar mejor.
- La persona profesional revisa límites y sentido.

## Datos base

Usa:

```text
assets/datos/ausentismo_ejemplo.csv
assets/datos/incidentes_ejemplo.csv
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

El resultado se guarda en:

```text
outputs/informe_base.md
```

## Estructura sugerida del informe

1. Resumen ejecutivo.
2. Datos usados y límites.
3. Resultados observados.
4. Hipótesis posibles, no conclusiones definitivas.
5. Acciones preventivas sugeridas.
6. Próximas preguntas.

## Paso a paso

1. Ejecuta el script.
2. Abre `outputs/informe_base.md`.
3. Lee los resultados observados.
4. Copia el informe base en una IA.
5. Pide mejorar claridad sin inventar causas.
6. Revisa el texto final con criterio profesional.

## Prompt para mejorar el informe

```text
Redacta un informe ejecutivo con estos indicadores agregados.
Distingue hechos observados, hipótesis posibles, límites del análisis y recomendaciones prudentes.
Incluye una advertencia de que no se usaron datos personales identificables.
No inventes causas.
No nombres responsables.
No hagas recomendaciones individualizadas.
```

## Cómo reemplazar los datos

Si tienes otro archivo seguro:

1. Guárdalo en `assets/datos/externos/`.
2. Revisa columnas.
3. Decide qué indicadores agregados quieres calcular.
4. Cambia las rutas en `scripts/04_generar_informe_base.py`.
5. Cambia los nombres de columnas si son diferentes.
6. Ejecuta el script.
7. Revisa el informe.

Prompt para pedir ayuda:

```text
Quiero adaptar un script que genera informes.
El nuevo CSV está en: assets/datos/externos/mi_archivo.csv.
Sus columnas son: [pega aquí columnas].
Propón 3 indicadores agregados seguros y dime qué líneas del script debo cambiar.
No uses datos identificables ni hagas análisis individual.
```

## Más robusto: informe con secciones obligatorias

Puedes pedir a la IA que el informe final tenga siempre:

```text
## Datos usados
## Resultados observados
## Lo que no se puede concluir
## Preguntas pendientes
## Recomendaciones prudentes
```

Prompt:

```text
Reorganiza este informe usando exactamente estas secciones:
Datos usados, Resultados observados, Lo que no se puede concluir, Preguntas pendientes, Recomendaciones prudentes.
Mantén lenguaje claro para profesionales de salud ocupacional.
```

## Validación antes de compartir

- [ ] El informe dice que los datos son sintéticos o agregados.
- [ ] No hay nombres de personas o instituciones.
- [ ] Se separan hechos e hipótesis.
- [ ] No hay conclusiones causales sin evidencia.
- [ ] Las recomendaciones son prudentes.

## Relacionado

- [[03-python-desde-cero/generar-informes|Generar informes]]
- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[06-recursos/prompts|Banco de prompts]]
