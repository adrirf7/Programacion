def calcularDoble(num):
    return num*num

numeros=[1, 2, 3, 4, 5]

resultado= map(calcularDoble, numeros)
print(list(resultado))