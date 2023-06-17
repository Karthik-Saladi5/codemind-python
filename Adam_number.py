n = int(input())
temp = n
sq = n * n

rev = int(str(n)[::-1])

sqrev = rev * rev

revsq = int(str(sqrev)[::-1])

print(revsq==sq)
    