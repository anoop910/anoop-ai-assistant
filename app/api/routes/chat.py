from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas.chat_request import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()


service = ChatService()


@router.post("/chat")
def chat(request: ChatRequest):

    response = service.chat(request.message, request.user_id)

    return StreamingResponse(response, media_type="text/plain")

@router.get("/ok")
def health_checker():
    return "App Running...."
