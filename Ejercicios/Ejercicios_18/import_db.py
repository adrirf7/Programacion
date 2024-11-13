import pymysql

def db():
    conexion = pymysql.connect(
        host="localhost",       # Dirección del servidor (localhost para base de datos local)
        user="root",         # Usuario de la base de datos
        password="curso",  # Contraseña del usuario
        database="supermercado"    # Nombre de la base de datos
    )
    return conexion