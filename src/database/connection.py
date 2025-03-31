from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Database connection string
DB_URL = os.getenv("DB_URL")

# Create a new SQLAlchemy engine instance
engine = create_engine(DB_URL, pool_size=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)