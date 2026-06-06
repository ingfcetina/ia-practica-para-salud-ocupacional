# pyright: reportMissingImports=false
from pathlib import Path
import pandas as pd  # type: ignore[import-not-found]
import matplotlib  # type: ignore[import-not-found]
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]
DATOS = ROOT / "assets" / "datos" / "incidentes_ejemplo.csv"
SALIDA = ROOT / "assets" / "imagenes" / "incidentes_por_tipo.png"


def main() -> None:
    datos = pd.read_csv(DATOS)
    conteo = datos["tipo_incidente"].value_counts()
    print("Incidentes por tipo:")
    print(conteo.to_string())

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    conteo.plot(kind="bar", color="#27ae60")
    plt.title("Incidentes por tipo")
    plt.xlabel("Tipo de incidente")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(SALIDA, dpi=160)
    plt.close()
    print(f"Gráfico guardado en {SALIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
