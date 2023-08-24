from fastapi import APIRouter
from passlib.hash import sha256_crypt
from Mongo_db.db import conm
from Mongo_db.models import User
from Mongo_db.chemas import user_Entity, users_Entity

Registro_user=APIRouter()

@Registro_user.post('/registrar')
async def create_user(user: User):
  new_user = dict(user)
  del new_user ["id"]
  new_user["password"] = sha256_crypt.encrypt(new_user["password"])
  new_user["name_user"] = sha256_crypt.encrypt(new_user["name_user"])
  id = conm.DataBase_Full.Usuarios.insert_one(new_user).inserted_id
  user = conm.DataBase_Full.Usuarios.find_one({"_id": id})
  return ("Haz sido registrado con exitos")
 