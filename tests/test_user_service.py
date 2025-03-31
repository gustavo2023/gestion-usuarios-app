import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User, Base
from services.user_service import create_user, validate_email, get_all_users

TEST_DB_URL = "sqlite:///:memory:"  # Base de datos en memoria

engine = create_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False},
    future=True
)
TestingSessionLocal = sessionmaker(autocommit=False, bind=engine)

@pytest.fixture
def test_db():
    # Recrear el esquema de la base de datos para cada prueba
    Base.metadata.drop_all(bind=engine)  # Eliminar tablas existentes
    Base.metadata.create_all(bind=engine)  # Recrear tablas
    db = TestingSessionLocal()
    yield db  # proveer la sesión a la prueba
    db.rollback()  # Rollback cualquier cambio realizado durante la prueba
    db.close()  # Cerrar la sesión después de la prueba

def test_create_user_valid(test_db):
    user = create_user(test_db, "Ana", "ana@example.com", "pass123")
    assert user.id is not None  # Verifica que se asignó un ID

@pytest.mark.parametrize("email,expected", [
    ("test@example.com", True),
    ("invalid-email", False),
    ("another@bad", False),
    ("missing@dotcom", False)
])
def test_validate_email(email, expected):
    assert validate_email(email) == expected

def test_create_user_empty_fields(test_db):
    with pytest.raises(ValueError) as exc_info:
        create_user(test_db, "", "ana@example.com", "pass123")
    
    assert "obligatorios" in str(exc_info.value)

def test_get_all_users(test_db):
    create_user(test_db, "Ana", "ana@example.com", "pass123")
    create_user(test_db, "Bob", "bob@example.com", "pass456")
    users = get_all_users(test_db)
    assert len(users) == 2