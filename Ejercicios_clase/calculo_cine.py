edad_cliente = int(input ("Cuantos años tienes ? "))
if edad_cliente < 5:
    print ("Entrada gratuita")
elif edad_cliente < 13:
    print ("La entrada son 5 euros ")
elif edad_cliente < 18:
    print ("La entrada son 7 euros")
else :
    print ("La entrada son 10 euros ")