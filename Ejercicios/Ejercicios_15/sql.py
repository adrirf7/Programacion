import import_db
conexion= import_db.db()
cursor=conexion.cursor()

def crear():
    try:
        
        user_id = int(input("Ingrese el id (a de ser mayor a 9) "))
        user_categoria= input("Ingrese el nombre de la categoria ")

        cursor.execute("insert into categoria values (%s, %s);", (user_id, user_categoria))
        print("operacion relizada con exito")
    except:
        print("--Error-- ingrese un id disponible")
    
def leer():
    cursor.execute("select * from categoria")

    resultados = cursor.fetchall()
    for id, categoria in resultados:
        print(f"id: {id} categoria: {categoria}")
    conexion.commit()

def actualizar():
    try:
        user_id= int(input("Ingrese el id de la categoria que deseas actualizar "))
        user_categoria= input(f"Ingrese el nuevo nombre para la categoria {user_id} ")

        cursor.execute("update categoria set categoria = %s where idcategoria= %s", (user_categoria, user_id,))
        print("operacion relizada con exito")
        conexion.commit()
    except:
        print("--Error-- ingrese un id disponible")

def eliminar():
    try:
        id_user= int(input("Ingrese el id de la categoria que deseas eliminar "))

        cursor.execute("delete from categoria where idcategoria = %s", (id_user,))
        print("operacion relizada con exito")
    except:
        print("--Error-- ingrese un id disponible")