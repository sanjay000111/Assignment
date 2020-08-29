# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_element(old):
    new_list =[]
    for element in old:
        if old.count(element) == 1:
            new_list.append(element)
    print(new_list)
    return new_list

list = []
print("Enter total numbers you want to input in your list : ")
n = int(input())
print("Enter numbers")
for i in range(n):
    x = int(input())
    list.append(x)
out = unique_element(list)
print("The list with unique element is : ",out)