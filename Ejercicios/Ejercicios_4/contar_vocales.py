vocales=input("Ingrese una cadena de texto ")
def contarVocales(vocal):
    contador=0
    vocales="a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    for caracter in vocal:
        if caracter in vocales: #Recorremos la cadena de text y sumamos 1 al contador por cada vocal
            contador =contador +1
    return contador
print(f"Hay {contarVocales(vocales)} vocales ")

