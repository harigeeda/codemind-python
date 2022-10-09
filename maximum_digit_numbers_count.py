x=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
	b.append(abs(i))
c=max(b)
f=str(c)
d=len(f)
g=int("1"+((d-1)*'0'))
for j in a:
	if (abs(j))>=g:
		print(j,end=" ")