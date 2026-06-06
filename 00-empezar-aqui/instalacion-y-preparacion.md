# Instalación y preparación, paso a paso

tags: #instalacion #python #obsidian #git #notebooks #preparacion

Esta guía está escrita para personas que **no han usado consola, PowerShell, Terminal ni programación**. La meta es que puedas abrir el vault, leer las notas, probar ejemplos y, si quieres, ejecutar Python.

> Si estás en una clase corta, no intentes instalar todo en vivo. Puedes leer el vault en GitHub u Obsidian y volver a esta guía después.

## Qué necesitas realmente

Hay tres niveles. Empieza por el primero.

| Nivel | Qué puedes hacer | Qué necesitas instalar |
|---|---|---|
| 1. Leer el material | Leer notas, datos y ejemplos. | Nada, solo navegador. |
| 2. Abrir como vault | Navegar con enlaces internos y grafo de Obsidian. | Obsidian. |
| 3. Ejecutar ejemplos | Correr Python, notebooks y generar gráficos. | Python, librerías y opcionalmente VS Code/Jupyter. |

## Nivel 1: usar el material sin instalar nada

1. Abre el repositorio en el navegador:

   <https://github.com/ingfcetina/ia-practica-para-salud-ocupacional>

2. Haz clic en `README.md` si no se abre automáticamente.
3. Lee la sección **Si eres estudiante**.
4. Abre las carpetas como si fueran carpetas normales.
5. Para ver datos, entra a:

```text
assets/datos/
```

6. Para ver notebooks, entra a:

```text
assets/notebooks/
```

GitHub permite leer notebooks, pero no ejecutarlos.

## Nivel 2: descargar el vault y abrirlo en Obsidian

### Paso 1: descargar el ZIP

Esta es la opción más simple.

1. Abre el repositorio:

   <https://github.com/ingfcetina/ia-practica-para-salud-ocupacional>

2. Busca el botón verde **Code**.
3. Haz clic en **Code**.
4. Haz clic en **Download ZIP**.
5. Espera a que descargue.
6. Busca el archivo descargado. Normalmente estará en `Descargas`.
7. Haz clic derecho sobre el ZIP.
8. Elige **Extraer todo** o **Extract all**.
9. Elige una ubicación fácil, por ejemplo:

```text
Documentos/ia-practica-para-salud-ocupacional
```

10. Abre la carpeta extraída. Debes ver archivos como:

```text
README.md
00-empezar-aqui
assets
scripts
```

### Paso 2: instalar Obsidian

1. Abre esta página:

   <https://obsidian.md/download>

2. Descarga Obsidian para tu sistema operativo.
3. Instálalo como cualquier programa normal.
4. Abre Obsidian.
5. Si pregunta qué hacer, elige **Open folder as vault** o **Abrir carpeta como vault**.
6. Selecciona la carpeta que descomprimiste.
7. Dentro de Obsidian, abre:

```text
00-empezar-aqui/mapa-del-vault.md
```

Si ves las notas con enlaces, ya está listo el vault.

## Nivel 3: ejecutar ejemplos con Python

Python sirve para leer los CSV, crear gráficos y generar informes. Si solo quieres leer el material, puedes saltar esta parte.

## Instalar Python en Windows, sin asumir consola

### Paso 1: descargar Python

1. Abre:

   <https://www.python.org/downloads/>

2. Haz clic en el botón grande que dice **Download Python**.
3. Espera la descarga.
4. Abre el instalador.

### Paso 2: instalar Python

En la primera pantalla del instalador:

1. Marca la casilla **Add python.exe to PATH** o **Add Python to PATH**.
2. Luego haz clic en **Install Now**.
3. Espera a que termine.
4. Cierra el instalador.

> La casilla **Add Python to PATH** es importante. Permite que Windows encuentre Python cuando ejecutes comandos.

### Paso 3: abrir una ventana de comandos en la carpeta correcta

No necesitas saber PowerShell de antemano. Haz esto:

1. Abre la carpeta del repositorio en el Explorador de archivos.
2. Verifica que dentro ves `README.md`, `assets` y `scripts`.
3. Haz clic en la barra superior donde aparece la ruta de la carpeta.
4. Escribe:

```text
cmd
```

5. Presiona **Enter**.

Se abrirá una ventana negra en esa misma carpeta. Esa ventana es la consola.

### Paso 4: verificar Python

Copia este comando, pégalo en la ventana negra y presiona **Enter**:

```bash
python --version
```

Si funciona, verás algo parecido a:

```text
Python 3.13.2
```

Si no funciona, prueba:

```bash
py --version
```

Si `py` funciona, usa `py` en lugar de `python` para los comandos.

## Instalar Python en macOS, paso a paso

### Paso 1: descargar Python

1. Abre:

   <https://www.python.org/downloads/>

2. Descarga Python para macOS.
3. Abre el instalador `.pkg`.
4. Sigue los pasos del instalador.

### Paso 2: abrir Terminal en la carpeta

1. Abre la carpeta del repositorio en Finder.
2. Abre la aplicación **Terminal**.
3. Escribe `cd ` con un espacio al final.
4. Arrastra la carpeta del repositorio desde Finder hasta la ventana de Terminal.
5. Presiona **Enter**.

Eso ubica la Terminal dentro de la carpeta del proyecto.

### Paso 3: verificar Python

Copia y ejecuta:

```bash
python3 --version
```

Si ves una versión de Python, está listo.

## Nota sobre otros sistemas

Esta guía se enfoca en **Windows y macOS**, porque son los sistemas más probables para el grupo. Si usas otro sistema operativo, pide apoyo específico al docente o usa la documentación oficial de Python: <https://www.python.org/downloads/>.

## Instalar las librerías del proyecto

Python solo no basta. También necesitas librerías para datos y gráficos.

En la ventana de comandos o Terminal, dentro de la carpeta del proyecto, ejecuta:

### Windows

```bash
python -m pip install -r requirements.txt
```

Si `python` no funcionó pero `py` sí:

```bash
py -m pip install -r requirements.txt
```

### macOS

```bash
python3 -m pip install -r requirements.txt
```

Este comando instala:

- `pandas`, para trabajar con tablas;
- `matplotlib`, para crear gráficos.

## Validar que todo quedó bien

Ejecuta este comando.

### Windows

```bash
python scripts/00_validar_datos.py
```

O, si usas `py`:

```bash
py scripts/00_validar_datos.py
```

### macOS

```bash
python3 scripts/00_validar_datos.py
```

Resultado esperado:

```text
OK ausentismo_ejemplo.csv: 20 filas
OK incidentes_ejemplo.csv: 12 filas
OK checklist_inspeccion_ejemplo.csv: 7 filas
OK indicadores_dashboard_ejemplo.csv: 12 filas
OK checklist_interactivo.html
```

Si ves esos mensajes, la validación funcionó.

## Ejecutar los ejemplos de Python

### Windows

```bash
python scripts/01_analizar_ausentismo.py
python scripts/02_graficar_incidentes.py
python scripts/03_limpiar_datos.py
python scripts/04_generar_informe_base.py
```

Si usas `py`:

```bash
py scripts/01_analizar_ausentismo.py
py scripts/02_graficar_incidentes.py
py scripts/03_limpiar_datos.py
py scripts/04_generar_informe_base.py
```

### macOS

```bash
python3 scripts/01_analizar_ausentismo.py
python3 scripts/02_graficar_incidentes.py
python3 scripts/03_limpiar_datos.py
python3 scripts/04_generar_informe_base.py
```

Los resultados aparecen en:

```text
assets/imagenes/ausentismo_por_area.png
assets/imagenes/incidentes_por_tipo.png
outputs/ausentismo_limpio.csv
outputs/informe_base.md
```

## Abrir notebooks sin complicarse

La opción más fácil para notebooks es **VS Code**.

### Instalar VS Code

1. Abre:

   <https://code.visualstudio.com/Download>

2. Descarga e instala VS Code.
3. Abre VS Code.
4. Instala estas extensiones:
   - Python: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>
   - Jupyter: <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>

### Abrir la carpeta en VS Code

1. En VS Code, haz clic en **File**.
2. Haz clic en **Open Folder**.
3. Selecciona la carpeta del repositorio.
4. En el panel izquierdo, entra a:

```text
assets/notebooks/
```

5. Abre `01_analizar_ausentismo.ipynb`.
6. Si VS Code pregunta por un **Kernel**, elige Python.
7. Ejecuta las celdas con el botón ▶.

## Opción avanzada: abrir notebooks con JupyterLab

Solo usa esta opción si quieres aprender Jupyter directamente.

Instala soporte para notebooks:

### Windows

```bash
python -m pip install -r requirements-notebooks.txt
```

### macOS

```bash
python3 -m pip install -r requirements-notebooks.txt
```

Luego abre JupyterLab:

### Windows

```bash
python -m jupyter lab
```

### macOS

```bash
python3 -m jupyter lab
```

Se abrirá una página en el navegador. Entra a:

```text
assets/notebooks/
```

## Abrir la página interactiva

No necesitas instalar nada.

1. Abre la carpeta del repositorio.
2. Entra a `assets`.
3. Haz doble clic en:

```text
checklist_interactivo.html
```

Se abrirá en el navegador.

## Actualizar el repositorio

Si descargaste ZIP, la forma más simple es volver a descargar el ZIP.

Si alguien te enseñó a usar Git y clonaste el repositorio, abre la consola en la carpeta y ejecuta:

```bash
git pull
```

## Si algo no funciona

| Problema | Qué hacer |
|---|---|
| No sé si estoy en la carpeta correcta | Debes ver `README.md`, `assets` y `scripts`. |
| `python` no funciona en Windows | Prueba `py --version`. |
| `python3` no funciona en macOS | Reinstala Python desde `python.org` y vuelve a abrir Terminal. |
| Sale `No module named pandas` | Ejecuta el comando de instalación de librerías otra vez. |
| No encuentro el notebook | Está en `assets/notebooks/`. |
| VS Code pide Kernel | Elige Python. Si no aparece, instala Python y reinicia VS Code. |
| El gráfico no aparece | Revisa la carpeta `assets/imagenes/`. |
| Tengo miedo de dañar algo | Haz una copia de la carpeta antes de modificar archivos. |

## Prompt para pedir ayuda a una IA

```text
Estoy siguiendo una guía para instalar Python y abrir notebooks.
No tengo experiencia con consola.
Estoy en [Windows/macOS].
Este es el paso donde estoy: [describe el paso].
Este es el error o pantalla que veo: [pega el texto].
Explícame qué hacer con instrucciones paso a paso, sin asumir que sé usar terminal.
```

## Regla de privacidad

No uses datos reales identificables para practicar. Usa los archivos sintéticos de [[06-recursos/datasets-ejemplo|Datasets de ejemplo]].

## Relacionado

- [[00-empezar-aqui/ruta-de-aprendizaje|Ruta de aprendizaje]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[assets/notebooks/README|Notebooks de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]
- [[06-recursos/enlaces-oficiales|Enlaces oficiales]]
