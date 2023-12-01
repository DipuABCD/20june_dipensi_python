#48 Write a Python function to calculate the factorial of a number (a nonnegative integer) .

num_str = input("Enter a non-negative integer:- ")

if num_str.isdigit():
    num = int(num_str)
    if num < 0:
        print("Factorial is defined only for non-negative integers.")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print("Factorial of", num, "is", factorial)
else:
    print("Invalid input. Please enter a non-negative integer.")
