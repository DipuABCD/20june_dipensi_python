#17. Write a Python program to split a list into different variables.

input_str = input("Enter element of the list separated by spaces: ")
my_list = [(item) for item in input_str.split()]
var1,var2,var3=my_list
print("You entered the list:",my_list)
print("var1:",var1)
print("var2:",var2)
print("var3:",var3)