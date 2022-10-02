x=input()
b=list(map(int,input().split()))
a,x=map(int,input().split())
s=[]
for i in b:
    if i>=a and i<=x:
        s.append(i)
if (len(s))>0:
    print(min(s))
else:
    print("-1")