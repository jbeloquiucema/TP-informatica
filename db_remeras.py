import sqlite3
DATABASE_NAME = "remeras.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS remeras(
                remera_code INTEGER PRIMARY KEY,
                color TEXT NOT NULL,
                tamaño_letra INTEGER NOT NULL,
                price REAL NOT NULL,
                cantidad INTEGER NOT NULL,
                frase TEXT NOT NULL,
                talle INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
