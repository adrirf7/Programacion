import sql

def menu():
    opciones_menu={1: "Crear nueva categoría", 2: "Leer categorías existentes", 3: "Actualizar una categoría", 4: "Eliminar una categoría", 5: "Salir"}
    while True:
        print("\n=== Gestión de Categorías ===")
        for numero, opcion in opciones_menu.items():
            print(f"{numero}.- {opcion}")

        try:
            opcion=int(input("\nSeleccione una opción: "))

            if opcion == 1:
                sql.crear()
            
            elif opcion ==2:
                sql.leer()
            
            elif opcion==3:
                sql.actualizar()
            
            elif opcion== 4:
                sql.eliminar()
            else:
                print("Saliendo del programa")
                break
        except:
            print("Ingrese una opcion valida")
