a=int(input())
x=[]
y=[]
for i in range(1,(a*10)):
    k=str(i)
    if str(i)==k[::-1] and i<a:
        x.append(i)
    if str(i)==k[::-1] and i>a:
        y.append(i)
x1=x[-1]
x2=y[0]
k1=a-x1
k2=x2-a
if k1<k2:
    print(x1)
elif k1>k2:
    print(x2)
else:
    print(x1,x2)