from fastapi import FastAPI
from Login.Login import Login
from Registro_de_usuarios.Registro_users import Registro_user

app = FastAPI()

app.include_router(Login)
app.include_router(Registro_user)