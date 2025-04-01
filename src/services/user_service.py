import re
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.user import User
from passlib.context import CryptContext
from utils.logger import logger
from functools import wraps

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def transactional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db = kwargs.get('db') or args[0]
        try:
            result = func(*args, **kwargs)
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            raise e
    return wrapper

def validate_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_name(name: str) -> bool:
    """
    Verifica si el nombre es válido.
    Solo permite letras y espacios, incluyendo caracteres acentuados y la letra ñ.
    """
    return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", name))

@transactional
def create_user(db: Session, nombre: str, email: str, password: str):
    logger.info(f"Intentando crear un usuario: {nombre} con email: {email}")
    
    if not all([nombre, email, password]):
        logger.error("Campos vacios al crear usuario")
        raise ValueError("Todos los campos son obligatorios")
    
    if not validate_name(nombre):
        logger.error(f"Nombre inválido: {nombre}")
        raise ValueError("El nombre solo puede contener letras y espacios")
    
    if not validate_email(email):
        logger.error(f"Formato invalido de email: {email}")
        raise ValueError("Formato de email invalido")
    
    if db.query(User).filter(User.email == email).first():
        logger.warning(f"Email ya registrado: {email}")
        raise ValueError("El email ya está registrado")
    
    hashed_password = pwd_context.hash(password)
    user = User(nombre=nombre, email=email, password=hashed_password)
    db.add(user)
    logger.info(f"usuario creado exitosamente: {nombre}")
    return user

def get_all_users(db: Session):
    logger.info("Obteniendo todos los usuarios de la base de datos")
    return db.query(User).order_by(User.id).all()