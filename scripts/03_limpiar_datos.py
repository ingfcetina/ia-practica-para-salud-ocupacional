# pyright: reportMissingImports=false
from pathlib import Path
import pandas as pd  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]

# Archivo de entrada.
# Para limpiar otro CSV, cambia esta ruta. Si cambian las columnas, ajusta
# también la lista del bucle más abajo.
DATOS = ROOT / "assets" / "datos" / "ausentismo_ejemplo.csv"

# Archivo de salida con una copia limpia.
SALIDA = ROOT / "outputs" / "ausentismo_limpio.csv"


def main() -> None:
    datos = pd.read_csv(DATOS)
    print("Valores vacíos por columna:")
    print(datos.isna().sum().to_string())

    # Quitamos espacios sobrantes en columnas de texto.
    # Si tu archivo no tiene alguna de estas columnas, elimínala de la lista
    # o reemplázala por el nombre correcto.
    for columna in ["area", "mes", "motivo_agregado", "turno"]:
        datos[columna] = datos[columna].astype(str).str.strip()

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    datos.to_csv(SALIDA, index=False)
    print(f"Datos limpios guardados en {SALIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
