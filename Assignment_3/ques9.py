#   Write a function that returns the number of prime numbers that exist up to and including a given
#   number. Hint - By convention, 0 and 1 are not prime.
#   count_primes(100) --> 25

def count_prime(n):
    count = 0
    for i in range(2,n+1):
        flag = 0
        for j in range(2,(i//2)+1):
            if i%j==0:
                flag = 1
                break
        if flag == 0:
            count += 1
    return count

n = int(input("Enter the range : "))
no_of_prime = count_prime(n)
print(no_of_prime)