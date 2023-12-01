#20.Write a Python program to create a tuple with numbers.

data=[]
n=int(input("ENter number of data:- "))
for i in range(n):
    x=int(input("Enter numbers:- "))
    data.append(x)
print(tuple(data))