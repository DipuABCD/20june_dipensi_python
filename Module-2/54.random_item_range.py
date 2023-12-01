#54. How can you pick a random item from a range? 

"""
-> To pick a random item from a range, you can use a programming language that supports random number generation 
and has built-in functions for working with ranges.
-> Python has a built-in 'random' module that allows you to generate random numbers and perform random operations,
including picking a random item from a range.
"""
import random
d=[]

n=int(input("Enter number of list data:-"))
for i in range(n):
    t=input("Enter list dta:-")
    d.append(t)
print("This is list of data")
print(d)

random.choice(d)
print(d)
y="y"
while y!="n":
    t=random.randint(11111,99999)
    print(t)
    y=input("Do you want to countinue 'y' for 'yes' 'n' for 'no' :-")
