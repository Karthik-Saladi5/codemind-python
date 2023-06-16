def check_dup(a, n, val):
    c = 0
    for i in range(n):
        if a[i] == val:
            c += 1
        if c > 1:
            break
    if c == 1:
        return val
    return -1

n = int(input())
a = list(map(int,input().split()))
temp=0

flag = 0
for i in range(n):
    ans = check_dup(a, n, a[i])
    if ans != -1:
        print(ans, end=' ')
        flag = 1

if flag == 0:
    print("-1")
