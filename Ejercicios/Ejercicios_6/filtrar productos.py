productos = [
    {"nombre": "Manzanas", "tipo": "perecedero"},
    {"nombre": "Arroz", "tipo": "no perecedero"},
    {"nombre": "Lechuga", "tipo": "perecedero"},
    {"nombre": "Frijoles enlatados", "tipo": "no perecedero"},
    {"nombre": "Queso", "tipo": "perecedero"},
    {"nombre": "Pasta", "tipo": "no perecedero"},
    {"nombre": "Plátanos", "tipo": "perecedero"},
    {"nombre": "Atún enlatado", "tipo": "no perecedero"},
    {"nombre": "Patatas", "tipo": "perecedero"},
    {"nombre": "Cereal", "tipo": "no perecedero"}
]

def esPerecedero(producto): 
    return producto["tipo"]=="perecedero"

resultado= filter(esPerecedero, productos)

for i in resultado:
    print(i["nombre"])