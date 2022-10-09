a=input()
b=list(map(int,input().split()))
k=[]
for i in b:
	m=str(i)
	z=(m[::-1])
	k.append(int(z))
print(*(k))
