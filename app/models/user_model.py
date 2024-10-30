from pydantic import BaseModel

class User(BaseModel):
       
    usuario: str
    password: str 
    id: int= None
    nombre: str
    apellido: str
    documento: str
    telefono:str
    id_rol: int
    estado:bool
    
class Login(BaseModel):
    usuario: str
    password: str 