a=input()
b=[]
d=[]
c=len(a.split())
for i in (a.split()):
    b.append(i)
for j in range(0,c):
    if j%2==0:
        d.append(str(b[j])[::-1])
    else:
        d.append(b[j])
print(*(d))
        
        