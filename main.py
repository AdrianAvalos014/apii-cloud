# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Optional

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # "base de datos" simple en memoria
# tareas = []

# class Tarea(BaseModel):
#     id: int
#     userId: str   # 🔥 CLAVE
#     titulo: str
#     descripcion: str = ""
#     fechaLimite: str = ""
#     prioridad: str = "Media"
#     completada: bool = False

# @app.get("/tareas/{user_id}")
# def obtener_tareas(user_id: str):
#     return [t for t in tareas if t["userId"] == user_id]


# # class Tarea(BaseModel):
# #     id: int
# #     titulo: str
# #     descripcion: Optional[str] = ""
# #     fechaLimite: Optional[str] = ""
# #     prioridad: str = "Media"
# #     completada: bool = False


# @app.get("/")
# def home():
#     return {"mensaje": "API funcionando en Render"}


# @app.post("/tareas")
# def crear_tarea(tarea: Tarea):
#     tareas.append(tarea.dict())
#     return {"msg": "Tarea creada", "data": tarea}


# @app.get("/tareas")
# def obtener_tareas():
#     return tareas

# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from typing import List

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # 🔥 "DB" en memoria
# tareas = []


# # ================= MODELO =================
# class Tarea(BaseModel):
#     id: int
#     userId: str
#     titulo: str
#     descripcion: str = ""
#     fechaLimite: str = ""
#     prioridad: str = "Media"
#     completada: bool = False


# # ================= ENDPOINTS =================

# @app.get("/")
# def home():
#     return {"mensaje": "API funcionando en Render"}


# # 🔥 GET POR USUARIO
# @app.get("/tareas/{user_id}")
# def obtener_tareas(user_id: str):
#     return [t for t in tareas if t["userId"] == user_id]


# # 🔥 CREAR
# @app.post("/tareas")
# def crear_tarea(tarea: Tarea):
#     tareas.append(tarea.dict())
#     return {"msg": "Tarea creada", "data": tarea}

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# tareas = []

# class Tarea(BaseModel):
#     id: int
#     userId: str
#     titulo: str
#     descripcion: str | None = None
#     fechaLimite: str | None = None
#     prioridad: str
#     completada: bool


# # ================= GET POR USUARIO =================
# @app.get("/tareas/{userId}")
# def get_tareas(userId: str):
#     return [t for t in tareas if t.userId == userId]


# # ================= POST =================
# @app.post("/tareas")
# def crear_tarea(tarea: Tarea):
#     tareas.append(tarea)
#     return tarea


# # ================= PUT =================
# @app.put("/tareas/{userId}/{taskId}")
# def actualizar_tarea(userId: str, taskId: int, tarea: Tarea):
#     for i, t in enumerate(tareas):
#         if t.id == taskId and t.userId == userId:
#             tareas[i] = tarea
#             return tarea
#     return {"error": "No encontrada"}


# # ================= DELETE =================
# @app.delete("/tareas/{userId}/{taskId}")
# def eliminar_tarea(userId: str, taskId: int):
#     global tareas
#     tareas = [t for t in tareas if not (t.id == taskId and t.userId == userId)]
#     return {"ok": True}

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # 🔥 "DB en memoria" (Render la reinicia a veces)
# tareas = []

# class Tarea(BaseModel):
#     id: int
#     userId: str
#     titulo: str
#     descripcion: str | None = None
#     fechaLimite: str | None = None
#     prioridad: str
#     completada: bool


# # ================= GET POR USUARIO =================
# @app.get("/tareas/{userId}")
# def get_tareas(userId: str):
#     return [t for t in tareas if t.userId == userId]


# # ================= POST =================
# @app.post("/tareas")
# def crear_tarea(tarea: Tarea):
#     tareas.append(tarea)
#     return tarea






# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# tareas = []

# class Tarea(BaseModel):
#     id: int
#     userId: str
#     titulo: str
#     descripcion: str | None = None
#     fechaLimite: str | None = None
#     prioridad: str
#     completada: bool


# @app.get("/tareas/{userId}")
# def get_tareas(userId: str):
#     return [t for t in tareas if t.userId == userId]


# @app.post("/tareas")
# def crear_tarea(tarea: Tarea):
#     tareas.append(tarea)
#     return tarea



from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# "DB" en memoria
tareas = []

# ======================
# MODELO CORRECTO
# ======================
class Tarea(BaseModel):
    id: int
    userId: str
    titulo: str
    descripcion: str | None = None
    fechaLimite: str | None = None
    prioridad: str
    completada: bool

# ======================
# HOME
# ======================
@app.get("/")
def home():
    return {"msg": "API OK"}

# ======================
# GET POR USUARIO
# ======================
@app.get("/tareas/{userId}")
def obtener_tareas(userId: str):
    return [t for t in tareas if t.userId == userId]

# ======================
# POST
# ======================
@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    tareas.append(tarea)
    return {"msg": "ok", "data": tarea}
