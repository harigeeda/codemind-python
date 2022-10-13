a=list(map(int,input().split(",")))
s=0
k=[]
for i in a:
    for j in range(1,i+1):
        if i%j==0:
            s+=j
    if s in a:
        k.append(i)
        s=0
    else:
        s=0
m=sorted(k)
if len(k)>0:
    print(*(m))
else:
    print("-1")