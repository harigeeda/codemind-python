a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=[]
for i in b:
    if i>=c and i<=d:
        s.append(i)
print(sum(s))