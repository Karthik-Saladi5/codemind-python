import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def next_prime_difference(number):
    if number < 2:
        return 2 - number

    next_prime = number + 1
    while not is_prime(next_prime):
        next_prime += 1

    return next_prime - number
    
n1=int(input())
n2=int(input())
n3=next_prime_difference(n1+n2)
print(n3)