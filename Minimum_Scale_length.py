a=int(input())
b=list(map(int,input().split()))
c=max(b)
k=[]
s=0
for i in range(1,c+1):
    for j in b:
        if j%i==0:
            s+=1
    if s==a:
        k.append(i)
        s=0
    else:
        s=0
print(max(k))