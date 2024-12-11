from pydantic import BaseModel, Field
# Modelo para Subtareas
class Subtask(BaseModel):
    id: int
    title: str
    completed: bool = False