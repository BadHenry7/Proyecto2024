from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.rol_routes import router as Rol_router
from app.routes.atributo_routes import router as atributo_router
from app.routes.atributoxusuario_routes import router as atrixuser_router
from app.routes.pago_routes import router as Pago_router
from app.routes.diagnosticos_routes import router as Diagnosticos_router
from app.routes.historial_routes import router as historial_router
from app.routes.sintomas_routes import router as sintomas_router

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
app.include_router(Diagnosticos_router) 
app.include_router(historial_router) 
app.include_router(sintomas_router) 



"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) """