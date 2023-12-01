#11. Write a Python program to write a list to a file.


    
x = open("Q4.txt", 'a')

my_list = ['My Father name is Bharatbhai.', 'My Brother name is nayan.', 'My Mother name is jagrutiben.']

x.write('\n')
for item in my_list:
    x.write(f'{item}\n')

x.close()
