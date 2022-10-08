a=input()
b=list(map(int,input().split()))
s=0
c=[]
for i in b:
    for j in range(1,i+1):
        if i%j==0:
            s+=1
    if s==2:
        c.append(i)
        s=0
    else:
        s=0
d=(sum(c)/len(c))
print("{:.2f}".format(d))
        