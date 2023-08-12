def user_Entity(item) -> dict:
    return {
         "id": str(item["_id"]),
         "Nombre": item["Nombre"],
         "Apellido": item["Apellido"],
         "Usuario": item["Usuario"],
         "email":item["email"],
         "password":  item["password"]
}

def users_Entity(entity) -> license:
   return [user_Entity(item) for item in entity]