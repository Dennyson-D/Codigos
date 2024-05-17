from fastapi import FastAPI
from fastapi_pagination import LimitOffsetPage, LimitOffsetParams, add_pagination, paginate
from routers import api_router

app = FastAPI(title = 'WorkoutApi')
app.include_router(api_router)