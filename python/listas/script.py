libros = ["Biblia", "Catecismo", "Corán", "Concilio Vaticano"]
print(libros)
print(len(libros))

frutas = ["Manzana", "Pera", "Sandía", "Orange", "Kiwi", "Bananas"]
frutas[0:1] = ["Estrella", "Melón"]
frutas.insert(1,"Cereza")
frutas.append("Mangostino")
frutas.remove("Kiwi")


verduras = ["Col", "Champiñones", "Jalapeño"]

verduras.remove("Champiñones")

frutas.extend(verduras)
frutas.pop(0)


numeros = [1,2,3,7,8,9]
numeros.pop()
bool = [True, False]

print(type(frutas + verduras + numeros + bool))
print(type(numeros))
print(type(bool))

personas = list(('Andrea', 'Alejo', 'Juan Pablo'))
print(personas)
print(frutas[1])
print(frutas[2:5])
print(frutas[:6])

if "Manzana" in frutas:
    print("Existe esta fruta en la lista")
else:
    print("Esta fruta no existe")
    
frutas[1] = "Mango"
frutas[0] = "Naranja"
print(frutas)

