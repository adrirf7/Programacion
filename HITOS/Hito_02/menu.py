import crud_sql as sql

def inicioUsuario():
        while True:
                try:
                        opciones={
                                1: "Inicia Sesion",
                                2: "Registrate"
                        }
                        print("\n---Inicia sesion o registrate---")
                        for numero, opcion in opciones.items():
                                print(f"{numero}.- {opcion}")

                        user_input=int(input("Que deseas Hacer: "))
                        if user_input ==2:
                                sql.registroUser()
                                break
                        else:
                                sql.inicioSesion()
                                break
                except:
                        print("Ingrese una opcion valida")
        
def menuAcciones():
        opciones={
                1: "Ver catalogo",
                2: "Ver carrito",
                3: "Ver pedidos"
        }
        while True:
                try:
                        print("\n---Opciones Disponibles---")
                        for numero, opcion in opciones.items():
                                print(f"{numero}.- {opcion}")

                        user_input=int(input("Que deseas Hacer: "))
                        if user_input == 1:
                                sql.leerCatalogo() 
                        elif user_input== 2:
                                sql.verCarrito()
                except:
                        print("--ERROR-- Ingrese una opcion valida ")
        
def menuCompra():
        
        opciones={
                1: "Comprar prodcutos del carrito",
                2: "Modificar Carrito",
                 3: "volver al Menu"
                }
        while True:
                try:
                        print("\n--Opciones--")
                        for numero, opcion in opciones.items():
                                print(f"{numero}.- {opcion}")
                                        
                        user_input= int(input("Ingrese una opcion: "))
                        return user_input
                except:
                        print("--ERROR-- Ingrese una opcion valida ")

def menuCarrito():
        opciones={
        1: "Añadir productos al carrito",
        2: "Volver a categorias",
        3: "Ver el carrito"
        }
        
        while True:
                try:
                        print("\n--Opciones--")
                        for numero, opcion in opciones.items():
                                print(f"{numero}.- {opcion}")
                                
                        user_input=int(input("Que deseas hacer?: "))
                        return user_input
                except:
                        print("--ERROR--Ingrese una opcion valida")

def menuModificarCarrito():
        opciones={
                1: "Modificar unidades de un Producto",
                2: "Eliminar un Producto",
                3: "Volver"
        }
        
        while True:
                try:
                        print("\n--Opciones--")
                        for numero, opcion in opciones.items():
                                print(f"{numero}.- {opcion}")
                                
                        user_input=int(input("Que deseas hacer?: "))
                        return user_input
                except:
                        print("--ERROR--Ingrese una opcion valida")