a=int(input())
b=list(map(int,input().split()))
c=int(input())
s=[]
for i in b:
    if i<=c:
        s.append(i)
print(sum(s))