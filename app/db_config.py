import os

POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "postgres")
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", "postgres")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+pg8000://{POSTGRES_HOST}:{POSTGRES_PASSWORD}@db/{POSTGRES_DATABASE}"
)
