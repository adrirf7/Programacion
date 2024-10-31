with open ("Ejercicios/Ejercicios_12/alumnos.txt", "r") as archivo:
    lineas= archivo.readlines()
    for linea in lineas:
        print(linea.strip())