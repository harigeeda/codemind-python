a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
b=set(x)
c=set(y)
s=0
for i in b:
	if i not in c:
		s+=1
for j in c:
	if j not in b:
		s+=1
print(s)