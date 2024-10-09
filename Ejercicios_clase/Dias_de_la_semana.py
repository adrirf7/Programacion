numero = int(input("Numero de la semana "))
match numero:
    case 1:
        print("Lunes")
    case 2:
        print ("martes")
    case 3:
        print ("miercoles")
    case 4:
        print ("jueves")
    case 5:
        print ("viernes")
    case 6:
        print ("sabado")
    case 7:
        print ("domingo")
    case _ :
        print ("numero invalido")