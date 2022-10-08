a,b=map(int,input().split())
m=list(map(int,input().split()))
k=list(map(int,input().split()))
x=set(m)
y=set(k)
s=0
for i in x:
    if i in y:
        s+=1
print(s)
