#   Write a program to print N fibonacci numbers where N is being passed from command line and you
#   can run python program using command - python fibo.py 20, where N=20.

import sys
a,b = 0,1
print(a,end=" ,")
print(b,end=" ,")
for i in range(int(sys.argv[1])-2):
    c =a+b
    a = b
    b= c
    print(c,end=" ,")