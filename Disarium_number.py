a=input()
b=len(a)
s=0
for i in range(0,b):
		s+=(int(a[i]))**(i+1)
t=int(a)
print(s==t)		