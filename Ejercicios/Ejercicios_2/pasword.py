pasword="python123"
while True:
    input_usuario= input("Ingrese contraseña ")
    if input_usuario == pasword:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, intente de nuevo ")