def ingresarDinero():
    if ingreso <= 0:
        return "--ERROR--Ingrese una cantidad superior a 0 "
    else:
        saldo_actualizado=saldo_user + ingreso
        return saldo_actualizado

def retirarDinero():
    saldo_actualizado= saldo_user-retiro
    return saldo_actualizado 


while True:
    saldo_user= float(input("\nIngrese la cantidad de saldo "))
    if saldo_user<=0:
        print("--ERROR--Ingrese una cantidad superior a 0-- ")
    else:
        break

operaciones ={1: "Ingresar Dinero", 2: "Retirar Dinero", 3: "Mostrar Saldo", 4: "Estadisticas", 5: "Salir"}



while True:
    print("------Operaciones Disponibles------")
    for numero, operacion in operaciones.items():
        print(f"{numero}.- {operacion}")
    user_operacion=int(input("\nIngrese el numero de la operacion que deseas realizar "))
    if (user_operacion> 5 or user_operacion <= 0):
        print("--ERROR--Ingrese una operacion Valida-- ")
    elif user_operacion == 5:
        break
    else:
        if user_operacion == 1:
            ingreso= float(input("Añada la cantidad de dinero que desea Ingresar "))
            print(f"Tu saldo actual es: {ingresarDinero()}\n")
        elif user_operacion == 2:
            retiro= float(input("Añada la cantidad de dinero que desea retirar "))
            print(f"Tu saldo actual es: {retirarDinero()}\n")
