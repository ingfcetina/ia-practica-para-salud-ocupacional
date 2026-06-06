# pyright: reportMissingImports=false
from pathlib import Path
import pandas as pd  # type: ignore[import-not-found]
import matplotlib  # type: ignore[import-not-found]
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]

# Archivo de entrada.
# Para usar otro CSV, cambia solo esta ruta y verifica que tenga las columnas
# "area" y "dias_ausencia". Guarda datos propios en assets/datos/externos/.
DATOS = ROOT / "assets" / "datos" / "ausentismo_ejemplo.csv"

# Archivo de salida del gráfico.
# Puedes cambiar el nombre del PNG si quieres guardar varias versiones.
SALIDA = ROOT / "assets" / "imagenes" / "ausentismo_por_area.png"


def main() -> None:
    # Leemos la tabla.
    datos = pd.read_csv(DATOS)

    # Agrupamos por área y sumamos días de ausencia.
    # Si tu archivo usa otros nombres de columnas, cambia "area" y
    # "dias_ausencia" por los nombres correspondientes.
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
