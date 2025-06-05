from fastapi import APIRouter
from app.schemas.attendance import AttendanceResponse
import sqlite3
from typing import List
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # プロジェクトルート
DB_PATH = BASE_DIR/"data"/"attendance.db"

router = APIRouter()

@router.get("/attendance", response_model=List[AttendanceResponse])
def get_attendance():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    conn.close()

    return [AttendanceResponse(id=row[0], name=row[1], status=row[2], datetime=row[3]) for row in rows]
