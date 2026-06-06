# Generador de informes

tags: #mini-proyecto #informes

Objetivo: convertir indicadores agregados en un informe ejecutivo breve.

## Estructura sugerida

1. Resumen ejecutivo.
2. Datos usados y límites.
3. Resultados observados.
4. Hipótesis, no conclusiones definitivas.
5. Acciones preventivas sugeridas.
6. Próximas preguntas.

## Script validado

```bash
python scripts/04_generar_informe_base.py
```

El resultado se guarda en `outputs/informe_base.md` y puede usarse como base para revisar cómo pedir un informe a una IA.

## Prompt

```text
Redacta un informe ejecutivo con estos indicadores agregados.
Distingue hechos, hipótesis y recomendaciones.
Incluye una advertencia de que no se usaron datos personales identificables.
```

## Relacionado

- [[03-python-desde-cero/generar-informes|Generar informes]]
- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
