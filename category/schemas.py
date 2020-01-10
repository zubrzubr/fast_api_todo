from typing import List

from pydantic import BaseModel

from task.schemas import Task


class CategoryBase(BaseModel):
    name: str
    tasks: List[Task] = []


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
