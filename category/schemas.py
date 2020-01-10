from typing import List

from pydantic import BaseModel

from task.schemas import Task


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True
