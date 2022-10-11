a=int(input())
b=list(map(int,input().split()))
e=[]
o=[]
k=[]
for i in b:
	if i%2!=0:
		e.append(i)
	else:
		o.append(i)
c=min(len(e),len(o))
for j in range(0,c):
	k.append(e[j])
	k.append(o[j])
z=abs(len(e)-len(o))
if len(e)>len(o):
	k+=(e[-z:])
if len(o)>len(e):
	k+=(o[-z:])
u=0
if len(k)%2==0:
	u=0
else:
	k.append("0")

print(*(k))
	