vueltas =0
with open ("Ejercicios/Ejercicios_12/notas.txt", "w") as archivo: #Crea el nuevo archivo
    while vueltas<3: 
        texto= input("Escribe el contenido ") #solicita contenido a usuario
        vueltas+=1
        archivo.write (f"{texto}\n") #escribe contenido y baja una linea

