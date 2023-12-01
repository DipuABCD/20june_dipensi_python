#41.Write a Python program to combine two dictionary adding values for common keys. 
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

d1={}
key=['a','b','c']
for i in range(len(key)):
    value=int(input(f"Enter Number for {key[i]}:-"))
    d1[key[i]] = value
print("~~~~~~~")
d2={}
key=['a','b','d']
for i in range(len(key)):
    value=int(input(f"Enter Number for {key[i]}:-"))
    d2[key[i]]=value

print(d1)
print(d2)
print("~~~~~~~")
for i in d1.keys():
    if i in d2.keys():
        d1[i]=d1[i]+d2[i]
    d2[i]=d1[i]
print(d2)