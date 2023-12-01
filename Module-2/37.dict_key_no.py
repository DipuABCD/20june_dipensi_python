#37 Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

my_dict = {}

for i in range(1,16):
    value = input(f"Enter the value for key {i}:- ")
    my_dict[i] = value

print("\n Your dictionary:- ")
for key, value in my_dict.items():
    print(f"{key} : {value}")