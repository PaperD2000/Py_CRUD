import sqlite3

def conectar():
    mi_conexion = sqlite3.connect("CRUDpy")
    cursor = mi_conexion.cursor()

    try:
        sql= """
        CREATE TABLE IF NOT EXISTS Personas(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido TEXT NOT NULL,
            DNI TEXT NOT NULL UNIQUE,
            Edad INTEGER NOT NULL,
            Correo TEXT NOT NULL UNIQUE,
            Direccion TEXT DEFAULT 'No especificado'
            
        )
        """
        cursor.execute(sql)
        return mi_conexion

    except Exception as ex:
        print("Error de conexion:", ex)

    finally:
        cursor.close()
