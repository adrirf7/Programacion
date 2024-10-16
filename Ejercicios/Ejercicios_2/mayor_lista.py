lista=[]
while True:
    numeros=input("Ingresa un numero (o escribe 'hecho' para finalizar) ")
    if numeros == "hecho":
        break
    else:
        numero=int(numeros)
        lista.append(numero)

numero_mayor=0
for i in lista:
    if i > numero_mayor:
        numero_mayor=i
print(f"El numero mas alto de la lista es {i}")