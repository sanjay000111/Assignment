#  Write a program that creates a dictionary for all the numbers in a given limit and indicate whether
#  number is Prime or Non Prime. Let’s suppose limit is 7 so list should be created in the following way -
#  {2:”Prime”,3:”Prime”,4:”NonPrime”,5:”Prime”,6:”NonPrime”,7:”Prime”} Once dictionary is created,
#  delete all the Non-Prime key-value pairs and print their counts on output screen.'''

n = int(input("Enter the limit : "))
dict = {}
for i in range(2,n+1):
    flag = 0
    for j in range(2,i//2+1):
        if i%j == 0:
            flag = 1
            dict[i] = "Non Prime"
            break
    if flag == 0:
        dict[i] ="Prime"
print("The dictionary is : ",dict)
d1 = dict.copy()
c =0
for value in d1.keys():
    if d1[value] == "Non Prime":
        dict.pop(value)
        c+=1
print("The dictionary with Prime Numbers  is : ",dict)
print("The total Non Prime values are : ",c)