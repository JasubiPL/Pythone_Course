from fastapi import FastAPI, Depends,  HTTPException
from pydantic import BaseModel
from fastapi.security import OaAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth = OaAuth2PasswordBearer(tokenUrl="/login")

class User(BaseModel):
  username: str
  full_name: str
  email: str
  disabled: bool

class UserDB(User):
  password:str

user_bd = {
  "mouredev": {
    "username": "mouredev", 
    "full_name": "Brais Moure",
    "email": "braismoure@outlook.com",
    "disabled": False,
    "password": "123456"
  },
  "jasubip": {
    "username": "jasubip", 
    "full_name": "Jasubi Pineyro",
    "email": "jasubip@outlook.com",
    "disabled": True,
    "password": "6789"
  }
}

def seach_user(username: str):
  if username in user_bd:
    return UserDB(user_bd[username])
  
@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
  user_bd = user_bd.get(form.username)
  if not user_bd:
    raise HTTPException(status_code=400, detail="Incorrect username")
  
  user = seach_user(form.username)
  if not form.password == user.password:
    raise HTTPException(status_code=400, detail="Incorrect password")
  
  return{"access_token": user.username, "token_type": "bearer"}
