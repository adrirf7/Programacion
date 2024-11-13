# Importa la conexión a la base de datos y establece el cursor para ejecutar consultas
import import_db
from datetime import datetime, timedelta
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
    
def crearPedido():
    try:
        pedido_id = int(input("Ingrese el id del pedido: "))
        idCliente = input("Ingrese el id del cliente: ")
        fecha_pedido0 = datetime.now()
        fecha_entrega0= fecha_pedido0 + timedelta(days=2)

        fecha_pedido= fecha_pedido0.strftime("%Y-%m-%d %H:%M:%S")
        fecha_entrega = fecha_entrega0.strftime("%Y-%m-%d %H:%M:%S") 
        
        # Inserta la nueva categoría en la base de datos
        cursor.execute("INSERT INTO PEDIDO VALUES (%s, %s, %s, %s);", (pedido_id, idCliente, fecha_pedido, fecha_entrega ))
        print("Operación realizada con éxito")
    except:
        # Muestra un mensaje de error si el ID ya está en uso
        print("--Error-- ingrese un id disponible")

def leerPedido():
    cursor.execute("SELECT * FROM PEDIDO")
    resultados= cursor.fetchall()

    for idPedido, idCliente, fechaPedido, fechaEntrega in resultados:
        print(f"idPEdido: {idPedido} || idCliente: {idCliente} || fechaPedido: {fechaPedido} || fechaEntrega {fechaEntrega}")

def actualizarPedido():
    try:
        id_pedido = int(input("Ingrese el id del pedido que deseas actualizar "))
        id_cliente = input(f"Ingrese el nuevo cliente para el pedido {id_pedido} ")
        fecha_pedido= input("Ingrese la fecha de peido: (A/M/D h/m/s):  ")
        fecha_entrega= input("Ingrese la fecha de entrega: (A/M/D h/m/s): ")

        # Actualiza el nombre de la categoría en la base de datos
        cursor.execute("UPDATE PEDIDO SET idcliente = %s, fechapedido =%s, fechaentrega= %s, WHERE idpedido = %s", (id_pedido, id_cliente, fecha_pedido, fecha_entrega))
        print("Operación realizada con éxito")
        conexion.commit()
    except:
        print("--Error-- ingrese un id disponible")

def eliminarPedido():
    try: 
        id_pedido = str(input("Ingrese el id del pedido que Deseas Eliminar: "))

        # Elimina la categoría de la base de datos
        cursor.execute("DELETE FROM PEDIDO WHERE idpedido = %s", (id_pedido,))
        print("Operación realizada con éxito")
    except:
        print("Ingrese un id valido")
