# Importa el módulo sql, que contiene las funciones de gestión de la base de datos
import sql

# Función principal para el menú de opciones de la aplicación
def menu():
    # Diccionario de opciones del menú con descripciones de cada acción
    opciones_menu = {
        1: "Crear nueva categoría",
        2: "Leer categorías existentes",
        3: "Actualizar una categoría",
        4: "Eliminar una categoría",
        5: "Salir"
    }

    while True:
        # Muestra el menú de opciones al usuario
        print("\n=== Gestión de Categorías ===")
        for numero, opcion in opciones_menu.items():
            print(f"{numero}.- {opcion}")

        try:
            # Solicita al usuario seleccionar una opción
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                sql.crear()  
            elif opcion == 2:
                sql.leer()  
            elif opcion == 3:
                sql.actualizar()  
            elif opcion == 4:
                sql.eliminar() 
            else:
                # Opción de salida del programa
                print("Saliendo del programa")
                break
        except:
            # Muestra un mensaje de error si la entrada no es válida
            print("Ingrese una opción válida")
