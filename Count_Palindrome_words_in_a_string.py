def ispalin(s):
    k = s[::-1]
    return s.lower()==k.lower()

sen=input()
words=sen.split()
c=0
for word in words:
    if ispalin(word):
        c+=1
print(c)