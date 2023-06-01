def isd(n):
    d=[int(d) for d in str(n)]
    for i in d:
        if i==0 or n%i!=0:
            return False
    return True

def sdn(l,u):
    r=[]
    for n in range(l,u+1):
        if isd(n):
            r.append(n)
    return r

lb=int(input())
ub=int(input())
rl=sdn(lb,ub)
for i in range(len(rl)):
    print(rl[i],end=" ")