def areaCuadrado(area): #Calculamos el area del cuadrado
    num=lado_cuadrado ** 2
    return num

def perimetroCuadrado(perimetro): #Calculamos su perimetro
    num=lado_cuadrado * 4
    return num

def areaRectangulo(area): #Calculo area del rectangulo
    num= base_rectangulo * altura_rectangulo
    return num

def perimetroRectangulo(perimetro): #Calculo perimetro del rectangulo
    num= 2* (base_rectangulo + altura_rectangulo)
    return num

lista=["Cuadrado", "Rectangulo", "Salir"] #Lista con los elementos que se mostraran en el menu
print("-----Menu-----")
for i in range(len(lista)): #Se muestra la lista ordenada y numerada 
    print (f"{i+1}.- {lista[i]}") #Sumamos 1 a i para que empiece la lista en 1

while True:
    user_input= int(input("Dime una opcion: "))
    if user_input == 1:
        lado_cuadrado= int(input("Dame el lado del Cuadrado: "))
        for numeros in range(lado_cuadrado):
            print("*  " * lado_cuadrado)    
        print(f"Su area es {areaCuadrado(lado_cuadrado)}")
        print(f"Su perimetro es {perimetroCuadrado(lado_cuadrado)}")
    elif user_input== 2: 
        base_rectangulo= int(input("Dame la base del Rectangulo: "))
        altura_rectangulo =int(input("Dame la base del Rectangulo: "))
        
        for numeros in range(altura_rectangulo):
            print("* " * base_rectangulo)
        print(f"Su area es {areaRectangulo(base_rectangulo)}")
        print(f"Su perimetro es {perimetroRectangulo(base_rectangulo)}")
    elif user_input== 3:
        print("Saliendo del programa...")
        break     
    else:
        print("Ingrese una opcion valida ")









