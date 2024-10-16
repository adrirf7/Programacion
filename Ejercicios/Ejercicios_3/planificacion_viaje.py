ciudades=("Madrid", "Tokio", "Sídney", "Ciudad del Cabo", "Berlin")
print("------Itinerario de Viaje------")

for i in range(5):
    print(f"{i+1}.- {ciudades[i]}")

user_input= int(input("Ingresa la posición para saber qué ciudad visitarás: "))
print(f"En la posicion {user_input} visitaras {ciudades[user_input -1]}")



