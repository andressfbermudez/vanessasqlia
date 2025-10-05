from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from backend import chat_bot_service
from backend.database.database_connection import get_db_connection

chat_bot_router = APIRouter()

@chat_bot_router.post("/vanessa-ia/process-prompt")
async def process_prompt_controller(
        request: Request,
        database: Session = Depends(get_db_connection)
):
    # Recibir el JSON enviado desde el frontend
    data = await request.json()
    prompt = data.get("prompt")

    # Llamar al servicio y procesar el prompt
    response = chat_bot_service.process_prompt_service(prompt, database)

    # Retornar la respuesta al frontend
    return JSONResponse(content={"response": response})
