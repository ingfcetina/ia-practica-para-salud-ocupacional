# Instalación y preparación

tags: #instalacion #python #obsidian #preparacion

Esta guía te ayuda a preparar el computador para usar el vault, abrir las notas, ejecutar los scripts de Python y probar la página interactiva.

> Si estás en una clase de una hora, no te preocupes si no alcanzas a instalar todo. Puedes seguir el material desde GitHub u Obsidian y revisar los resultados ya generados.

## Qué vas a instalar

| Herramienta | Para qué sirve |
|---|---|
| Obsidian | Abrir este repositorio como vault y navegar con enlaces internos. |
| Python | Ejecutar ejemplos de análisis de datos. |
| Librerías `pandas` y `matplotlib` | Leer tablas CSV y crear gráficos. |
| Editor de texto o código | Leer y modificar scripts. Puede ser VS Code, Cursor, Codex, Notepad u otro. |

## Paso 1: descargar el repositorio

Si lo recibes como enlace de GitHub:

1. Abre el repositorio en el navegador.
2. Presiona **Code**.
3. Elige **Download ZIP**.
4. Descomprime el archivo en una carpeta fácil de encontrar, por ejemplo `Documentos/ia-practica-para-salud-ocupacional`.

Si sabes usar Git, también puedes clonar el repositorio:

```bash
git clone https://github.com/ingfcetina/ia-practica-para-salud-ocupacional.git
```

## Paso 2: instalar Obsidian

1. Ve a <https://obsidian.md/>.
2. Descarga Obsidian para tu sistema operativo.
3. Instálalo y ábrelo.
4. Selecciona **Open folder as vault** o **Abrir carpeta como vault**.
5. Elige la carpeta del repositorio.
6. Abre [[00-empezar-aqui/mapa-del-vault|Mapa del vault]].

## Paso 3: instalar Python

### En Windows

1. Ve a <https://www.python.org/downloads/>.
2. Descarga la versión estable más reciente de Python.
3. Durante la instalación, marca la opción **Add Python to PATH**.
4. Finaliza la instalación.
5. Abre PowerShell o la Terminal.
6. Verifica:

```bash
python --version
```

Si Windows abre Microsoft Store en lugar de mostrar la versión, instala Python desde `python.org` y revisa los alias de ejecución de aplicaciones en la configuración de Windows.

### En macOS

1. Ve a <https://www.python.org/downloads/>.
2. Descarga Python para macOS.
3. Instálalo.
4. Abre Terminal.
5. Verifica:

```bash
python3 --version
```

En macOS puede que debas usar `python3` en lugar de `python`.

### En Linux

En muchas distribuciones Python ya viene instalado. Verifica:

```bash
python3 --version
```

Si no está instalado, usa el gestor de paquetes de tu distribución.

## Paso 4: abrir una terminal en la carpeta del vault

La terminal debe estar ubicada en la carpeta donde están `README.md`, `assets/` y `scripts/`.

En Windows puedes:

1. Abrir la carpeta en el Explorador.
2. Hacer clic derecho dentro de la carpeta.
3. Elegir **Abrir en Terminal**.

Verifica que ves archivos como:

```text
README.md
assets/
scripts/
requirements.txt
```

## Paso 5: instalar librerías de Python

Ejecuta:

```bash
pip install -r requirements.txt
```

Si tu sistema usa `python3`, puede que necesites:

```bash
python3 -m pip install -r requirements.txt
```

## Paso 6: validar los datos

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

## Paso 7: ejecutar los ejemplos

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

## Paso 8: abrir la página interactiva

Abre este archivo con doble clic:

```text
assets/checklist_interactivo.html
```

No necesita internet ni servidor. Se abre en el navegador.

## Si algo no funciona

| Problema | Qué intentar |
|---|---|
| `python` no se reconoce | Prueba `python3 --version` o reinstala Python marcando **Add Python to PATH**. |
| `pip` no se reconoce | Prueba `python -m pip install -r requirements.txt`. |
| Falta `pandas` o `matplotlib` | Ejecuta de nuevo `pip install -r requirements.txt`. |
| El gráfico no aparece | Revisa `assets/imagenes/`; los scripts guardan imágenes ahí. |
| El vault no abre en Obsidian | Asegúrate de abrir la carpeta completa, no un archivo suelto. |

## Regla de privacidad

No uses datos reales identificables para practicar. Usa los archivos sintéticos de [[06-recursos/datasets-ejemplo|Datasets de ejemplo]].

## Relacionado

- [[00-empezar-aqui/ruta-de-aprendizaje|Ruta de aprendizaje]]
- [[06-recursos/datasets-ejemplo|Datasets de ejemplo]]
- [[scripts/README|Scripts de ejemplo]]
