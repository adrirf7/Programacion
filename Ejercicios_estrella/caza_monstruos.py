import random

# Se establece el nivel, el tipo de monstruo y la probabilidad de ser capturado
monstruos = [   
    {"nivel": 1, "especie": "vampiro", "probabilida_captura": 45},
    {"nivel": 2, "especie": "hombre lobo", "probabilida_captura": 40},
    {"nivel": 3, "especie": "bruja", "probabilida_captura": 30},
    {"nivel": 4, "especie": "fantasma", "probabilida_captura": 20},
    {"nivel": 5, "especie": "frankestein", "probabilida_captura": 10},
]

objetos = [
    {"valor": 1, "nombre": "Estaca", "probabilidad_objeto": 50},
    {"valor": 2, "nombre": "Pocion", "probabilidad_objeto": 40},
    {"valor": 3, "nombre": "Hechizo", "probabilidad_objeto": 30}, 
]

intentos = 0
aparicion = random.choice(monstruos)  # Aparición del monstruo

def bienvenida():  # print de bienvenida
    print("\n¡Bienvenido a la caza de monstruos de Halloween!\nIntenta capturar al monstruo")
    print(f"--|| Ha aparecido un {aparicion['especie']} de nivel {aparicion['nivel']} ||--\n")

def captura():
    objeto_user = int(input("--Elige: || 1: Estaca || 2: Pocion magica || 3: Hechizo ||-- "))  # usuario elige objeto
    # Ajustar el índice porque el input comienza desde 1
    objeto = objetos[objeto_user - 1]
    print(f"Has elegido: {objeto['nombre']}\n")

    # Media entre la probabilidad del monstruo y la del objeto usado
    probabilidad_final = (objeto["probabilidad_objeto"] + aparicion["probabilida_captura"]) // 2 

    probabilidad = random.randint(1, 100)  # probabilidad aleatoria para el usuario
    if probabilidad <= probabilidad_final:  # Si el número de probabilidad está dentro del rango de la probabilidad
        return "ganaste", objeto
    else:
        return "perdiste", objeto

def resultadoFinal():  # Mensaje para el resultado en caso de perder
    if intentos == 3:
        print(f"--- Lo siento, no lograste capturar al {aparicion['especie']} ---")

bienvenida()  # llamar a la función de bienvenida
while intentos < 3:
    try:
        resultado, objeto = captura()  # llamar a la función captura
    
        if resultado == "ganaste":  # si gana muestra mensaje y rompe el bucle
            print(f"Felicidades, has capturado un {aparicion["especie"]} con un/a {objeto["nombre"]}")
            break
        else:
            print(f"Tu {objeto["nombre"]} falló en capturar un {aparicion["especie"]}")
            intentos += 1
            print(f"Te quedan {3 - intentos} intentos\n")  # mostrar los intentos restantes

    except (ValueError, IndexError):  # Manejo de excepciones para opciones inválidas
        print("Ingrese una opción válida")

resultadoFinal()  # Muestra el mensaje final en caso de perder
