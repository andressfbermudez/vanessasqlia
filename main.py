from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from backend.chat_bot_controller import chat_bot_router

app = FastAPI()

# Configuración de templates
templates = Jinja2Templates(directory="frontend")

# Rutas del admin
app.include_router(chat_bot_router)

# Configuracion de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Para montar correctamente el frontend y poder servirlo
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Gestionar solicitud a la raiz del dominio
@app.get("/")
async def root( request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )
