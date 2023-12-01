#49. Write a Python function to check whether a number is in a given range.

number_to_check = float(input("Enter the number to check: "))
lower_bound = float(input("Enter the lower bound of the range: "))
upper_bound = float(input("Enter the upper bound of the range: "))

if lower_bound <= number_to_check <= upper_bound:
    print(f"{number_to_check} is in the range [{lower_bound}, {upper_bound}]")
else:
    print(f"{number_to_check} is not in the range [{lower_bound}, {upper_bound}]")
