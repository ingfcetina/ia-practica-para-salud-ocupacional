# Glosario

tags: #glosario #recursos #principiantes

Este glosario explica términos frecuentes del vault en lenguaje simple. No busca definiciones académicas completas; busca ayudarte a seguir las prácticas sin perderte en la jerga.

## Cómo usar este glosario

- Si una palabra técnica te bloquea, búscala aquí primero.
- Usa la columna **Referencia** para ir a documentación oficial o fuentes confiables.
- Si todavía no queda clara, pídele a una IA: `Explícame este término con un ejemplo de salud ocupacional`.
- Vuelve después a la práctica: la meta es aprender haciendo.

## Inteligencia artificial

| Término | Explicación simple | Ejemplo en este vault | Referencia |
|---|---|---|---|
| Inteligencia artificial | Sistemas que realizan tareas que normalmente requieren capacidades humanas como lenguaje, razonamiento, clasificación o generación. | Pedir a ChatGPT que ayude a interpretar indicadores agregados. | [IBM: What is AI?](https://www.ibm.com/think/topics/artificial-intelligence) |
| IA generativa | IA que produce contenido nuevo: texto, código, tablas, resúmenes, imágenes o diseños. | Crear un borrador de informe ejecutivo. | [Google Cloud: Generative AI](https://cloud.google.com/discover/what-is-generative-ai) |
| Modelo de lenguaje | Sistema entrenado para procesar y generar lenguaje natural. | ChatGPT o Claude respondiendo una pregunta. | [IBM: Large language models](https://www.ibm.com/think/topics/large-language-models) |
| ChatGPT | Herramienta web de IA útil para explicar, resumir, redactar y explorar ideas. | Pedir preguntas para analizar ausentismo. | [ChatGPT](https://chatgpt.com/) |
| Claude | Herramienta de IA útil para revisar textos largos, guiones y documentos. | Mejorar una actividad de capacitación. | [Claude](https://claude.ai/) |
| Claude Code | Herramienta de línea de comandos para trabajar con código y archivos de un proyecto usando Claude. | Revisar estructura del vault y proponer cambios. | [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code/overview) |
| Codex | Asistente orientado a programación y creación de código. | Crear o corregir un archivo HTML o script Python. | [OpenAI Codex](https://openai.com/codex/), [Codex CLI](https://github.com/openai/codex) |
| Prompt | Instrucción que se escribe a una IA. | `Actúa como analista de salud ocupacional...` | [OpenAI prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) |
| Contexto | Información que das a la IA para que entienda mejor la tarea. | Objetivo, audiencia, datos disponibles y límites. | [[06-recursos/prompts|Banco de prompts]] |
| Iterar | Mejorar un resultado en varios pasos. | Pedir una primera versión, revisarla y solicitar ajustes. | [[04-herramientas-ia/claude-code-y-codex|Usar este vault con Claude Code y Codex]] |
| Alucinación | Respuesta inventada o incorrecta que la IA presenta con seguridad aparente. | La IA inventa causas de ausentismo que no están en los datos. | [IBM: AI hallucinations](https://www.ibm.com/think/topics/ai-hallucinations) |
| Copiloto | Forma de usar IA como apoyo, no como reemplazo del criterio humano. | La IA propone; la persona profesional valida. | [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]] |

## Programación y web

| Término | Explicación simple | Ejemplo en este vault | Referencia |
|---|---|---|---|
| Programar | Dar instrucciones precisas a un computador para resolver una tarea. | Leer un CSV y crear un gráfico. | [Python tutorial](https://docs.python.org/3/tutorial/) |
| Código | Texto con instrucciones que puede ejecutar un computador. | Los archivos en `scripts/`. | [MDN: Getting started with the web](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web) |
| Script | Archivo de código pequeño para una tarea concreta. | `scripts/01_analizar_ausentismo.py`. | [[scripts/README|Scripts de ejemplo]] |
| Variable | Nombre que guarda un valor para usarlo después. | `datos = pd.read_csv(...)`. | [Python variables](https://docs.python.org/3/tutorial/introduction.html) |
| Función | Bloque de código que realiza una tarea. | `main()` en los scripts. | [Python functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) |
| Librería | Conjunto de herramientas listas para usar en un lenguaje. | `pandas` y `matplotlib`. | [Python modules](https://docs.python.org/3/tutorial/modules.html) |
| Terminal | Ventana donde se escriben comandos. | Ejecutar `python scripts/00_validar_datos.py`. | [MDN: Command line crash course](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools/Command_line) |
| Ruta de archivo | Ubicación de un archivo dentro de carpetas. | `assets/datos/ausentismo_ejemplo.csv`. | [Python pathlib](https://docs.python.org/3/library/pathlib.html) |
| HTML | Lenguaje para estructurar páginas web. | `assets/checklist_interactivo.html`. | [MDN: HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) |
| CSS | Lenguaje para dar estilo visual a una página web. | Colores, tamaños y distribución del checklist. | [MDN: CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) |
| JavaScript | Lenguaje para agregar interacción a una página web. | Calcular el porcentaje de cumplimiento. | [MDN: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) |
| Navegador | Programa para abrir páginas web. | Chrome, Edge, Firefox o Safari. | [MDN: How browsers work](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/How_browsers_work) |
| Prototipo | Versión simple para probar una idea antes de construir algo grande. | Checklist interactivo de seguridad ocupacional. | [[06-recursos/ideas-proyectos|Ideas de ampliación y proyectos]] |

## Python y análisis de datos

| Término | Explicación simple | Ejemplo en este vault | Referencia |
|---|---|---|---|
| Python | Lenguaje de programación usado para análisis, automatización y prototipos. | Scripts de análisis en `scripts/`. | [Python](https://www.python.org/), [Python docs](https://docs.python.org/3/) |
| pip | Herramienta para instalar librerías de Python. | `python -m pip install -r requirements.txt`. | [Installing Python packages](https://packaging.python.org/en/latest/tutorials/installing-packages/) |
| pandas | Librería de Python para trabajar con tablas. | Leer `ausentismo_ejemplo.csv`. | [pandas docs](https://pandas.pydata.org/docs/) |
| DataFrame | Tabla de datos dentro de pandas. | La variable `datos`. | [pandas DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) |
| Columna | Campo vertical de una tabla. | `area`, `mes`, `dias_ausencia`. | [[06-recursos/datasets-ejemplo|Datasets de ejemplo]] |
| Fila | Registro horizontal de una tabla. | Un mes y área dentro del CSV. | [[06-recursos/datasets-ejemplo|Datasets de ejemplo]] |
| Agrupar | Reunir datos por una categoría para resumirlos. | Sumar días de ausencia por área. | [pandas groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) |
| Indicador | Medida numérica que resume una situación. | Días de ausencia, incidentes reportados, cumplimiento. | [[02-practicas-guiadas/practica-04-dashboard-basico|Práctica 4: dashboard básico]] |
| matplotlib | Librería de Python para crear gráficos. | Gráfico de barras por tipo de incidente. | [matplotlib docs](https://matplotlib.org/stable/users/index.html) |
| CSV | Archivo de texto que guarda una tabla separada por comas. | Archivos en `assets/datos/`. | [Python csv module](https://docs.python.org/3/library/csv.html) |
| Jupyter Notebook | Archivo interactivo que combina texto, código y resultados. | Notebooks en `assets/notebooks/`. | [Jupyter](https://jupyter.org/), [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]] |
| requirements.txt | Archivo que lista librerías necesarias para ejecutar scripts. | `pandas` y `matplotlib`. | [pip requirements files](https://pip.pypa.io/en/stable/reference/requirements-file-format/) |
| Validar datos | Revisar que los archivos existen y tienen las columnas esperadas. | `scripts/00_validar_datos.py`. | [[scripts/README|Scripts de ejemplo]] |

## Datos, privacidad y ética

| Término | Explicación simple | Ejemplo en este vault | Referencia |
|---|---|---|---|
| Dato sintético | Dato inventado para practicar sin exponer información real. | Todos los CSV de `assets/datos/`. | [NIST: AI](https://www.nist.gov/artificial-intelligence) |
| Dato identificable | Información que permite reconocer a una persona o institución. | Nombre, documento, teléfono, historia clínica. | [HHS: Health information privacy](https://www.hhs.gov/hipaa/for-professionals/privacy/index.html) |
| Dato agregado | Información resumida por grupo, no por persona individual. | Días de ausencia por área y mes. | [[06-recursos/datasets-ejemplo|Datasets de ejemplo]] |
| Anonimización | Proceso de quitar o transformar datos que identifican personas o instituciones. | Reemplazar nombres por categorías agregadas. | [ICO](https://ico.org.uk/) |
| Sesgo | Distorsión que puede afectar datos, interpretación o decisiones. | Un área reporta más incidentes porque registra mejor, no porque sea más peligrosa. | [NIST AI](https://www.nist.gov/artificial-intelligence) |
| Correlación | Relación observada entre variables, sin probar causa. | Más ausencias en un mes no prueba automáticamente una causa. | [Wikipedia: Correlation does not imply causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation) |
| Causalidad | Relación donde un factor produce un efecto. | Requiere más evidencia que una tabla simple. | [CDC: Principles of epidemiology](https://www.cdc.gov/csels/dsepd/ss1978/index.html) |
| Validación humana | Revisión por una persona competente antes de usar un resultado. | Revisar un informe generado por IA. | [NIST AI](https://www.nist.gov/artificial-intelligence) |
| Decisión de alto riesgo | Decisión que puede afectar derechos, salud o trabajo de una persona. | Aptitud ocupacional, triaje, sanciones o decisiones clínicas. | [OECD AI Principles](https://oecd.ai/en/ai-principles) |
| Privacidad | Protección de información sensible. | No pegar datos reales en herramientas públicas de IA. | [OECD Privacy Guidelines](https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0188) |
| Consentimiento | Autorización informada para usar cierta información. | No se asume por defecto en datos de salud. | [WHO: Ethics and governance of AI for health](https://www.who.int/publications/i/item/9789240029200) |

## Salud ocupacional

| Término | Explicación simple | Ejemplo en este vault | Referencia |
|---|---|---|---|
| Salud ocupacional | Área enfocada en proteger y promover la salud en relación con el trabajo. | Analizar riesgos, ausentismo e incidentes de forma preventiva. | [WHO: Occupational health](https://www.who.int/health-topics/occupational-health) |
| Seguridad en el trabajo | Prevención de accidentes, incidentes y condiciones inseguras. | Checklist de inspección. | [ILO: Occupational safety and health](https://www.ilo.org/topics/occupational-safety-and-health) |
| Riesgo ocupacional | Posibilidad de daño asociado a una actividad, ambiente o condición de trabajo. | Exposición química o sobreesfuerzo. | [NIOSH](https://www.cdc.gov/niosh/) |
| Incidente | Evento que pudo causar o causó daño, lesión o pérdida. | Tropiezo sin lesión en un pasillo húmedo. | [OSHA](https://www.osha.gov/) |
| Severidad | Gravedad estimada de un evento. | Leve, moderada, alta. | [NIOSH hierarchy of controls](https://www.cdc.gov/niosh/hierarchy-of-controls/about/index.html) |
| Acción preventiva | Medida para reducir la probabilidad de que ocurra un evento. | Mejorar señalización o reforzar capacitación. | [NIOSH hierarchy of controls](https://www.cdc.gov/niosh/hierarchy-of-controls/about/index.html) |
| EPP | Elementos de protección personal. | Guantes, gafas, tapabocas, protección auditiva. | [OSHA PPE](https://www.osha.gov/personal-protective-equipment) |
| Ergonomía | Adaptación del trabajo a las capacidades y necesidades humanas. | Ajustar silla, monitor o pausas activas. | [NIOSH Ergonomics](https://www.cdc.gov/niosh/ergonomics/) |
| Ausentismo | Ausencias registradas al trabajo o actividades programadas. | Días de ausencia por área. | [[02-practicas-guiadas/practica-01-analizar-ausentismo|Práctica 1: analizar ausentismo]] |
| Checklist | Lista de verificación para revisar condiciones o acciones. | Checklist interactivo en HTML. | [[05-mini-proyectos/checklist-inteligente|Checklist inteligente]] |

## Obsidian y uso del vault

| Término | Explicación simple | Ejemplo en este vault | Referencia |
|---|---|---|---|
| Obsidian | Aplicación para leer y conectar notas Markdown. | Abrir este repositorio como vault. | [Obsidian](https://obsidian.md/), [Obsidian Help](https://help.obsidian.md/) |
| Vault | Carpeta de notas conectadas en Obsidian. | Este repositorio completo. | [Obsidian vaults](https://help.obsidian.md/Getting+started/Create+a+vault) |
| Markdown | Formato de texto simple para escribir notas con títulos, listas y enlaces. | Todos los archivos `.md`. | [Markdown Guide](https://www.markdownguide.org/basic-syntax/) |
| Wikilink | Enlace interno de Obsidian escrito con doble corchete. | `[[00-empezar-aqui/mapa-del-vault|Mapa del vault]]`. | [Obsidian internal links](https://help.obsidian.md/Linking+notes+and+files/Internal+links) |
| MOC | Mapa de contenido: nota que organiza otras notas. | `06-recursos/recursos-moc.md`. | [Obsidian links](https://help.obsidian.md/Linking+notes+and+files/Internal+links) |
| Tag | Etiqueta para buscar o agrupar notas. | `#python`, `#datos`, `#privacidad`. | [Obsidian tags](https://help.obsidian.md/Editing+and+formatting/Tags) |
| Mermaid | Lenguaje para crear diagramas desde texto. | Diagramas en [[06-recursos/diagramas-mermaid|Diagramas Mermaid]]. | [Mermaid docs](https://mermaid.js.org/intro/) |
| Relacionado | Sección final con enlaces a notas conectadas. | La mayoría de notas del vault. | [[00-empezar-aqui/como-usar-este-vault|Cómo usar este vault]] |

## Frases clave para recordar

- La IA propone; la persona profesional valida.
- Los datos sintéticos son para practicar; los datos reales requieren cuidado institucional.
- Un gráfico muestra patrones, no prueba causas por sí solo.
- Un prototipo sirve para aprender y conversar antes de construir algo grande.
- Si algo falla, revisa el objetivo del paso antes de memorizar comandos.

## Relacionado

- [[00-empezar-aqui/como-usar-este-vault|Cómo usar este vault]]
- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[01-conceptos-clave/que-es-programar-con-ia|Qué es programar con IA]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[06-recursos/diagramas-mermaid|Diagramas Mermaid]]
- [[06-recursos/enlaces-oficiales|Enlaces oficiales]]
