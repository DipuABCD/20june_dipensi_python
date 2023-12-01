#12. Write a Python program to copy the contents of a file to another file.

x = open("Q4.txt", 'r')
y = open("Q-12.txt", 'w')

try:
    for i in x:
        y.write(i)
    print("Contents copied successfully.")
except Exception as e:
    print(f"An error occurred:- {e}")
finally:
    x.close()
    y.close()
