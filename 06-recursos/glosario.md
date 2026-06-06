# Glosario

tags: #glosario #recursos #principiantes

Este glosario explica términos frecuentes del vault en lenguaje simple. No busca definiciones académicas completas; busca ayudarte a seguir las prácticas sin perderte en la jerga.

## Cómo usar este glosario

- Si una palabra técnica te bloquea, búscala aquí primero.
- Si todavía no queda clara, pídele a una IA: `Explícame este término con un ejemplo de salud ocupacional`.
- Vuelve después a la práctica: la meta es aprender haciendo.

## Inteligencia artificial

| Término | Explicación simple | Ejemplo en este vault |
|---|---|---|
| Inteligencia artificial | Sistemas que generan texto, código, imágenes o análisis a partir de instrucciones y datos. | Pedir a ChatGPT que ayude a interpretar indicadores agregados. |
| IA generativa | IA que produce contenido nuevo: texto, código, tablas, resúmenes o diseños. | Crear un borrador de informe ejecutivo. |
| Modelo de lenguaje | Sistema entrenado para procesar y generar lenguaje natural. | ChatGPT o Claude respondiendo una pregunta. |
| ChatGPT | Herramienta web de IA útil para explicar, resumir, redactar y explorar ideas. | Pedir preguntas para analizar ausentismo. |
| Claude | Herramienta de IA útil para revisar textos largos, guiones y documentos. | Mejorar una actividad de capacitación. |
| Codex | Asistente orientado a programación y creación de código. | Crear o corregir un archivo HTML o script Python. |
| Prompt | Instrucción que se escribe a una IA. | `Actúa como analista de salud ocupacional...` |
| Contexto | Información que das a la IA para que entienda mejor la tarea. | Objetivo, audiencia, datos disponibles y límites. |
| Iterar | Mejorar un resultado en varios pasos. | Pedir una primera versión, revisarla y solicitar ajustes. |
| Alucinación | Respuesta inventada o incorrecta que la IA presenta con seguridad aparente. | La IA inventa causas de ausentismo que no están en los datos. |
| Copiloto | Forma de usar IA como apoyo, no como reemplazo del criterio humano. | La IA propone; la persona profesional valida. |

## Programación y web

| Término | Explicación simple | Ejemplo en este vault |
|---|---|---|
| Programar | Dar instrucciones precisas a un computador para resolver una tarea. | Leer un CSV y crear un gráfico. |
| Código | Texto con instrucciones que puede ejecutar un computador. | Los archivos en `scripts/`. |
| Script | Archivo de código pequeño para una tarea concreta. | `scripts/01_analizar_ausentismo.py`. |
| Variable | Nombre que guarda un valor para usarlo después. | `datos = pd.read_csv(...)`. |
| Función | Bloque de código que realiza una tarea. | `main()` en los scripts. |
| Librería | Conjunto de herramientas listas para usar en un lenguaje. | `pandas` y `matplotlib`. |
| Terminal | Ventana donde se escriben comandos. | Ejecutar `python scripts/00_validar_datos.py`. |
| Ruta de archivo | Ubicación de un archivo dentro de carpetas. | `assets/datos/ausentismo_ejemplo.csv`. |
| HTML | Lenguaje para estructurar páginas web. | `assets/checklist_interactivo.html`. |
| CSS | Lenguaje para dar estilo visual a una página web. | Colores, tamaños y distribución del checklist. |
| JavaScript | Lenguaje para agregar interacción a una página web. | Calcular el porcentaje de cumplimiento. |
| Navegador | Programa para abrir páginas web. | Chrome, Edge, Firefox o Safari. |
| Prototipo | Versión simple para probar una idea antes de construir algo grande. | Checklist interactivo de seguridad ocupacional. |

## Python y análisis de datos

| Término | Explicación simple | Ejemplo en este vault |
|---|---|---|
| Python | Lenguaje de programación usado para análisis, automatización y prototipos. | Scripts de análisis en `scripts/`. |
| pip | Herramienta para instalar librerías de Python. | `pip install -r requirements.txt`. |
| pandas | Librería de Python para trabajar con tablas. | Leer `ausentismo_ejemplo.csv`. |
| DataFrame | Tabla de datos dentro de pandas. | La variable `datos`. |
| Columna | Campo vertical de una tabla. | `area`, `mes`, `dias_ausencia`. |
| Fila | Registro horizontal de una tabla. | Un mes y área dentro del CSV. |
| Agrupar | Reunir datos por una categoría para resumirlos. | Sumar días de ausencia por área. |
| Indicador | Medida numérica que resume una situación. | Días de ausencia, incidentes reportados, cumplimiento. |
| matplotlib | Librería de Python para crear gráficos. | Gráfico de barras por tipo de incidente. |
| CSV | Archivo de texto que guarda una tabla separada por comas. | Archivos en `assets/datos/`. |
| requirements.txt | Archivo que lista librerías necesarias para ejecutar scripts. | `pandas` y `matplotlib`. |
| Validar datos | Revisar que los archivos existen y tienen las columnas esperadas. | `scripts/00_validar_datos.py`. |

## Datos, privacidad y ética

| Término | Explicación simple | Ejemplo en este vault |
|---|---|---|
| Dato sintético | Dato inventado para practicar sin exponer información real. | Todos los CSV de `assets/datos/`. |
| Dato identificable | Información que permite reconocer a una persona o institución. | Nombre, documento, teléfono, historia clínica. |
| Dato agregado | Información resumida por grupo, no por persona individual. | Días de ausencia por área y mes. |
| Anonimización | Proceso de quitar o transformar datos que identifican personas o instituciones. | Reemplazar nombres por categorías agregadas. |
| Sesgo | Distorsión que puede afectar datos, interpretación o decisiones. | Un área reporta más incidentes porque registra mejor, no porque sea más peligrosa. |
| Correlación | Relación observada entre variables, sin probar causa. | Más ausencias en un mes no prueba automáticamente una causa. |
| Causalidad | Relación donde un factor produce un efecto. | Requiere más evidencia que una tabla simple. |
| Validación humana | Revisión por una persona competente antes de usar un resultado. | Revisar un informe generado por IA. |
| Decisión de alto riesgo | Decisión que puede afectar derechos, salud o trabajo de una persona. | Aptitud ocupacional, triaje, sanciones o decisiones clínicas. |
| Privacidad | Protección de información sensible. | No pegar datos reales en herramientas públicas de IA. |
| Consentimiento | Autorización informada para usar cierta información. | No se asume por defecto en datos de salud. |

## Salud ocupacional

| Término | Explicación simple | Ejemplo en este vault |
|---|---|---|
| Salud ocupacional | Área enfocada en proteger y promover la salud en relación con el trabajo. | Analizar riesgos, ausentismo e incidentes de forma preventiva. |
| Seguridad en el trabajo | Prevención de accidentes, incidentes y condiciones inseguras. | Checklist de inspección. |
| Riesgo ocupacional | Posibilidad de daño asociado a una actividad, ambiente o condición de trabajo. | Exposición química o sobreesfuerzo. |
| Incidente | Evento que pudo causar o causó daño, lesión o pérdida. | Tropiezo sin lesión en un pasillo húmedo. |
| Severidad | Gravedad estimada de un evento. | Leve, moderada, alta. |
| Acción preventiva | Medida para reducir la probabilidad de que ocurra un evento. | Mejorar señalización o reforzar capacitación. |
| EPP | Elementos de protección personal. | Guantes, gafas, tapabocas, protección auditiva. |
| Ergonomía | Adaptación del trabajo a las capacidades y necesidades humanas. | Ajustar silla, monitor o pausas activas. |
| Ausentismo | Ausencias registradas al trabajo o actividades programadas. | Días de ausencia por área. |
| Checklist | Lista de verificación para revisar condiciones o acciones. | Checklist interactivo en HTML. |

## Obsidian y uso del vault

| Término | Explicación simple | Ejemplo en este vault |
|---|---|---|
| Obsidian | Aplicación para leer y conectar notas Markdown. | Abrir este repositorio como vault. |
| Vault | Carpeta de notas conectadas en Obsidian. | Este repositorio completo. |
| Markdown | Formato de texto simple para escribir notas con títulos, listas y enlaces. | Todos los archivos `.md`. |
| Wikilink | Enlace interno de Obsidian escrito con doble corchete. | `[[00-empezar-aqui/mapa-del-vault|Mapa del vault]]`. |
| MOC | Mapa de contenido: nota que organiza otras notas. | `06-recursos/recursos-moc.md`. |
| Tag | Etiqueta para buscar o agrupar notas. | `#python`, `#datos`, `#privacidad`. |
| Relacionado | Sección final con enlaces a notas conectadas. | La mayoría de notas del vault. |

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
