from fastapi import FastAPI

from tasks import api

api_prefix = '/api'

app = FastAPI()

app.include_router(
    api.router,
    prefix=api_prefix
)
