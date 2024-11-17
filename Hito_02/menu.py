import crud_sql as sql

# Menú principal para el inicio de sesión o registro
def inicioUsuario():
    while True:
        try:
            # Opciones iniciales: iniciar sesión o registrarse
            opciones = {
                1: "Inicia Sesion",
                2: "Registrate"
            }
            print("\n---Inicia sesion o registrate---")
            for numero, opcion in opciones.items():
                print(f"{numero}.- {opcion}")

            user_input = int(input("Que deseas Hacer: "))
            if user_input == 2:
                sql.registroUser()  # Llama a la función de registro
                break
            else:
                sql.inicioSesion()  # Llama a la función de inicio de sesión
                break
        except:
            print("Ingrese una opcion valida")

# Menú principal de acciones disponibles para el usuario
def menuAcciones():
    opciones = {
        1: "Ver catalogo",
        2: "Ver carrito",
        3: "Ver pedidos",
        4: "Cerrar Programa"
    }
    
    print("\n---Opciones Disponibles---")
    for numero, opcion in opciones.items():
        print(f"{numero}.- {opcion}")

    user_input = int(input("Que deseas Hacer: "))
    if user_input == 1:
        sql.leerCatalogo()  # Muestra los productos disponibles en el catálogo
    elif user_input == 2:
        menuCompra()  # Abre el menú para gestionar el carrito de compras
    elif user_input == 3:
        sql.leerPedidos()  # Muestra los pedidos realizados por el usuario
    elif user_input == 4:
        print("Cerrando el programa...")
        exit()  # Cierra el programa
    else:
        print("--ERROR--Ingrese una opcion valida")

# Menú para gestionar el carrito de compras
def menuCompra():
    opciones = {
        1: "Comprar prodcutos del carrito",
        2: "Modificar Carrito",
        3: "volver al Menu"
    }
    while True:
        try:
            sql.contenidoCarrito()  # Muestra los productos actualmente en el carrito
            print("\n--Opciones--")
            for numero, opcion in opciones.items():
                print(f"{numero}.- {opcion}")
                                        
            user_input = int(input("Ingrese una opcion: "))
            if user_input == 1:
                sql.crearPedido()  # Finaliza la compra y crea un pedido
            elif user_input == 2:
                menuModificarCarrito()  # Permite modificar el contenido del carrito
            elif user_input == 3:
                menuAcciones()  # Vuelve al menú principal
            else:
                print("Ingrese una opcion valida")
        except:
            print("--ERROR-- Ingrese una opcion valida ")

# Menú para añadir, ver o volver desde el carrito
def menuCarrito():
    opciones = {
        1: "Añadir productos al carrito",
        2: "Ver el carrito",
        3: "Volver a categorias"
    }
    while True:
        try:
            print("\n--Opciones--")
            for numero, opcion in opciones.items():
                print(f"{numero}.- {opcion}")
                                
            user_input = int(input("Que deseas hacer?: "))
            
            if user_input == 1:
                sql.añadirCarrito()  # Agrega un producto al carrito
            elif user_input == 2:
                menuCompra()  # Muestra el contenido del carrito
                break
            elif user_input == 3:
                sql.leerCatalogo()  # Vuelve al catálogo de productos
            else:
                print("--ERROR--Ingresa una opcion valida")    
        except:
            print("--ERROR--Ingrese una opcion valida")

# Menú para modificar los productos dentro del carrito
def menuModificarCarrito():
    opciones = {
        1: "Modificar unidades de un Producto",
        2: "Eliminar un Producto",
        3: "Volver"
    }
    while True:
        try:
            print("\n--Opciones--")
            for numero, opcion in opciones.items():
                print(f"{numero}.- {opcion}")
                                
            user_input = int(input("Que deseas hacer?: "))
            if user_input == 1:
                sql.contenidoCarrito()  # Muestra el contenido del carrito
                sql.modificarUnidadesProducto()  # Modifica la cantidad de un producto
            if user_input == 2:
                sql.contenidoCarrito()  # Muestra el contenido del carrito
                sql.eliminarProductoCarrito()  # Elimina un producto del carrito
            else:
                menuCompra()  # Vuelve al menú de carrito
        except:
            print("--ERROR--Ingrese una opcion valida")

# Menú para ver detalles de pedidos realizados
def menuDetallesPedidos():
    opciones = {
        1: "Ver detalles de un pedido",
        2: "Volver al Menu",
    }
    while True:
        try:
            print("\n--Opciones--")
            for numero, opcion in opciones.items():
                print(f"{numero}.- {opcion}")
                                
            user_input = int(input("Que deseas hacer?: "))
            if user_input == 1:
                sql.leerDetallesPedido()  # Muestra información detallada de un pedido
            elif user_input == 2:
                menuAcciones()  # Vuelve al menú principal
            else:
                print("--ERROR--Ingrese una opcion valida")
        except:
            print("--ERROR--Ingrese una opcion valida")
