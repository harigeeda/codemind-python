x=int(input())
s=0
n=1
z=str(x)
a=len(z)
for i in range(0,a):
	s+=int(z[i])
	n*=int(z[i])
if s==n:
	print("Spy Number")
else:
	print("Not Spy Number")