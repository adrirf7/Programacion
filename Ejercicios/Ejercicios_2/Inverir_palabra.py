palabra= input("Escribe una palabra ")
palabra_invertida=""

for letra in palabra:
    palabra_invertida = letra + palabra_invertida
print (f"Palabra invertida: {palabra_invertida}")