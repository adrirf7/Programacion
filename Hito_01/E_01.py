def calculoCuadrado(): #Calculo del area del cuadrado
    lado_cuadrado= int(input("Dame el lado del Cuadrado: ")) 
    area=lado_cuadrado ** 2
    perimetro=lado_cuadrado * 4

    for i in range(lado_cuadrado): #Repite la operacion tantas veces como lados ha ingresado el usuario
        print("*  " * lado_cuadrado)    #Imprime tantos "*" por vuelta correspondientes al valor del lado
    print(f"Su area es: {area}") 
    print(f"Su perimetro es: {perimetro}") 

def calculoRectangulo(): #Calculo del area del rectangulo
    base_rectangulo= int(input("Dame la base del Rectangulo: "))
    altura_rectangulo =int(input("Dame la altura del Rectangulo: "))

    area= base_rectangulo * altura_rectangulo
    perimetro= 2* (base_rectangulo + altura_rectangulo)
    
    for i in range(altura_rectangulo): #Debera repetir el proceso tantas veces como corresponda con el valor de Altura
        print("*  " * base_rectangulo) #imprimira tantos "*" como correspondan al valor de la base
    print(f"Su area es: {area}") 
    print(f"Su perimetro es: {perimetro}\n")

def mostrarMenu():
    print("\n-----Menu-----")
    for numero, forma in lista.items(): #Se muestra la lista ordenada y numerada 
        print (f"{numero}.- {forma}") 
    user_input= int(input("Dime una opcion: ")) #Pide al usuario elegir entre las 3 opciones de la lista
    return user_input

lista={1 :"Cuadrado", 2: "Rectangulo", 3: "Salir"} #Diccionario con los elementos que se mostraran en el menu

while True: 
    try: #solo aceptara valores valores numericos 
        user_input=mostrarMenu()  #Llamar a la funcion del menu estableciendo el valor que retorna como user_input
        if user_input not in lista: #Solo se aceptaran valores <=3
            print("--ERROR-- Ingrese una opcion valida")

        elif user_input == 1:
            calculoCuadrado() #Llamar a la funcion del cuadrado

        elif user_input== 2: 
            calculoRectangulo() #Llamar a la funcion del rectangulo
        
        elif user_input== 3: 
            print("Saliendo del programa...")
            break     
    except:
         print("--ERROR---Ingrese una opcion numerica valida ")









