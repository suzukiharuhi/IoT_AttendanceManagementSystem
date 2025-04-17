from fastapi import FastAPI
from app.api import attendance

app = FastAPI()

# ルーティング登録
app.include_router(attendance.router)
