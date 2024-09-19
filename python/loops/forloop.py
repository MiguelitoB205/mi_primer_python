libros = ["Biblia", "Catecismo", "Cien años de soledad"]
albumes = ["Dónde están los ladrones", "Physical", "House of Holy"]

libros.append("Iliada de Homero")
albumes.remove("Dónde están los ladrones")
for x in libros:
    for y in albumes:
        print(x, y)