class Persona:
    def __init__(self,nombre,apellido):
        self.primernombre = nombre
        self.apel=apellido
        
    def printnombre(self):
        print(self.primernombre, self.apel)
        
x = Persona("Miguel","Buitrago")
x.printnombre()

class Estudiante(Persona):
    def __init__(self,nombre,apellido):
        super().__init__(nombre, apellido)
        self.graduacion=2024
    
x = Estudiante("Miguel", "Buitrago")
print(x.graduacion)