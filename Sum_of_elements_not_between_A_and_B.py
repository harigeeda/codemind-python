a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
k=0
for i in b:
    if i<c or i>d:
        k+=i
print(k)