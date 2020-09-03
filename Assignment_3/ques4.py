#   Given an integer n, return True if n is within 10 of either 100 or 200
#   almost_there(90) --> True
#   almost_there(104) --> True
#   almost_there(150) --> False
#   almost_there(209) --> True
#   NOTE: `abs(num)` returns the absolute value of a number

def almost_there(n):
        if (n>=90 and n<=110) or (n>=190 and n<=210):
            return True
        else:
            return False

n = int(input("Enter a number : "))
result = almost_there(n)
print(result)