from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from models.Subtask import Subtask
# Modelo para Tareas
class Task(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)  # Obligatorio, `Field(...)` lo marca como requerido
    completed: bool = False
    priority: Optional[int] = Field(None, ge=1, le=5)
    due_date: Optional[datetime] = None  # Opcional, porque es `Optional` y el valor por defecto es `None`
    category: Optional[str] = None
    subtasks: List[Subtask] = []