from pydantic import BaseModel


class TaskBase(BaseModel):
    id: int
    name: str
    description: str = None
    is_done = bool


class Task(TaskBase):
    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass
