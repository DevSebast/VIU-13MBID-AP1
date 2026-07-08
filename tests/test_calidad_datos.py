from pathlib import Path
import pandas as pd

# Ruta donde se encuentran los archivos de datos
DATA_PATH = Path("data/raw")


def cargar_creditos():
    """Carga el dataset de créditos."""
    return pd.read_csv(DATA_PATH / "datos_creditos.csv", sep=";")


def cargar_tarjetas():
    """Carga el dataset de tarjetas."""
    return pd.read_csv(DATA_PATH / "datos_tarjetas.csv", sep=";")


def test_existen_archivos():
    """Verifica que existan los archivos de entrada."""
    assert (DATA_PATH / "datos_creditos.csv").exists()
    assert (DATA_PATH / "datos_tarjetas.csv").exists()


def test_creditos_no_vacio():
    """Verifica que el dataset de créditos tenga registros."""
    df = cargar_creditos()
    assert not df.empty


def test_tarjetas_no_vacio():
    """Verifica que el dataset de tarjetas tenga registros."""
    df = cargar_tarjetas()
    assert not df.empty


def test_columna_id_cliente():
    """Verifica que ambas fuentes tengan la columna id_cliente."""
    creditos = cargar_creditos()
    tarjetas = cargar_tarjetas()

    assert "id_cliente" in creditos.columns
    assert "id_cliente" in tarjetas.columns