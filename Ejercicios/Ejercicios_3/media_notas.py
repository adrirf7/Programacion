notas={}
while True:
    asignatura =input("Ingresa el nombre de la asignatura (o 'fin' para terminar) ")
    if asignatura == "fin":
        break
    else:
        nota = int(input(f"Ingresa la calificacion de {asignatura}: "))
        notas [asignatura]= nota

print("------Resumen de calificaciones:------")
for asignatura, nota in notas.items():
    print(f"-{asignatura}: {nota}")
    
media = sum(notas.values()) / len(notas)
print(f"La media de las calificaciones es: {media:.2f}")