def set_fun(x):
	k=[]
	for i in x:
		if i not in k:
			k.append(i)
	return((k))
a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=set_fun(c)
f=set_fun(d)
s=[]
for i in e:
	if i not in f:
		s.append(i)
for j in f:
	if j not in e:
		s.append(j)
print(*(s))