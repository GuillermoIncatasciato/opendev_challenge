from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql+pg8000://postgres:{POSTGRES_PASSWORD}@db/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    return SessionLocal()