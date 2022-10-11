def prime(x):
	if x==1:
		return False
	for i in range(2,x):
		if x%i==0:
			return False
	return True
a=int(input())
b=int(input())
c=a+b
d=c+1
s=0
while True:
	if prime(d)==True:
		s+=d
		break
	else:
		d+=1
print(s-c)
	