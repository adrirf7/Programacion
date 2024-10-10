palabra= input("Dime una palabra ")
contador=0
vocales="a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
for caracter in palabra:
    if caracter in vocales:
        contador =contador +1
print ("Hay", contador, " vocales en tu palabra")
