from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad
class User(BaseModel):
  name: str
  surname: str
  url: str
  age: int

#Lista de usuarios creados como entidad del objeto User
user_list = [User(name="Juan", surname="Perez", url="https://www.google.com", age=30),
             User(name="Carlos", surname="Perez", url="https://www.google.com", age=35),
             User(name="Jose", surname="Perez", url="https://www.google.com", age=20),
             User(name="Pedro", surname="Perez", url="https://www.google.com", age=30)]

@app.get("/usersjson")
async def usersjson():
  return [{"name": "Juan", "surname": "Perez", "url": "https://www.google.com", "age": 30},
          {"name": "Carlos", "surname": "Perez", "url": "https://www.google.com", "age": 35},
          {"name": "Jose", "surname": "Perez", "url": "https://www.google.com", "age": 20},
          {"name": "Pedro", "surname": "Perez", "url": "https://www.google.com", "age": 30}]

@app.get("/users")
async def usersjson():
  return user_list

