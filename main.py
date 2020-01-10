from fastapi import FastAPI

from database import engine
from task import models as task_models
from task import api as task_api
from category import models as category_models
from category import api as category_api

api_prefix = '/api'

app = FastAPI()

task_models.Base.metadata.create_all(bind=engine)
category_models.Base.metadata.create_all(bind=engine)


app.include_router(
    task_api.router,
    prefix=api_prefix
)
app.include_router(
    category_api.router,
    prefix=api_prefix
)
