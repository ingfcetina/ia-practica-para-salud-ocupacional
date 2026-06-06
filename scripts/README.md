# Scripts de ejemplo

Estos scripts usan datos sintéticos de `assets/datos/` y guardan resultados simples en `outputs/` o `assets/imagenes/`.

Si prefieres aprender con celdas paso a paso, abre [[assets/notebooks/README|Notebooks de ejemplo]].

## Preparar ambiente

Instala Python desde <https://www.python.org/downloads/> y sigue la guía completa:

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]

Para instalar librerías desde la carpeta del repositorio:

### Windows

```bash
python -m pip install -r requirements.txt
```

Si `python` no funciona:

```bash
py -m pip install -r requirements.txt
```

### macOS

```bash
python3 -m pip install -r requirements.txt
```

Documentación oficial sobre instalación de paquetes: <https://packaging.python.org/en/latest/tutorials/installing-packages/>.

## Orden sugerido

### Windows

1. `python scripts/00_validar_datos.py`
2. `python scripts/01_analizar_ausentismo.py`
3. `python scripts/02_graficar_incidentes.py`
4. `python scripts/03_limpiar_datos.py`
5. `python scripts/04_generar_informe_base.py`

Si usas `py`, reemplaza `python` por `py`.

### macOS

1. `python3 scripts/00_validar_datos.py`
2. `python3 scripts/01_analizar_ausentismo.py`
3. `python3 scripts/02_graficar_incidentes.py`
4. `python3 scripts/03_limpiar_datos.py`
5. `python3 scripts/04_generar_informe_base.py`

## Qué hace cada script

| Script | Qué hace | Resultado |
|---|---|---|
| `00_validar_datos.py` | Revisa que existan los CSV y las columnas esperadas. | Mensajes `OK`. |
| `01_analizar_ausentismo.py` | Agrupa días de ausencia por área. | `assets/imagenes/ausentismo_por_area.png`. |
| `02_graficar_incidentes.py` | Cuenta incidentes por tipo. | `assets/imagenes/incidentes_por_tipo.png`. |
| `03_limpiar_datos.py` | Revisa vacíos y normaliza textos simples. | `outputs/ausentismo_limpio.csv`. |
| `04_generar_informe_base.py` | Calcula indicadores y redacta un informe base. | `outputs/informe_base.md`. |

## Importante

Los datos son sintéticos. No reemplaces estos archivos con datos reales identificables de pacientes, trabajadores o instituciones.

## Relacionado

- [[00-empezar-aqui/instalacion-y-preparacion|Instalación y preparación]]
- [[assets/notebooks/README|Notebooks de ejemplo]]
- [[06-recursos/enlaces-oficiales|Enlaces oficiales]]
