import numpy as np

def convertirMayusculas(texto):
    return texto.upper()

def convertirMinusculas(texto):
    return texto.lower()

def txtPalindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]
