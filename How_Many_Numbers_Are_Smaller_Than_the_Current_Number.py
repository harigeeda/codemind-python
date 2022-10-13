a=int(input())
b=list(map(int,input().split()))
s=[]
k=0
for i in range(a):
    for j in b:
        if j<b[i]:
            k+=1
    s.append(k)
    k=0
print(*(s))
            
    