# Notebooks de ejemplo

Estos notebooks permiten recorrer los ejemplos paso a paso con celdas de explicación y código comentado.

## Qué es un notebook

Un notebook de Jupyter es un archivo `.ipynb` que combina:

- texto explicativo;
- código Python;
- resultados;
- tablas;
- gráficos.

Es ideal para aprender porque puedes ejecutar una celda a la vez y ver qué pasa.

Para una explicación más completa, revisa [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]].

## Notebooks incluidos

| Notebook | Qué practica | Datos usados |
|---|---|---|
| `01_analizar_ausentismo.ipynb` | Leer ausentismo, agrupar por área y graficar. | `assets/datos/ausentismo_ejemplo.csv` |
| `02_graficar_incidentes.ipynb` | Contar incidentes por tipo y revisar severidad. | `assets/datos/incidentes_ejemplo.csv` |
| `03_checklist_y_dashboard.ipynb` | Calcular cumplimiento y graficar indicadores. | `assets/datos/checklist_inspeccion_ejemplo.csv`, `assets/datos/indicadores_dashboard_ejemplo.csv` |
| `04_generar_informe_base.ipynb` | Crear un borrador de informe con indicadores agregados. | `assets/datos/ausentismo_ejemplo.csv`, `assets/datos/incidentes_ejemplo.csv` |

## Cómo abrirlos desde Python con JupyterLab

1. Abre una terminal en la carpeta raíz del repositorio.
2. Instala dependencias:

```bash
pip install -r requirements-notebooks.txt
```

3. Ejecuta:

```bash
jupyter lab
```

4. Se abrirá Jupyter en el navegador.
5. Entra a:

```text
assets/notebooks/
```

6. Abre un notebook.
7. Ejecuta las celdas en orden con el botón ▶.

En macOS o Linux puede que necesites usar:

```bash
python3 -m pip install -r requirements-notebooks.txt
python3 -m jupyter lab
```

## Cómo abrirlos en Visual Studio Code

1. Instala VS Code: <https://code.visualstudio.com/Download>.
2. Instala la extensión oficial de Python: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>.
3. Instala la extensión oficial de Jupyter: <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>.
4. Abre la carpeta completa del repositorio en VS Code.
5. Abre un archivo `.ipynb` de `assets/notebooks/`.
6. Si VS Code lo pide, selecciona el kernel de Python.
7. Ejecuta las celdas en orden.

## Cómo verlos en GitHub

GitHub permite abrir los `.ipynb` para leerlos, pero no ejecutarlos. Para ejecutar celdas necesitas JupyterLab o VS Code.

## Importante

- Ejecuta los notebooks desde la carpeta raíz del repositorio para que las rutas funcionen.
- No uses datos reales identificables.
- Si una celda falla, lee el mensaje de error y revisa [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]].

## Relacionado

- [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]]
- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]
