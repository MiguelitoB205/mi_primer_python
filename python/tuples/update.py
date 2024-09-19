thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
y.remove("apple")
del thistuple
thistuple = tuple(y)

print(thistuple)