# Scripts de ejemplo

Estos scripts usan datos sintéticos de `assets/datos/` y guardan resultados simples en `outputs/` o `assets/imagenes/`.

Si prefieres aprender con celdas paso a paso, abre [[assets/notebooks/README|Notebooks de ejemplo]].

## Preparar ambiente

Instala Python desde <https://www.python.org/downloads/> y luego ejecuta:

```bash
pip install -r requirements.txt
```

Documentación oficial sobre instalación de paquetes: <https://packaging.python.org/en/latest/tutorials/installing-packages/>.

Con `uv`, también puedes ejecutar sin instalar globalmente:

```bash
uv run --with pandas --with matplotlib python scripts/01_analizar_ausentismo.py
```

## Orden sugerido

1. `python scripts/00_validar_datos.py`
2. `python scripts/01_analizar_ausentismo.py`
3. `python scripts/02_graficar_incidentes.py`
4. `python scripts/03_limpiar_datos.py`
5. `python scripts/04_generar_informe_base.py`

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
