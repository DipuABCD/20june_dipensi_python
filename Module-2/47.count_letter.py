#47. Write a Python program to create a dictionary from a string. 
#Note: Track the count of the letters from the string. Sample string: 'w3resource' 
#Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

sample_string = input("Enter a string: ")

letter_count = {}
for letter in sample_string:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)
