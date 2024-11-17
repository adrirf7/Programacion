import bd_connect, getpass, random, menu
from datetime import datetime, timedelta

conexion = bd_connect.db()
cursor = conexion.cursor()
id_usuario = None

# Función para registrar un usuario
def registroUser():
        global id_usuario, user
        try:
            print("---Registrate---")
            user = input("Email: ").strip()
            password = getpass.getpass("Contraseña: ").strip()

            # Inserta el usuario en la base de datos
            cursor.execute("INSERT INTO clientes (correo, password) VALUES (%s, %s)", (user, password))
            conexion.commit()
            print("Usuario registrado correctamente.")

            # Extraemos y asignamos el idCliente a la variable global id_usuario
            cursor.execute("SELECT idCliente FROM clientes WHERE correo = %s", (user,))
            id_usuario = cursor.fetchone()[0]  # Asignamos el id_cliente como global
            return id_usuario  # Devolvemos el id_usuario para que quede asignado

        except:
            print("\n--Usuario ya Existente--")
            # Redirige al usuario según su elección
            redireccion = int(input("Si deseas iniciar sesion introduzca 1 || Si deseas seguir en el registro introduzca 2: "))
            if redireccion == 1:
                inicioSesion()
            else:
                registroUser()

# Función para iniciar sesión
def inicioSesion():
    global id_usuario, user
    try:
        while True:
            print("\n--Inicio de Sesion--")
            user = input("Email: ").strip()
            password = getpass.getpass("Contraseña: ").strip()
            
            # Verifica la contraseña en la base de datos
            cursor.execute("SELECT password from clientes where correo = %s", (user,))
            resultado = cursor.fetchone()
            password_db = resultado[0]

            if password == password_db:
                print("Sesion Iniciada Correctamente")
                # Extraemos y asignamos el idCliente a la variable global id_usuario
                cursor.execute("SELECT idCliente FROM clientes WHERE correo = %s", (user,))
                id_usuario = cursor.fetchone()[0]  # Asignamos el id_cliente como global
                return id_usuario  # Devolvemos el id_usuario para que quede asignado
            
            else:
                print("--Contraseña incorrecta. Intentalo de nuevo--")

    except:
        print("\n--El usuario NO existe--")
        # Redirige al usuario según su elección
        redireccion = int(input("Si deseas Registrarte introduzca 1 || Si deseas seguir en el proceso introduzca 2: "))
        if redireccion == 1:
            registroUser()
        else:
            inicioSesion()

# Función para leer el catálogo de categorías
def leerCatalogo():
    # Consulta las categorías disponibles
    cursor.execute("Select * from categorias")
    resultado = cursor.fetchall()

    print("\n---Catalogo de Categorias---")
    for numero, categoria in resultado:
        print(f"{numero}.- {categoria}")
    print(f"{numero + 1}.-- Volver al Menu ") #Añade 1 al ultimo nuemero del indice para volver al menu
    
    while True:
        try:
            opciones = [num for num, _ in resultado]
            user_input = int(input("Que categoria deseas ver?: "))

            if user_input in opciones:
                # Muestra los productos disponibles en la categoría seleccionada
                cursor.execute("SELECT nombreProducto, precio, stock FROM productos WHERE idCategoria = %s", (user_input,))
                resultado = cursor.fetchall()
                for nombre, precio, stock in resultado:
                    print(f"Producto: {nombre} || Precio: {precio} || Stock: {stock}")
                menu.menuCarrito()
                break 
                
            elif user_input == numero + 1:
                # Regresa al menú principal si se elige la última opción
                menu.menuAcciones()
                print("--ERROR--Ingrese una opcion valida")
        except ValueError:
            print("--ERROR--Ingrese una opcion valida")

# Función para añadir productos al carrito
def añadirCarrito():
    while True:
        try: 
            # Solicita el nombre del producto y la cantidad deseada
            producto = (input("Ingrese el nombre del producto que deseas añadir al carrito: ")).strip()
            unidades = int(input(f"Ingresa la cantidad de unidades para {producto}: "))  
            
            # Verifica si el producto existe en la base de datos
            cursor.execute("SELECT idProducto, precio from productos where nombreProducto=%s", (producto,))
            producto_info = cursor.fetchone()
            
            if unidades <= 0:  # Control para evitar añadir cantidades inválidas
                print("--No puedes añadir menos de 1 unidad de producto")
            else:
                if producto_info is None: #Mensaje para cuando el producto no exista
                    print(f"--ERROR-- Producto '{producto}' no encontrado.")
                else:
                    idProducto, precio_unitario = producto_info
                    subtotal = unidades * precio_unitario
                            
                    # Verifica el stock disponible
                    cursor.execute("SELECT stock FROM productos where idProducto = %s", (idProducto,))
                    resultado = cursor.fetchone()
                    stock = resultado[0]
                            
                    if unidades > stock: #Verifica que el usuario no ingrese una cantidad de unidades superior a las del stock
                        print("----Stock insuficiente para las unidades añadidas----")
                    else:
                        # Añade el producto al carrito
                        cursor.execute("insert into carrito (idCliente, idProducto, cantidad, precioUnitario, subtotal) VALUES (%s, %s, %s, %s, %s)", (id_usuario, idProducto, unidades, precio_unitario, subtotal))

                        conexion.commit()
                        print(f"Producto {producto} añadido al carrito con {unidades} unidades.")
                        break
        except:
            print("--ERROR-- Ingrese un numero entero")

# Función para leer el contenido del carrito
def contenidoCarrito():
    print(f"\n-----Carrito de {user}-----")
    # Consulta los productos añadidos al carrito
    cursor.execute(
        "SELECT productos.nombreProducto, carrito.cantidad, carrito.precioUnitario, carrito.subtotal "
        "FROM carrito JOIN productos ON carrito.idProducto = productos.idProducto "
        "WHERE carrito.idCliente = %s", (id_usuario,)
    )
    items = cursor.fetchall()
    
    total = 0
    for nombre_producto, cantidad, precio_unitario, subtotal in items:
        print(f"|| Producto: {nombre_producto} || Unidades: {cantidad} || Precio: {precio_unitario} || Subtotal: {subtotal}")
        total += subtotal

    print(f"\nTotal del Carrito: {total:.2f}")
    
# Función para eliminar un producto del carrito
def eliminarProductoCarrito():
    producto = input("Ingrese el producto que deseas Eliminar: ") 
    
    # Extraer el id del producto
    cursor.execute("SELECT idProducto from productos where nombreProducto=%s", (producto,))
    idProducto = cursor.fetchone()
    if idProducto == None: #Comprueba que el producto existe
        print(f"Producto: {producto} inexistente")
    else:
        # Eliminar el producto del carrito del usuario
        cursor.execute("""
            DELETE FROM carrito
            WHERE idProducto = %s AND idCliente = %s
        """, (idProducto, id_usuario))
        conexion.commit()
        
        print(f" El producto {producto} ha sido eliminado del carrito.")

# Función para modificar las unidades de un producto en el carrito
def modificarUnidadesProducto():
    producto = input("Ingrese el producto que deseas modificar: ") 
    unidades = int(input(f"Ingrese el numero de unidades para {producto}: "))
    
    # Obtener el id del Producto
    cursor.execute("SELECT idProducto from productos where nombreProducto=%s", (producto,))
    idProducto = cursor.fetchone()
    
    # Obtener el precio unitario del producto
    cursor.execute("SELECT precio FROM productos WHERE idProducto = %s", (idProducto,))
    precio_unitario = cursor.fetchone()

    if precio_unitario:
        precio_unitario = precio_unitario[0]
        # Calcular el nuevo subtotal
        nuevo_subtotal = unidades * precio_unitario
    
        # Actualizar el carrito con la nueva cantidad y el nuevo subtotal
        cursor.execute("""
            UPDATE carrito
            SET cantidad = %s, subtotal = %s
            WHERE idProducto = %s AND idCliente = %s
        """, (unidades, nuevo_subtotal, idProducto, id_usuario))
        conexion.commit()
        
        print(f"Cantidad del producto {producto} actualizada a {unidades} unidades.")
    else:
        print(f"Producto con id {producto} no encontrado.")
    
# Función para crear un pedido
def crearPedido():
    fecha_pedido, fecha_entrega = generarFecha()  # Genera fechas de pedido y entrega
    total_pedido = totalPedido()  # Calcula el total del pedido
    
    if total_pedido > 0: #Verifica que no haya añadido productos con 0 unidades
        print("\n-----Menu de Compra-----")
        direccion = input("Ingrese una direccion para el envio: ")
        
        # Inserta el pedido en la tabla de pedidos
        cursor.execute(
            """
            INSERT INTO Pedidos (idCliente, fechaPedido, fechaEntrega, direccionEntrega, totalPedido)
            VALUES (%s, %s, %s, %s, %s)""", (id_usuario, fecha_pedido, fecha_entrega, direccion, total_pedido)
        )
        conexion.commit()
        
        # Obtener el idPedido recién insertado
        cursor.execute("SELECT LAST_INSERT_ID()")
        id_pedido = cursor.fetchone()[0]
        
        # Insertar los detalles del pedido
        cursor.execute("""
            INSERT INTO Detalles_Pedido (idPedido, idProducto, cantidad, precioUnitario, subtotal)
            SELECT 
                %s, 
                idProducto, 
                cantidad, 
                precioUnitario, 
                subtotal
            FROM Carrito
            WHERE idCliente = %s
        """, (id_pedido, id_usuario))
        conexion.commit()
        
        # Actualizar el stock de los productos
        cursor.execute("SELECT idProducto, cantidad from carrito where idCliente=%s", (id_usuario,)) #Selecciona todos los productos, con sus unidades del carrito del usuario
        carrito = cursor.fetchall()
        #Actuializa el stock de cada prodcuto del carrito
        for idProducto, cantidad in carrito:
            cursor.execute("UPDATE productos p set stock = p.stock - %s where idProducto = %s", (cantidad, idProducto))
            conexion.commit()
        
        # Eliminar los productos del carrito tras realizar el pedido
        cursor.execute("DELETE FROM Carrito WHERE idCliente = %s", (id_usuario,))
        conexion.commit()

        print("---Compra realizada con éxito.---")
        print(f"Su pedido será entregado en {fecha_entrega} a la dirección: {direccion}")
    
    else:
        print("---Para poder comprar primero necesitas añadir productos al carrito---")

# Función para generar fechas de pedido y entrega
def generarFecha():
    random_days = random.randint(7, 15)  # Fecha de entrega aleatoria entre una y dos semanas
    random_hour = random.randint(7, 20)  # Horario de entrega entre las 7 am y las 8 pm
    random_minute = random.randint(0, 59)  # Minutos aleatorios para la entrega
    
    fecha_pedido0 = datetime.now()  # Obtiene la hora local al momento del pedido
    fecha_entrega0 = fecha_pedido0 + timedelta(days=random_days)  # Suma los días al día del pedido
    fecha_entrega0 = fecha_entrega0.replace(hour=random_hour, minute=random_minute, second=0)  # Configura hora y minutos
    
    # Formato de fecha compatible con SQL
    fecha_pedido = fecha_pedido0.strftime("%Y-%m-%d %H:%M:%S") 
    fecha_entrega = fecha_entrega0.strftime("%Y-%m-%d %H:%M:%S")

    return fecha_pedido, fecha_entrega

# Función para calcular el total del pedido
def totalPedido():
    # Obtiene los productos en el carrito del usuario
    cursor.execute("""
        SELECT c.cantidad, p.precio
        FROM carrito c
        JOIN productos p ON c.idProducto = p.idProducto
        WHERE c.idCliente = %s
    """, (id_usuario,))
    
    productos_carrito = cursor.fetchall()
    
    if not productos_carrito:  # Si no hay productos, retorna 0
        return 0
    
    total_pedido = 0 
    for cantidad, precio_unitario in productos_carrito:
        subtotal = cantidad * precio_unitario
        total_pedido += subtotal
    
    return total_pedido

# Función para leer los pedidos del usuario
def leerPedidos():
    cursor.execute("""
        SELECT 
            p.idPedido,
            p.fechaPedido,
            p.fechaEntrega,
            p.direccionEntrega,
            p.totalPedido
        FROM 
            Pedidos p
        JOIN 
            Clientes c ON p.idCliente = c.idCliente
        WHERE 
            c.idCliente = %s
    """, (id_usuario,))
    
    resultado = cursor.fetchall()
    print(f"\n-----Pedidos de {user}-----")
    for id, fechaPedido, fechaEntrega, direccion, total in resultado:
        print(f"Pedido ID: {id} || Pedido Realizado el: {fechaPedido} || Fecha de entrega el: {fechaEntrega} || Direccion de entrega: {direccion} || Total: {total}")
    menu.menuDetallesPedidos()

# Función para leer los detalles de un pedido específico
def leerDetallesPedido():
    id_pedido = int(input("Ingrrese el ID del pedido que deseas ver: "))
    cursor.execute("""
        SELECT 
            pr.nombreProducto,
            dp.cantidad,
            dp.precioUnitario,
            dp.subtotal
        FROM 
            Detalles_Pedido dp
        JOIN 
            Productos pr ON dp.idProducto = pr.idProducto
        WHERE 
            dp.idPedido = %s
    """, (id_pedido,))
    resultado = cursor.fetchall()
    
    total = 0
    print(f"\n-----Detalles del pedido {id_pedido}-----")
    for producto, cantidad, precio, subtotal in resultado:
        print(f"Producto: {producto} || Unidades: {cantidad} || Precio: {precio} || Total: {subtotal}") 
        total += subtotal #Suma el precio del producto al subtotal
        
    print(f"\nTotal del pedido: {total}")
