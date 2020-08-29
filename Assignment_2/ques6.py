# Write a Python function that checks whether a passed in string is palindrome or not.

def ispalindrome(str):
    if str == str[::-1]:
        print("Palindrome String")
    else:
        print("Not a Palindrome String")


str = input("Enter a string : ")
ispalindrome(str)