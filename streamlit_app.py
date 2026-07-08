import streamlit as st
import requests

# URL de la API en Render
API_URL = "https://api-prediccion-mora.onrender.com/predict"

st.set_page_config(
    page_title="Predicción de Mora",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Predicción de Riesgo de Mora")
st.write(
    """
    Esta aplicación permite estimar si un cliente presenta
    riesgo de mora utilizando un modelo de Machine Learning.
    """
)

st.header("Información del cliente")

id_cliente = st.number_input("ID Cliente", value=100001.0)

importe_solicitado = st.number_input(
    "Importe solicitado",
    value=15000.0
)

duracion_credito = st.number_input(
    "Duración del crédito (meses)",
    value=24,
    step=1
)

situacion_vivienda = st.selectbox(
    "Situación de vivienda",
    [
        "ALQUILER",
        "PROPIA",
        "HIPOTECA",
        "OTROS"
    ]
)

ingresos = st.number_input(
    "Ingresos",
    value=45000.0
)

objetivo_credito = st.selectbox(
    "Objetivo del crédito",
    [
        "PERSONAL",
        "EDUCACIÓN",
        "SALUD",
        "INVERSIONES",
        "MEJORAS_HOGAR",
        "PAGO_DEUDAS"
    ]
)

pct_ingreso = st.number_input(
    "% ingreso destinado al crédito",
    value=0.32
)

tasa_interes = st.number_input(
    "Tasa de interés",
    value=10.5
)

antiguedad_cliente = st.number_input(
    "Antigüedad del cliente",
    value=36.0
)

estado_cliente = st.selectbox(
    "Estado del cliente",
    [
        "ACTIVO",
        "PASIVO"
    ]
)

gastos_ult_12m = st.number_input(
    "Gastos últimos 12 meses",
    value=1200.0
)

genero = st.selectbox(
    "Género",
    [
        "M",
        "F"
    ]
)

limite_credito_tc = st.number_input(
    "Límite tarjeta de crédito",
    value=5000.0
)

nivel_educativo = st.selectbox(
    "Nivel educativo",
    [
        "UNIVERSITARIO_COMPLETO",
        "SECUNDARIO_COMPLETO",
        "DESCONOCIDO",
        "UNIVERSITARIO_INCOMPLETO",
        "POSGRADO_INCOMPLETO",
        "POSGRADO_COMPLETO"
    ]
)

operaciones_ult_12m = st.number_input(
    "Operaciones últimos 12 meses",
    value=20.0
)

personas_a_cargo = st.number_input(
    "Personas a cargo",
    value=2.0
)

estado_civil_N = st.selectbox(
    "Estado civil",
    [
        "C",
        "S",
        "N",
        "D"
    ]
)

estado_credito_N = st.selectbox(
    "Estado del crédito",
    [
        "C",
        "P"
    ]
)

antiguedad_empleado_N = st.number_input(
    "Antigüedad empleado",
    value=5.0
)

edad_N = st.selectbox(
    "Rango de edad",
    [
        "menor_25",
        "25_a_30"
    ]
)

if st.button("Realizar predicción"):

    datos = {
        "id_cliente": id_cliente,
        "importe_solicitado": importe_solicitado,
        "duracion_credito": duracion_credito,
        "situacion_vivienda": situacion_vivienda,
        "ingresos": ingresos,
        "objetivo_credito": objetivo_credito,
        "pct_ingreso": pct_ingreso,
        "tasa_interes": tasa_interes,
        "antiguedad_cliente": antiguedad_cliente,
        "estado_cliente": estado_cliente,
        "gastos_ult_12m": gastos_ult_12m,
        "genero": genero,
        "limite_credito_tc": limite_credito_tc,
        "nivel_educativo": nivel_educativo,
        "operaciones_ult_12m": operaciones_ult_12m,
        "personas_a_cargo": personas_a_cargo,
        "estado_civil_N": estado_civil_N,
        "estado_credito_N": estado_credito_N,
        "antiguedad_empleado_N": antiguedad_empleado_N,
        "edad_N": edad_N
    }

    try:
        respuesta = requests.post(API_URL, json=datos)

        if respuesta.status_code == 200:

            resultado = respuesta.json()

            if resultado["prediccion"] == "Y":
                st.error("⚠️ Riesgo de mora")
            else:
                st.success("✅ Cliente sin riesgo de mora")

            st.write(resultado["descripcion"])

        else:
            st.error("Error al consultar la API.")
            st.write(respuesta.text)

    except Exception as e:
        st.error(f"No fue posible conectarse con la API.\n\n{e}")