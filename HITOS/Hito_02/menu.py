import crud_sql as sql

def menuPrincipal():
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
        }
        print("\n---Opciones Disponibles---")
        for numero, opcion in opciones.items():
                print(f"{numero}.- {opcion}")
        
        user_input=int(input("Que deseas Hacer: "))
        if user_input == 1:
                sql.leerCatalogo()
