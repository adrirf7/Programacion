texto= input("Ingrese texto ")
texto = [str(palabra) for palabra in texto.split()]

palabras_largas=[]

'''for palabra in texto:
    if len(palabra) >= 5:
        palabras_largas.append(palabra)
print(palabras_largas)'''

def palabrasLargas(palabras):
    if len(palabra) >= 5:
        return palabra

for palabra in texto:
    palabras_largas.append(palabrasLargas)
    
print(palabras_largas)