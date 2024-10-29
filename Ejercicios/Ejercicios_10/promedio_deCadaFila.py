import numpy as np

matriz= np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

promedio_fila= np.mean(matriz, axis=1)
print (promedio_fila)