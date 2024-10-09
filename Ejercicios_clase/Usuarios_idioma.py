idioma = input("Idioma ")
edad=  int (input ("Edad "))
if edad <13:
    print ("Clase niño")
elif edad <18:
    print ("Clase adolescente")
elif edad <60:
    print ("clase adulto")
else:
    print ("clase adulto mayor")
match idioma:
    case "es":
        print ("Bienvenido, hoy es miercoles 9 de octubre")
    case "en":
        print ("Welcome, today is Wednesday, October 9") 
    case "fr":
        print ("Bienvenue, nous sommes le mercredi 9 octobre")
    case _:
        print ("idioma no soportado")


