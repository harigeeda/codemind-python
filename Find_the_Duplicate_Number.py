a=input()
b=list(map(int,input().split()))
c=[]
for i in b:
    if i not in c:
        c.append(i)
for j in c:
    k=b.count(j)
    if k==2:
        print(j)
        break