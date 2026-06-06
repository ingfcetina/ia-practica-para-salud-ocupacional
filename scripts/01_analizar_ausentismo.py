# pyright: reportMissingImports=false
from pathlib import Path
import pandas as pd  # type: ignore[import-not-found]
import matplotlib  # type: ignore[import-not-found]
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]
DATOS = ROOT / "assets" / "datos" / "ausentismo_ejemplo.csv"
SALIDA = ROOT / "assets" / "imagenes" / "ausentismo_por_area.png"


def main() -> None:
    datos = pd.read_csv(DATOS)
    resumen = datos.groupby("area")["dias_ausencia"].sum().sort_values(ascending=False)  # type: ignore[attr-defined,call-arg]
    print("Días de ausencia por área:")
    print(resumen.to_string())

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    resumen.plot(kind="bar", color="#2f80ed")
    plt.title("Días de ausencia por área")
    plt.xlabel("Área")
    plt.ylabel("Días de ausencia")
    plt.tight_layout()
    plt.savefig(SALIDA, dpi=160)
    plt.close()
    print(f"Gráfico guardado en {SALIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
