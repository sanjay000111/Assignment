#   Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
#   extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#   summer_69([1, 3, 5]) --> 9
#   summer_69([4, 5, 6, 7, 8, 9]) --> 9
#   summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(a,n):
    sum = 0
    if 6 in a:
        st_pos = a.index(6)
        lt_pos = a.index(9)
    else:
        st_pos = -1
        lt_pos = -1
    for i in range(len(a)):
        if i>=st_pos and i<=lt_pos:
            pass
        else:
            sum+=a[i]
    return sum

a = []
n = int(input("Enter the no. of element  : "))
for i in range(n):
    x = int(input())
    a.append(x)
print(a)
res = summer_69(a,n)
print(res)