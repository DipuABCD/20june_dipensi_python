#6. Write a Python program to count the number of strings where the string length is 2 or more and the first and 
#last character are same from a given list of strings.

list=input("Enter a list of string (comma-separated):-").split(',')
count = 0

for string in list:
    if len(string.strip()) >= 2 and string.strip()[0] == string.strip()[-1]:
        count += 1
print(f"The numbr of string with the same first and last character:- {count}")



