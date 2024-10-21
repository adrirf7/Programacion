def ingresarDinero(saldo_user): #Funcio para ingresar dinero
    ingreso= float(input("Añada la cantidad de dinero que desea Ingresar "))
    if ingreso <= 0:
        return "--ERROR--Ingrese una cantidad superior a 0 "
    else:
        
        return saldo_user + ingreso, ingreso

def retirarDinero(saldo_user): #funcion para sacar dinero
    saldo_actualizado= saldo_user-retiro
    if saldo_actualizado>0:
        return saldo_actualizado
    else:
        return "--ERROR-- No puedes quedarte en negativo"

def saldoInicial():
    while True: #Bucle infinito hasta que el ususario ingrese un valor valido
        try: #Solo seran admitidos valores numericos
            saldo_user= float(input("\nIngrese la cantidad de saldo "))
            if saldo_user>0: #Solo seran admitidos valores superiores a 0
                return saldo_user
            else:
                print("--ERROR-- Ingrese un valor numerico")
                break
        except : #En caso de que el usuario ingrese valores no numericos
            return"--ERROR-- Ingrese un valor numerico"

def mostrarMenu():
    print("------Operaciones Disponibles------")
    for numero, operacion in operaciones.items(): #Muestra las operaciones ordenadas y numeradas
        print(f"{numero}.- {operacion}")
    
operaciones ={1: "Ingresar Dinero", 2: "Retirar Dinero", 3: "Mostrar Saldo", 4: "Estadisticas", 5: "Salir"} #Establecemos las operaciones disponibles 
contador_ingresos, contador_retiradas, ingreso_stats, retiro_stats=0, 0, 0, 0 #contadores para las estadisticas 
saldo_user = saldoInicial()


while True: #Bucle infinito hasta que seleccione la opcion de salir
    mostrarMenu()
    try: #Solo aceptara valores numercios menores a las opciones del menu
        user_operacion=int(input("\nIngrese el numero de la operacion que deseas realizar ")) #Accion que desea hacer el usuario
        
        if user_operacion == 5:
            print("Saliendo del programa...\nGracias por utilizar nuestros servicios")
            break

        elif user_operacion == 1:
            ingresarDinero(saldo_user)
            saldo_user = ingresarDinero(saldo_user) #Se actualiza el valor de saldo_user para futuras operaciones
            ingreso_stats += 
            contador_ingresos += 1 #Se suma uno al contador que se mostrara en la opcion de estadisticas

        elif user_operacion == 2:
            retiro= float(input("Añada la cantidad de dinero que desea retirar "))
            saldo_user =retirarDinero(saldo_user) #Se actualiza el valor de saldo_user para futuras operaciones 
            contador_retiradas += 1
            retiro_stats += retiro

        elif user_operacion == 3: #Mostrar saldo
            print(f"Tu saldo actual es {saldo_user}") #saldo_user es el valor que se actualiza con cada operacion

        elif user_operacion ==4: #Mostrar estadisticas
            print(f"\n-Has realizado {contador_ingresos} ingresos, con un total de {ingreso_stats} €")
            print(f"-Has realizado {contador_retiradas} retiradas, con un valor total de {retiro_stats} €\n")
        
        else:
            print("--ERROR--Ingrese una operacion Valida--\n")
    
    except : #En caso de que el usuario ingrese valores no numericos
            print("--ERROR--Ingrese una operacion Valida--\n")

