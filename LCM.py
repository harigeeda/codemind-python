x,y=map(int,input().split())
s=[]
t=[]
u=[]
if x==0 or y==0:
    print("0")
else:
    for i in range(0,10**4,x):
        s.append(i)
    for j in range(0,10**4,y):
        t.append(j)
    for l in s:
        if l in t:
            u.append(l)
    print(u[1])