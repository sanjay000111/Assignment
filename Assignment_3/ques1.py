#   Write a Python function to check whether a string is pangram or not.
#   Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
#   For example: "The quick brown fox jumps over the lazy dog”

def check(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True

str = input("Enter a string : ")
res = check(str)
if(res == True):
    print("Pangram String ")
else:
    print("NOt a Pangram String")