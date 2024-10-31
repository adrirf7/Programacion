import numpy as np

array = np.random.randint(1,101, size = 10) #array de numeros aleatorios
try:
    with open ("Ejercicios/Ejercicios_13/numeros.txt", "w") as archivo:
        for numeros in array: #Escribimos cada numero del array con un salto de liena
            archivo.write(f"{numeros}\n")

except FileNotFoundError:
    print("El archivo no ha sido encontrado")

try:
    with open ("Ejercicios/Ejercicios_13/numeros.txt", "r") as archivo:
        contenido= archivo.read() #Lee el contenido de nuemeros.txt
        array_copntendio=np.array(contenido) #Mete el contenido en un array
        print(contenido) #Muestra el contenido

except FileNotFoundError:
    print("Archivo no encontrado")
        
