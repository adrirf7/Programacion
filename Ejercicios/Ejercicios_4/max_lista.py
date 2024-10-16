entrada= input("Ingrese una lista de numeros separada por espacios ")
entrada = [int(numero) for numero in entrada.split()] # Convertimos la entrada str del usuario a una cadena separada de int

def encontrar_maximo(lista):
    maximo= lista[0]
    for i in lista: # Definimos maximo como el valor en la posicion 0 de la lista
        if i > maximo: # i maximo solo se actualizara si el siguiente numero de la lista es mayor que el
            maximo =i
    print (i)
    
encontrar_maximo(entrada)