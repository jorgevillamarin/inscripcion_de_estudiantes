def user_Entity(item) -> dict:
    return {
         "id": str(item["_id"]),
         "name_user": str (item["name_user"]),
         "Full_Name": item["Full_Name"],
         "password": item["password"]
}

def users_Entity(entity) -> license:
   return [user_Entity(item) for item in entity]
 