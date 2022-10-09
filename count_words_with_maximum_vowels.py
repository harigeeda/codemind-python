a=input()
b="aeiou"
s=[]
for i in (a.split()):
	k=0
	for j in i:
		if j in b:
			k+=1
	s.append(str(k))
	k=0
c=max(s)
d=str(c)
e=s.count(d)
print(e)