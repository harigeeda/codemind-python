a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    a=str(i)
    if a==a[::-1]:
        s+=1
print(s)