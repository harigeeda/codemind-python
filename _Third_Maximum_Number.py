a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
d=[]
for i in c:
    if i not in d:
        d.append(i)
if len(d)>=3:
    print(d[-3])
else:
    print(max(d))
