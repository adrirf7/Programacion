lista= input("Ingrese una lista de numeros separada por espacios ")
lista = [int(numero) for numero in lista.split()]

def encontrar_maximo(lista):
    for i in range(len(lista)):
        if i > lista[0]:
            lista= i
    print (i)
encontrar_maximo(lista)