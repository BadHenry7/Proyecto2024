from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.rol_routes import router as Rol_router
from app.routes.atributo_routes import router as atributo_router
from app.routes.atributoxusuario_routes import router as atrixuser_router
from app.routes.pago_routes import router as Pago_router
from app.routes.Transacciones_routes import router as Transaccion_router
from app.routes.pago_detalle_routes import router as pago_detalle_router
from app.routes.deuda_routes import router as deuda_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router) 
app.include_router(Rol_router)
app.include_router(atributo_router)  
app.include_router(atrixuser_router)  
app.include_router(Pago_router)  
app.include_router(Transaccion_router) 
app.include_router(pago_detalle_router) 
app.include_router(deuda_router) 



"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) """