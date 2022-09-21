a=int(input())
b=list(map(int,input().split()))
c=" "
for i in range(0,a):
	c+=str(b[i])
print(int(c,2))