'''lista_pares= list(range(10, 0, -2))
print(lista_pares)

num=7
for i in range(1,11):
    print(f"{num} X {i} = {num * i})'''

precios = [100, 200, 300, 400]

def aumentarDiezPorciento (precio):
    return precio * 1.10

precios_aumentados= list(map(aumentarDiezPorciento , precios))
print (precios_aumentados)

precios = [100, 200, 300, 400]

def aumentar_10_por_ciento(precio):
    return precio * 1.10

precios_aumentados = list(map(aumentar_10_por_ciento, precios))
print(precios_aumentados)

