radio= float(input("Ingrese el valor del radio "))
def calcularArea(area):
    potencia= radio**2
    area= potencia*3.14
    return area
print(calcularArea(radio))