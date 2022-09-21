a=int(input())
b=list(map(int,input().split()))
d=list(set(b))
s=[]
for i in d:
    if (b.count(i))==i:
        s.append(i)
if len(s)==0:
    print("-1")
else:
    n=((sum(s))/len(s))
    print("{:.2f}".format(n))
