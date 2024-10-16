#Estructuras de datos
#Listas

#Se puede inicializar una lista vacía
lista = []

#Se puede inicializar una lista con valores
amigos = ["Juan", "Ana", "Carlos", "Sofía", "Pedro"] # Esto es una lista

#Podemos acceder a cada elemento de la lista, utilizando su índice

#amigos = ["Juan", "Ana", "Carlos", "Sofía", "Pedro"]
#            0       1       2         3        4

print (amigos[3])   #Muestra el elemento que corresponda con el índice

#print(amigos[6])
#Al hacer referencia a un elemento que no existe da el siguiente error
#IndexError: list index out of range

print(amigos)       #Muestra todos los elementos de la lista

#Para recorrer todos los elementos de la lista, utilizaremos un bucle
#for indicandole que vaya cogiendo elemento a elemento y metiendolo en
#una variable, por ejemplo en este caso 'amigo'
for amigo in amigos:
    print(amigo)

#si quiero conocer el tamaño de una lista, debemos utilizar la función 'len'

print(f"Tienes {len(amigos)} amigos, deberías salir más")

#La función len, tambien nos devuelve el número de caracteres de una variable string
cadena_texto = "En un lugar de la mancha de cuyo nombre no quiero acordarme."

print(f"La longitud de la cadena es: {len(cadena_texto)}")

for caracter in cadena_texto:
    print(caracter)

#Las listas son mutables, es decir, que pueden cambiar de tamaño y se pueden modificar sus elementos
#Esta es la gran diferencia con las tuplas

#Añadir un elemento a una lista
#Para añadir un elemento a una lista, utilizamos el método append de la clase lista

print(f"Esta es la lista amigos antes del append: {amigos}")

amigos.append("Faustino")

print(f"Esta es la lista amigos Despues del append: {amigos}")

#Tambien podemos añadir un elemento a la lista en el lugar que queramos
#Para eso utilizamos el método insert

print(f"Esta es la lista amigos antes del insert: {amigos}")

amigos.insert(0,"Paloma")

print(f"Esta es la lista amigos después del insert: {amigos}")

#Tambien podemos eliminar elementos de una lista
#Para ello utilizaremos el método remove

amigos.remove("Ana")
print(f"Esta es la lista amigos después del remove: {amigos}")