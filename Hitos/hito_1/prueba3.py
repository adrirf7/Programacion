def actualizar_saldo(saldo, monto, operacion):  # Función para actualizar el saldo
    if monto <= 0:
        return f"--ERROR-- Ingrese una cantidad superior a 0"
    nuevo_saldo = saldo + (monto if operacion == 'ingreso' else -monto)
    if nuevo_saldo < 0:
        return "--ERROR-- No puedes quedarte en negativo"
    return nuevo_saldo

def obtener_saldo_inicial():  # Función para solicitar saldo inicial
    while True:
        try:
            saldo = float(input("\nIngrese la cantidad de saldo: "))
            if saldo > 0:
                return saldo
            print("--ERROR-- Ingrese una cantidad superior a 0--")
        except ValueError:
            print("--ERROR-- Ingrese un valor numérico")

operaciones = {1: "Ingresar Dinero", 2: "Retirar Dinero", 3: "Mostrar Saldo", 4: "Estadísticas", 5: "Salir"}  # Menú de operaciones

# Inicialización de contadores
saldo_user = obtener_saldo_inicial()
contador_ingresos, contador_retiradas, ingreso_stats, retiro_stats = 0, 0, 0, 0

while True:
    print("\n------ Operaciones Disponibles ------")
    for numero, operacion in operaciones.items():
        print(f"{numero}.- {operacion}")

    try:
        user_operacion = int(input("\nIngrese el número de la operación que deseas realizar: "))

        if user_operacion == 5:
            print("Saliendo del programa...\nGracias por utilizar nuestros servicios")
            break

        if user_operacion == 1:  # Ingresar dinero
            ingreso = float(input("Añada la cantidad de dinero que desea ingresar: "))
            resultado = actualizar_saldo(saldo_user, ingreso, 'ingreso')
            if isinstance(resultado, str):  # Mensaje de error
                print(resultado)
            else:
                saldo_user = resultado
                ingreso_stats += ingreso
                contador_ingresos += 1

        elif user_operacion == 2:  # Retirar dinero
            retiro = float(input("Añada la cantidad de dinero que desea retirar: "))
            resultado = actualizar_saldo(saldo_user, retiro, 'retiro')
            if isinstance(resultado, str):  # Mensaje de error
                print(resultado)
            else:
                saldo_user = resultado
                retiro_stats += retiro
                contador_retiradas += 1

        elif user_operacion == 3:  # Mostrar saldo
            print(f"Tu saldo actual es {saldo_user:.2f} €")

        elif user_operacion == 4:  # Mostrar estadísticas
            print(f"\n- Has realizado {contador_ingresos} ingresos, con un total de {ingreso_stats:.2f} €")
            print(f"- Has realizado {contador_retiradas} retiradas, con un total de {retiro_stats:.2f} €\n")
        
        else:
            print("--ERROR-- Ingrese una operación válida--\n")

    except ValueError:  # En caso de que el usuario ingrese valores no numéricos
        print("--ERROR-- Ingrese una operación válida--\n")
