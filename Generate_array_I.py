a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
e=""
for i in range(0,a,2):
    c.append(b[i])
for j in range(1,a,2):
    d.append(b[j])
for k in range(0,a//2):
    z=str(c[k])
    e+=(z*d[k])
print(" ".join(e))