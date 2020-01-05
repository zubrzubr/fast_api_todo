from fastapi import FastAPI

from database import engine
from task import api, models

api_prefix = '/api'

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(
    api.router,
    prefix=api_prefix
)
