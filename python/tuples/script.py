mytuple1 = ("apple", "banana", "cherry")
print(len(mytuple1))
print(type(mytuple1))
y = list(mytuple1)
y.append("orange")
mytuple1 = tuple(y)
print(mytuple1)


mytuple2=(1,5,7,9,3)
print(mytuple2)
print(len(mytuple2))
print(type(mytuple2))

mytuple3=(True,False,False,True)
print(len(mytuple3))

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


print(mytuple1[-1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1]="kiwi"
x = tuple(y)

print(x)