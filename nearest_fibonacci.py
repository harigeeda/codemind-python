a=int(input())
b=0
c=1
x=[]
y=[]
for i in range(a):
    if b<=a:
        x.append(b)
    else:
        y.append(b)
    d=b
    b=c
    c=(b+d)
k=x[-1]
l=y[0]
k1=a-k
k2=l-a
if k1<k2:
    print(k)
elif k1>k2:
    print(l)
else:
    print(k,l)