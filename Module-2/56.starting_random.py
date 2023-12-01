#56. How will you set the starting value in generating random numbers?
"""
-> The random number generator needs a number to start with (a seed value), to be able to generate a random number.
->By default the random number generator uses the currunt system time use the seed() method to customize the start
 number of the random number generator.
"""
import random

y="y"
while y!="n":
    random.seed(10)
    print(random.random())
    y=input("Do you want to countinue 'y' for 'yes' 'n' for 'no' :-")