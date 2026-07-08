"""
Script de preparación de datos.
Automatiza el proceso de limpieza, transformación e integración
de los datos del proyecto.
"""

from pathlib import Path
import pandas as pd

# Rutas del proyecto
BASE_PATH = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_PATH / "data" / "raw"
PROCESSED_PATH = BASE_PATH / "data" / "processed"


def preparar_datos():
    print("Leyendo archivos...")

    df_creditos = pd.read_csv(
        RAW_PATH / "datos_creditos.csv",
        sep=";"
    )

    df_tarjetas = pd.read_csv(
        RAW_PATH / "datos_tarjetas.csv",
        sep=";"
    )

    print("Aplicando limpieza...")

    # Eliminar columnas innecesarias
    if "nivel_tarjeta" in df_tarjetas.columns:
        df_tarjetas.drop(columns=["nivel_tarjeta"], inplace=True)

    # Filtrar edades
    df_creditos = df_creditos[df_creditos["edad"] < 90]

    # Eliminar registros nulos
    df_creditos.dropna(inplace=True)

    print("Integrando datasets...")

    df_integrado = pd.merge(
        df_creditos,
        df_tarjetas,
        on="id_cliente",
        how="inner"
    )

    print("Transformando variables...")

    estado_civil = {
        "CASADO": "C",
        "SOLTERO": "S",
        "DESCONOCIDO": "N",
        "DIVORCIADO": "D",
    }

    estado_credito = {
        0: "P",
        1: "C",
    }

    df_integrado["estado_civil_N"] = (
        df_integrado["estado_civil"]
        .map(estado_civil)
    )

    df_integrado["estado_credito_N"] = (
        df_integrado["estado_credito"]
        .map(estado_credito)
    )

    df_integrado["antiguedad_empleado_N"] = pd.cut(
        df_integrado["antiguedad_empleado"],
        bins=[0, 4, 10, 50],
        labels=["menor_5", "5_a_10", "mayor_10"],
        right=False
    ).cat.add_categories("NA").fillna("NA")

    df_integrado["edad_N"] = pd.cut(
        df_integrado["edad"],
        bins=[0, 24, 50],
        labels=["menor_25", "25_a_30"]
    )

    df_integrado.drop(
        columns=[
            "estado_civil",
            "estado_credito",
            "antiguedad_empleado",
            "edad",
        ],
        inplace=True
    )

    PROCESSED_PATH.mkdir(exist_ok=True)

    salida = PROCESSED_PATH / "datos_integrados.csv"

    df_integrado.to_csv(
        salida,
        index=False
    )

    print(f"Archivo generado correctamente: {salida}")

    return df_integrado


if __name__ == "__main__":
    preparar_datos()