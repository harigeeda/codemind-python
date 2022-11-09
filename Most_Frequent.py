a=int(input())
b=list(map(int,input().split()))
c=set(b)
s=[]
for i in c:
    s.append(b.count(i))
d=max(s)
for j in c:
    if b.count(j)==d:
        print(j)
        break
        