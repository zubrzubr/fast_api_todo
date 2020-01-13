from sqlalchemy.orm import Session


class CrudService(object):
    model = None

    def delete(self, db: Session, item_id: int):
        q = db.query(self.model).filter_by(id=item_id).delete()
        db.commit()
        return q

    def add(self, db: Session, schema):
        schema = self.model(**schema.dict())
        db.add(schema)
        db.commit()
        db.refresh(schema)
        return schema

    def update(self, db: Session, schema, item_id: int):
        q = db.query(self.model).filter_by(id=item_id).update(schema)
        if not q:
            return
        db.commit()
        return schema

    def get_all(self, db: Session, skip, limit):
        return db.query(self.model).offset(skip).limit(limit).all()

    def get(self, db: Session, item_id: int):
        return db.query(self.model).filter_by(id=item_id).one_or_none()
