def areaCuadrado(area): #Calculo del area del cuadrado
    num=lado_cuadrado ** 2
    return num

def perimetroCuadrado(perimetro): #Calculo del perimetro
    num=lado_cuadrado * 4
    return num

def areaRectangulo(area): #Calculo del area del rectangulo
    num= base_rectangulo * altura_rectangulo
    return num

def perimetroRectangulo(perimetro): #Calculo perimetro del rectangulo
    num= 2* (base_rectangulo + altura_rectangulo)
    return num

lista=["Cuadrado", "Rectangulo", "Salir"] #Lista con los elementos que se mostraran en el menu

while True: #Bucle infinito para mostrar consantemente el menu y pedir una opcion al usuario hasa que inserte 3
    print("-----Menu-----")
    for i in range(len(lista)): #Se muestra la lista ordenada y numerada 
        print (f"{i+1}.- {lista[i]}") #Sumamos 1 a i para que empiece la lista en 1

    user_input= int(input("Dime una opcion: ")) #Pide al usuario elegir entre las 3 opciones de la lista
    if user_input == 1:
        lado_cuadrado= int(input("Dame el lado del Cuadrado: ")) #Solicita el valor para el lado del cuadrado
        for numeros in range(lado_cuadrado): #Repite la operacion tantas veces como lados ha ingresado el usuario
            print("*  " * lado_cuadrado)    #Imprime tantos "*" por vuelta correspondientes al valor del lado
        print(f"Su area es: {areaCuadrado(lado_cuadrado)}") #Llama a la funcion para mostrar por pantalla el valor del Area
        print(f"Su perimetro es: {perimetroCuadrado(lado_cuadrado)}") #Llama a la funcion para mostrar por pantalla el valor del Perimetro
    elif user_input== 2: #Mismo procedimiento que con el cuadrado pero añadiendo la variable de Altura
        base_rectangulo= int(input("Dame la base del Rectangulo: "))
        altura_rectangulo =int(input("Dame la base del Rectangulo: "))
        
        for numeros in range(altura_rectangulo): #Debera repetir el proceso tantas veces como corresponda con el valor de Altura
            print("* " * base_rectangulo) #imprimira tantos "*" como correspondan al valor de la base
        print(f"Su area es: {areaRectangulo(base_rectangulo)}") 
        print(f"Su perimetro es: {perimetroRectangulo(base_rectangulo)}")
    elif user_input== 3: #Si el valor ingresado es 3 el programa sale del bucle
        print("Saliendo del programa...")
        break     
    else: #Si no se ha ingresado ningun valor del 1 al 3 pide al ususario que ingrese un numero valido
        print("ERROR---Ingrese una opcion valida ")









