from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    description: str = None
    category_id: int = None
    is_done: bool


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
