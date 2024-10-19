def ingresarDinero(saldo_user, ingreso):
    if ingreso <= 0:
        return "--ERROR--Ingrese una cantidad superior a 0 "
    else:
        saldo_actualizado = saldo_user + ingreso
        return saldo_actualizado, saldo_actualizado

def retirarDinero(saldo_user, retiro):
    saldo_actualizado= saldo_user-retiro
    if saldo_actualizado>0:
        return saldo_actualizado, saldo_actualizado
    else:
        return "--ERROR-- No puedes quedarte en negativo"


while True: #Bucle infinito hasta que el ususario ingrese un valor valido
    try: #Solo seran admitidos valores numericos
        saldo_user= float(input("\nIngrese la cantidad de saldo "))
        if saldo_user<=0: #Solo seran admitidos valores superiores a 0
            print("--ERROR--Ingrese una cantidad superior a 0-- ")
        else:
            break
    except : #En caso de que el usuario ingrese valores no numericos
        print("--ERROR-- Ingrese un valor numerico")

operaciones ={1: "Ingresar Dinero", 2: "Retirar Dinero", 3: "Mostrar Saldo", 4: "Estadisticas", 5: "Salir"} #Establecemos las operaciones disponibles 
#Contadores de cantidad de veces que se ha ingresado y retirado dinero
contador_ingresos=0
contador_retiradas=0

while True: #Bucle infinito hasta que seleccione la opcion de salir
    print("------Operaciones Disponibles------")
    for numero, operacion in operaciones.items(): #Muestra las operaciones ordenadas y numeradas
        print(f"{numero}.- {operacion}")
    try: #Solo aceptara valores numercios
        user_operacion=int(input("\nIngrese el numero de la operacion que deseas realizar "))
        
        if user_operacion not in operaciones:
            print("--ERROR--Ingrese una operacion Valida-- ")
            continue
        
        elif user_operacion == 5:
            print("Saliendo del programa...")
            break

        elif user_operacion == 1:
            ingreso= float(input("Añada la cantidad de dinero que desea Ingresar "))
            saldo_user, _=ingresarDinero(saldo_user, ingreso)
            contador_ingresos += 1

        elif user_operacion == 2:
            retiro= float(input("Añada la cantidad de dinero que desea retirar "))
            contador_retiradas += 1
            saldo_user, _=retirarDinero(saldo_user, retiro)

        elif user_operacion == 3:
            print(f"Tu saldo actual es {saldo_user}")

        else:
            print(f"-Has realizado {contador_ingresos} ingresos, y {contador_retiradas} retiradas")
    
    except : #En caso de que el usuario ingrese valores no numericos
            print("--ERROR--Ingrese una operacion Valida--\n")

