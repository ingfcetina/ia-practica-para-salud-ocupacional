# Guía de Python y Jupyter Notebooks

tags: #python #jupyter #notebooks #instalacion

Esta guía explica, con lenguaje simple, qué es Python, qué es Jupyter Notebook y cómo usarlos sin asumir experiencia previa con programación o consola.

## Qué es Python

Python es un lenguaje para darle instrucciones al computador.

En este vault lo usamos para tareas pequeñas:

- leer una tabla CSV;
- contar registros;
- crear gráficos;
- generar un informe base.

Ejemplo:

```python
print("Hola")
```

Ese código le dice a Python que muestre la palabra `Hola`.

## Qué es Jupyter Notebook

Un **Jupyter Notebook** es un archivo interactivo con extensión `.ipynb`.

Combina:

- explicación escrita;
- código Python;
- resultados;
- tablas;
- gráficos.

Es útil para aprender porque puedes ejecutar una parte pequeña, mirar el resultado y continuar.

## Script o notebook: cuál usar

| Si quieres... | Usa... |
|---|---|
| Aprender paso a paso | Notebook `.ipynb` |
| Ejecutar una tarea completa | Script `.py` |
| Ver explicación y resultado juntos | Notebook |
| Automatizar un proceso | Script |

## Qué es una celda

Un notebook tiene bloques llamados **celdas**.

| Tipo de celda | Qué hace |
|---|---|
| Texto / Markdown | Explica el paso. |
| Código / Code | Ejecuta Python. |

Para ejecutar una celda, normalmente presionas el botón ▶ que aparece junto a ella.

## La forma más fácil: usar VS Code

Para principiantes, recomiendo abrir notebooks con **Visual Studio Code** porque permite ver carpetas, archivos y notebooks en una sola ventana.

### Paso 1: instalar Python

Sigue la guía principal:

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]

### Paso 2: instalar VS Code

1. Abre <https://code.visualstudio.com/Download>.
2. Descarga VS Code para tu sistema.
3. Instálalo.
4. Ábrelo.

### Paso 3: instalar extensiones

En VS Code:

1. Busca el ícono de extensiones. Parece unos cuadritos en la barra izquierda.
2. Busca `Python`.
3. Instala la extensión oficial de Microsoft.
4. Busca `Jupyter`.
5. Instala la extensión oficial de Microsoft.

Links oficiales:

- Python para VS Code: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>
- Jupyter para VS Code: <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>

### Paso 4: abrir la carpeta del repositorio

1. En VS Code, haz clic en **File**.
2. Haz clic en **Open Folder**.
3. Selecciona la carpeta del repositorio.
4. Debes ver carpetas como:

```text
00-empezar-aqui
assets
scripts
```

### Paso 5: abrir un notebook

1. En el panel izquierdo, abre:

```text
assets/notebooks/
```

2. Haz clic en:

```text
01_analizar_ausentismo.ipynb
```

3. Si VS Code pregunta por un **Kernel**, elige Python.
4. Ejecuta la primera celda con ▶.
5. Sigue celda por celda.

## Instalar JupyterLab, paso a paso

JupyterLab abre notebooks en el navegador. Es muy útil, pero requiere ejecutar algunos comandos.

### Paso 1: abrir la consola en la carpeta correcta

#### Windows

1. Abre la carpeta del repositorio en el Explorador.
2. Verifica que ves `README.md`, `assets` y `scripts`.
3. Haz clic en la barra de dirección de la carpeta.
4. Escribe:

```text
cmd
```

5. Presiona **Enter**.

Se abrirá una ventana negra en esa carpeta.

#### macOS

1. Abre Terminal.
2. Escribe `cd ` con un espacio.
3. Arrastra la carpeta del repositorio a la Terminal.
4. Presiona **Enter**.

#### Linux

1. Abre la carpeta del repositorio.
2. Haz clic derecho.
3. Elige **Abrir en Terminal**, si tu entorno lo permite.

### Paso 2: instalar Jupyter

#### Windows

Copia y pega:

```bash
python -m pip install -r requirements-notebooks.txt
```

Si no funciona, prueba:

```bash
py -m pip install -r requirements-notebooks.txt
```

#### macOS / Linux

Copia y pega:

```bash
python3 -m pip install -r requirements-notebooks.txt
```

### Paso 3: abrir JupyterLab

#### Windows

```bash
python -m jupyter lab
```

Si usas `py`:

```bash
py -m jupyter lab
```

#### macOS / Linux

```bash
python3 -m jupyter lab
```

Se abrirá una pestaña del navegador.

### Paso 4: abrir un notebook

Dentro de JupyterLab:

1. Busca la carpeta `assets`.
2. Abre `notebooks`.
3. Abre `01_analizar_ausentismo.ipynb`.
4. Ejecuta la primera celda.
5. Sigue en orden.

## Ver notebooks en GitHub

Puedes abrir notebooks desde GitHub para leerlos, pero no para ejecutarlos.

Sirve para:

- ver el contenido;
- leer explicaciones;
- revisar código.

No sirve para:

- ejecutar celdas;
- crear nuevos gráficos;
- modificar resultados.

## Orden recomendado

1. `assets/notebooks/01_analizar_ausentismo.ipynb`
2. `assets/notebooks/02_graficar_incidentes.ipynb`
3. `assets/notebooks/03_checklist_y_dashboard.ipynb`
4. `assets/notebooks/04_generar_informe_base.ipynb`

## Errores frecuentes

| Lo que ves | Qué significa | Qué hacer |
|---|---|---|
| `No module named pandas` | Falta instalar librerías. | Ejecuta instalación de `requirements-notebooks.txt`. |
| `jupyter no se reconoce` | Jupyter no está instalado o no está en la ruta. | Usa `python -m jupyter lab` o reinstala. |
| No encuentra el CSV | Abriste Jupyter desde otra carpeta. | Cierra Jupyter y ábrelo desde la carpeta del repositorio. |
| VS Code pide Kernel | Necesita saber qué Python usar. | Elige Python en la lista. |
| No aparece Python como Kernel | VS Code no detecta Python. | Reinicia VS Code después de instalar Python. |

## Prompt para pedir ayuda

```text
Estoy intentando abrir un notebook Jupyter de este repositorio.
No tengo experiencia con programación.
Uso [Windows/macOS/Linux].
Estoy usando [VS Code/JupyterLab/GitHub].
Esto es lo que veo: [pega error o describe pantalla].
Dame pasos muy concretos para resolverlo.
```

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
