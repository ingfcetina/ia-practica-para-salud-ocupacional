# Notebooks de ejemplo

Estos notebooks permiten aprender paso a paso con texto, código y resultados en el mismo archivo.

## Qué es un notebook

Un notebook de Jupyter es un archivo `.ipynb`. Tiene dos tipos de partes:

- explicaciones escritas;
- celdas de código que puedes ejecutar con un botón ▶.

Es como una guía práctica donde puedes leer y probar al mismo tiempo.

Para una explicación más completa, revisa [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]].

## Notebooks incluidos

| Notebook | Qué practica | Datos usados |
|---|---|---|
| `01_analizar_ausentismo.ipynb` | Leer ausentismo, agrupar por área y graficar. | `assets/datos/ausentismo_ejemplo.csv` |
| `02_graficar_incidentes.ipynb` | Contar incidentes por tipo y revisar severidad. | `assets/datos/incidentes_ejemplo.csv` |
| `03_checklist_y_dashboard.ipynb` | Calcular cumplimiento y graficar indicadores. | `assets/datos/checklist_inspeccion_ejemplo.csv`, `assets/datos/indicadores_dashboard_ejemplo.csv` |
| `04_generar_informe_base.ipynb` | Crear un borrador de informe con indicadores agregados. | `assets/datos/ausentismo_ejemplo.csv`, `assets/datos/incidentes_ejemplo.csv` |

## Opción recomendada para principiantes: VS Code

1. Instala Python siguiendo [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]].
2. Instala VS Code: <https://code.visualstudio.com/Download>.
3. Abre VS Code.
4. Instala la extensión **Python**.
5. Instala la extensión **Jupyter**.
6. En VS Code, elige **File → Open Folder**.
7. Abre la carpeta completa del repositorio.
8. En el panel izquierdo, abre `assets/notebooks/`.
9. Haz clic en `01_analizar_ausentismo.ipynb`.
10. Si pide un **Kernel**, elige Python.
11. Ejecuta cada celda con el botón ▶.

## Opción con JupyterLab

Usa esta opción si quieres abrir notebooks en el navegador.

1. Abre una consola en la carpeta del repositorio.
2. Instala Jupyter:

### Windows

```bash
python -m pip install -r requirements-notebooks.txt
```

Si `python` no funciona:

```bash
py -m pip install -r requirements-notebooks.txt
```

### macOS / Linux

```bash
python3 -m pip install -r requirements-notebooks.txt
```

3. Abre JupyterLab:

### Windows

```bash
python -m jupyter lab
```

### macOS / Linux

```bash
python3 -m jupyter lab
```

4. En el navegador, entra a `assets/notebooks/`.
5. Abre un notebook.
6. Ejecuta celdas en orden.

## Cómo verlos en GitHub

GitHub permite abrir los `.ipynb` para leerlos, pero no ejecutarlos. Para ejecutar celdas necesitas VS Code o JupyterLab.

## Importante

- Abre siempre la carpeta completa del repositorio, no solo el notebook suelto.
- Ejecuta las celdas en orden.
- No uses datos reales identificables.
- Si una celda falla, copia el error y pide ayuda con este prompt:

```text
Estoy ejecutando un notebook de Python.
No tengo experiencia programando.
Este es el error: [pega el error].
Explícame qué significa y qué paso debo revisar.
```

## Relacionado

- [[06-recursos/guia-python-jupyter|Guía de Python y Jupyter Notebooks]]
- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]
