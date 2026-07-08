from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "modelo_creditos.pkl"

modelo = joblib.load(MODEL_PATH)


def predecir(datos):
    df = pd.DataFrame([datos])

    pred = modelo.predict(df)[0]

    return pred