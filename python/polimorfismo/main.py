class Libro:
    def __init__(self, editorial, autor):
        self.editorial = editorial
        self.autor = autor
        
    def leer(self):
        print("Léete este libro!")
        
class Biblia(Libro):
    def leer(self):
        return super().leer()

class Iliada(Libro):
    def leer(self):
        return super().leer()
    
class Harry_Potter(Libro):
    def leer(self):
        return super().leer()
    
biblia1 = Biblia("San Pablo", "San Mateo, San Lucas, Esdras")
iliada1 = Iliada("Panamericana", "Homero")
harrypotter1 = Harry_Potter("Norma", "J.K Rowlling")

for x in (biblia1, iliada1, harrypotter1):
    print(x.editorial)
    print(x.autor)
    x.leer()