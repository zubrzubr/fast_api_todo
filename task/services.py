from sqlalchemy.orm import Session

from task import schemas, models


class TaskService(object):
    def delete(self, db: Session, task_id: int):
        q = db.query(models.Task).filter_by(id=task_id).delete()
        db.commit()
        return q

    def add(self, db: Session, task: schemas.Task):
        task = models.Task(**task.dict())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def update(self, db: Session, task: schemas.Task, task_id: int):
        q = db.query(models.Task).filter_by(id=task_id).update(task)
        if not q:
            return
        db.commit()
        return task

    def get_all(self, db: Session, skip, limit):
        return db.query(models.Task).offset(skip).limit(limit).all()

    def get(self, db: Session, task_id: int):
        return db.query(models.Task).filter_by(id=task_id).one_or_none()
