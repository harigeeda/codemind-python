a=input()
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if len(b)>0:
    print(a.index(b[0]))
else:
    print("-1")