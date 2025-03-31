from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database.connection import Base

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())