a=int(input())
b=list(map(int,input().split()))
s=""
for i in b:
    s+=str(i)
k=str(s)
j=0
for l in k:
    j+=int(l)
print(j)