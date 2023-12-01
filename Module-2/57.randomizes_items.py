#57. How will you randomizes the items of a list in place?

import random
d=[]

n=int(input("Enter number of list data:-"))
for i in range(n):
    t=input("Enter list dta:-")
    d.append(t)
print("This is list of data")
print(d)

random.shuffle(d)
print(d)