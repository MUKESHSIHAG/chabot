from fastapi import FastAPI
from .database import init_db
from .routers import chat

app = FastAPI()

app.include_router(chat.router)

@app.on_event("startup")
def on_startup():
    init_db()
