a=int(input())
b=list(map(int,input().split()))
x="1234567890"
c=a/2
d=a//2
k=b[:d]
l=b[d:]
s=0
m=0
for i in k:
	s+=i
for j in l:
	m+=j
print(abs(s-m))