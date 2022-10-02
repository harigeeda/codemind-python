a=int(input())
b=list(map(int,input().split()))
s=[]
c=min(b)
d=str(c)
e=len(d)
f="9"*e
g=int(f)
for i in b:
    if i<=g:
        s.append(i)
print(len(s))