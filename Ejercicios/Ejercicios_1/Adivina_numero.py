import random
numero_secreto= random.randint(1,100)
print("----Adivina el numero secreto del 1 al 100----")
while True:
    numero_usuario= int(input("Intenta adivinar el nuemro "))
    if numero_usuario < numero_secreto:
        print ("mas alto")
    elif numero_usuario>numero_secreto:
        print ("Mas bajo")
    else:
        print("¡¡Enorabuena lo has adivinado!!")
        break