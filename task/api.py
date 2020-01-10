from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from task import schemas
from task.services import TaskService


router = APIRouter()
service = TaskService()


@router.get("/tasks/{task_id}",  response_model=schemas.Task)
async def get_task(task_id: int, db: Session = Depends(get_db)):
    return service.get(db=db, task_id=task_id)


@router.get("/tasks", response_model=List[schemas.Task])
async def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db=db, skip=skip, limit=limit)


@router.patch("/tasks/{task_id}", response_model=schemas.Task)
async def patch_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return service.update(db=db, task=task, task_id=task_id)


@router.post("/tasks", response_model=schemas.Task)
async def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return service.add(db=db, task=task)


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    return service.delete(db=db, task_id=task_id)
