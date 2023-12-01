#17. When is the finally block executed?

""""
-> finally block is always executed after leaving the try statement.
-> In case if some exception was not handled by except block, 
-> it is re-raised after execution of finally block.
-> The sequence of execution is as follows:-
    1. Code within the try block is executed.   
    2. If an exception is thrown during the execution of the try block, the corresponding catch block (if applicable) is executed.
    3. The code within the finally block is executed, regardless of whether an exception occurred or not.
"""
#example:

try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Division by zero error")
finally:
    print("This will always execute")
