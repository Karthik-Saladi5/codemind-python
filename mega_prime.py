def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False

n=int(input())
if isprime(n):
    while n!=0:
        d=n%10
        if isprime(d):
            flag=1
        else:
            print('Not Mega Prime')
            break
        n=n//10
    else:
        print('Mega Prime')
else:
    print('Not Mega Prime')