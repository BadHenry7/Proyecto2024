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


class Reportesss(BaseModel):
    fecha: str
    fecha2: str


class EditarCita(BaseModel):
    id:int  = None  
        