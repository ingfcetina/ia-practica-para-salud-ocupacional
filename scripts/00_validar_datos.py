# pyright: reportMissingImports=false
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATASETS = {
    "ausentismo_ejemplo.csv": {"mes", "area", "dias_ausencia", "eventos_ausencia", "motivo_agregado", "turno"},
    "incidentes_ejemplo.csv": {"fecha", "area", "descripcion", "tipo_incidente", "severidad", "accion_inicial"},
    "checklist_inspeccion_ejemplo.csv": {"item", "categoria", "respuesta", "observacion_sintetica"},
    "indicadores_dashboard_ejemplo.csv": {"mes", "indicador", "valor", "unidad"},
}


def validar_csv(nombre: str, columnas_requeridas: set[str]) -> None:
    ruta = ROOT / "assets" / "datos" / nombre
    if not ruta.exists():
        raise FileNotFoundError(f"No existe: {ruta}")
    with ruta.open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        columnas = set(lector.fieldnames or [])
        faltantes = columnas_requeridas - columnas
        if faltantes:
            raise ValueError(f"{nombre} no tiene columnas requeridas: {sorted(faltantes)}")
        filas = list(lector)
        if not filas:
            raise ValueError(f"{nombre} no tiene filas de ejemplo")
    print(f"OK {nombre}: {len(filas)} filas")


def main() -> None:
    for nombre, columnas in DATASETS.items():
        validar_csv(nombre, columnas)
    html = ROOT / "assets" / "checklist_interactivo.html"
    if not html.exists():
        raise FileNotFoundError(f"No existe: {html}")
    print("OK checklist_interactivo.html")


if __name__ == "__main__":
    main()
