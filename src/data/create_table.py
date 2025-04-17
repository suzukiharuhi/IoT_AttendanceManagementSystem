from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

# SQLiteの.dbファイル（なければ自動で作成される）
engine = create_engine("sqlite:///./attendance.db", echo=True)

# モデルのベース
Base = declarative_base()

# テーブル定義
class Attendance(Base):
    __tablename__ = "attendance"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    datetime = Column(DateTime, default=datetime.now)

# テーブル作成（DBがまだ空ならこれで作られる）
Base.metadata.create_all(bind=engine)
