def sumarCinco(num):
    return num + 5

numeros= [1, 2, 3, 4, 5]

resultado= map(sumarCinco, numeros)
print(list(resultado))