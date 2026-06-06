# Diagramas Mermaid

tags: #mermaid #diagramas #recursos #conceptos

Estos diagramas ayudan a explicar visualmente los conceptos centrales del vault. Obsidian y GitHub pueden renderizar Mermaid en bloques de código.

Referencia oficial: <https://mermaid.js.org/intro/>

## 1. Flujo general de trabajo con IA

```mermaid
flowchart TD
    A[Problema profesional] --> B[Datos seguros o sintéticos]
    B --> C[Prompt claro]
    C --> D[Respuesta o código de IA]
    D --> E[Prueba con datos de ejemplo]
    E --> F[Revisión humana]
    F --> G{¿Es útil y seguro?}
    G -- Sí --> H[Documentar resultado]
    G -- No --> I[Corregir prompt o código]
    I --> C
```

Idea clave: la IA no reemplaza la validación profesional; ayuda a avanzar más rápido con prototipos y explicaciones.

## 2. De CSV a gráfico con Python

```mermaid
flowchart LR
    A[CSV sintético] --> B[pandas lee la tabla]
    B --> C[Limpiar y revisar columnas]
    C --> D[Agrupar datos]
    D --> E[matplotlib crea gráfico]
    E --> F[Interpretación prudente]
```

Notas relacionadas:

- [[03-python-desde-cero/leer-datos-csv|Leer datos CSV]]
- [[03-python-desde-cero/graficar-resultados|Graficar resultados]]
- [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]]

## 3. Diferencia entre script y notebook

```mermaid
flowchart TD
    A[Quiero aprender o explorar] --> B[Notebook .ipynb]
    B --> C[Celdas de texto]
    B --> D[Celdas de código]
    B --> E[Resultados visibles]

    F[Quiero automatizar una tarea] --> G[Script .py]
    G --> H[Ejecutar comando]
    H --> I[Resultado reproducible]
```

Notas relacionadas:

- [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]]
- [[assets/notebooks/README|Notebooks de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]

## 4. Decisión segura con datos e IA

```mermaid
flowchart TD
    A[Resultado generado por IA] --> B{¿Usa datos reales identificables?}
    B -- Sí --> C[Detener y anonimizar]
    B -- No --> D{¿Hace recomendaciones individuales?}
    D -- Sí --> E[Revisar con profesional autorizado]
    D -- No --> F{¿Separa hechos de hipótesis?}
    F -- No --> G[Pedir corrección]
    F -- Sí --> H[Usar como apoyo para discusión]
```

Notas relacionadas:

- [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]]
- [[00-empezar-aqui/reglas-de-privacidad|Reglas de privacidad]]

## 5. Arquitectura simple del vault

```mermaid
flowchart TD
    A[README] --> B[00 Empezar aquí]
    A --> C[01 Conceptos clave]
    A --> D[02 Prácticas guiadas]
    A --> E[03 Python desde cero]
    A --> F[04 Herramientas IA]
    A --> G[05 Mini proyectos]
    A --> H[06 Recursos]
    H --> I[Glosario]
    H --> J[Datasets]
    H --> K[Diagramas]
    D --> L[Datos sintéticos]
    E --> M[Scripts]
    E --> N[Notebooks]
```

## 6. Uso de Claude Code o Codex

```mermaid
sequenceDiagram
    participant Persona as Estudiante o docente
    participant Agente as Claude Code / Codex
    participant Repo as Vault en GitHub
    participant Python as Python/Jupyter

    Persona->>Agente: Lee README y mapa del vault
    Agente->>Repo: Revisa estructura y archivos
    Agente-->>Persona: Resume ruta y propone plan
    Persona->>Agente: Aprueba una tarea pequeña
    Agente->>Python: Ejecuta validaciones o scripts
    Python-->>Agente: Devuelve resultados
    Agente-->>Persona: Explica hallazgos y límites
```

Notas relacionadas:

- [[04-herramientas-ia/claude-code-y-codex|Usar este vault con Claude Code y Codex]]
- [[06-recursos/prompts|Banco de prompts]]

## 7. De idea a mini proyecto

```mermaid
flowchart TD
    A[Idea de proyecto] --> B[Definir audiencia]
    B --> C[Elegir datos sintéticos]
    C --> D[Diseñar prototipo mínimo]
    D --> E[Crear script, notebook o HTML]
    E --> F[Probar]
    F --> G[Documentar límites]
    G --> H[Compartir o presentar]
```

Notas relacionadas:

- [[06-recursos/ideas-proyectos|Ideas de ampliación y proyectos]]
- [[05-mini-proyectos/mini-proyectos-moc|Mini proyectos]]

## Cómo crear tus propios diagramas

Pídele a una IA:

```text
Crea un diagrama Mermaid tipo flowchart para explicar este proceso a estudiantes principiantes.
Usa máximo 8 nodos, etiquetas cortas y lenguaje claro.
```

Luego pega el resultado en un bloque:

````markdown
```mermaid
flowchart TD
    A[Inicio] --> B[Resultado]
```
````

## Relacionado

- [[06-recursos/glosario|Glosario]]
- [[06-recursos/enlaces-oficiales|Enlaces oficiales]]
- [[04-herramientas-ia/claude-code-y-codex|Usar este vault con Claude Code y Codex]]
