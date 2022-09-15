b=int(input())
c=[]
d=[]
e=[]
for i in range(1,b+1):
    if i>1:
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            c.append(i)
for j in range(1,b+1):
    if b%j==0:
        d.append(j)
for k in c:
    if k in d:
        e.append(k)
z=len(e)
y=len(d)
print(y-z)
