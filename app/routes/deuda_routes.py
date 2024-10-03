from fastapi import APIRouter, HTTPException
from app.controllers.deuda_controller import *
from app.models.deuda_model import Deuda

router = APIRouter()

nueva_deuda = debtController() #definido donde

@router.post("/create_debt/")
async def create_debt(deuda: Deuda):
    rpta = nueva_deuda.create_debt(deuda)
    return rpta


@router.get("/get_debt/{deuda_id}",response_model=Deuda)
async def get_debt(deuda_id: int):
    rpta = nueva_deuda.get_debt(deuda_id)
    return rpta

@router.get("/get_debts/")
async def get_debts():
    rpta = nueva_deuda.get_debts()
    return rpta

    

@router.put("/update_debts/{deuda_id}")
async def update_debts(deuda_id: int ,deuda: Deuda,):
    rpta = nueva_deuda.update_debts(deuda_id, deuda)
    return rpta 

@router.delete("/delete_debts/{deuda_id}")
async def delete_debts(deuda_id: int):
    rpta = nueva_deuda.delete_debts(deuda_id)
    
    return rpta 