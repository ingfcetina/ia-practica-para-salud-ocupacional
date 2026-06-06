# pyright: reportMissingImports=false
from pathlib import Path
import pandas as pd  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]
DATOS = ROOT / "assets" / "datos" / "ausentismo_ejemplo.csv"
SALIDA = ROOT / "outputs" / "ausentismo_limpio.csv"


def main() -> None:
    datos = pd.read_csv(DATOS)
    print("Valores vacíos por columna:")
    print(datos.isna().sum().to_string())

    for columna in ["area", "mes", "motivo_agregado", "turno"]:
        datos[columna] = datos[columna].astype(str).str.strip()

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    datos.to_csv(SALIDA, index=False)
    print(f"Datos limpios guardados en {SALIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
