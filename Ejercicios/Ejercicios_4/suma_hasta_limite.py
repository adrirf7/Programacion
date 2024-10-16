entrada= int(input("Ingrese un numero limite "))

def sumaHastaLimite(num):
    limite=0
    for i in range(num+1): # Hacemos un bucle para que sume todos los nuemos hasta el limite
        limite +=i
    print (limite)
sumaHastaLimite(entrada)
