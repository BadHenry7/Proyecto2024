from pydantic import BaseModel

class Pago_detalle(BaseModel):
    id: int= None
    id_pago: int
    tipo_pago: str
    monto: float
    fecha_pago:str
    estado:bool