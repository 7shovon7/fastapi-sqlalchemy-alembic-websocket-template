from fastapi import APIRouter

from api.public.chat import router as chat_router
from api.public.ws import router as ws_router


api = APIRouter()


api.include_router(
    chat_router,
    prefix='/chat',
    tags=['Chat'],
)

api.include_router(
    ws_router,
    prefix='/ws',
    tags=['WebSocket'],
)
