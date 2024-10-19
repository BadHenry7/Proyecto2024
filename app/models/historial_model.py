from pydantic import BaseModel

class Historial(BaseModel):
    id: int= None
    id_usuario: int
    id_sintoma: int
    fecha:str
    estado:bool
    