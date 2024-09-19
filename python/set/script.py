myset = {"apple","banana","cherry",True,1,2}
##print(myset)
##print(len(myset))
for x in myset:
    print(x)
print("banana" in myset)

myset.add("Watermelon")
print(myset)

thisset={"manzana", "banana", "cereza"}
tropical={"mango", "coco", "piña"}
thisset.update(tropical)
print(thisset)
