s1=input()
s2=input()
words1=s1.lower().split()
words2=s2.lower().split()
c=0
for word1 in words1:
    if word1 in words2:
        c+=1
print(c)