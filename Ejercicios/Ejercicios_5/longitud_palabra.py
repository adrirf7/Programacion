palabras=["Luz", "Mesa", "Perro", "Rapido", "Increible"]

def longitud(palabra):
        return len(palabra)

resultado= map(longitud, palabras)
print(list(resultado))