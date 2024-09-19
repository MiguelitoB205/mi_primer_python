class MisNumeros:
    def __iter__(self):
        self.a = 2
        return self
    
    def __next__(self):
        x = self.a
        self.a +=2
        return x
    
myclass = MisNumeros()
myiter = iter(myclass)

print (next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
    
    