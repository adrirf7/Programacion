#Los diccionarios con estructuras que contienen pares clave y valor
#Cada clave tiene su valor

#Como definimos un diccionario

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

#Como accedemos a los valores de un diccionario.
#Utilizando las claves.

print( persona["nombre"])

print( persona["edad"])

print( persona["ciudad"])

print("##################@@@@@@@@@@@@@@@@@@@###################")
#Muestra los valores de cada clave en cada vuelta del bucle cambia de clave y nos muestra su valor
for clave in persona:
    print(persona[clave]) 


#Podemos crear una agenda con un diccionario, utilizaremos el nombre del contacto como clave y el telefono como valor
print("##################@@@@@@@@@@@@@@@@@@@###################")

contactos = {"Pedro":"44444444", "Juan":"33333333", "Nuria":"9999999"}

for clave in contactos:
    print(f"El teléfono de {clave} es {contactos[clave]}") 

#Métodos útiles de los diccionarios:
#keys(): Devuelve una vista de todas las claves.
#values(): Devuelve una vista de todos los valores.
#items(): Devuelve una vista de todos los pares clave-valor.

stock_fruteria = {"manzana": 3, "banana": 2, "naranja": 1}
for fruta, cantidad in stock_fruteria.items():
    print(f"Tengo {cantidad} {fruta}(s)")