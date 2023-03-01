from fastapi import FastAPI
from fastapi.responses import FileResponse 

app = FastAPI()

@app.get("/")
def root():
    return {"Hi": "there...again"}

@app.get("/cat")
def cat():
    return FileResponse("files/buddy-1.jpg")
