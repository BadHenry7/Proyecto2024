from pydantic import BaseModel

class Deuda(BaseModel):
    id: int= None
    id_usuario: int
    monto_total: float
    monto_pagado: float
    saldo_restante:float
    descripcion:str
    fecha_deuda:str
    estado:bool


    								
