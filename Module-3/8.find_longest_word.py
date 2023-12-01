#8.  Write a python program to find the longest words.

# Take user input for the list of words
input_string = input("Enter a list of words separated by spaces:- ")
word_list = input_string.split()


longest_length = max(len(word) for word in word_list)
longest_words = [word for word in word_list if len(word) == longest_length]

print("Longest words:- ", longest_words)
