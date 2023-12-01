#35. How Do You Traverse Through A Dictionary Object In Python? 

d1={}
n= int(input("Enter number of pairs:"))
for i in range(n):
    key=input("Enter number of key:")
    Value=input("Enter number of value:")
    d1[key]=Value
print(d1)

for i in d1:
    print(i, "~~~>", d1[i])