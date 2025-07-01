
from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config



engine = AsyncEngine(create_engine(
    Config.DB_URI,
    echo=True,
    future=True,
    connect_args={"check_same_thread": False}
))
