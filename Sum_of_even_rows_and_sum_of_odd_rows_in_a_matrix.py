a,b=map(int,input().split())
e=0
o=0
even=[]
odd=[]
k=[]
for i in range(a):
    k.append(list(map(int,input().split())))
for j in range(a):
    if j%2==0:
        even.append(k[j])
    else:
        odd.append(k[j])
for l in even:
    e+=(sum(l))
for n in odd:
    o+=sum(n)
print(e,o)