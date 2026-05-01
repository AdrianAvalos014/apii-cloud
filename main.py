from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# "base de datos" simple en memoria
tareas = []

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = ""
    fechaLimite: Optional[str] = ""
    prioridad: str = "Media"
    completada: bool = False


@app.get("/")
def home():
    return {"mensaje": "API funcionando en Render"}


@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    tareas.append(tarea.dict())
    return {"msg": "Tarea creada", "data": tarea}


@app.get("/tareas")
def obtener_tareas():
    return tareas
