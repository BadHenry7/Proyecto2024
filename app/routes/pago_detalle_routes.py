from fastapi import APIRouter, HTTPException
from app.controllers.pago_detalle_controller import *
from app.models.pago_detalle_model import Pago_detalle

router = APIRouter()

nuevo_pago_detalle = pay_detail_Controller() #definido donde

@router.post("/create_pay_detalle/")
async def create_pay_detalle(pago_detalle: Pago_detalle):
    rpta = nuevo_pago_detalle.create_pay_detalle(pago_detalle)
    return rpta


@router.get("/get_pay_detalle/{pago_detalle_id}",response_model=Pago_detalle)
async def get_pay_detalle(pago_detalle_id: int):
    rpta = nuevo_pago_detalle.get_pay_detalle(pago_detalle_id)
    return rpta

@router.get("/get_pays_detalles/")
async def get_pays_detalles():
    rpta = nuevo_pago_detalle.get_pays_detalles()
    return rpta

    

@router.put("/update_pay_detalle/{pago_detalle_id}")
async def update_pay_detalle(pago_detalle_id: int ,pago_detalle: Pago_detalle,):
    rpta = nuevo_pago_detalle.update_pay_detalle(pago_detalle_id, pago_detalle)
    return rpta 

@router.delete("/delete_pay_detalle/{pago_detalle_id}")
async def delete_pay_detalle(pago_detalle_id: int):
    rpta = nuevo_pago_detalle.delete_pay_detalle(pago_detalle_id)
    
    return rpta 