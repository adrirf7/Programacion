menu={
    "Ensalada cesar": (8.5, 350),
    "Hamburguesa con queso": (12.00, 800),
    "Pizza Margarita": (10.00, 700),
    "Tacos de pollo": (9.00, 450),
    "Batido de fresa": (5.00, 200)
}
lista_pedido=[]
precio_total=0
calorias_total =0

print("----------MENU----------")
for plato, (precio, calorias) in menu.items():
    print(f"-{plato}: {precio}€ ({calorias} Kcal)")

while True:
    pedido= input("Ingresa el nombre del producto que deseas agregar (o 'fin' para terminar): ")
    if pedido== "fin":
        break
    elif pedido in menu:
        lista_pedido.append(pedido)
        precio_total += menu[pedido][0]
        calorias_total += menu[pedido][1]
    else:
        print("Plato no valido")
print("-----Tu pedido-----")
for pedido in lista_pedido:
    print (f"-{pedido}")

print(f"Precio total: {precio_total}€")
print(f"Calorias totales: {calorias_total} Kcal")