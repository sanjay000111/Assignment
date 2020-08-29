'''Write a Python function that accepts a string and calculates the number of upper case letters and
lower case letters. You can use functions .isupper() and .islower().        '''

def check(st):
    c1,c2 = 0,0
    for letter in st:
        if(letter.isupper()):
            c1+=1
        elif(letter.islower()):
            c2+=1
        else:
            pass
    return c1,c2

str = input("Enter string : ")
u,l = check(str)
print("Lower case letters are : ",l,"\nUpper case letters are : ",u)