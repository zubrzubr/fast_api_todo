from sqlalchemy.orm import Session

from common.services import CrudService
from task import schemas, models


class TaskService(CrudService):
    model = models.Task

    def add(self, db: Session, task: schemas.TaskCreate):
        return super(TaskService, self).add(db, task)

    def update(self, db: Session, task: schemas.TaskCreate, task_id: int):
        return super(TaskService, self).update(db, task, task_id)
