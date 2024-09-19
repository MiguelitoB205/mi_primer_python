"""fruits={"apple", "banana", "cherry"}
##fruits.remove("banana")
##print(fruits)
del fruits
print(fruits)
"""
vegetales={"zanahoria", "habichuela", "tomate"}
x = vegetales.pop()
print(vegetales)

for x in vegetales:
    print(x)
    
set1={"a","b","c"}
set2 ={1,2,3}
set3={"Angela","andrés","Ricardo","a"}
set4={"Angela","apple","coconut","watermelon"}
myset=set1.intersection(set2,set3,set4)


print(myset)