a=int(input())
b=list(map(int,input().split()))
c=set(b)
s=0
for i in c:
    k=b.count(i)
    s+=k//2
print(s)
