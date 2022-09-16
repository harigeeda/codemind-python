x,y=map(int,input().split())
z=2*y
d=x+z
if x==0:
	if y%2==0 and z%2==0:
		print("YES")
	else:
		print("NO")
else:
	if d%2==0:
		print("YES")
	else:
		print("NO")