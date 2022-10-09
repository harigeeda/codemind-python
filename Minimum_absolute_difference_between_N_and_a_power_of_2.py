a=int(input())
k=[]
l=[]
for i in range(1,a+1):
    b=2**i
    if b<=a:
        k.append(b)
    else:
        l.append(b)
        
k1=k[-1]
l1=l[0]
c=a-k1
d=l1-a
if c<d:
    print(c)
else:
    print(d)