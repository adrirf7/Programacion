import numpy as np  # Importamos la biblioteca NumPy para realizar cálculos numéricos

try:
    # Abrimos el archivo en modo lectura
    with open("Ejercicios/Ejercicios_13/nota_estudiantes.txt", "r") as archivo:
        # Leemos todas las líneas del archivo y las guardamos en una lista
        contenido = archivo.readlines()
        
        # Lista para almacenar las notas de cada estudiante
        notas = []
        for linea in contenido:
            # Eliminamos espacios en blanco y dividimos la línea en una lista de números, convirtiendo cada uno a float
            fila = [float(num) for num in linea.strip().split(",")]
            notas.append(fila)  # Agregamos la fila procesada a la lista 'notas'

        # Convertimos la lista de listas en un array de NumPy
        matriz = np.array(notas)

        # Calculamos la media de cada fila (cada estudiante) usando el eje 1 (filas)
        medias = np.mean(matriz, axis=1)
        
        # Iteramos sobre las medias e imprimimos un mensaje personalizado para cada estudiante
        for i, media in enumerate(medias):
            print(f"Media alumno {i + 1} es: {media:.2f}")  # Usamos i+1 para que empiece en 1 en vez de 0
        
except FileNotFoundError:
    # Capturamos el error en caso de que el archivo no exista y mostramos un mensaje de error
    print("Archivo no encontrado")





