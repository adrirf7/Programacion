canciones = []
while True: 
    user_input = input ("Ingresa el nombre de la canción (o 'fin' para terminar) ")
    if user_input == "fin":
        break 
    else:
        canciones.append(user_input)

print("-----tu lista de reproduccion:------")
for i in range(len(canciones)):
    print (f"{i}.- {canciones[i]}")

reproduccion = int(input("Ingrese una cancion para reproducir "))

if reproduccion > i:
    print("cancion invalida")
else:
    print(f"Reproduciendo: {canciones[reproduccion]}")
