#13. Write a Python program to select an item randomly from a list. 

s=list()
a=int(input("Enter number of list:-"))
for i in range(a):
    x=int(input("Enter number:-"))
    s.append(x)
print(s)
s.sort()
d=s[1]
print(d)