from fastapi import APIRouter
from api.v1 import path

v1Router = APIRouter()

v1Router.include_router(path.folder_router, prefix="/v1", tags=["v1"])

