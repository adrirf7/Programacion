# Importa el módulo sql, que contiene las funciones de gestión de la base de datos
import sql

def menuPrincipal():
    # Diccionario de opciones del menú con descripciones de cada acción
    menu_principal={
        1: "Tabla categoria",
        2: "Tabla Clientes",
        3: "Tabla Pedidos",
        4: "Tabla Detalles",
        5: "Salir"
    }
    while True:
        print("\n=== Tablas Disponibles ===")
        for numero, opcion in menu_principal.items():
            print(f"{numero}.- {opcion}")
        try:
            tabla=int(input("Que tabla deseas modificar?: "))
            
            if tabla ==1:
                menuCategoria() #Llama al menu categoria
                break
            
            elif tabla==2:
                menuCliente() #llama al menu cliente
                break
            elif tabla==3:
                menuPedido()
                break
            elif tabla ==4:
                menuDetalle()
            else:
                print("Saliendo del programa...")
                break
        except:
                print("Ingrese una tabla valida")


def menuCategoria():
    opciones_menu = {
        1: "Crear nueva categoría",
        2: "Leer categorías existentes",
        3: "Actualizar una categoría",
        4: "Eliminar una categoría",
        5: "Volver a la seleccion de tablas"
    }
    #Menu de opciones para las tablas de la base de datos
 
    while True:
            # Muestra el menú de opciones al usuario
            print("\n=== Gestión Tabla Categoria ===")
            for numero, opcion in opciones_menu.items():
                print(f"{numero}.- {opcion}")

            try:
                # Solicita al usuario seleccionar una opción
                opcion = int(input("\nSeleccione una opción: "))

                if opcion == 1:
                    sql.crearCategoria()  
                elif opcion == 2:
                    sql.leerCategoria()  
                elif opcion == 3:
                    sql.actualizarCategoria()  
                elif opcion == 4:
                    sql.eliminarCategoria() 
                else:
                    menuPrincipal() #Volver al menu principal
                    break
            except:
                # Muestra un mensaje de error si la entrada no es válida
                print("Ingrese una opción válida")
    
def menuCliente():
    opciones_menu = {
        1: "Crear un nuevo cliente",
        2: "Leer clientes existentes",
        3: "Actualizar un cliente",
        4: "Eliminar un cliente",
        5: "Volver a la seleccion de tablas"
    }
    #Menu de opciones para las tablas de la base de datos
    while True:
        print("\n=== Gestión Tabla Cliente ===")
        for numero, opcion in opciones_menu.items():
            print(f"{numero}.- {opcion}")
            
        try:
            # Solicita al usuario seleccionar una opción
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                sql.crearCliente()  
            elif opcion == 2:
                sql.leerCliente()  
            elif opcion == 3:
                sql.actualizarCliente()  
            elif opcion == 4:
                sql.eliminarCliente() 
            else:
                menuPrincipal() #Volver al menu principal
                break
        except:
            # Muestra un mensaje de error si la entrada no es válida
            print("Ingrese una opción válida")

def menuPedido():
    opciones_menu = {
        1: "Crear nuevo pedido",
        2: "Leer pedidos existentes",
        3: "Actualizar un pedido",
        4: "Eliminar un pedido",
        5: "Volver a la seleccion de tablas"
    }
    #Menu de opciones para las tablas de la base de datos
    while True:
        print("\n=== Gestión Tabla Pedidos ===")
        for numero, opcion in opciones_menu.items():
            print(f"{numero}.- {opcion}")
    
        try:
            # Solicita al usuario seleccionar una opción
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                sql.crearPedido()  
            elif opcion == 2:
                sql.leerPedido()  
            elif opcion == 3:
                sql.actualizarPedido()  
            elif opcion == 4:
                sql.eliminarPedido() 
            else:
                menuPrincipal() #Volver al menu principal
                break
        except:
            # Muestra un mensaje de error si la entrada no es válida
            print("Ingrese una opción válida")


        