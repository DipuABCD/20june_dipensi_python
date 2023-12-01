#14. How many except statements can a try-except block have? Name Some built-in exception classes:

"""
-> A try-except block in Python can have multiple except clauses to catch different types of exceptions. There is no strict limit on the number 
of except statements you can have in a single try-except block, but keep in mind that having too many except clauses can make your code harder 
to read and maintain.

As for some built-in exception classes, here are a few common ones:-

~> ZeroDivisionError:- Raised when division or modulo by zero is encountered.
~> ValueError:- Raised when a function receives an argument of the correct type but an inappropriate value.
~> TypeError:- Raised when an operation or function is applied to an object of inappropriate type.
~> FileNotFoundError:- Raised when an attempt to open a file fails (usually when the file does not exist).
~> IndexError:- Raised when a sequence subscript is out of range.
~> KeyError:- Raised when a dictionary key is not found.
~> NameError:- Raised when a local or global name is not found.
~> IOError:- Raised when an I/O operation (such as reading or writing a file) fails.
~> ImportError:- Raised when an import statement cannot locate the module definition.
~> RuntimeError:- Raised when an error is detected that doesn't fall into other categories.
~> AssertionError:- Raised when an assert statement fails.    

"""