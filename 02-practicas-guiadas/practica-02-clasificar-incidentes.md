# Práctica 2: clasificar incidentes

tags: #practica #incidentes #ia

Objetivo: convertir descripciones breves y sintéticas de incidentes en categorías útiles para prevención.

## Archivo de datos

Usa `assets/datos/incidentes_ejemplo.csv`.

## Script validado

Para contar y graficar incidentes por tipo, ejecuta:

```bash
python scripts/02_graficar_incidentes.py
```

El script guarda el gráfico en `assets/imagenes/incidentes_por_tipo.png`.

## Categorías sugeridas

- caída al mismo nivel;
- corte o punción;
- sobreesfuerzo;
- exposición química;
- riesgo biológico;
- golpe o atrapamiento;
- ergonomía;
- otro.

## Prompt para IA

```text
Actúa como profesional de seguridad y salud en el trabajo.
Clasifica estas descripciones sintéticas de incidentes en categorías preventivas.
Devuelve una tabla con descripcion, categoria, nivel_confianza y comentario.
Si la descripción es ambigua, marca nivel_confianza bajo.
```

## Revisión humana

La clasificación automática no es verdad final. Sirve para ordenar información y detectar patrones; debe revisarse por una persona competente.

## Relacionado

- [[03-python-desde-cero/limpiar-datos|Limpiar datos]]
- [[06-recursos/prompts|Banco de prompts]]
