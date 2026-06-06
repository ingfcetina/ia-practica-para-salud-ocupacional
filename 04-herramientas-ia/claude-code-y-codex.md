# Usar este vault con Claude Code y Codex

tags: #claude-code #codex #ia #programacion #herramientas

Esta es una guía operativa para usar **Claude Code** y **Codex** con este vault: instalación, comandos, prompts y validaciones.

Si primero necesitas entender qué son y cuándo conviene usarlos, revisa [[04-herramientas-ia/asistentes-de-codigo|Asistentes de código]].

> Regla principal: usa estos asistentes con datos sintéticos. No pegues ni subas datos reales identificables de pacientes, trabajadores, empresas o instituciones.

## Para qué sirven

| Herramienta | Mejor uso en este vault |
|---|---|
| Claude Code | Revisar estructura del vault, mejorar textos largos, explicar código, proponer actividades y editar archivos con contexto del proyecto. |
| Codex | Crear scripts, corregir errores, generar HTML, validar notebooks, ejecutar comandos y modificar el repositorio. |
| ChatGPT web o Claude web | Pensar ideas, explicar conceptos, resumir y redactar sin necesariamente editar archivos del proyecto. |

## Antes de usar Claude Code o Codex

Necesitas tener listo:

1. el repositorio descargado o clonado;
2. Python instalado;
3. Git instalado si vas a clonar o actualizar;
4. Node.js instalado si la herramienta se instala vía `npm`;
5. una cuenta activa del proveedor correspondiente;
6. revisar [[01-conceptos-clave/limites-riesgos-etica|Límites, riesgos, ética y privacidad]].

Guía base: [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]].

## Explicación rápida: qué es Python

**Python** es un lenguaje de programación muy usado para análisis de datos, automatización, inteligencia artificial y prototipos. En este vault lo usamos para tareas pequeñas:

- leer archivos CSV;
- agrupar datos;
- crear gráficos;
- generar informes base;
- probar ideas antes de construir una aplicación más completa.

No necesitas memorizar todo Python para empezar. La idea es entender el flujo:

```text
archivo de datos → código Python → resultado visible → interpretación crítica
```

Ejemplo mínimo:

```python
import pandas as pd

datos = pd.read_csv("assets/datos/ausentismo_ejemplo.csv")
print(datos.head())
```

Ese código significa:

1. cargar la librería `pandas`;
2. leer una tabla CSV;
3. mostrar las primeras filas.

Para más detalle, revisa [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]].

## Instalar Node.js

Algunas herramientas de línea de comandos se instalan con `npm`, que viene con Node.js.

1. Ve a <https://nodejs.org/>.
2. Descarga la versión LTS recomendada.
3. Instálala.
4. Abre una terminal y verifica:

```bash
node --version
npm --version
```

Si ambos comandos muestran versión, puedes instalar herramientas con `npm`.

## Instalar Claude Code

Consulta siempre la documentación oficial porque los comandos pueden cambiar:

- Documentación de Claude Code: <https://docs.anthropic.com/en/docs/claude-code/overview>
- Configuración de Claude Code: <https://docs.anthropic.com/en/docs/claude-code/setup>

Una instalación típica puede verse así:

```bash
npm install -g @anthropic-ai/claude-code
```

Luego, desde la carpeta del repositorio:

```bash
claude
```

Si el comando cambia, usa el comando actualizado de la documentación oficial.

## Instalar Codex

Consulta siempre la documentación oficial:

- OpenAI Codex: <https://openai.com/codex/>
- Repositorio de Codex CLI: <https://github.com/openai/codex>

Una instalación típica de la CLI puede verse así:

```bash
npm install -g @openai/codex
```

Luego, desde la carpeta del repositorio:

```bash
codex
```

Si el comando cambia, usa el comando actualizado del repositorio oficial.

## Abrir el vault con una herramienta de código

Primero entra a la carpeta del repositorio:

```bash
cd ia-practica-para-salud-ocupacional
```

Verifica que estás en el lugar correcto:

```bash
ls
```

En Windows PowerShell:

```powershell
dir
```

Deberías ver:

```text
README.md
assets/
scripts/
00-empezar-aqui/
```

Después inicia Claude Code o Codex desde esa carpeta.

## Primer prompt recomendado

Úsalo al abrir Claude Code o Codex dentro del repositorio:

```text
Lee README.md y 00-empezar-aqui/mapa-del-vault.md.
Este es un vault educativo de Obsidian para estudiantes de salud ocupacional.
Antes de cambiar archivos, resume la estructura del proyecto y dime qué notas son la ruta principal para estudiantes.
No uses datos reales ni propongas datos identificables.
```

## Prompt para revisar instalación

```text
Revisa 00-empezar-aqui/instalacion-y-preparacion.md y assets/notebooks/README.md.
Busca pasos confusos para estudiantes principiantes en Windows y macOS.
Propón mejoras concretas sin cambiar archivos todavía.
```

## Prompt para validar datos y scripts

```text
Ejecuta estos comandos y resume resultados:

python scripts/00_validar_datos.py
python scripts/01_analizar_ausentismo.py
python scripts/02_graficar_incidentes.py
python scripts/03_limpiar_datos.py
python scripts/04_generar_informe_base.py

Si algo falla, explica el error en lenguaje simple y propone una corrección mínima.
```

En macOS puede que el asistente deba usar `python3`:

```text
Si `python` no funciona, intenta con `python3`.
```

## Prompt para revisar notebooks

```text
Revisa los notebooks en assets/notebooks/.
Verifica que las celdas tengan comentarios claros para estudiantes principiantes.
No cambies el objetivo de cada notebook.
Si propones cambios, mantén datos sintéticos y lenguaje simple.
```

## Prompt para crear una práctica nueva

```text
Quiero agregar una práctica guiada nueva para estudiantes de salud ocupacional.
Debe usar datos sintéticos, tener objetivo, archivo de datos, pasos, código simple, preguntas de discusión y sección Relacionado con wikilinks.
Propón primero el diseño de la práctica antes de crear archivos.
```

## Prompt para crear un proyecto completo

```text
Quiero crear un mini proyecto para este vault.
Primero propón: objetivo, audiencia, datos sintéticos necesarios, archivos que crearías, pasos para estudiantes, validaciones y riesgos de privacidad.
No escribas código todavía. Espera mi aprobación del plan.
```

Después de aprobar el plan:

```text
Implementa el proyecto aprobado con cambios pequeños.
Usa datos sintéticos, comentarios para principiantes y enlaces Obsidian en la sección Relacionado.
Al final ejecuta validaciones y resume qué cambió.
```

Más ideas: [[06-recursos/ideas-proyectos|Ideas de ampliación y proyectos]].

## Prompt para mejorar un archivo HTML

```text
Revisa assets/checklist_interactivo.html.
Quiero que siga siendo un solo archivo HTML, fácil de abrir con doble clic.
Mejora comentarios y accesibilidad básica, pero no agregues frameworks ni dependencias externas.
```

## Prompt para cuidar privacidad

```text
Revisa el texto y los ejemplos que voy a compartir.
Busca cualquier dato que parezca identificable o que pueda interpretarse como recomendación clínica, legal u ocupacional definitiva.
Devuelve una lista de riesgos y una versión más segura.
```

## Prompt para actualizar links de Obsidian

```text
Revisa los wikilinks del vault.
Verifica que cada enlace interno de Obsidian apunte a una nota existente.
Si encuentras enlaces rotos, corrígelos con el menor cambio posible.
```

## Qué pedir y qué no pedir

### Sí pedir

- Explicar código en lenguaje simple.
- Crear ejemplos pequeños.
- Validar rutas y archivos.
- Mejorar instrucciones para estudiantes.
- Revisar privacidad y seguridad.
- Proponer actividades prácticas.

### No pedir

- Analizar datos reales identificables.
- Tomar decisiones clínicas u ocupacionales individuales.
- Crear recomendaciones definitivas sin revisión profesional.
- Subir información privada a servicios externos.
- Cambiar muchos archivos sin explicar el plan.

## Flujo de trabajo recomendado

```text
1. Pedir lectura del contexto
2. Pedir plan breve
3. Aprobar o corregir el plan
4. Pedir cambios pequeños
5. Ejecutar validaciones
6. Revisar resultados
7. Guardar cambios en Git si corresponde
```

## Validaciones útiles

Para datos y scripts:

```bash
python scripts/00_validar_datos.py
python scripts/01_analizar_ausentismo.py
python scripts/02_graficar_incidentes.py
python scripts/03_limpiar_datos.py
python scripts/04_generar_informe_base.py
```

Para revisar cambios Git:

```bash
git status
git diff
```

Para actualizar el repositorio:

```bash
git pull
```

## Si una herramienta pide permisos

Claude Code y Codex pueden pedir permiso para:

- leer archivos;
- editar archivos;
- ejecutar comandos;
- instalar paquetes;
- usar red;
- hacer commits.

Antes de aceptar, revisa si la acción tiene sentido. No aceptes comandos que no entiendas si afectan archivos reales, credenciales o datos sensibles.

## Ideas de ampliación

Puedes usar Claude Code o Codex para construir proyectos graduales como:

- tablero de ausentismo sintético;
- clasificador de incidentes;
- checklist interactivo por tema;
- informe ejecutivo asistido por IA;
- presentación web interactiva;
- glosario con tarjetas de estudio.

La guía completa está en [[06-recursos/ideas-proyectos|Ideas de ampliación y proyectos]].

## Recomendación docente

Para una clase, muestra primero el flujo con datos sintéticos:

1. abrir el vault;
2. pedir al asistente que lea `README.md`;
3. ejecutar `scripts/00_validar_datos.py`;
4. pedir explicación del resultado;
5. ejecutar un notebook;
6. pedir a la IA que explique una celda.

Así las personas ven que la IA ayuda a aprender, pero no reemplaza el criterio profesional.

## Relacionado

- [[04-herramientas-ia/claude|Claude]]
- [[04-herramientas-ia/codex|Codex]]
- [[06-recursos/prompts|Banco de prompts]]
- [[06-recursos/ideas-proyectos|Ideas de ampliación y proyectos]]
- [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]]
- [[06-recursos/enlaces-oficiales|Enlaces oficiales]]
- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
