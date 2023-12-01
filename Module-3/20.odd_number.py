#20. Write python program that user to enter only odd numbers, else will raise an exception.

try:
    num = int(input("Enter an odd number:- "))
    if num % 2 == 0:
        raise Exception("Even number entered. Please enter an odd number.")
    else:
        print(num)
except Exception as e:
    print("Error:", e)
