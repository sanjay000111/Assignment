#  Write a function that checks whether a number is in a given range (inclusive of high and low).

def num_in_range():
    print("Input range : ")
    a = int(input())
    b = int(input())
    print("Enter number to search : ",end="")
    num = int(input())
    flag = 0
    for i in range(a, b + 1):
        if i == num:
            flag = 1
    if flag == 1:
        print("Number exist in given range")
    else:
        print("Number does not exist in given range")


num_in_range()