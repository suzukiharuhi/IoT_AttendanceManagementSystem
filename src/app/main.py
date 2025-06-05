from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import attendance

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ReactアプリのURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーティング登録
app.include_router(attendance.router)
