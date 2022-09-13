s=""
n=int(input())
x=str(n)
a=len(x)
for i in range(1,a+1):
	s+=x[-i]
print(s)