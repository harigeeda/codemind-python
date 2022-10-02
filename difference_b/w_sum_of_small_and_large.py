a=input()
b=[]
c=[]
for i in (a.split()):
    b.append(ord(max(i)))
    c.append(ord(min(i)))
print(sum(b)-sum(c))
    