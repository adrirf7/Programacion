import random

def resultadoJuego(): #Establecemos las reglas del juego
    if user_input == computer:
        return "Empate"
    elif (user_input == 1 and computer== 3 ) or (user_input == 2 and computer == 1) or (user_input == 3 and computer == 2):
        return "Ganaste"
    else:
        return "Perdiste"

elementos={1: "Piedra", 2: "Papel", 3: "Tijera"} #Diccionario en el que se almacena el numero asignado a su valor
victorias_usuario=0
victorias_computer=0


while victorias_usuario <3 and victorias_computer <3 : #Bucle hasta que uno de los dos llegue a 3 victorias
    print(f"\n-----|| Usuario : {victorias_usuario} || Computer: {victorias_computer} ||-----") #Contador de victorias
    
    user_input = int(input("Elije: 1- Piedra | 2- Papel | 3- Tijera: ")) #Eleccion del usuario
    computer= random.randint(1, 3) #Eleccion de la maquina
    
    try: #Para cuando el ususario introduce un valor valido
        print(f"-Has elegido: {elementos[user_input]}") #Print de eleccion del usuario
        print(f"-La maquina ha elegido: {elementos[computer]}") #Print de la eleccion de la maquina 
        if resultadoJuego() == "Ganaste":
            victorias_usuario += 1
        elif resultadoJuego() == "Perdiste":
            victorias_computer += 1

        print (f"{resultadoJuego()}\n") 
    except: #para cuando el ususario introduce un valor superior a 3 
        print("Numero invalido")
    

if victorias_usuario > victorias_computer: #Muestra el mensaje final de victoria o derrota
    print("------------------------------------------")
    print(f"-----|| Usuario : {victorias_usuario} || Computer: {victorias_computer} ||-----")
    print("Has ganado!!!!")
else:
    print("------------------------------------------")
    print(f"-----|| Usuario : {victorias_usuario} || Computer: {victorias_computer} ||-----")
    print("Has perdido...")