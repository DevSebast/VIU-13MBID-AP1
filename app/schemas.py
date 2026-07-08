from typing import Optional
from pydantic import BaseModel


class Cliente(BaseModel):
    id_cliente: float
    importe_solicitado: float
    duracion_credito: int
    situacion_vivienda: str
    ingresos: float
    objetivo_credito: str
    pct_ingreso: float
    tasa_interes: float
    antiguedad_cliente: float
    estado_cliente: str
    gastos_ult_12m: float
    genero: str
    limite_credito_tc: float
    nivel_educativo: str
    operaciones_ult_12m: float
    personas_a_cargo: float
    estado_civil_N: str
    estado_credito_N: str
    antiguedad_empleado_N: Optional[float] = None
    edad_N: str