import random

def resultadoJuego(): #Establecemos las reglas del juego
    print(f"\n-----|| Usuario : {victorias_usuario} || Computer: {victorias_computer} ||-----") #Contador de victorias
    user_input = int(input("Elije: 1- Piedra | 2- Papel | 3- Tijera: ")) #Eleccion del usuario
    print(f"-Has elegido: {elementos[user_input]}") #Print de eleccion del usuario
    print(f"-La maquina ha elegido: {elementos[computer]}") #Print de la eleccion de la maquina 
 
    if user_input == computer: #Empate
        return "Empate"
    elif (user_input == 1 and computer== 3 ) or (user_input == 2 and computer == 1) or (user_input == 3 and computer == 2): #Establecemos las condiciones de victoria 
        return "Ganaste"
    else: #Sino solo queda la opcion de derrota
        return "Perdiste"

def resultadoGanador():
    print("------------------------------------------")
    print(f"-----|| Usuario : {victorias_usuario} || Computer: {victorias_computer} ||-----") #Contador victorias
    if victorias_usuario>victorias_computer: 
        print("Has Ganado!!!") 
    else:
        print("Has Perdido...")
    print("------------------------------------------")

elementos={1: "Piedra", 2: "Papel", 3: "Tijera"} #Diccionario en el que se almacena el numero asignado a su valor
victorias_usuario=0
victorias_computer=0

while victorias_usuario <3 and victorias_computer <3 : #Bucle hasta que uno de los dos llegue a 3 victorias
    computer= random.randint(1, 3) #Eleccion de la maquina
    
    try: #Para cuando el ususario introduce un valor valido
        resultado=resultadoJuego()

        if resultado == "Ganaste": 
            victorias_usuario += 1

        elif resultado == "Perdiste":
            victorias_computer += 1

        print (f"{resultado}\n") 

    except: #para cuando el usuario introduce un valor invalido 
        print("Numero invalido")
    
resultadoGanador()
