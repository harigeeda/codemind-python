a=int(input())
b=list(map(int,input().split()))
c=max(b)
d=str(c)
s=0
e=(len(d)-1)
f=10**e
for i in b:
    if i>=f:
        s+=1
print(s)