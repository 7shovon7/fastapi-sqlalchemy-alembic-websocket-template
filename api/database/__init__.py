from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.config import settings


DATABASE_URI = settings.DATABASE_URI
engine = create_engine(DATABASE_URI, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
