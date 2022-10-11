def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
x=int(input())
k=str(x)
s=0
if prime(x)==True:
    s+=0
else:
    s+=1
for j in k:
    d=int(j)
    if prime(d)==True:
        s+=0
    else:
        s+=1
if s==0:
    print("Mega Prime")
else:
    print("Not Mega Prime")
    