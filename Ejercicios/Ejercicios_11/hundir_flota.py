import numpy as np

#pritn tablero
tablero= np.zeros((5, 5))

#valores aleatorios para ubicar los barcos
barco_fila=np.random.randint(0,6)
barco_columna=np.random.randint(0,6)

#integrar barcos
tablero[barco_fila, :]=1
tablero[:, barco_columna]=1

tablero_visible= np.zeros((5, 5))
print(tablero_visible)

#contadores
barcos= np.sum(tablero==1)
aciertos=0
intentos=0

#Ataque
while aciertos< barcos:
    print(f"Intentos: {intentos}")
    ataque_fila= int(input("Ingrese valor fila ")) -1
    ataque_columna= int(input("Ingrese valor columna ")) -1

    #comprobacion 
    if tablero[ataque_fila, ataque_columna]==1:
        tablero_visible[ataque_fila, ataque_columna]=2
        aciertos +=1
        intentos +=1
        print("tocado")
    else:
        print("agua")
        tablero_visible[ataque_fila, ataque_columna]=-1
    print(tablero_visible)

print("Barcos Hundidos")

