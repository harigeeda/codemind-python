a=input()
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=[]
for i in b:
    if i<c or i>d:
        s.append(i)
if len(s)>0:
    print(min(s))
else:
    print("-1")