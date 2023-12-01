#13. Explain Exception handling? What is an Error in Python?
"""
->Exception handling is a programming concept that allows you to gracefully handle errors and unexpected situations that might occur during 
the execution of a program. 
->In Python, exceptions are objects that represent errors or exceptional conditions that disrupt the normal flow of a program. 
->Key components of exception handling in Python:
 * Try block:- This is where you place the code that might raise an exception. It is surrounded by a try statement. 
 * Except block:- This block is used to handle specific exceptions. If an exception occurs in the try block that matches the type specified in 
                    the except block, the code inside the except block will be executed. 
 * Else block:- This block is executed if no exception occurs in the try block. It is optional.
 * Finally block:- This block is always executed, regardless of whether an exception occurred or not. It is used for cleanup operations like 
                   closing files or releasing resources.
->Here's a basic example of exception handling in Python:-
"""

"""
An Error in Python:

->In Python, an error is an abnormal condition that prevents the program from running correctly. 
->Errors can be broadly categorized into three types:
 * Syntax Errors:- Also known as parsing errors, these occur when the Python interpreter encounters code that does not conform to the language 
                   syntax rules. 
 * Runtime Errors:- Also known as exceptions, these occur during the execution of a program when something unexpected happens. 
 * Logical Errors:- These errors do not cause the program to crash, but they lead to incorrect or unexpected results. 

Python provides tools like exception handling to help deal with runtime errors and maintain program stability even when unexpected situations occur. 
It's important to handle errors effectively to create robust and reliable programs.
"""