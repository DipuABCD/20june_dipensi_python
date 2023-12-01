#14. Write a Python program to find the second smallest number in a list.

s=list()
a=int(input("Enter number of list:-"))
for i in range(a):
    x=int(input("Enter number:-"))
    s.append(x)
print(s)
s.sort()
d=s[1]
print(d)