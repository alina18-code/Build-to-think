import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

def database_url ():
    url = os.environ.get("DATABASE_URL")
    if not url:
        return "sqlite:///" + (BASE_DIR / "buildtothink.db" ).as_posix()

    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql+psycopg://", 1)
    elif url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+psycopg://", 1)
    return url


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URL = database_url()
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get("FLASK_DEBUG") != "1"

    if not SECRET_KEY:
            raise RuntimeError("SECRET_KEY is not set. Add it to your .env file.")
