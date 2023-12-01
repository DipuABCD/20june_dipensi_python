#4. Write a Python program to read first n lines of a file.

f1=open("Q4.txt",'a')
f1.write('''My Name Is Dipensi.
I am from Rajkot.
I'm study in tops tecnology- rajkot.''')
f1.close()
x=open("Q4.txt",'r')
print(x.readlines()[:5])
