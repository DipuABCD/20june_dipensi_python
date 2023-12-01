#24. Write a Python program to convert a list to a tuple. 

data=[]
n=int(input("Enter number of data:- "))
for i in range(n):
    x=int(input("Enter your value:- "))
    data.append(x)

print(tuple(data))