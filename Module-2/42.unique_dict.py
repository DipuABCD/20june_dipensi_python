#42. Write a Python program to print all unique values in a dictionary.

mydict={}
n=int(input("Enter number of pairs:"))
for i in range(n):
    key=input("Enter your key's:- ")
    value=input("Enter your value's:- ")
    mydict[key]=value
print("User input dictionary:- ", mydict)
d=list(mydict.values())
for i in range(len(d)):
    if d[i] not in d[i+1:]:
        print("Unique value in the dictionary:- ",d[i])
    else:
        pass