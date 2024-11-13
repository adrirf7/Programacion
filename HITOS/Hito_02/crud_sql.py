import bd_connect, getpass, menu
conexion = bd_connect.db()
cursor = conexion.cursor()
id_usuario=None
id_carrito=None

def registroUser():
        global id_usuario
        try:
            print("---Registrate---")
            email= input("Email: ").strip()
            password= getpass.getpass("Contraseña: ").strip()

            cursor.execute("INSERT INTO clientes (correo, contrasela) VALUES (%s, %s)", (email, password))
            conexion.commit()
            print("Usuario registrado correctamente.")

            # Extraemos y asignamos el idCliente a la variable global id_usuario
            cursor.execute("SELECT idCliente FROM clientes WHERE correo = %s", (email,))
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
    global id_usuario
    try:
        while True:
            print("\n--Inicio de Sesion--")
            email= input("Email: ").strip()
            password= getpass.getpass("Contraseña: ").strip()
            password_db=cursor.execute("SELECT contrasela from clientes where correo = %s", (email,))
            resultado= cursor.fetchone()
            password_db =resultado[0]

            if password == password_db:
                print("Sesion Iniciada Correctamente")
                # Extraemos y asignamos el idCliente a la variable global id_usuario
                cursor.execute("SELECT idCliente FROM clientes WHERE correo = %s", (email,))
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

def obtener_o_crear_carrito():
    #Obtiene el carrito existente del usuario o crea uno nuevo si no existe.
    global id_usuario, id_carrito

    # Verifica si el carrito ya existe
    cursor.execute("SELECT idCarrito FROM carrito WHERE idCliente = %s", (id_usuario,))
    carrito = cursor.fetchone()

    if carrito:
        id_carrito = carrito[0]  # Usa el idCarrito existente
        print(f"Carrito existente encontrado con id {id_carrito}.")
    else:
        # Si no existe carrito, se crea uno nuevo
        cursor.execute("INSERT INTO carrito (idCliente) VALUES (%s)", (id_usuario,))
        conexion.commit()
        
        # Recuperamos el idCarrito recién creado
        cursor.execute("SELECT LAST_INSERT_ID()")
        id_carrito = cursor.fetchone()[0]
        print(f"Nuevo carrito creado con id {id_carrito} para el usuario {id_usuario}.")
    
    return id_carrito  # Retorna el id del carrito, ya sea el existente o el nuevo

def añadirCarrito():
    opciones={
        1: "Añadir productos al carrito",
        2: "Volver a categorias",
        3: "Ver el carrito"
    }
    while True:
        print("\n--Opciones--")
        for numero, opcion in opciones.items():
            print(f"{numero}.- {opcion}")
        user_input=int(input("Que deseas hacer?: "))

        if user_input== 1:
            producto = (input("Ingrese el nombre del producto que deseas añadir al carrito: "))
            unidades= int(input(f"Ingresa la cantidad de unidades para {producto}: "))

            cursor.execute("SELECT idProducto from productos where nombreProducto=%s", (producto,))
            idProducto=cursor.fetchone()

            cursor.execute("SELECT precio FROM Productos WHERE nombreProducto = %s", (producto,))
            precio=cursor.fetchone()    
            precio_unitario = precio[0]
            subtotal = unidades*precio_unitario

            # Obtener el carrito del usuario
            cursor.execute("insert into carrito (idCliente, idProducto, cantidad, precioUnitario, subtotal) VALUES (%s, %s, %s, %s, %s)",(id_usuario, idProducto, unidades, precio_unitario, subtotal, id_carrito))

            conexion.commit()
            print(f"Producto {producto} añadido al carrito con {unidades} unidades.")
        
        elif user_input==2:
            leerCatalogo()
        
