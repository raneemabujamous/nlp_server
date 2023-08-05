# __init__.py

from fastapi import APIRouter

from .auth.auth import router as routercrawlingBot

api_router = APIRouter()
api_router.include_router(routercrawlingBot)
