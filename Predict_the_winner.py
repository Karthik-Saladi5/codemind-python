def absd(a, b):
    if a > b:
        return a - b
    else:
        return b - a

n = int(input())
a = list(map(int,input().split()))

xvals = 0
yvals = 0
for i in range(n):
    if i % 2 == 0:
        xvals += a[i]
    else:
        yvals += a[i]

if absd(xvals, yvals) % 4 == 0:
    print("X")
else:
    print("Y")
