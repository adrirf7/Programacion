# Importa la conexión a la base de datos y establece el cursor para ejecutar consultas
import import_db
conexion = import_db.db()
cursor = conexion.cursor()

# Función para insertar una nueva categoría en la tabla
def crearCategoria():
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
def leerCategoria():
    cursor.execute("SELECT * FROM categoria")
    resultados = cursor.fetchall()
    
    for id, categoria in resultados:
        print(f"id: {id} categoría: {categoria}")
    conexion.commit()

# Función para actualizar el nombre de una categoría existente
def actualizarCategoria():
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
def eliminarCategoria():
    try:
        id_user = int(input("Ingrese el id de la categoría que deseas eliminar "))
        
        # Elimina la categoría de la base de datos
        cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (id_user,))
        print("Operación realizada con éxito")
    except:
        print("--Error-- ingrese un id disponible")

def crearCliente():
    try:
        #Soliditar id Cliente (Solo acepta cadenas <= 5)
        while True: 
            id_cliente = str(input("Ingrese el id del cliente: "))
            if len(id_cliente) <= 5:
                break
            else:
                print("Ingrese un id Valido")
        
        cia= input("Ingrese CIA: ")
        contacto = str(input("Ingrese nombre de contacto: "))
        cargo = str(input("Ingrese cargo: "))
        direccion= input("Ingrese una direccion: ")
        ciudad=("Ingrese una ciudad: ")
        region=("Ingrese region: ")
        cp=input("Ingrese cp: ")
        pais= (input("ingrese Pais: "))
        tlf=int(input("Ingrese numero de telefono: "))
        fax=int(input("Ingrese fax "))
        
        cursor.execute("INSERT INTO CLIENTE values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_cliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax))
        print("Operación realizada con éxito")
    except:
        print("--Error-- Revisa los valores ingresados")

def leerCliente():
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
    
    for id, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax in resultados:
        print(f"id: {id}|| CIA: {cia}|| Contacto: {contacto}|| Cargo: {cargo}|| Direccion: {direccion}|| Ciudad: {ciudad}|| Region: {region}|| CP: {cp}|| Pais: {pais}|| TLF: {tlf}|| Fax: {fax}")
    conexion.commit()

def  actualizarCliente():
    try:
        id_cliente = str(input("Ingrese el id del cliente que Deseas Actualizar: "))
        cia= input("Ingrese CIA: ")
        contacto = str(input("Ingrese nombre de contacto: "))
        cargo = str(input("Ingrese cargo: "))
        direccion= input("Ingrese una direccion: ")
        ciudad=("Ingrese una ciudad: ")
        region=("Ingrese region: ")
        cp=input("Ingrese cp: ")
        pais= (input("ingrese Pais: "))
        tlf=int(input("Ingrese numero de telefono: "))
        fax=int(input("Ingrese fax "))

        cursor.execute("""
   UPDATE cliente
   SET cia = %s, contacto = %s, cargo = %s, direccion = %s, ciudad = %s, 
       region = %s, cp = %s, pais = %s, tlf = %s, fax = %s
   WHERE idcliente = %s
    """, (cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax, id_cliente))
        print("Operacion realizada con exito")
        conexion.commit()
    except:
        print("--ERROR-- Ingrese un id Valido")

def eliminarCliente():
    try: 
        id_cliente = str(input("Ingrese el id del cliente que Deseas Eliminar: "))

        # Elimina la categoría de la base de datos
        cursor.execute("DELETE FROM cliente WHERE idcliente = %s", (id_cliente,))
        print("Operación realizada con éxito")
    except:
        print("Ingrese un id valido")