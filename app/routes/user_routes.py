from fastapi import APIRouter, HTTPException
from app.controllers.user_controller import *
from app.models.user_model import User
from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

router = APIRouter()

nuevo_usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    return rpta


@router.get("/get_user/{user_id}",response_model=User)
async def get_user(user_id: int):
    rpta = nuevo_usuario.get_user(user_id)
    return rpta

@router.get("/get_users/")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta

    

@router.put("/actualizaruser/{user_id}")
async def update_user(user_id: int,user: User,):
    rpta = nuevo_usuario.update_user(user_id,user)
    
    return rpta 

@router.delete("/eliminarusuario/{user_id}")
async def delete_user(user_id: int):
    rpta = nuevo_usuario.delete_user(user_id)
    
    return rpta 



@router.post("/usuarios/carga-masiva/")
async def carga_masiva(file: UploadFile = File(...)):
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="Formato de archivo no soportado. Solo se acepta Excel.")

    # Leer el archivo Excel
    contents = await file.read()
    df = pd.read_excel(BytesIO(contents))
    
    # Verificar que las columnas sean correctas
    required_columns = ['usuario', 'password', 'nombre', 'apellido', 'documento', 'telefono', 'id_rol', 'estado']
    if not all(column in df.columns for column in required_columns):
        raise HTTPException(status_code=400, detail="Faltan columnas necesarias en el Excel.")
    
    # Convertir las filas del DataFrame en una lista de usuarios
    users = []
    for _, row in df.iterrows():
        user = User(
            usuario=row['usuario'],
            password=row['password'],
            nombre=row['nombre'],
            apellido=row['apellido'],
            documento=row['documento'],
            telefono=row['telefono'],
            id_rol=row['id_rol'],
            estado=row['estado']
        )
        users.append(user)
    
    # Llamar al método que inserta los usuarios
    rpta = nuevo_usuario.create_users(users)
    
    return rpta

