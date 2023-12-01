#3. Write a Python program to append text to a file and display the text. 

from fileinput import close


f1=open("hello.txt",'a')
f1.write("\nhello python!!!")
f1.close()

f2=open("hello.txt",'r')
print(f2.read())