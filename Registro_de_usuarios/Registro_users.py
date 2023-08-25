from fastapi import APIRouter, HTTPException, status
from passlib.hash import sha256_crypt
from Mongo_db.db import conm
from Mongo_db.models import User
from fastapi.responses import JSONResponse
from Mongo_db.chemas import user_Entity, users_Entity
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from datetime import datetime, timedelta
from pydantic import BaseModel
import jwt
from typing import Optional

Registro_user=APIRouter()

@Registro_user.post('/registrar')
async def create_user(user: User):
  new_user = dict(user)
  del new_user ["id"]
  id = conm.DataBase_Full.Usuarios.insert_one(new_user).inserted_id
  user = conm.DataBase_Full.Usuarios.find_one({"_id": id})
  return ("Haz sido registrado con exitos")
 
class UserLogin(BaseModel):
    name_user: str
    password: str


@Registro_user.post('/login')
async def login_user(user: UserLogin):
    # Obtiene la colección de usuarios de la base de datos
    collection: Collection = conm.DataBase_Full["Usuarios"]
    
    # Busca el usuario en la base de datos por su nombre de usuario
    stored_user = collection.find_one({"name_user": user.name_user})
    
    if stored_user is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    # Compara la contraseña ingresada con la contraseña almacenada en la base de datos
    if stored_user["password"] == user.password:
        # Genera el token JWT
        token_payload = {
            "sub": user.name_user,
            "exp": datetime.utcnow() + timedelta(hours=3)  # Token válido por 3 horas
        }
        secret_key = "tu_clave_secreta"  # Cambia esto a una clave segura
        
        token = jwt.encode(token_payload, secret_key, algorithm="HS256")
        
        return JSONResponse(content={"message": "Inicio de sesión exitoso", "token": token})
    else:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")