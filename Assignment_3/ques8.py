#   Write a function that takes in a list of integers and returns True if it contains 007 in order
#   spy_game([1,2,4,0,0,7,5]) --> True
#   spy_game([1,0,2,4,0,5,7]) --> True
#   spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(list):
    for num in list:
        if num == 0:
            f_zero = list.index(num)
            break
    else:
         return False
    for i in range(f_zero,len(list)):
        if list[i] == 0:
            s_zero = i
            for j in range(s_zero,len(list)):
                if list[j] == 7:
                    return True
    return False

list = []
n = int(input("Enter how many numbers you want to input : "))
print("Enter elements in list")
for i in range(n):
    x = int(input())
    list.append(x)
print(list)
res = spy_game(list)
print(res)