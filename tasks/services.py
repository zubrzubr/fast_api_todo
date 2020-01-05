from sqlalchemy.orm import Session

from tasks import schemas, models


class TaskService(object):
    def delete(self, item_id):
        return item_id

    def add(self, db: Session, task: schemas.TaskCreate):
        task = models.Task(**task.dict())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def update(self, item_id):
        return item_id

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Task).offset(skip).limit(limit).all()

    def get(self, item_id):
        return item_id
