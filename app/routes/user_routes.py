from fastapi import APIRouter, HTTPException, UploadFile, File
from app.controllers.user_controller import *
from app.models.user_model import User,Estado,Login,Buscar,Actualizar


router = APIRouter()

nuevo_usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    rpta = nuevo_usuario.create_user(user)
    return rpta



@router.post("/get_user")
async def get_user(user: Buscar):
    rpta = nuevo_usuario.get_user(user)
    return rpta


@router.get("/get_users/")
async def get_users():
    rpta = nuevo_usuario.get_users()
    return rpta

@router.get("/getpaciente")
async def get_paciente():
    rpta = nuevo_usuario.get_paciente()
    return rpta


@router.get("/getmedico")
async def get_medico():
    rpta = nuevo_usuario.get_medico()
    return rpta

@router.put("/actualizaruser")
async def update_user(user :Actualizar):
    rpta = nuevo_usuario.update_user(user)
    return rpta 

@router.delete("/eliminarusuario/{user_id}")
async def delete_user(user_id: int):
    rpta = nuevo_usuario.delete_user(user_id)
    
    return rpta 


@router.post("/create_user_masivo")
async def create_user_masivo(file: UploadFile = File(...)):
    rpta = nuevo_usuario.create_user_masivo(file)  # Esto está bien
    return rpta



@router.post("/login")
async def login(user: Login):
    rpta = nuevo_usuario.login(user)
    return rpta

@router.put("/estado_user")
async def estado_user(user: Estado):
    rpta = nuevo_usuario.estado_user(user)
    return rpta 

#v_usuario   