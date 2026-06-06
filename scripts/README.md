# Scripts de ejemplo

Estos scripts usan datos sintéticos de `assets/datos/` y guardan resultados simples en `outputs/` o `assets/imagenes/`.

## Preparar ambiente

```bash
pip install -r requirements.txt
```

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

## Importante

Los datos son sintéticos. No reemplaces estos archivos con datos reales identificables de pacientes, trabajadores o instituciones.
