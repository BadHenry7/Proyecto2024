from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.rol_routes import router as Rol_router
from app.routes.atributo_routes import router as atributo_router
from app.routes.atributoxusuario_routes import router as atrixuser_router
from app.routes.cita_medica_routes import router as Cita_router
from app.routes.diagnosticos_routes import router as Diagnosticos_router
from app.routes.historial_routes import router as historial_router
from app.routes.sintomas_routes import router as sintomas_router
from red.botsi_routes import router as botci_router

from app.routes.token_routes import router as token_router
from app.routes.modulo_routes import router as modulo_router
from app.routes.moduloxperfil_routes import router as moduloxperfil_router
from app_Dynamobd.app import router as incapacidad_Dunamobd


from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173","http://localhost:3000","http://127.0.0.1:8000","https://api-nodejs-buxf.onrender.com",  # URL local de Svelte en desarrollo
        "https://494d-161-10-149-66.ngrok-free.app","https://7a66-161-10-149-66.ngrok-free.app", "http://26.156.183.54:5173","http://localhost:5174"   # URL de ngrok
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(user_router) 
app.include_router(Rol_router)
app.include_router(atributo_router)  
app.include_router(atrixuser_router)  
app.include_router(Cita_router)  
app.include_router(Diagnosticos_router) 
app.include_router(historial_router) 
app.include_router(sintomas_router) 
app.include_router(botci_router)
app.include_router(token_router)
app.include_router(modulo_router)
app.include_router(moduloxperfil_router)
app.include_router(incapacidad_Dunamobd)




"""

@app.route('/')
def home():
    return ('+page.svelte')"""

"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 
"""
#...
#