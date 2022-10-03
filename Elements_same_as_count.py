a=int(input())
b=list(map(int,input().split()))
c=[]
k=[]
for z in b:
    if z not in c:
        c.append(z)
for i in c:
    d=(b.count(i))
    if d==i:
        k.append(i)
if len(k)>0:
    print(*(k))
else:
    print("-1")
        
    