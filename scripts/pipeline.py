"""
Pipeline principal del proyecto.

Ejecuta de forma secuencial:

1. Preparación de datos
2. Entrenamiento del modelo
3. Evaluación del modelo
"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def ejecutar(script, descripcion):
    print("\n" + "=" * 60)
    print(descripcion)
    print("=" * 60)

    resultado = subprocess.run(
        [sys.executable, str(BASE_DIR / script)]
    )

    if resultado.returncode != 0:
        raise RuntimeError(f"Error ejecutando {script}")


def main():

    ejecutar(
        "preparacion_datos.py",
        "PASO 1 - PREPARACIÓN DE DATOS"
    )

    ejecutar(
        "entrenamiento.py",
        "PASO 2 - ENTRENAMIENTO DEL MODELO"
    )

    ejecutar(
        "evaluar_modelo.py",
        "PASO 3 - EVALUACIÓN DEL MODELO"
    )

    print("\n" + "=" * 60)
    print("PIPELINE EJECUTADO CORRECTAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    main()