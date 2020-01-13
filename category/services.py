from sqlalchemy.orm import Session

from category import models, schemas
from common.services import CrudService


class CategoryService(CrudService):
    model = models.Category

    def add(self, db: Session, category: schemas.CategoryCreate):
        return super(CategoryService, self).add(db, category)
