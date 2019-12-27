from fastapi import APIRouter

from tasks.schemas import Item
from tasks.services import TaskService


router = APIRouter()
service = TaskService()


@router.get("/tasks/{item_id}")
async def read_item(item_id: int):
    return service.get_item(item_id)


@router.put("/tasks/{item_id}")
async def update_item(item_id: int):
    return service.update_item(item_id)


@router.post("/tasks/")
async def add_item(item: Item):
    return service.add_item(item)


@router.delete("/tasks/{item_id}")
async def update_item(item_id: int):
    return service.delete_item(item_id)
