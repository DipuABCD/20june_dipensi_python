#9. Write a Python program to count the number of lines in a text file.

def count_lines():
    try:
        file = open('Q4.txt', 'r')
        line_count = sum(1 for line in file)
        file.close()
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return 0

line_count = count_lines()
print("Number of lines:", line_count)
