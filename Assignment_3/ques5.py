#   Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#   has_33([1, 3, 3]) → True
#   has_33([1, 3, 1, 3]) → False
#   has_33([3, 1, 3]) → False

def has_33(list):
    for num in range(0,len(list)-1):
        if list[num] == 3 and list[num + 1] == 3:
            return True
    return False

n = int(input("Enter numbers to input in list : "))
list = []
for i in range(n):
    x = int(input())
    list.append(x)
print(list)
result = has_33(list)
print(result)