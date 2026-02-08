from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory task storage (for now)
tasks = []

# Task model
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: str


@app.get("/")
def root():
    return {"message": "Task Manager API is running"}


# Create task
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        description=task.description,
        completed=False
    )
    tasks.append(new_task)
    return new_task


# Get all tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks


# Get task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Complete task
@app.put("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")