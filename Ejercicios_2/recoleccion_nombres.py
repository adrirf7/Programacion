nombres=[]
while True:
    input_nombres= input("Ingrese un nombre (o 'fin' para finalizar) ")
    if input_nombres == "fin":
        break
    else:
        nombres.append(input_nombres)

print ("------Lista Nombres------")
for nombre in nombres:
    print(f"-{nombre}")
