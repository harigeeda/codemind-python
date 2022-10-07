for i in range(int(input())):
    x=int(input())
    s=[]
    k=[]
    for i in range(1,x+100):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                if i<=x:
                    s.append(i)
                elif i>x:
                    k.append(i)
        else:
            s.append(i)
    length=[]
    s1=s[-1]
    k1=k[0]
    a=x-s1
    b=k1-x
    if a<b:
        length.append(s1)
    elif a>b:
        length.append(k1)
    elif a==b:
        length.append(s1)
        length.append(k1)
    if len(length)==1:
        print(*(length))
    else:
        print(min(length))
        