numero = int(input("Dame un numero positivo "))
if numero < 0:
    print ("Escribe un numero positivo")
else: 
    suma=0
    for i in range (1, numero+1):
        suma = suma+i
print ("la suma de los ", numero, "primeros nuemros es ", suma)