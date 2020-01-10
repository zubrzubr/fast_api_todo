from sqlalchemy.orm import Session

from category import models


class CategoryService(object):
    def get_all(self, db: Session, skip, limit):
        return db.query(models.Category).offset(skip).limit(limit).all()
