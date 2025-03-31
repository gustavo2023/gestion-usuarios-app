from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # Updated import
from dotenv import load_dotenv
import os

# Carga variables de entorno desde el archivo .env
load_dotenv()

# Cadena de texto de conexión a la base de datos
DB_URL = os.getenv("DB_URL")

# Se crea una instancia de SQLAlchemy Engine con la URL de la base de datos
# Se establece un tamaño de pool de conexiones y un tiempo de reciclaje
engine = create_engine(DB_URL, pool_size=10, pool_recycle=3600, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para los modelos ORM
Base = declarative_base()  # Updated to use the new import