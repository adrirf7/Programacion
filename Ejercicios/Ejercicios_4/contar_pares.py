lista= input("Ingrese una lista de numeros ")
lista=[int(numero) for numero in lista.split()] #Convertimos la entrada str del usuario a una cadena separada de int

def contar_pares(lista):
    pares=0
    for numero in lista:
        if numero %2 == 0: #Si el resto es 0 suma 1 al contador de pares
            pares += 1
    print(f"La cantidad de pares es: {pares}")

contar_pares(lista)



