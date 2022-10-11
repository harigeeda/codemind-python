a=int(input())
b=list(map(int,input().split()))
c=max(b)
s=[]
for i in range(c,0,-1):
	if c%i==0:
		s.append(i)
m=0
for j in s:
	for k in b:
		if k%j==0:
			m+=1
	if m==a:
		print(j)
		break
	else:
		m=0
		