a,b=map(int,input().split())
c=list(map(int,input().split()))
s=0
for i in c:
    j=abs(i)
    k=str(j)
    if len(k)==b:
        s+=1
print(s)