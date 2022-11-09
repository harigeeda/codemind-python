a=int(input())
b=list(map(int,input().split()))
c=[]
k="123456789"
s=0
for i in b:
    if str(i) in k:
        c.append(i)
    else:
        s+=1
for j in range(s):
    c.append("0")
print(*(c))