a=int(input())
b=list(map(int,input().split()))
c=max(b)
k=c
s=0
while True:
    for i in b:
        if c%i==0:
            s+=1
    if s==a:
        print(c)
        break
    else:
        s=0
        c+=k