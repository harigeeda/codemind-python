a=int(input())
s=list(map(int,input().split()))
m=[]
k=1
for i in range(a):
    for j in range(a):
        if s[j]==(s[i]):
            continue
        else:
            k*=(s[j])
    m.append(k)
    k=1
print(*(m))
    