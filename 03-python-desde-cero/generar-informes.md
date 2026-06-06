# Generar informes

tags: #python #informes #ia

Python puede producir resultados y la IA puede ayudar a convertirlos en un informe claro.

## Flujo recomendado

1. Calcular indicadores con Python.
2. Copiar solo datos agregados.
3. Pedir a la IA un borrador de informe.
4. Revisar conclusiones, sesgos y límites.

## Script validado

```bash
python scripts/04_generar_informe_base.py
```

El script genera `outputs/informe_base.md` con resultados observados y preguntas para discutir.

## Prompt

```text
Con estos indicadores agregados, redacta un informe ejecutivo de una página.
Separa resultados observados, posibles hipótesis, límites del análisis y recomendaciones prudentes.
No inventes causas ni nombres responsables.
```

## Relacionado

- [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]]
- [[06-recursos/prompts|Banco de prompts]]
