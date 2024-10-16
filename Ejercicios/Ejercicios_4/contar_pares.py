lista= input("Ingrese una lista de numeros ")
lista=[int(numero) for numero in lista.split()]

def contar_pares(lista):
    pares=0
    for numero in lista:
        if numero %2 == 0:
            pares += 1
    print(f"La cantidad de pares es: {pares}")

contar_pares(lista)



