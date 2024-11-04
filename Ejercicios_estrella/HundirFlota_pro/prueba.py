import numpy as np

def ubicacionBarcos():
    tablero = np.zeros((20, 20))  # Generamos el tablero real donde se ubicaran los barcos

    # Longitudes de los barcos
    longitudes_barcos = [2, 3, 4]
    
    for longitud in longitudes_barcos:
        while True:
            # Elegimos aleatoriamente la dirección del barco: 0 para horizontal, 1 para vertical
            direccion = np.random.randint(0, 2)
            if direccion == 0:  # Horizontal
                fila = np.random.randint(0, 20)
                columna = np.random.randint(0, 20 - longitud + 1)  # Asegurarse de que quepa
                if np.all(tablero[fila, columna:columna + longitud] == 0):  # Comprobar que no hay superposición
                    tablero[fila, columna:columna + longitud] = 1  # Ubicamos el barco
                    break
            else:  # Vertical
                fila = np.random.randint(0, 20 - longitud + 1)  # Asegurarse de que quepa
                columna = np.random.randint(0, 20)
                if np.all(tablero[fila:fila + longitud, columna] == 0):  # Comprobar que no hay superposición
                    tablero[fila:fila + longitud, columna] = 1  # Ubicamos el barco
                    break

    # Tablero de mentira donde no se muestre la ubicación del barco
    tablero_visible = np.zeros((20, 20))
    
    return tablero, tablero_visible

def bienvenida():  # Mensaje bienvenida
    print("\n¡Bienvenido a la batalla naval!")
    print("Intenta destruir el barco\n")

def UserInput(): 
    print(f"----Intentos: {intentos}----")  # contador intentos
    print(tablero_visible)  # Muestra el tablero de mentira para no revelar la ubicación del barco
    
    ataque_fila = int(input("Ingrese valor fila ")) - 1  # Input de la fila
    ataque_columna = int(input("Ingrese valor columna ")) - 1  # Input de la columna
    return ataque_fila, ataque_columna

# Contadores
def contadores():
    aciertos = 0
    intentos = 0
    return aciertos, intentos

def mensajeFinal():
    print("----El barco ha sido hundido----")
    print(f"Intentos Totales: {intentos}")
    imprimir_tablero(tablero_visible)
    print("------Has ganado------")

# Llamada de funciones
tablero, tablero_visible = ubicacionBarcos() 
aciertos, intentos = contadores()
bienvenida()

while aciertos < 1:  # Mientras que el contador sea 0
    try:
        ataque_fila, ataque_columna = UserInput()  # Llamada a la función del input

        # Comprobación 
        if tablero[ataque_fila, ataque_columna] == 1:  # Comprueba si en la ubicación del usuario hay un 1 (barco)
            tablero_visible[ataque_fila, ataque_columna] = 2  # Si acierta reemplaza la casilla por un 2
            aciertos += 1
            intentos += 1
            print(f"\nEn la casilla {ataque_fila + 1, ataque_columna + 1} Se encuentra el barco. Tocado\n")
        else:
            print(f"\nEn la casilla {ataque_fila + 1, ataque_columna + 1} No hay nada. Agua\n")
            tablero_visible[ataque_fila, ataque_columna] = -1  # Muestra un -1 en la casilla donde no hay barco
            intentos += 1
    except ValueError:  # Específico para la captura de errores de tipo
        print("--ERROR-- Ingrese un número válido")
    except IndexError:  # Captura errores de índice
        print("--ERROR-- Las coordenadas deben estar entre 1 y 20")

mensajeFinal()
