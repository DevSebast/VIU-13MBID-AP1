from pathlib import Path
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)


# =====================================
# Rutas
# =====================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "processed" / "datos_integrados.csv"
MODEL_PATH = BASE_DIR / "models" / "modelo_creditos.pkl"


# =====================================
# Cargar datos
# =====================================

print("Cargando datos...")

df = pd.read_csv(DATA_PATH)

target = "falta_pago"

X = df.drop(columns=[target])
y = df[target]


# =====================================
# División de datos
# =====================================

X_temp, X_test, y_temp, y_test = train_test_split(
    X,
    y,
    test_size=0.10,
    random_state=42,
    stratify=y
)

X_train, X_val, y_train, y_val = train_test_split(
    X_temp,
    y_temp,
    test_size=0.22,
    random_state=42,
    stratify=y_temp
)


# =====================================
# Cargar modelo
# =====================================

print("Cargando modelo entrenado...")

modelo = joblib.load(MODEL_PATH)


# =====================================
# Predicciones
# =====================================

print("Realizando predicciones...")

y_pred = modelo.predict(X_test)


# =====================================
# Métricas
# =====================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("RESULTADOS DEL MODELO")
print("==============================")

print(f"\nAccuracy: {accuracy:.4f}")

print("\nReporte de clasificación:\n")

print(classification_report(y_test, y_pred))


# =====================================
# Matriz de confusión
# =====================================

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot(cmap="Blues")

plt.title("Matriz de Confusión")

plt.tight_layout()

plt.show()

print("\nEvaluación finalizada correctamente.")