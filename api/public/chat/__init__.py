from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database import get_session
from api.public.chat.crud import get_chats_by_conversation, save_chat
from api.public.chat.shcemas import ChatCreate, ChatRead
from api.utils.logger import logger_config


router = APIRouter()
logger = logger_config(__name__)


@router.get('', response_model=List[ChatRead], status_code=200)
async def get_chats(
    sender_id: str,
    receiver_id: str,
    limit: Optional[int] = 20,
    db: Session = Depends(get_session),
):
    return await get_chats_by_conversation(
        user_id1=sender_id,
        user_id2=receiver_id,
        db=db,
        limit=limit,
    )


@router.post('', response_model=ChatRead, status_code=201)
async def save_the_chat(
    chat: ChatCreate,
    db: Session = Depends(get_session),
):
    return await save_chat(chat=chat, db=db)
