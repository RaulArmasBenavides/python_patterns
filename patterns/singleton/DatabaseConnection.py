import sqlite3

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creando una nueva conexión a la base de datos.")
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.connection = sqlite3.connect(":memory:")
        return cls._instance

    def get_connection(self):
        return self.connection

# Uso
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print("¿Es la misma conexión?", db1.get_connection() is db2.get_connection())
