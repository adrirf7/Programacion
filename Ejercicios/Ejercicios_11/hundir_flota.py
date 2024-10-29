import numpy as np

def ubicacionBarco():
    tablero= np.zeros((5, 5)) #generamos el tablero real donde se ubicara el barco

    #valores aleatorios para ubicar los barcos
    barco_fila=np.random.randint(0,5)
    barco_columna=np.random.randint(0,5)

    #integrar barco en el tablero
    tablero[barco_fila, barco_columna ]=1

    #Tablero de mentira donde no se muestre la ubicacion del barco
    tablero_visible= np.zeros((5, 5))
    
    return tablero, tablero_visible

def bienvenida(): #Mensaje bienvenida
    print("\n¡Bienvenido a la batalla naval!")
    print("Intenta destruir el barco\n")
    
def UserInput(): 
    print(f"----Intentos: {intentos}----") #contador intentos
    print(f"{tablero_visible}\n") #Muestra el tablero de mentira para no revelar la ubicacion del barco
    
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
    print (tablero_visible)
    print ("------Has ganado------")

#llamada de funciones
tablero, tablero_visible= ubicacionBarco() 
aciertos, intentos=contadores()
bienvenida()

while aciertos< 1: #mientras que el contador sea 0
    try:
        ataque_fila, ataque_columna = UserInput() #llamada a la funcion del input

        #comprobacion 
        if tablero[ataque_fila, ataque_columna]==1: #comprueba si en la ubicacion del usuario hay un 1 (barco)

            tablero_visible[ataque_fila, ataque_columna]=2 #Si acierta remplaza la casilla por un 2
            aciertos +=1
            intentos +=1
            print(f"\nEn la casilla {ataque_fila, ataque_columna} Se encuentra el barco. Tocado\n")
        else:

            print(f"\nEn la casila {ataque_fila, ataque_columna} No hay nada. Agua\n")
            tablero_visible[ataque_fila, ataque_columna]=-1 #Muestra un -1 en la casilla donde no hay barco
            intentos +=1
    except:
        print("--ERROR-- Ingrese un numero valido")

mensajeFinal()

