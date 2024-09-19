class ejercicio():
    def __len__(self):
        return 0
    
miObjeto = ejercicio()
print(bool(miObjeto))

def x():
    return True

print(x())

if x():
    print("verdad")
else:
    print("falso")
    
y = 200
print(isinstance(y,int))