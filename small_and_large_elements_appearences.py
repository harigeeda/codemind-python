a=input()
s=[]
for i in (a.split()):
	for j in i:
		s.append(ord(j))
b=min(s)
c=max(s)
d=chr(b)
e=chr(c)
dc=a.count(d)
ec=a.count(e)
print("{} {} {} {}".format(d,dc,e,ec))