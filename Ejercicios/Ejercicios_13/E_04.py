import numpy as np  # Importamos la biblioteca NumPy para realizar cálculos numéricos


try:
    # Abrimos el archivo en modo lectura
    with open("Ejercicios/Ejercicios_13/valores.txt", "r") as archivo:
        # Leemos todas las líneas del archivo y las guardamos en una lista
        contenido = archivo.read().splitlines()
        for i in contenido:
            print(i)

        array = np.array([int(i) for i in contenido])

        positivos = [int(i) for i in array if i > 0]
        print (f"Los numeros positivos son: {positivos}")
       
except FileNotFoundError:
    # Capturamos el error en caso de que el archivo no exista y mostramos un mensaje de error
    print("Archivo no encontrado")