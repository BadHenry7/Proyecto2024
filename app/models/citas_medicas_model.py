from pydantic import BaseModel

class Citasm(BaseModel):
   
    id: int= None
    id_paciente:int
    fecha: str
    hora: str
    estado: bool
    id_usuario:int

class Buscar(BaseModel):
    id_paciente:int