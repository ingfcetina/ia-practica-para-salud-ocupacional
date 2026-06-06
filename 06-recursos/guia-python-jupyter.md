# Guía de Python y Jupyter Notebooks

tags: #python #jupyter #notebooks #instalacion

Esta guía explica qué es Jupyter Notebook, cómo abrir notebooks desde Python y cómo instalar Python en Windows, macOS y Linux.

## Qué es Jupyter Notebook

Un **Jupyter Notebook** es un archivo interactivo con extensión `.ipynb`. Combina:

- texto explicativo;
- código Python;
- resultados de código;
- tablas;
- gráficos;
- comentarios paso a paso.

Es útil para aprender porque no tienes que ejecutar todo un programa completo. Puedes ejecutar una celda, mirar el resultado, cambiar algo y volver a probar.

## Diferencia entre script y notebook

| Formato | Archivo | Uso recomendado |
|---|---|---|
| Script Python | `.py` | Automatizar una tarea de principio a fin. |
| Notebook Jupyter | `.ipynb` | Aprender, explorar datos, explicar pasos y mostrar resultados. |

En este vault tienes ambos:

- scripts en `scripts/`;
- notebooks en `assets/notebooks/`.

## Qué significa ejecutar una celda

Un notebook está dividido en **celdas**.

Hay dos tipos principales:

| Tipo de celda | Qué contiene |
|---|---|
| Markdown | Texto, títulos, listas y explicaciones. |
| Code | Código Python que puedes ejecutar. |

Cuando ejecutas una celda de código, Python procesa esas instrucciones y muestra el resultado debajo.

## Instalar Python en Windows

1. Abre <https://www.python.org/downloads/>.
2. Descarga la versión estable recomendada.
3. Ejecuta el instalador.
4. Muy importante: marca **Add Python to PATH**.
5. Presiona **Install Now**.
6. Abre PowerShell o Terminal.
7. Verifica:

```bash
python --version
```

Si funciona, verás algo como:

```text
Python 3.13.2
```

### Si Windows abre Microsoft Store

A veces Windows tiene un alias que abre Microsoft Store en lugar de Python.

Prueba:

```bash
py --version
```

Si eso funciona, puedes usar:

```bash
py -m pip install -r requirements.txt
py scripts/00_validar_datos.py
```

También puedes revisar los alias en:

```text
Configuración → Aplicaciones → Configuración avanzada de aplicaciones → Alias de ejecución de aplicaciones
```

## Instalar Python en macOS

1. Abre <https://www.python.org/downloads/>.
2. Descarga Python para macOS.
3. Instálalo.
4. Abre Terminal.
5. Verifica:

```bash
python3 --version
```

En macOS normalmente se usa `python3`, no `python`.

Para instalar librerías:

```bash
python3 -m pip install -r requirements.txt
```

Para ejecutar scripts:

```bash
python3 scripts/00_validar_datos.py
```

## Instalar Python en Linux

En muchas distribuciones Python ya está instalado.

Verifica:

```bash
python3 --version
```

Si no aparece, instala Python con el gestor de paquetes de tu distribución.

Ejemplo en Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Luego instala librerías:

```bash
python3 -m pip install -r requirements.txt
```

## Instalar Jupyter

Para usar notebooks necesitas instalar dependencias adicionales.

Desde la carpeta del repositorio ejecuta:

```bash
pip install -r requirements-notebooks.txt
```

En macOS/Linux puede ser:

```bash
python3 -m pip install -r requirements-notebooks.txt
```

Este archivo instala:

- pandas;
- matplotlib;
- JupyterLab;
- Notebook;
- ipykernel.

## Abrir notebooks desde Python con JupyterLab

1. Abre una terminal en la carpeta raíz del repositorio.
2. Instala dependencias:

```bash
pip install -r requirements-notebooks.txt
```

3. Ejecuta:

```bash
jupyter lab
```

4. Se abrirá una pestaña del navegador.
5. En el explorador de archivos de Jupyter, entra a:

```text
assets/notebooks/
```

6. Abre un notebook, por ejemplo:

```text
01_analizar_ausentismo.ipynb
```

7. Ejecuta las celdas en orden.

## Abrir notebooks desde VS Code

Esta es una opción cómoda para estudiantes.

1. Instala VS Code: <https://code.visualstudio.com/Download>.
2. Instala la extensión oficial de Python: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>.
3. Instala la extensión oficial de Jupyter: <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>.
4. Abre VS Code.
5. Selecciona **File → Open Folder**.
6. Abre la carpeta del repositorio.
7. Entra a `assets/notebooks/`.
8. Abre un archivo `.ipynb`.
9. Presiona **Select Kernel** si VS Code lo solicita.
10. Elige el Python instalado.
11. Ejecuta las celdas con el botón ▶.

## Abrir notebooks en GitHub

GitHub permite ver notebooks directamente en el navegador, pero normalmente no permite ejecutarlos.

Sirve para:

- leer el contenido;
- revisar el código;
- ver la estructura del ejercicio.

No sirve para:

- modificar y ejecutar celdas interactivamente;
- generar nuevos resultados locales.

Para ejecutar, usa JupyterLab o VS Code.

## Orden recomendado de notebooks

1. `assets/notebooks/01_analizar_ausentismo.ipynb`
2. `assets/notebooks/02_graficar_incidentes.ipynb`
3. `assets/notebooks/03_checklist_y_dashboard.ipynb`
4. `assets/notebooks/04_generar_informe_base.ipynb`

## Qué hacer si una celda falla

| Mensaje o problema | Posible solución |
|---|---|
| `ModuleNotFoundError: No module named 'pandas'` | Ejecuta `pip install -r requirements-notebooks.txt`. |
| `jupyter: command not found` | Instala Jupyter con `pip install -r requirements-notebooks.txt`. |
| No encuentra el CSV | Abre Jupyter desde la carpeta raíz del repositorio. |
| VS Code pide kernel | Selecciona el Python donde instalaste las librerías. |
| El gráfico no aparece | Ejecuta todas las celdas anteriores en orden. |

## Regla de privacidad

Nunca cargues datos reales identificables en notebooks compartidos o herramientas públicas. Usa los datos sintéticos de [[06-recursos/datasets-ejemplo|Datasets de ejemplo]].

## Enlaces oficiales

- Python: <https://www.python.org/downloads/>
- Jupyter: <https://jupyter.org/install>
- VS Code: <https://code.visualstudio.com/Download>
- Extensión Python para VS Code: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>
- Extensión Jupyter para VS Code: <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>
- Instalación de paquetes Python: <https://packaging.python.org/en/latest/tutorials/installing-packages/>

## Relacionado

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[assets/notebooks/README|Notebooks de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
