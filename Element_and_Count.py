a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if i not in c:
        c.append(i)
for j in c:
    k=b.count(j)
    print(j,k,end=" ")