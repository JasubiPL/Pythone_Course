from fastapi import FastAPI, Depends,  HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="/login")

class User(BaseModel):
  username: str
  full_name: str
  email: str
  disabled: bool

class UserDB(User):
  password:str

users_bd = {
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

def seach_user_db(username: str):
  if username in users_bd:
    return UserDB(**users_bd[username])
  
def seach_user(username: str):
  if username in users_bd:
    return User(**users_bd[username])

async def current_user(token: str = Depends(oauth2)):
  user = seach_user(token)
  if not user:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autentiacion invalidas", headers={"WWW-Authenticate": "Bearer"})
  
  if user.disabled:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo", headers={"WWW-Authenticate": "Bearer"})
  
  return user


@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
  user_bd = users_bd.get(form.username)
  if not user_bd:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username")
  
  user = seach_user_db(form.username)
  if not form.password == user.password:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
  
  return{"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
  return user