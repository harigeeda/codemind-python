s=0
y=0
a=int(input())
b=str(a)
c=len(b)
d=""
for i in range(1,a+1):
    if a%i==0:
        s+=1
for j in range(1,c+1):
    d+=b[-j]
k=int(d)
for g in range(1,k+1):
    if k%g==0:
        y+=1
if a%10==0:
    print("not prime")
elif s<=2 and y<=2:
    print("circular prime")
elif s<=2 and y>2:
    print("prime but not a circular prime")
else:
    print("not prime")