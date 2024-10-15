numeros= []
while True:
    user_input= int(input("Ingrese un numero (o '0' para terminar) "))
    if user_input == 0:
        break
    else:
        numeros.append(user_input)

media= sum(numeros) / len(numeros)
print (media)
