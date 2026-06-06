# Instalación y preparación

tags: #instalacion #python #obsidian #git #notebooks #preparacion

Esta guía te ayuda a preparar el computador para usar el vault, abrir las notas, ejecutar scripts de Python, abrir notebooks y probar la página interactiva.

> Si estás en una clase de una hora, no te preocupes si no alcanzas a instalar todo. Puedes seguir el material desde GitHub u Obsidian y revisar los resultados ya generados.

## Qué vas a instalar

| Herramienta | Para qué sirve | Enlace oficial |
|---|---|---|
| Obsidian | Abrir este repositorio como vault y navegar con enlaces internos. | <https://obsidian.md/download> |
| Python | Ejecutar ejemplos de análisis de datos. | <https://www.python.org/downloads/> |
| Git | Clonar el repositorio y actualizarlo. | <https://git-scm.com/downloads> |
| VS Code | Abrir scripts y notebooks con una interfaz visual. | <https://code.visualstudio.com/Download> |
| Jupyter | Ejecutar notebooks `.ipynb`. | <https://jupyter.org/install> |
| pandas y matplotlib | Leer tablas CSV y crear gráficos. | <https://pandas.pydata.org/docs/>, <https://matplotlib.org/stable/users/index.html> |

Más referencias en [[06-recursos/enlaces-oficiales|Enlaces oficiales]].

## Paso 1: descargar el repositorio

### Opción rápida: descargar ZIP

1. Abre el repositorio en GitHub: <https://github.com/ingfcetina/ia-practica-para-salud-ocupacional>.
2. Presiona **Code**.
3. Elige **Download ZIP**.
4. Descomprime el archivo en una carpeta fácil de encontrar.

Ejemplo:

```text
Documentos/ia-practica-para-salud-ocupacional
```

### Opción con Git: clonar

Primero instala Git desde <https://git-scm.com/downloads>. Luego ejecuta:

```bash
git clone https://github.com/ingfcetina/ia-practica-para-salud-ocupacional.git
cd ia-practica-para-salud-ocupacional
```

Para aprender más sobre clonar repositorios, consulta la documentación de GitHub: <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>.

## Paso 2: instalar y abrir Obsidian

1. Descarga Obsidian desde <https://obsidian.md/download>.
2. Instálalo y ábrelo.
3. Selecciona **Open folder as vault** o **Abrir carpeta como vault**.
4. Elige la carpeta del repositorio.
5. Abre [[00-empezar-aqui/mapa-del-vault|Mapa del vault]].

Documentación oficial de Obsidian: <https://help.obsidian.md/>.

## Paso 3: instalar Python

### Windows

1. Ve a <https://www.python.org/downloads/>.
2. Descarga la versión estable más reciente de Python.
3. Durante la instalación, marca **Add Python to PATH**.
4. Finaliza la instalación.
5. Abre PowerShell o Terminal.
6. Verifica:

```bash
python --version
```

Si Windows abre Microsoft Store en lugar de mostrar la versión, instala Python desde `python.org` y revisa los alias de ejecución de aplicaciones en la configuración de Windows.

### macOS

1. Descarga Python desde <https://www.python.org/downloads/>.
2. Instálalo.
3. Abre Terminal.
4. Verifica:

```bash
python3 --version
```

En macOS puede que debas usar `python3` en lugar de `python`.

### Linux

En muchas distribuciones Python ya viene instalado. Verifica:

```bash
python3 --version
```

Si no está instalado, usa el gestor de paquetes de tu distribución.

## Paso 4: abrir terminal en la carpeta del vault

La terminal debe estar ubicada donde están `README.md`, `assets/`, `scripts/` y `requirements.txt`.

En Windows:

1. Abre la carpeta en el Explorador.
2. Haz clic derecho dentro de la carpeta.
3. Elige **Abrir en Terminal**.

Verifica que estás en la carpeta correcta:

```bash
dir
```

En macOS/Linux:

```bash
ls
```

Debes ver algo parecido a:

```text
README.md
assets/
scripts/
requirements.txt
```

## Paso 5: instalar librerías para scripts

Ejecuta:

```bash
pip install -r requirements.txt
```

Si tu sistema usa `python3`:

```bash
python3 -m pip install -r requirements.txt
```

Documentación oficial sobre instalación de paquetes: <https://packaging.python.org/en/latest/tutorials/installing-packages/>.

## Paso 6: instalar soporte para notebooks

Los notebooks están en:

```text
assets/notebooks/
```

Para abrirlos en VS Code:

1. Instala VS Code: <https://code.visualstudio.com/Download>.
2. Instala la extensión Python: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>.
3. Instala la extensión Jupyter: <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>.
4. Abre la carpeta del repositorio.
5. Abre cualquier archivo `.ipynb` de `assets/notebooks/`.

Para abrirlos con JupyterLab:

```bash
pip install -r requirements-notebooks.txt
jupyter lab
```

Luego entra a la carpeta `assets/notebooks/` desde el navegador.

Más detalles: [[assets/notebooks/README|Notebooks de ejemplo]].

## Paso 7: validar los datos

Ejecuta:

```bash
python scripts/00_validar_datos.py
```

En macOS o Linux puede ser:

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

## Paso 8: ejecutar los scripts

```bash
python scripts/01_analizar_ausentismo.py
python scripts/02_graficar_incidentes.py
python scripts/03_limpiar_datos.py
python scripts/04_generar_informe_base.py
```

Los resultados se guardan en:

- `assets/imagenes/ausentismo_por_area.png`
- `assets/imagenes/incidentes_por_tipo.png`
- `outputs/ausentismo_limpio.csv`
- `outputs/informe_base.md`

## Paso 9: abrir la página interactiva

Abre este archivo con doble clic:

```text
assets/checklist_interactivo.html
```

No necesita internet ni servidor. Se abre en el navegador.

## Paso 10: actualizar el repositorio con Git

Si descargaste ZIP, vuelve a descargar el ZIP cuando haya una nueva versión.

Si clonaste con Git, puedes actualizar con:

```bash
git pull
```

## Si algo no funciona

| Problema | Qué intentar |
|---|---|
| `python` no se reconoce | Prueba `python3 --version` o reinstala Python marcando **Add Python to PATH**. |
| `pip` no se reconoce | Prueba `python -m pip install -r requirements.txt`. |
| Falta `pandas` o `matplotlib` | Ejecuta de nuevo `pip install -r requirements.txt`. |
| No abre un notebook | Instala VS Code + extensiones Python/Jupyter o instala `requirements-notebooks.txt`. |
| El gráfico no aparece | Revisa `assets/imagenes/`; los scripts guardan imágenes ahí. |
| El vault no abre en Obsidian | Asegúrate de abrir la carpeta completa, no un archivo suelto. |
| `git` no se reconoce | Instala Git desde <https://git-scm.com/downloads>. |

## Regla de privacidad

No uses datos reales identificables para practicar. Usa los archivos sintéticos de [[06-recursos/datasets-ejemplo|Datasets de ejemplo]].

## Relacionado

- [[00-empezar-aqui/ruta-de-aprendizaje|Ruta de aprendizaje]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[assets/notebooks/README|Notebooks de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]
- [[06-recursos/enlaces-oficiales|Enlaces oficiales]]
