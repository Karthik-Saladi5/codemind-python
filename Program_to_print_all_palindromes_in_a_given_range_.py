def ispalindrome(n):
    v = int(str(n)[::-1])
    return v == n

m = int(input())
n = int(input())
for i in range(m, n + 1):
    if ispalindrome(i):
        print(i, end=" ")
