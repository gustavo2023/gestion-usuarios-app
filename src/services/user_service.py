import re
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.user import User

# Valida que el email tenga un formato correcto
# Utiliza una expresión regular para verificar el formato del email
def validate_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Función para crear un nuevo usuario en la base de datos
# Recibe una sesión de base de datos y los datos del usuario
def create_user(db: Session, nombre: str, email: str, password: str):
    # Verifica si todos los campos son obligatorios
    # Si falta alguno, lanza una excepción
    if not all([nombre, email, password]):
        raise ValueError("Todos los campos son obligatorios")
    
    # Verifica si el email tiene un formato válido
    # Si no es válido, lanza una excepción
    if not validate_email(email):
        raise ValueError("Formato de email invalido")
    
    # Verifica si el email ya está registrado en la base de datos
    # Si ya está registrado, lanza una excepción
    try:
        user = User(nombre=nombre, email=email, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise ValueError("El email ya esta registrado")