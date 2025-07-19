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

#-------------Para autenticacion con gitlab
from fastapi import FastAPI, Depends, HTTPException, Security, Request, Response 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from starlette.responses import RedirectResponse 
from jose import JWTError, jwt 
import requests 
from datetime import datetime, timedelta 
#----------------------------------

app = FastAPI()

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
security = HTTPBearer()


# Configuración de OAuth2 


#Configuración de GitLab OAuth2 
GITLAB_CLIENT_ID = "299d33ddd76f4c8eb38c9478d3cc75620958a65424bd117d7747832b09fe22d2" 
GITLAB_CLIENT_SECRET ="gloas-52ae7a851ee10e1bfd8f4f2a9fa0248958b184b64ce9a4b7d0b986c9899a802c"
GITLAB_REDIRECT_URI = "http://127.0.0.1:8000/login2/" 
GITLAB_AUTHORIZE_URL = "https://gitlab.com/oauth/authorize" 
#Clave secreta para JWT 
SECRET_KEY = "your-secret-key" 
ALGORITHM = "HS256"






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
        "https://494d-161-10-149-66.ngrok-free.app","https://7a66-161-10-149-66.ngrok-free.app", "http://26.156.183.54:5173","http://localhost:5174"   
        ,'http://localhost:4200'# URL de ngrok
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



# @app.middleware("http")
# async def check_authentication(request: Request, call_next):
#     allowed_paths = ["/login2/", "/static", "/favicon.ico"]
    
#     # Si la ruta comienza con algo permitido, dejar pasar
#     if any(request.url.path.startswith(path) for path in allowed_paths):
#         response = await call_next(request)
#         return response
    
#     # Si no, redirigir al login
#     return RedirectResponse(url="/login2/")


#Ruta de inicio de sesión 
@app.get("/login2/") 
async def ogin(request: Request, code: str=None): 
    if code is None: 
        #Si no se proporciona un código de autorización, redirige al usuario al endpoint de autorización de GitLab 
        authorize_url = f"{GITLAB_AUTHORIZE_URL}?client_id={GITLAB_CLIENT_ID}&redirect_uri={GITLAB_REDIRECT_URI}&response_type=code&scope=read_user" 
        return RedirectResponse (url=authorize_url) 
    #Intercambio de código de autorización por un token de acceso en GitLab 
    token_url = "https://gitlab.com/oauth/token" 
    data = { 
    "client_id": GITLAB_CLIENT_ID, 
    "client_secret": GITLAB_CLIENT_SECRET, 
    "grant_type": "authorization_code", 
    "code": code, 
    "redirect_uri": GITLAB_REDIRECT_URI, 
    } 
    response= requests.post(token_url, data=data) 
    if response.status_code != 200: 
        print(response.text) # Imprime el contenido de la respuesta para obtener más detalles sobre el error
    response_data= response.json() 
    access_token= response_data.get("access_token") 
    if not access_token: 
        raise HTTPException(status_code=400, detail="No se pudo obtener el token de acceso") 
    expires_delta= timedelta(minutes=50) 
    #token_content ["sub": access token, "scopes": ["items"]} 
    token_content = {"sub": access_token, "scopes": ["items"], "exp": datetime.utcnow() + expires_delta} 
    jwt_token= jwt.encode(token_content, SECRET_KEY, algorithm= ALGORITHM) 
    #Aquí puedes redirigir al usuario a otra página o enviar el token JWT en la respuesta 
    return {"access_token": jwt_token, "token_type": "bearer"}







#Ruta para verificar la validez del token JWT 
@app.get("/verify-token/") 
def verify_token(token: str): 
    try: 
        print ("ssssssssssss")
        #Decodifica el token JWT y verifica su firma 
        decoded_token= jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
        sub=decoded_token.get("sub") 
        scopes= decoded_token.get("scopes", []) 
        #Aquí puedes realizar cualquier otra verificación o lógica basada en el contenido del token 
        #Por ejemplo, puedes verificar si el sub o scopes son välidos 
        return {"valid": True, "sub": sub, "scopes": scopes}
    except JWTError as e: 
    #Si el token no es válido o ha expirado, se generará una excepción JWTError 
        raise HTTPException(status_code=401, detail="Token inválido o expirado")


#Ruta para obtener datos del usuario autenticado en östlab 
@app.get("/user/") 
#def get_user_data(token: str = Depends(oauth2_scheme)): 
def get_user_data(credentials: HTTPAuthorizationCredentials = Depends(security)): 
    try: 
        token = credentials.credentials
        print ("2",token)
        #Decodifica el token JWT para obtener el token de acceso 
        decoded_token=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) 
        access_token= decoded_token.get("sub") 
        #Realiza una solicitud a la API de Gitlab para obtener datos del usuario 
        user_url = "https://gitlab.com/api/v4/user" 
        headers = { 
        "Authorization": f"Bearer {access_token}" 
        }
        response=requests.get(user_url, headers=headers) 
        user_data = response.json() 
        #Aquí puedes retornar los datos del usuario o realizar cualquier otra logica basada en los datos 
        return user_data 
    except JWTError as e:
    #Si el token no es válido o ha expirado, se generará una excepción JWTerror 
        raise HTTPException(status_code=401, detail="Token inválido o expirado")



@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm= Depends()):
    return {form_data.username}
  

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