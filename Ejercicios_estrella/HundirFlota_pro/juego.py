import numpy as np

def ubicacionBarco():
    tablero= np.zeros((20, 20)) #generamos el tablero real donde se ubicara el barco

    longitud_barcos=[2,3,4]

    for longitud in longitud_barcos:
        while True:
            orientacion = np.random.randint(0,2)

            if orientacion ==1:
                fila = np.random.randint(0,21) 
                columna = np.random.randint (0,21 - longitud) 
                
                if np.all(tablero[fila, columna: columna + longitud] == 0):
                    tablero [fila-1, columna-1: columna-1 + longitud] = 1
                    print(fila, columna, longitud, orientacion)
                    break
            
            else:
                fila = np.random.randint(0,21) 
                columna = np.random.randint (0,21 - longitud) 

                if np.all(tablero[fila, columna: columna + longitud] == 0):
                    tablero [fila-1: fila + longitud-1, columna-1] = 1
                    print(fila, columna, longitud, orientacion)
                    break

    #Tablero de mentira donde no se muestre la ubicacion del barco
    tablero_visible= np.zeros((20, 20), dtype=int)
    
    return tablero, tablero_visible

def bienvenida(): #Mensaje bienvenida
    print("\n¡Bienvenido a la batalla naval!")
    print("Intenta destruir el barco\n")
    
def UserInput(): 
    
    print(f"----Intentos: {intentos}----") #contador intentos
    for fila in tablero_visible:
        print("  ".join(str(int(i)) for i in fila))  # Muestra el tablero final
    ataque_fila= int(input("Ingrese valor fila ")) -1 #Input de la fila
    ataque_columna= int(input("Ingrese valor columna ")) -1 #Input de la columna
    return ataque_fila, ataque_columna

#contadores
def contadores():
    aciertos=0
    intentos=0
    return aciertos, intentos

def mensajeFinal():
    print("----El barco ha sido hundido----")
    print(f"Intentos Totales: {intentos}")
    print(tablero_visible)
    print ("------Has ganado------")

#llamada de funciones
tablero, tablero_visible= ubicacionBarco() 
aciertos, intentos=contadores()
bienvenida()

while aciertos< 9: #mientras que el contador sea 0
    try:
        ataque_fila, ataque_columna = UserInput() #llamada a la funcion del input

        #comprobacion 
        if tablero[ataque_fila, ataque_columna]==1: #comprueba si en la ubicacion del usuario hay un 1 (barco)
            tablero_visible[ataque_fila, ataque_columna]=2 #Si acierta remplaza la casilla por un 2
            aciertos +=1
            intentos +=1
            print(f"\nEn la casilla {ataque_fila +1 , ataque_columna +1} Se encuentra el barco. Tocado\n")
        else:

            print(f"\nEn la casila {ataque_fila +1 , ataque_columna +1} No hay nada. Agua\n")
            tablero_visible[ataque_fila, ataque_columna]= 7 #Muestra un -1 en la casilla donde no hay barco
            intentos +=1
    except:
        print("--ERROR-- Ingrese un numero valido")

mensajeFinal()