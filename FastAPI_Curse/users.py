from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
@app.get("/usersjson")
async def usersjson():
  return [{"name": "Juan", "surname": "Perez", "url": "https://www.google.com", "age": 30},
          {"name": "Carlos", "surname": "Perez", "url": "https://www.google.com", "age": 35},
          {"name": "Jose", "surname": "Perez", "url": "https://www.google.com", "age": 20},
          {"name": "Pedro", "surname": "Perez", "url": "https://www.google.com", "age": 30}]

@app.get("/users")
async def usersjson():
  return user_list

@app.get("/user/{id}")
async def user(id:int):
  return searchUsers(id)
  
@app.get("/user/")
async def user(id:int):
  return searchUsers(id)

def searchUsers(id):
  users = filter(lambda user:user.id == id, user_list)
  try:
    return list(users)[0]
  except:
    return {"err": "No se ha encontrado usuario"}


#---->POST

@app.post("/user/")
async def user(user:User):
  if type(searchUsers(user.id)) == User:
    return {"err": "El usuario ya existe"}
  else:
    user_list.append(user)
    return {"El Usuario ha sido creado con exito": user}
  
#---->PUT
@app.put("/user/")
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
  

  
