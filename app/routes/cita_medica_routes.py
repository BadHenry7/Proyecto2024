from fastapi import APIRouter, HTTPException
from app.controllers.cita_medica_controller import *
from app.models.citas_medicas_model import Citasm,Buscar

router = APIRouter()

nueva_cita = citaController() #definido donde

@router.post("/create_cita/")
async def create_cita(cita: Citasm):
    rpta = nueva_cita.create_cita(cita)
    return rpta


@router.get("/get_cita/{cita_id}",response_model=Citasm)
async def get_cita(cita_id: int):
    rpta = nueva_cita.get_cita(cita_id)
    return rpta

@router.post("/post_citas_users/")
async def post_citas_users(cita: Buscar):
    rpta = nueva_cita.post_citas_users(cita)
    return rpta

@router.get("/get_citas/")
async def get_citas():
    rpta = nueva_cita.get_citas()
    return rpta
    

@router.put("/update_cita/{cita_id}")
async def update_cita(cita_id: int ,cita: Citasm,):
    rpta = nueva_cita.update_cita(cita_id, cita)
    return rpta 

@router.delete("/eliminarcita/{cita_id}")
async def delete_cita(cita_id: int):
    rpta = nueva_cita.delete_cita(cita_id)
    return rpta 