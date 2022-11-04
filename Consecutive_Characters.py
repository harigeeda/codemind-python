a=input()
b=[]
s=0
d=len(a)
for i in range(d-1):
    if a[i]==a[i+1]:
        s+=1
    else:
        b.append(s)
        s=0
b.append(s)
print(max(b)+1)
    