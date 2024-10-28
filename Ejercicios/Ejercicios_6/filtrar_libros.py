libros = [
    {"titulo": "Cien años de soledad", "categoria": "novela"},
    {"titulo": "El laberinto de la soledad", "categoria": "ensayo"},
    {"titulo": "Don Quijote de la Mancha", "categoria": "novela"},
    {"titulo": "Residencia en la Tierra", "categoria": "poesía"},
    {"titulo": "La náusea", "categoria": "novela"},
    {"titulo": "Hombres de maíz", "categoria": "novela"},
    {"titulo": "Las venas abiertas de América Latina", "categoria": "ensayo"},
    {"titulo": "Veinte poemas de amor y una canción desesperada", "categoria": "poesía"},
    {"titulo": "La República", "categoria": "ensayo"},
    {"titulo": "Antología poética", "categoria": "poesía"}
]

def categoriaLibro(categoria):
    return categoria["categoria"]== "novela"

resultado= filter(categoriaLibro, libros)

for i in resultado:
    print(i["titulo"])
