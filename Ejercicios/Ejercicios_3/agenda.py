agenda={}
while True:
    nombre= input("ingrese nombre (o 'fin' para terminar) ")
    if nombre == "fin":
        break 
    else:
        telefono = input ("ingrese numero de telefono ")
        agenda [nombre] =telefono

print("-------Tu lista de contactos-------")
for nombre, telefono in agenda.items():
    print(f"- {nombre}: {telefono}")

busqueda_numero= input("Ingresa el nombre del contacto que deseas buscar: ")

if busqueda_numero in agenda:
    print (f"{busqueda_numero}: {agenda[busqueda_numero]}")
