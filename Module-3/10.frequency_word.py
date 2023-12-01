#10. Write a Python program to count the frequency of words in a file. 

from collections import Counter

x = open("Q4.txt", 'r')
y = x.read().split()
word_frequency = Counter(y)
print(word_frequency)
x.close()
