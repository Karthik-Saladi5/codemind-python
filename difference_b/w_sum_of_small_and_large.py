s=input()
maxx=[]
minn=[]
words=s.split()
for word in words:
    maxx.append(ord(max(word)))
    minn.append(ord(min(word)))
print(sum(maxx)-sum(minn))