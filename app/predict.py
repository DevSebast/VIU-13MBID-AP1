from pathlib import Path
import joblib
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "modelo_creditos.pkl"

modelo = joblib.load(MODEL_PATH)


def predecir(datos):

    df = pd.DataFrame([datos])

    # Columnas numéricas
    columnas_numericas = [
        "id_cliente",
        "importe_solicitado",
        "duracion_credito",
        "ingresos",
        "pct_ingreso",
        "tasa_interes",
        "antiguedad_cliente",
        "gastos_ult_12m",
        "limite_credito_tc",
        "operaciones_ult_12m",
        "personas_a_cargo"
    ]

    for c in columnas_numericas:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Esta columna puede venir vacía
    df["antiguedad_empleado_N"] = np.nan

    # Columnas categóricas
    columnas_categoricas = [
        "situacion_vivienda",
        "objetivo_credito",
        "estado_cliente",
        "genero",
        "nivel_educativo",
        "estado_civil_N",
        "estado_credito_N",
        "edad_N"
    ]

    for c in columnas_categoricas:
        df[c] = df[c].astype(str)

    pred = modelo.predict(df)[0]

    return pred