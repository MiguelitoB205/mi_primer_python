

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
p1 = Persona("Miguel", 28)

print(p1.nombre)
print(p1.edad)

class Estudiante(Persona):
    def __init__(self, nombre, edad, ano):
        super().__init__(nombre, edad)
        self.grado = ano
        
    def welcome(self):
        print("Obtuviste ", self.nombre, "de edad de ", self.edad, " el grado del año ", self.grado)
   
x = Estudiante("Miguel", 28, 2019)
x.welcome()