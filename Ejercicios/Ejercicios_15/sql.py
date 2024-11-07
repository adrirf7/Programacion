# Importa la conexión a la base de datos y establece el cursor para ejecutar consultas
import import_db
conexion = import_db.db()
cursor = conexion.cursor()

# Función para insertar una nueva categoría en la tabla
def crear():
    try:
        user_id = int(input("Ingrese el id (debe ser mayor a 9): "))
        user_categoria = input("Ingrese el nombre de la categoría ")
        
        # Inserta la nueva categoría en la base de datos
        cursor.execute("INSERT INTO categoria VALUES (%s, %s);", (user_id, user_categoria))
        print("Operación realizada con éxito")
    except:
        # Muestra un mensaje de error si el ID ya está en uso
        print("--Error-- ingrese un id disponible")

# Función para leer y mostrar todas las categorías de la tabla
def leer():
    cursor.execute("SELECT * FROM categoria")
    resultados = cursor.fetchall()
    
    for id, categoria in resultados:
        print(f"id: {id} categoría: {categoria}")
    conexion.commit()

# Función para actualizar el nombre de una categoría existente
def actualizar():
    try:
        user_id = int(input("Ingrese el id de la categoría que deseas actualizar "))
        user_categoria = input(f"Ingrese el nuevo nombre para la categoría {user_id} ")
        
        # Actualiza el nombre de la categoría en la base de datos
        cursor.execute("UPDATE categoria SET categoria = %s WHERE idcategoria = %s", (user_categoria, user_id))
        print("Operación realizada con éxito")
        conexion.commit()
    except:
        print("--Error-- ingrese un id disponible")

# Función para eliminar una categoría existente por su ID
def eliminar():
    try:
        id_user = int(input("Ingrese el id de la categoría que deseas eliminar "))
        
        # Elimina la categoría de la base de datos
        cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (id_user,))
        print("Operación realizada con éxito")
    except:
        print("--Error-- ingrese un id disponible")
