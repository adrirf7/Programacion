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
#Contador de veces que se realizan las operaciones que se mostraran en la opcion de estadisticas
contador_ingresos=0 
contador_retiradas=0
#Contadores de la cantidad monetatria en ingresos y retiradas que se mostraran en la opcion de estadisticas
ingreso_stats=0 
retiro_stats=0

while True: #Bucle infinito hasta que seleccione la opcion de salir
    print("------Operaciones Disponibles------")
    for numero, operacion in operaciones.items(): #Muestra las operaciones ordenadas y numeradas
        print(f"{numero}.- {operacion}")
    try: #Solo aceptara valores numercios menores a las opciones del menu
        user_operacion=int(input("\nIngrese el numero de la operacion que deseas realizar ")) #Accion que desea hacer el usuario
        
        if user_operacion == 5:
            print("Saliendo del programa...\nGracias por utilizar nuestros servicios")
            break

        elif user_operacion == 1:
            ingreso= float(input("Añada la cantidad de dinero que desea Ingresar "))
            _, saldo_user = ingresarDinero(saldo_user, ingreso) #Se actualiza el valor de saldo_user para futuras operaciones
            ingreso_stats += ingreso
            contador_ingresos += 1 #Se suma uno al contador que se mostrara en la opcion de estadisticas

        elif user_operacion == 2:
            retiro= float(input("Añada la cantidad de dinero que desea retirar "))
            saldo_user, _=retirarDinero(saldo_user, retiro) #Se actualiza el valor de saldo_user para futuras operaciones 
            contador_retiradas += 1
            retiro_stats += retiro

        elif user_operacion == 3: #Mostrar saldo
            print(f"Tu saldo actual es {saldo_user}") #saldo_user es el valor que se actualiza con cada operacion

        else: #Mostrar estadisticas
            print(f"\n-Has realizado {contador_ingresos} ingresos, con un total de {ingreso_stats} €")
            print(f"-Has realizado {contador_retiradas} retiradas, con un valor total de {retiro_stats} €\n")
    
    except : #En caso de que el usuario ingrese valores no numericos
            print("--ERROR--Ingrese una operacion Valida--\n")

