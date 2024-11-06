import utilidades 

user_input= input("Ingrese una cadena de texto ")


print ("Texto en mayusculas:", utilidades.convertirMayusculas(user_input))

print ("Texto en minusculas:", utilidades.convertirMinusculas(user_input))

if utilidades.txtPalindromo(user_input):
    print("El texto es palindromo")
else:
    print("El texto no es palindromo")