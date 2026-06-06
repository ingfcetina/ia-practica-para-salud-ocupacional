# Checklist inteligente

tags: #mini-proyecto #checklist #web #principiantes

Objetivo: adaptar una página web simple para hacer una actividad de inspección o capacitación en salud ocupacional.

Este mini proyecto está pensado para personas que no programan todavía. La idea es cambiar textos con cuidado, probar el archivo y pedir ayuda a la IA cuando haga falta.

## Archivo base

Abre este archivo con doble clic:

```text
assets/checklist_interactivo.html
```

También hay datos sintéticos para analizar checklist:

```text
assets/datos/checklist_inspeccion_ejemplo.csv
```

## Qué hace el ejemplo

- muestra preguntas de inspección;
- permite elegir `Sí`, `No` o `Sin responder`;
- calcula porcentaje de cumplimiento;
- muestra una recomendación general;
- no guarda datos ni envía información a internet.

## Qué puedes reemplazar

En el archivo HTML busca esta parte:

```javascript
const preguntas = [
  "El área de trabajo está libre de obstáculos visibles",
  "Los elementos de protección personal requeridos están disponibles",
  "Las rutas de evacuación están señalizadas y despejadas",
  "Los residuos se encuentran separados según el protocolo",
  "El personal conoce a quién reportar un incidente o condición insegura",
];
```

Puedes reemplazar las frases por preguntas de tu tema.

Ejemplo para ergonomía:

```javascript
const preguntas = [
  "La pantalla está a una altura cómoda para la persona usuaria",
  "La silla permite apoyar la espalda",
  "Los pies pueden apoyarse de forma estable",
  "Hay pausas activas durante la jornada",
  "El teclado y el mouse están ubicados sin tensión en hombros",
];
```

## Paso a paso

1. Abre `assets/checklist_interactivo.html` en un editor de texto.
2. Busca `const preguntas = [`.
3. Cambia solo las frases entre comillas.
4. Guarda el archivo.
5. Haz doble clic sobre el HTML para abrirlo en el navegador.
6. Prueba todas las respuestas.
7. Si algo se rompe, vuelve al archivo original o pide ayuda a la IA.

## Cómo pedirle a la IA que lo adapte

```text
Quiero adaptar este HTML para una capacitación de ergonomía.
Mantén un solo archivo HTML.
No uses librerías externas.
Cambia solo las preguntas y recomendaciones necesarias.
Agrega comentarios simples para explicar qué parte puedo modificar.
No recolectes datos personales.
```

Prompt si tienes un error:

```text
Modifiqué este archivo HTML y ahora no funciona.
Te pego el código completo.
Encuentra el error y explícame qué línea debo corregir.
Haz una corrección mínima.
```

## Ideas de adaptación

| Tema | Preguntas posibles |
|---|---|
| Ergonomía | postura, pantalla, silla, pausas, iluminación. |
| Emergencias | rutas, señalización, punto de encuentro, extintores. |
| Laboratorio | gafas, guantes, rotulado, ventilación, residuos. |
| Orden y aseo | obstáculos, derrames, almacenamiento, pasillos. |
| EPP | disponibilidad, uso correcto, reposición, capacitación. |

## Validación antes de compartir

- [ ] El archivo abre con doble clic.
- [ ] Las preguntas son claras.
- [ ] No hay nombres de personas o instituciones.
- [ ] Las recomendaciones no son sancionatorias.
- [ ] La actividad se entiende en menos de 5 minutos.

## Relacionado

- [[02-practicas-guiadas/practica-05-presentacion-web-interactiva|Práctica 5: presentación web interactiva]]
- [[04-herramientas-ia/claude-code-y-codex|Usar este vault con Claude Code y Codex]]
- [[06-recursos/ideas-proyectos|Ideas de ampliación y proyectos]]
