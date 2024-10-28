vehiculos = [
    {"modelo": "Toyota Corolla", "estado_revision": "aprobada"},
    {"modelo": "Honda Civic", "estado_revision": "pendiente"},
    {"modelo": "Ford Fiesta", "estado_revision": "aprobada"},
    {"modelo": "Nissan Sentra", "estado_revision": "pendiente"},
    {"modelo": "Chevrolet Aveo", "estado_revision": "aprobada"},
    {"modelo": "Mazda 3", "estado_revision": "pendiente"},
    {"modelo": "Volkswagen Jetta", "estado_revision": "aprobada"},
    {"modelo": "Hyundai Elantra", "estado_revision": "pendiente"},
    {"modelo": "Kia Rio", "estado_revision": "aprobada"},
    {"modelo": "Renault Sandero", "estado_revision": "pendiente"}
]

def estadoRevision(vehiculo):
    return vehiculo["estado_revision"]== "aprobada"

resultado= filter(estadoRevision, vehiculos)

for coches in resultado:
    print(coches["modelo"])

