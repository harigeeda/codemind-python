a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
x=[]
for j in c:
    if j not in x:
        x.append(j)
y=set(d)
for i in x:
    if i in y:
        print(i,end=" ")