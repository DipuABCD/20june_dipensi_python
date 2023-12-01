#19. How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

#python exception handling is achieved by three keyword blocks – try, except, and finally.
#The try block contains the code that may raise exceptions or errors.
#The except block is used to catch the exceptions and handle them.
#The finally block code is always executed, whether the program executed properly or it raised an exception.

try:
    a=int(input("Enter value of A:- "))
    b=int(input("Enter value of B:- "))
    print("sum:- ",a+b)
except:
    print("Error!")
finally:
    x=int(input("Enter X:- "))
    y=int(input("Enter Y:- "))
    print("Mul:- ",x*y)