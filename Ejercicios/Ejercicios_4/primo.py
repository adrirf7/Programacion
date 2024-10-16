entrada=int(input("Ingrese un numero "))

def esPrimo(num):
    if num<=1: # Si es 1 o menor no es primo
        return False
    elif num == 2: # El unico numero par primo es el 2
        return True
    elif num %2==0: # Comprobamos si es par
        return False
    else:
        for i in range(2, int(num**0.5) +1): # Aplicamos la formula para el resto de numeros impares
            if num % i== 0:
                return False   
            else:
                return True

print(esPrimo(entrada))

