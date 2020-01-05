from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    description: str = None
    is_done = bool


class Task(TaskBase):
    id = int

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass
