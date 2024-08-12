import sqlite3

def check_tables(db_path):
    try:
        # Conectar a la base de datos
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Listar todas las tablas en la base de datos
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Imprimir las tablas
        if tables:
            print("Tablas en la base de datos:")
            for table in tables:
                print(f" - {table[0]}")
        else:
            print("No hay tablas en la base de datos.")

    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        # Cerrar la conexión
        if connection:
            connection.close()

if __name__ == "__main__":
    db_path = 'site.db'  # Ruta a tu base de datos
    check_tables(db_path)