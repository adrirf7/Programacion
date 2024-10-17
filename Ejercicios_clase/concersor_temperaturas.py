def conversor(celsius):
    fahrenheit= (num * 9/5) + 32 
    return fahrenheit

celsius = input ("Ingrese temperatura en Celsius ")
celsius =[float(temp) for temp in celsius.split()]
temperaturas={}
for num in celsius:
    temperaturas [num]= conversor(num)

for num, fahrenheit in temperaturas.items():
        print(f"- {num} Cº = {fahrenheit} Fº")