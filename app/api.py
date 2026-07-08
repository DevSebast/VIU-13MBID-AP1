from fastapi import FastAPI
from app.schemas import Cliente
from app.predict import predecir

app = FastAPI(
    title="API Predicción de Mora",
    version="1.0"
)

@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente"
    }


@app.post("/predict")
def predict(cliente: Cliente):

    resultado = predecir(cliente.model_dump())

    return {
        "codigo": resultado,
        "prediccion": (
            "Alto riesgo de mora"
            if resultado == "Y"
            else "Bajo riesgo de mora"
        )
    }