a=input()
b=list(map(int,input().split()))
c=0
s=0
for i in b:
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==2:
        c+=1
        s=0
    else:
        s=0
print(c)
