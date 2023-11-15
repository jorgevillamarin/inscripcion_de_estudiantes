from fastapi import APIRouter
from Mongo_db.chemas import user_Entity, users_Entity
from Mongo_db.db import conm

Login=APIRouter()

@Login.get('/users')
async def find_all_user():
   return users_Entity(conm.DataBase_Full.Usuarios.find()) 