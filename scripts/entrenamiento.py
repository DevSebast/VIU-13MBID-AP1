from pathlib import Path
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score


# =====================================
# Rutas
# =====================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "processed" / "datos_integrados.csv"
MODEL_PATH = BASE_DIR / "models"

MODEL_PATH.mkdir(exist_ok=True)

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
# Columnas
# =====================================

num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()

# =====================================
# Preprocesamiento
# =====================================

numeric_transformer = Pipeline([
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, num_cols),
    ("cat", categorical_transformer, cat_cols)
])

# =====================================
# Modelo final
# =====================================

modelo = Pipeline([
    ("prep", preprocessor),
    ("model", LinearSVC(max_iter=5000))
])

# =====================================
# MLflow
# =====================================

mlflow.set_experiment("Prediccion_Mora")

with mlflow.start_run():

    modelo.fit(X_train, y_train)

    pred = modelo.predict(X_val)

    accuracy = accuracy_score(y_val, pred)

    print(f"Accuracy: {accuracy:.4f}")

    mlflow.log_param("modelo", "LinearSVC")
    mlflow.log_param("max_iter", 5000)

    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(
        modelo,
        artifact_path="modelo"
    )

    joblib.dump(
        modelo,
        MODEL_PATH / "modelo_creditos.pkl"
    )

print("\nModelo guardado correctamente.")

print(MODEL_PATH / "modelo_creditos.pkl")