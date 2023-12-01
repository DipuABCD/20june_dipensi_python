#51. Write a Python function that checks whether a passed string is palindrome or not .

def main():
    a=input("Enter a String:-")
    b=a[-1::-1]
    if(a==b):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

main()