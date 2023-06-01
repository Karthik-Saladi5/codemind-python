import math
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
    
lb=int(input())
ub=int(input())
for i in range(lb,ub+1):
    if is_prime(i):
        print(i)