import bd_connect, getpass, menu
conexion = bd_connect.db()
cursor = conexion.cursor()
id_usuario=None

def registroUser():
        global id_usuario, user
        try:
            print("---Registrate---")
            user= input("Email: ").strip()
            password= getpass.getpass("Contraseña: ").strip()

            cursor.execute("INSERT INTO clientes (correo, password) VALUES (%s, %s)", (user, password))
            conexion.commit()
            print("Usuario registrado correctamente.")

            # Extraemos y asignamos el idCliente a la variable global id_usuario
            cursor.execute("SELECT idCliente FROM clientes WHERE correo = %s", (user,))
            id_usuario = cursor.fetchone()[0]  # Asignamos el id_cliente como global
            return id_usuario  # Devolvemos el id_usuario para que quede asignado

        except:
            print("\n--Usuario ya Existente--")
            redireccion= int(input("Si deseas iniciar sesion introduzca 1 || Si deseas seguir en el registro introduzca 2: "))
            if redireccion == 1:
                inicioSesion()
            else:
                registroUser()

def inicioSesion():
    global id_usuario, user
    try:
        while True:
            print("\n--Inicio de Sesion--")
            user= input("Email: ").strip()
            password= getpass.getpass("Contraseña: ").strip()
            password_db=cursor.execute("SELECT password from clientes where correo = %s", (user,))
            resultado= cursor.fetchone()
            password_db =resultado[0]

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
        redireccion= int(input("Si deseas Registrarte introduzca 1 || Si deseas seguir en el proceso introduzca 2: "))
        if redireccion == 1:
            registroUser()
        else:
            inicioSesion()


def leerCatalogo():
    cursor.execute("Select * from categorias")
    resultado = cursor.fetchall()

    print("\n---Catalogo de Categorias---")
    for numero, categoria in resultado:
        print(f"{numero}.- {categoria}")
    print(f"{numero +1}.-- Volver al Menu ")

    opciones = [num for num, _ in resultado]
    user_input=int(input("Que categoria deseas ver?: "))

    if user_input in opciones:
        cursor.execute("SELECT nombreProducto, precio, stock FROM productos WHERE idCategoria = %s", (user_input,))
        resultado = cursor.fetchall()
        for nombre, precio, stock in resultado:
            print(f"Producto: {nombre} || Precio: {precio} || Stock: {stock}")
        añadirCarrito() 
        
    else:
        menu.menuAcciones() 

def añadirCarrito():

    while True:
        try:
            user_input=menu.menuCarrito()
            
            if user_input== 1:
                producto = (input("Ingrese el nombre del producto que deseas añadir al carrito: "))
                unidades= int(input(f"Ingresa la cantidad de unidades para {producto}: "))

                cursor.execute("SELECT idProducto, precio from productos where nombreProducto=%s", (producto,))
                producto_info = cursor.fetchone()

                if producto_info is None:
                    print(f"--ERROR-- Producto '{producto}' no encontrado.")
                    continue
                
                idProducto, precio_unitario = producto_info
                subtotal = unidades * precio_unitario
                
                # Obtener el carrito del usuario
                cursor.execute("insert into carrito (idCliente, idProducto, cantidad, precioUnitario, subtotal) VALUES (%s, %s, %s, %s, %s)",(id_usuario, idProducto, unidades, precio_unitario, subtotal))

                conexion.commit()
                print(f"Producto {producto} añadido al carrito con {unidades} unidades.")
            
            elif user_input==2:
                leerCatalogo()
                
            elif user_input ==3:
                verCarrito()
                break
                
            else:
                print("--ERROR--Ingresa una opcion valida")
                
        except Exception as e:
            print(f"--ERROR-- Ha ocurrido un error: {e}")

def verCarrito():
    print(f"\n-----Carrito de {user}-----")
    cursor.execute(
        "SELECT productos.nombreProducto, carrito.cantidad, carrito.precioUnitario, carrito.subtotal "
        "FROM carrito JOIN productos ON carrito.idProducto = productos.idProducto "
        "WHERE carrito.idCliente = %s", (id_usuario,)
    )
    items = cursor.fetchall()
    
    total = 0
    for item in items:
        nombre_producto, cantidad, precio_unitario, subtotal = item
        print(f"|| Producto: {nombre_producto} || Unidades: {cantidad} || Precio: {precio_unitario} || Subtotal: {subtotal}")
        total += subtotal

    print(f"\nTotal del Carrito: {total:.2f}")
    
    user_input = menu.menuCompra()
    
    if user_input== 1:
        cursor.execute(
            """
            INSERT INTO Pedidos (idCliente, fechaPedido, totalPedido)
            SELECT idCliente, 
            CURDATE(), -- Fecha actual
            SUM(subtotal) -- Suma de los subtotales de los productos en el carrito
            FROM Carrito
            WHERE idCliente = %s  -- Aquí debes pasar el id del cliente que está realizando el pedido
            GROUP BY idCliente;"""
        )

