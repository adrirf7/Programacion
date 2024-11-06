import numpy as np  


def escribirMatriz():


    matriz = np.random.randint(1, 11, size=(3, 3))  # Crea una matriz 3x3 con valores aleatorios entre 1 y 10
    try:
        with open("Ejercicios/Ejercicios_13/matriz.txt", "w") as archivo:


            for fila in matriz:
                linea = ",".join(map(str, fila))  # Convierte cada fila en una cadena con valores separados por comas
                archivo.write(linea + "\n")  # Escribe la fila en el archivo y agrega un salto de línea


    except FileNotFoundError:
        print("Archivo no encontrado")  


def leerMatriz():
    try:
        with open("Ejercicios/Ejercicios_13/matriz.txt", "r") as archivo:  
       
            for linea in archivo:
                matriz = np.array([list(map(int, linea.strip().split(",")))])  # Convierte cada línea en una fila de enteros
                print(matriz)  # Imprime cada fila de la matriz
   
    except FileNotFoundError:
        print("Archivo no encontrado")


escribirMatriz()
leerMatriz()
