# pyright: reportMissingImports=false
from pathlib import Path
import pandas as pd  # type: ignore[import-not-found]
import matplotlib  # type: ignore[import-not-found]
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]

# Archivo de entrada.
# Para usar otro CSV, cambia esta ruta y verifica que tenga una columna
# de categoría como "tipo_incidente". Guarda datos propios en assets/datos/externos/.
DATOS = ROOT / "assets" / "datos" / "incidentes_ejemplo.csv"

# Archivo de salida del gráfico.
SALIDA = ROOT / "assets" / "imagenes" / "incidentes_por_tipo.png"


def main() -> None:
    # Leemos la tabla de incidentes sintéticos.
    datos = pd.read_csv(DATOS)

    # Contamos cuántas veces aparece cada tipo de incidente.
    # Si tu archivo usa otro nombre de columna, cambia "tipo_incidente".
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
