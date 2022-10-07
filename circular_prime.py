a=int(input())
b=0
c=0
for i in range(1,a+1):
    if a%i==0:
        b+=1
x=str(a)
d=x[::-1]
e=int(d)
for j in range(1,e+1):
    if e%j==0:
        c+=1
if b==2 and c==2:
    print("circular prime")
elif b==2 and c!=2:
    print("prime but not a circular prime")
else:
    print("not prime")