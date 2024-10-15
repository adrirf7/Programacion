menu={
    "Ensalada César": (8.5, 350),
    "Hamburguesa con Queso": (12.00, 800),
    "Pizza Margherita": (10.00, 700),
    "Tacos de Pollo": (9.00, 450),
    "Batido de Fresa": (5.00, 200)

}
print("----------MENU----------")
for plato, (precio, calorias) in menu.items():
    print(f"-{plato}: {precio}€ ({calorias} Kcal)")

while True:
    pedido= input("Ingresa el nombre del producto que deseas agregar (o 'fin' para terminar): ")
    if pedido == "fin":
        break
    else:
        