#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

number=int(input("Enter number : "))
if number %2 == 0:
    print("{} is even number".format(number))
else:
    print("{} is odd number".format(number))
