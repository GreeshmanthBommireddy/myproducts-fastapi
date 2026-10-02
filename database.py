import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

db_url = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:12345678@localhost:5432/fastapi_db")
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
