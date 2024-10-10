numero= int(input("Dame un numero "))
contador=0 
for i in range(1, numero+1):
    if i %2 ==0:
        contador= contador+1
print (contador)
