from pydantic import BaseModel
 

class User(BaseModel):
    id: str 
    Nombre: str
    Apellido: str
    Usuario: str 
    email: str
    password: str
