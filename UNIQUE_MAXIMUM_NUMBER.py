a=int(input())
b=list(map(int,input().split()))
c=[]
k=[]
for i in b:
    if i not in c:
        c.append(i)
for j in c:
    if b.count(j)==1:
        k.append(j)
if len(k)>0:
    print(max(k))
else:
    print("-1")