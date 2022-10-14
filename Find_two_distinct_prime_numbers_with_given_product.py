def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=int(input())
k=[]
s=[]
for i in range(1,a+1):
    if prime(i)==True:
        k.append(i)
for j in k:
    for z in k:
        if z>j:
            m=j*z
            if m==a:
                s.append(j)
                s.append(z)
if len(s)>0:
    print(*(s))
else:
    print("-1")