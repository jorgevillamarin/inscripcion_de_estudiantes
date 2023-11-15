from fastapi import FastAPI
from Login.Login import Login
from Registro_de_usuarios.Registro_users import Registro_user
from fastapi import FastAPI
from decouple import config

app = FastAPI()

app.include_router(Login)
app.include_router(Registro_user)

# Configuración de la base de datos
MONGODB_URL = config("MONGODB_URL")
SECRET_KEY = config("SECRET_KEY")

# Otras configuraciones si las tienes
DEBUG = config("DEBUG", default=False, cast=bool)
PORT = config("PORT", default=8000, cast=int)
HOST = config("HOST", default="localhost")

app.get('/status')
async def conexion():
 return("backend conectado")