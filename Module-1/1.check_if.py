#Write a Python program to check if a number is positive, negative or zero.

number=float(input("Enter a number :"))
# if the number is positive
if number > 0:
        print("{} is Positive number".format(number))
         
# if the number is negative
elif number < 0:
        print("{} is negative number".format(number))
         
# if the number is equal to
# zero
else:
        print("Equal to zero")
         