from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

from models.Task import Task

app = FastAPI(title="Gestor de Tareas", description="API para gestionar tareas con FastAPI")

# Datos en memoria
tasks = []

# Endpoints
@app.get("/tasks", response_model=List[Task], summary="Obtener todas las tareas")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task, summary="Obtener una tarea por ID")
def get_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@app.post("/tasks", response_model=Task, summary="Crear una nueva tarea")
def create_task(task: Task):
    if any(t["id"] == task.id for t in tasks):
        raise HTTPException(status_code=400, detail="Ya existe una tarea con este ID")
    tasks.append(task.dict())
    return task

@app.put("/tasks/{task_id}", response_model=Task, summary="Actualizar una tarea por ID")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task.dict()
            return updated_task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tasks/{task_id}", status_code=204, summary="Eliminar una tarea por ID")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return None
