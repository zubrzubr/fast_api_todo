from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from tasks import schemas
from tasks.schemas import TaskCreate
from tasks.services import TaskService


router = APIRouter()
service = TaskService()


@router.get("/tasks/{item_id}")
async def read_item(item_id: int):
    return service.get(item_id)


@router.get("/tasks")
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
