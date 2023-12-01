#15. Write a Python program to get unique values from a list.

list=[]
n=int(input("Enter number of element in list:-"))
for i in range(n):
    x=int(input("Enter element:-"))
    list.append(x)
print(list)

data=[]
for x in list:
    if list not in data:
        data.append(x)
    print(data)