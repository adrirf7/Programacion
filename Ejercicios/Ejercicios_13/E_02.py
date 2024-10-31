import numpy as np

def calculoEstadisticas():
    """Calcula e imprime la media, máxima y mínima de las temperaturas en el array `contenido`."""
    # Calcular la media de las temperaturas
    media_temperaturas = np.mean(contenido)
    print(f"\nLa temperatura media es de {media_temperaturas:.2f}ºC")  # Mostrar con 2 decimales

    # Calcular la temperatura más alta
    temperatura_alta = np.max(contenido)
    print(f"La temperatura máxima es de {temperatura_alta:.2f}ºC")  # Mostrar con 2 decimales

    # Calcular la temperatura más baja
    temperatura_minima = np.min(contenido)
    print(f"La temperatura mínima es de {temperatura_minima:.2f}ºC")  # Mostrar con 2 decimales

# Intentar abrir el archivo y cargar las temperaturas
try:
    with open("Ejercicios/Ejercicios_13/temperaturas.txt", "r") as archivo:
        # Leer todas las temperaturas del archivo en un array de Numpy
        contenido = np.loadtxt(archivo)
        print(contenido)  # Imprimir las temperaturas cargadas para verificación

# Manejo de error si el archivo no se encuentra
except FileNotFoundError:
    print("Archivo no encontrado.")

# Llamar a la función para calcular y mostrar las estadísticas de temperaturas
calculoEstadisticas()


