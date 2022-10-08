a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
    if i%10!=0:
        k=int(i)
        c=str(i)
        for j in c:
            d=int(j)
            if k%d==0:
                s+=0
            else:
                s+=1
        if s==0:
            print(k,end=" ")
            s=0
        else:
            s=0