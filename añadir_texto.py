user_input= input("Ingrese el contenido para el diario: ")

with open ("diario.txt", "a") as archivo: #Escribir nueva linea ingresada por el usuario
    archivo.write(f"\n{user_input}")

with open("diario.txt", "r") as archivo: #Leer todo el contenido
    contenido= archivo.read()
    print(f"\n{contenido}")