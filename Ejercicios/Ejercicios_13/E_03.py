import numpy as np

try:
    with open ("Ejercicios/Ejercicios_13/nota_estudiantes.txt", "r") as archivo:
        contenido= np.loadtxt(archivo)
        print(contenido)
        
except FileNotFoundError:
    print("Archivo no encontrado")


medias= np.mean(contenido, axis=1)
print(medias)


