'''Write a program that creates a list of tuples for all the numbers in a given limit and indicate whether
number is Prime or Non Prime. Let’s suppose limit is 7 so list should be created in the following way -
[(2,Prime),(3,Prime),(4,Non Prime),(5,Prime),(6,Non Prime),(7,Prime)]       '''

n = int(input("Enter the limit : "))
list = []
for i in range(2,n+1):
    flag = 0
    for j in range(2,i//2+1):
        if i%j==0:
            flag = 1
            break
    if flag == 0:
        x = (i,'Prime')
        list.append(x)
    else:
        x = (i,'Non Prime')
        list.append(x)
print("The resultant list is ",list)