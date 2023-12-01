#5. Write a Python program to read last n lines of a file.

def read_last_n_lines(n):
    with open('Q4.txt', 'r') as file:
        lines = file.readlines()
    return lines[-n:]

n = int(input("Enter the number of lines to read: "))

last_n_lines = read_last_n_lines(n)

print(f"Last {n} lines of '{'Q4.txt'}':")
for line in last_n_lines:
    print(line.strip())

