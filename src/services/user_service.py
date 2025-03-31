import re
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.user import User  # Import the User model

def validate_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def create_user(db: Session, nombre: str, email: str, password: str):
    if not all([nombre, email, password]):
        raise ValueError("Todos los campos son obligatorios")
    
    if not validate_email(email):
        raise ValueError("Formato de email invalido")
    
    try:
        user = User(nombre=nombre, email=email, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise ValueError("El email ya esta registrado")