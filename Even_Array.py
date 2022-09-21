a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
	if i%2==0:
		s+=0
	else:
		s+=1
print(s==0)