#   LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both
#   numbers are even, but returns the greater if one or both numbers are odd
#   lesser_of_two_evens(2,4) --> 2
#   lesser_of_two_evens(2,5) --> 5

def fun(x,y):
    if x%2==0 and y%2==0:
        if(x<=y):
            return x
        else:
            return y
    else:
        if(x>=y):
            return x
        else:
            return y

x = int(input("Enter first number  : "))
y = int(input("Enter second number : "))
res  = fun(x,y)
print(res)