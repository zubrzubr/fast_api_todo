from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from task import schemas
from task.schemas import TaskCreate
from task.services import TaskService


router = APIRouter()
service = TaskService()


@router.get("/tasks/{item_id}",  response_model=schemas.Task)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    return service.get(db=db, task_id=task_id)


@router.get("/tasks", response_model=List[schemas.Task])
async def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db=db, skip=skip, limit=limit)


@router.put("/tasks/{item_id}")
async def update_item(item_id: int):
    return service.update(item_id)


@router.post("/tasks/", response_model=schemas.Task)
async def add_item(task: TaskCreate, db: Session = Depends(get_db)):
    return service.add(db=db, task=task)


@router.delete("/tasks/{item_id}")
async def update_item(item_id: int):
    return service.delete(item_id)
