from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["users"], responses={404: {"description": "Not found"}})

#Entidad
class User(BaseModel):
  id:int
  surname: str
  url: str
  age: int

#Lista de usuarios creados como entidad del objeto User
user_list = [User(id=4,name="Juan", surname="Perez", url="https://www.google.com", age=30),
             User(id=3,name="Carlos", surname="Perez", url="https://www.google.com", age=35),
             User(id=2,name="Jose", surname="Perez", url="https://www.google.com", age=20),
             User(id=1,name="Pedro", surname="Perez", url="https://www.google.com", age=30)]

#---->GET
@router.get("/")
async def usersjson():
  return user_list

@router.get("/{id}")
async def user(id:int):
  return searchUsers(id)
  

def searchUsers(id):
  users = filter(lambda user:user.id == id, user_list)
  try:
    return list(users)[0]
  except:
    return {"err": "No se ha encontrado usuario"}


#---->POST

@router.post("/", status_code=201)
async def user(user:User):
  if type(searchUsers(user.id)) == User:
    raise HTTPException(status_code=404, detail="El usuario ya existe")

  user_list.append(user)
  return {"El Usuario ha sido creado con exito": user}
  
#---->PUT
@router.put("/")
async def user(user:User):

  found =  False

  for index, saved_user in enumerate(user_list):
    if saved_user.id == user.id:
      user_list[index] = user
      found = True
    
  if not found:
    return {"err": "No se ha encontrado usuaro para actualizar"}
  else:
    return {"El usuario ha sido actualizado con exito": user}
  
#---->Delete

@router.delete("/{id}")
async def user(id:int):

  found =  False

  for index, saved_user in enumerate(user_list):
    if saved_user.id == id:
      del user_list[index]
      found = True
      return "El usuario ha sido eliminado con exito"
    
  if not found:
    return {"err": "No se ha encontrado usuaro para eliminar"}

  

  
