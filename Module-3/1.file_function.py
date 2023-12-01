#1. What is File function in python? What is keywords to create and write file. 

"""
-> In Python, there is no specific built-in function called "File function."
-> File Objects in Python. 
-> A file object allows us to use, access and manipulate all the user accessible files.
-> One can read and write any such files. 
"""

f1=open("hello.txt",'w')
f1.write("hello python!!!")
print(f1)