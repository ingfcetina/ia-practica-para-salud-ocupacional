# Notebooks de ejemplo

Estos notebooks permiten recorrer los ejemplos paso a paso con celdas de explicación y código comentado.

## Qué es un notebook

Un notebook combina texto, código y resultados en un mismo archivo. Es útil para aprender porque puedes ejecutar una celda a la vez y ver qué ocurre.

## Notebooks incluidos

| Notebook | Qué practica | Datos usados |
|---|---|---|
| `01_analizar_ausentismo.ipynb` | Leer ausentismo, agrupar por área y graficar. | `assets/datos/ausentismo_ejemplo.csv` |
| `02_graficar_incidentes.ipynb` | Contar incidentes por tipo y revisar severidad. | `assets/datos/incidentes_ejemplo.csv` |
| `03_checklist_y_dashboard.ipynb` | Calcular cumplimiento y graficar indicadores. | `assets/datos/checklist_inspeccion_ejemplo.csv`, `assets/datos/indicadores_dashboard_ejemplo.csv` |
| `04_generar_informe_base.ipynb` | Crear un borrador de informe con indicadores agregados. | `assets/datos/ausentismo_ejemplo.csv`, `assets/datos/incidentes_ejemplo.csv` |

## Cómo abrirlos

### Opción A: Visual Studio Code

1. Instala VS Code: <https://code.visualstudio.com/Download>.
2. Instala la extensión oficial de Python: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>.
3. Instala la extensión oficial de Jupyter: <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>.
4. Abre la carpeta del repositorio en VS Code.
5. Abre un archivo `.ipynb` de esta carpeta.
6. Selecciona el intérprete de Python del proyecto.

### Opción B: JupyterLab

Instala dependencias opcionales:

```bash
pip install -r requirements-notebooks.txt
```

Luego ejecuta:

```bash
jupyter lab
```

Abre la carpeta `assets/notebooks/` desde el navegador.

## Importante

- Ejecuta los notebooks desde la carpeta raíz del repositorio para que las rutas funcionen.
- No uses datos reales identificables.
- Si una celda falla, lee el mensaje de error y revisa [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]].

## Relacionado

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]
