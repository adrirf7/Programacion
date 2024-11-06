import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",       # Dirección del servidor (localhost para base de datos local)
    user="root",         # Usuario de la base de datos
    password="curso",  # Contraseña del usuario
    database="animales"    # Nombre de la base de datos
)

cursor= conexion.cursor()
consulta="""
select familia.familia, count(animal.animal) 
from animal
join familia on animal.idfamilia = familia.idfamilia
group by familia.familia;
"""
cursor.execute(consulta)

resultados= cursor.fetchall()
for familia, total in resultados:
   print(f"Familia: {familia}, Total de animales: {total}")

cursor.close()
conexion.close()
