a=int(input())
s=[]
k=[]
l=[]
for i in range(1,a+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            s.append(i)
for j in range(1,a+1):
    if a%j==0:
        k.append(j)
for m in k:
    if m not in s:
        l.append(m)
print(len(l))