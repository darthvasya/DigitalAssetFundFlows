# database/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

# Настройка подключения
DATABASE_URI = " "
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Функции для работы с БД
def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Экспорт функций и моделей
__all__ = ["init_db", "get_db", "Base", "engine"]
