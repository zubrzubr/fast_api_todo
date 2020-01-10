from sqlalchemy.orm import Session

from category import models, schemas


class CategoryService(object):
    def get_all(self, db: Session, skip, limit):
        return db.query(models.Category).offset(skip).limit(limit).all()

    def add(self, db: Session, category: schemas.Category):
        category = models.Category(**category.dict())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
