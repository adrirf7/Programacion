import numpy as np

matriz = np.random.randint(1, 51, size=(4, 3)) #Matriz con valores aleatorios de 4x3

print (matriz)
maximo=np.max(matriz, axis=0) #buscar el valor maximo de cada columna
print(f"\n{maximo}")