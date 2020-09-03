#   Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their
#   sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after
#   adjustment) exceeds 21, return ‘BUST’.
#   blackjack(5,6,7) --> 18
#   blackjack(9,9,9) --> 'BUST'
#   blackjack(9,9,11) --> 19

def blackjack(list):
    sum = 0
    for num in list:
        sum = sum+num
    if sum<=21:
        return sum
    else:
        for num in list:
            if num==11:
                sum = sum-10
                break
        if sum>21:
            return 'BUST'
        else:
            return sum


list = []
print("Input three numbers\n")
for i in range(3):
    x = int(input())
    list.append(x)
result = blackjack(list)
print(result)