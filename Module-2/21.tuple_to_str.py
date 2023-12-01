#21. Write a Python program to convert a tuple to a string.

user_input = input("Enter element of the tuple separated by spaces:- ")
user_tuple = tuple(user_input.split())

convert_string = ''.join(user_tuple)
print("convert_string:- ",convert_string)