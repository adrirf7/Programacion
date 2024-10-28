empleados = [
    {"nombre": "Ana López", "estado_laboral": "activo"},
    {"nombre": "Carlos Martínez", "estado_laboral": "inactivo"},
    {"nombre": "Lucía Gómez", "estado_laboral": "activo"},
    {"nombre": "Pedro Ramírez", "estado_laboral": "inactivo"},
    {"nombre": "Sofía Torres", "estado_laboral": "activo"},
    {"nombre": "Jorge Fernández", "estado_laboral": "activo"},
    {"nombre": "Marta Reyes", "estado_laboral": "inactivo"},
    {"nombre": "Luis Hernández", "estado_laboral": "activo"},
    {"nombre": "Claudia Pérez", "estado_laboral": "inactivo"},
    {"nombre": "Miguel Ortiz", "estado_laboral": "activo"}
]

def estadoEmpleado(estado):
    return estado ["estado_laboral"]== "activo"

resultado=filter(estadoEmpleado, empleados)

for empleado in resultado:
    print(empleado["nombre"])
