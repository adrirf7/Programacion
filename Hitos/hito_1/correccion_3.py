def ingresarDinero(saldo_user): #Funcio para ingresar dinero
        ingreso= float(input("Añada la cantidad de dinero que desea Ingresar "))
        if ingreso > 0:
           return saldo_user + ingreso, ingreso
    
def retirarDinero(saldo_user): #funcion para sacar dinero
        retiro= float(input("Añada la cantidad de dinero que desea retirar "))
        if retiro<=saldo_user:
            return saldo_user - retiro, retiro

def saldoInicial():
    while True: #Bucle infinito hasta que el ususario ingrese un valor valido
        try:
            saldo_user= float(input("\nIngrese la cantidad de saldo "))  

            if saldo_user>0: #Solo seran admitidos valores superiores a 0
                return saldo_user
                
            else:
                print( "--ERROR-- Ingrese un valor numerico")
        except:
             print("--ERROR-- Ingrese un valor numerico")
                

def mostrarMenu():
    print("------Operaciones Disponibles------")
    for numero, operacion in operaciones.items(): #Muestra las operaciones ordenadas y numeradas
        print(f"{numero}.- {operacion}")
    user_operacion=int(input("\nIngrese el numero de la operacion que deseas realizar ")) #Accion que desea hacer el usuario
    return user_operacion

def mostrarEstadisticas():
    print(f"\n-Has realizado {contador_ingresos} ingresos, con un total de {ingreso_stats} €")
    print(f"-Has realizado {contador_retiradas} retiradas, con un valor total de {retiro_stats} €\n")
    
operaciones ={1: "Ingresar Dinero", 2: "Retirar Dinero", 3: "Mostrar Saldo", 4: "Estadisticas", 5: "Salir"} #Establecemos las operaciones disponibles 
contador_ingresos, contador_retiradas, ingreso_stats, retiro_stats=0, 0, 0, 0 #contadores para las estadisticas 
saldo_user = saldoInicial()

while True: #Bucle infinito hasta que seleccione la opcion de salir
    user_operacion=mostrarMenu()
    try:      
        if user_operacion == 5:
                print("Saliendo del programa...\nGracias por utilizar nuestros servicios")
                break

        elif user_operacion == 1:
            nuevo_saldo, ingreso =ingresarDinero(saldo_user) #Llamar a la funcion

            saldo_user = nuevo_saldo #Se actualiza el valor de saldo_user para futuras operaciones
            contador_ingresos += 1 
            ingreso_stats += ingreso
    
        elif user_operacion == 2: 
            nuevo_saldo, retiro = retirarDinero(saldo_user) #Llamar a la funcion

            saldo_user =nuevo_saldo  #Se actualiza el valor de saldo_user para futuras operaciones 
            contador_retiradas += 1
            retiro_stats += retiro

        elif user_operacion == 3: #Mostrar saldo
                print(f"Tu saldo actual es {saldo_user}") #saldo_user es el valor que se actualiza con cada operacion

        elif user_operacion ==4: #Mostrar estadisticas
               mostrarEstadisticas()
            
        else:
                print("--ERROR--Ingrese una operacion Valida--\n")
    except:
         print("--A ocurrido un error-- Por favor no ingreses valores iguales e infieriores a 0, ni retires cantidades superiores a tu saldo\n")

