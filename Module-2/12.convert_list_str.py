#12. Write a Python program to convert a list of characters into a string.

data=list()
n=int(input("Enter number of value:-"))

for i in range(n):
    x=input("Enter your data:-")
    data.append(x) 

print(data)
str=''.join(data)
print("String:-",str)