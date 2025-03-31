import sys
import os
from sqlalchemy.sql import text  # Importar text de sqlalchemy para ejecutar consultas SQL en bruto

# Añadir el directorio src al path para poder importar el módulo connection
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

from database.connection import SessionLocal

db = SessionLocal()
try:
    # Usar text para ejecutar una consulta SQL en bruto
    db.execute(text("SELECT 1"))
    print("✅ Conexión exitosa a MySQL!")
except Exception as e:
    print(f"❌ Error de conexión: {e}")
finally:
    db.close()