a=int(input())
b=list(map(int,input().split()))
c=[]
for i in b:
    if i%2==0 and i not in c:
        c.append(i)
print(len(c))