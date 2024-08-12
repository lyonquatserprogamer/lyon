from main import db  # Importa el objeto db desde tu archivo main.py
from main import User, Post  # Importa los modelos que deseas crear
from sqlalchemy.exc import OperationalError

def create_db():
    try:
        # Crear todas las tablas
        db.create_all()
        print("Base de datos creada y tablas iniciales configuradas.")

    except OperationalError as e:
        print(f"Error al crear la base de datos: {e}")

if __name__ == "__main__":
    create_db()