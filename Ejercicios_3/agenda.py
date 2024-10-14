agenda={}
while True:
    nombre= input("ingrese nombre (o 'fin' para terminar) ")
    if nombre == "fin":
        break 
    else:
        telefono = input ("ingrese numero de telefono ")
        agenda [nombre] =telefono

print(agenda)
print ("hola")