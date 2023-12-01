#32. Write a Python script to sort (ascending and descending) a dictionary by value.

import operator
dic={}
n=int(input("Enter number of pair:"))
for i in range(n):
    key=int(input("Enter number of key's:"))
    Value=input("Enter number of value:")
    dic[key]=Value
print(dic)
d=sorted(dic.items(),key=operator.itemgetter(1))
print("Ascending:",d)
d=dict(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
print("Descending:",d)

