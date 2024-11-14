from pydantic import BaseModel

class Diagnosticos(BaseModel):
    
    id: int= None
    id_usuario: int
    resultado: str
    fecha_diagnostico: str
    estado: bool



class Reportesss(BaseModel):
    fecha: str
    fecha2: str