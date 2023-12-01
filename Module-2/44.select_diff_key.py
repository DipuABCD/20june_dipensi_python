#44.Write a Python program to create and display all combinations of letters, selecting each letter from a 
#different key in a dictionary. Sample data: {'1': ['a','b'], '2': ['c','d']} 
#Expected Output: ac ad bc bd

# Get user input for the dictionary
data = {}
num_keys = int(input("Enter the number of keys:- "))
for i in range(1, num_keys + 1):
    key = input(f"Enter key {i}:- ")
    letters = input(f"Enter letters for key {key} (separated by space):- ").split()
    data[key] = letters

# Display combinations
keys = list(data.keys())
combinations = []
for i in range(len(data[keys[0]])):
    for j in range(len(data[keys[1]])):
        combination = data[keys[0]][i] + data[keys[1]][j]
        combinations.append(combination)

print(' '.join(combinations))
