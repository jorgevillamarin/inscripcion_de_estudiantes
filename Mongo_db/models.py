from pydantic import BaseModel
 

class User(BaseModel):
    id: str 
    name_user:str
    Full_Name:str
    password:str
