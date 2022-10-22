a=int(input())
b=list(map(int,input().split()))
c=""
d=[]
e=[]
for i in range(0,a,2):
    d.append(b[i])
for j in range(1,a,2):
    e.append(b[j])
z=len(d)
for l in range(0,z):
    c+=str(d[l])*e[l]
for h in c:
    print(h,end=" ")