import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User, Base
from services.user_service import create_user, validate_email

TEST_DB_URL = "sqlite:///:memory:"  # Base de datos en memoria

engine = create_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False},
    future=True
)
TestingSessionLocal = sessionmaker(autocommit=False, bind=engine)

@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)  # Crea tablas
    db = TestingSessionLocal()
    yield db  # Entrega la sesión para pruebas
    db.rollback()  # Revierte cambios
    db.close()

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