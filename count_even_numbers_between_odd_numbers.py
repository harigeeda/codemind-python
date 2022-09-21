a=int(input())
b=list(map(int,input().split()))
s=0
i=1
while i<(a-1):
	if b[i-1]%2!=0 and b[i+1]%2!=0 and b[i]%2==0:
		s+=1
	i+=1
print(s)