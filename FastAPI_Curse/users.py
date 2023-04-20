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
  
