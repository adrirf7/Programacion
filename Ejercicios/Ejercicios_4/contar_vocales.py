vocales=input("Ingrese una cadena de texto ")
def contarVocales(vocal):
    contador=0
    vocales_lista="a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    for vocal in vocales:
        if vocal in vocales_lista: #Recorremos la cadena de text y sumamos  contador por cada vocal
            contador =contador +1
    return contador
print(f"Hay {contarVocales(vocales)} vocales ")

