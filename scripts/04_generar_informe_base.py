# pyright: reportMissingImports=false
from pathlib import Path
import pandas as pd  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]

# Archivos de entrada.
# Para adaptar este informe, cambia estas rutas y luego revisa que las
# columnas usadas abajo existan en tus archivos.
AUSENTISMO = ROOT / "assets" / "datos" / "ausentismo_ejemplo.csv"
INCIDENTES = ROOT / "assets" / "datos" / "incidentes_ejemplo.csv"

# Archivo de salida del informe.
SALIDA = ROOT / "outputs" / "informe_base.md"


def main() -> None:
    ausentismo = pd.read_csv(AUSENTISMO)
    incidentes = pd.read_csv(INCIDENTES)

    # Indicadores agregados.
    # Si cambias de dataset, reemplaza los nombres de columnas por los de tu archivo.
    total_dias = int(ausentismo["dias_ausencia"].sum())  # type: ignore[arg-type]
    area_mayor = ausentismo.groupby("area")["dias_ausencia"].sum().idxmax()  # type: ignore[attr-defined]
    total_incidentes = len(incidentes)
    incidente_frecuente = incidentes["tipo_incidente"].value_counts().idxmax()

    informe = f"""# Informe base con datos sintéticos

## Resultados observados

- Días totales de ausencia registrados: {total_dias}.
- Área con más días de ausencia agregados: {area_mayor}.
- Incidentes sintéticos registrados: {total_incidentes}.
- Tipo de incidente más frecuente: {incidente_frecuente}.

## Límites

Estos datos son sintéticos y sirven solo para practicar. No permiten tomar decisiones sobre personas, servicios o instituciones reales.

## Preguntas para discutir

- ¿Qué información faltaría antes de proponer acciones?
- ¿Puede haber sesgos de reporte?
- ¿Qué hallazgos deberían validarse con observación o consulta al equipo?
"""
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(informe, encoding="utf-8")
    print(f"Informe guardado en {SALIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
