# Importa el módulo sql, que contiene las funciones de gestión de la base de datos
import sql

def menuPrincipal():
    # Diccionario de opciones del menú con descripciones de cada acción
    menu_principal={
        1: "Tabla categoria",
        2: "Tabla Clientes",
        3: "Salir"
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
            else:
                print("Saliendo del programa")
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
        1: "Crear nueva categoría",
        2: "Leer categorías existentes",
        3: "Actualizar una categoría",
        4: "Eliminar una categoría",
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

        