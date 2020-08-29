#  Write a Python function to multiply all the numbers in a list and return the result.

def mult(list):
    pro = 1
    for element in list:
        pro*= element
    return pro


print("Enter the number of element you want to add in list : ")
n = int(input())
print("Enter elements")
list = []
for i in range(n):
    x = int(input())
    list.append(x)
result = mult(list)
print("The product of elements of list is : ",end="")
print(result)