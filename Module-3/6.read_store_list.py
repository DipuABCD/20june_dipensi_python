#6. Write a Python program to read a file line by line and store it into a list.

with open('Q4.txt', 'r') as file:
    lines_list = [line.strip() for line in file.readlines()]

if lines_list:
    print(f"Contents of '{'Q4.txt'}':")
    for line in lines_list:
        print(line)
else:
    print("No lines were read from the file.")
