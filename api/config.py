import os
import secrets
from typing import Literal
from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_NAME: str = f"AdMrt Chat API - {os.getenv('ENV', 'production').capitalize()}"
    DESCRIPTION: str = "Chat API for AdMrt.com"
    ENV: Literal["development", "staging", "production"] = os.getenv('ENV', 'production')
    VERSION: str = "0.1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DATABASE_URI: str = os.getenv('DATABASE_URI', 'sqlite:///database.db')


settings = Settings()
