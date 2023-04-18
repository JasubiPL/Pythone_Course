from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return "Hola FastAPI"

@app.get("/url")
async def url():
  return {"Hola FastAPI" : "Mi primer Backend"}