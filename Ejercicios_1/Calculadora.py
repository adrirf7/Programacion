numero_uno = float(input("Dame un numero "))
operacion= input ("Escribe una operacion ")
numero_dos = float(input ("escribe otro numero "))
if operacion == "+":
    calculo = numero_uno + numero_dos
    print(calculo)
elif operacion == "-":
    calculo = numero_uno - numero_dos
    print (calculo)
elif operacion== "*":
    calculo= numero_uno * numero_dos
    print (calculo)
else :
    if numero_dos ==0 :
        print("error")
    else :
        calculo = numero_uno / numero_dos
        print(calculo)
