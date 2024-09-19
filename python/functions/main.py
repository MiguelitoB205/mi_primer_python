def my_function(fname, lname):
    print(fname + " " + lname)
    
my_function("Miguel", "Buitrago")

def my_function_2(*kids):
    print("El niño más pequeño es " + kids[1])
    
my_function_2("Santiago", "Michael", "Elian")

def my_function_3(country="Colombia"):
    print("Soy de " + country)
my_function_3()
my_function_3("Venezuela")
my_function_3("Perú")
my_function_3("Brasil")

def my_function_4(x):
    return x * 5

print(my_function_4(3))

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nEjemplo con resultados")
tri_recursion(6)