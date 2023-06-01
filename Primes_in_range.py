import math
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
def primes(lb,ub):
    c=0
    for i in range(lb,ub+1):
        if is_prime(i):
            c+=1
    return c
lb=int(input())
ub=int(input())
count=primes(lb,ub)
print(count)
