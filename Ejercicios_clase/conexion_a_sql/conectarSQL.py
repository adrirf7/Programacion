import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",       # Dirección del servidor (localhost para base de datos local)
    user="root",         # Usuario de la base de datos
    password="curso",  # Contraseña del usuario
    database="animales"    # Nombre de la base de datos
)
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")

cursor=conexion.cursor()

consulta = """
SELECT ANIMAL.animal, FAMILIA.familia
FROM ANIMAL
JOIN FAMILIA ON ANIMAL.idFamilia = FAMILIA.idfamilia;

"""
cursor.execute(consulta)

resultados = cursor.fetchall()

for animal, familia in resultados:
    print(f"Animal: {animal}, Familia: {familia}")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
