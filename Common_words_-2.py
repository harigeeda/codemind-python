a=input()
b=input()
a=a.lower()
b=b.lower()
c=[]
d=[]
for i in (a.split()):
    if i in c:
        c.remove(i)
    else:
        c.append(i)
for j in (b.split()):
    if j in d:
        d.remove(j)
    else:
        d.append(j)
s=0
for z in c:
    if z in d:
        s+=1
print(s)