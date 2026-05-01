from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# "base de datos" simple en memoria (para demo)
tareas = []

class Tarea(BaseModel):
    titulo: str
    descripcion: str

@app.get("/")
def home():
    return {"mensaje": "API funcionando en Render"}

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    tareas.append(tarea)
    return {"msg": "Tarea creada", "data": tarea}

@app.get("/tareas")
def obtener_tareas():
    return tareas
