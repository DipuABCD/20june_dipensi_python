#Write a Python function that takes a list of words and returns the length of the longest one.
str=['apple', 'banana', 'blackberry', 'cocount', 'cherry']
a=len(str[0])
b=str[0]

for i in str:
    if(len(i)>a):
        a=len(i)
        b=i
print("The Longest Length Word Is:",b," ", "\nlength is:",a)
