#Ejercicio 1
numeros=[4, 9, 16, 25, 1, 7, 12]

def menoresDiez(n):
   return n<10

resultado= filter(menoresDiez, numeros)
print(list(resultado))

#Ejercicio 2

alturas_metros = [1.60, 1.75, 1.80, 1.50]

def metrosAcentimetros(n):
   return n*100

resultado= map(metrosAcentimetros, alturas_metros)
print(list(resultado))

