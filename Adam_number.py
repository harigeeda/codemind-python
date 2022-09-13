a=""
b=""
d=int(int(input()))
e=str(d)
f=len(e)
g=d*d
h=str(g)
i=len(h)
for j in range(1,f+1):
	a+=e[-j]
for k in range(1,i+1):
	b+=h[-k]
l=int(a)
m=l*l
z=int(b)
if g%10==0:
	print("False")
elif z==m:
	print("True")
else:
	print("False")