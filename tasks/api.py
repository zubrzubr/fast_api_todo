from fastapi import APIRouter

from tasks.pydantic_models import Item
from tasks.services import TaskService


router = APIRouter()
service = TaskService()


@router.get("/tasks/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.post("/tasks/")
async def add_item(item: Item):
    return service.add_item(item)
