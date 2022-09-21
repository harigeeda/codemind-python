a=int(input())
b=list(map(int,input().split()))
s=[]
k=0
for i in b:
	if i%2!=0:
		s.append(i)
for j in s:
	if (b.index(j))%2!=0:
		k+=0
	else:
		k+=1
print(k==0)