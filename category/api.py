from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from category import schemas
from category.services import CategoryService
from database import get_db

router = APIRouter()
service = CategoryService()


@router.get("/categories",  response_model=schemas.Category)
async def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db=db, skip=skip, limit=limit)


@router.post("/categories", response_model=schemas.CategoryCreate)
async def add_task(category: schemas.Category, db: Session = Depends(get_db)):
    return service.add(db=db, category=category)
