a=int(input())
b=a**2
c=str(b)
d=len(c)
s=0
for i in range(0,d):
    s+=int(c[i])
if s==a:
    print("Neon Number")
else:
    print("Not Neon Number")