a=int(input())
b=list(map(int,input().split()))
c=[]
k=0
for z in b:
    if z not in c:
        c.append(z)
for i in c:
    d=(b.count(i))
    if d==i:
        k+=1
print(k)
        
    