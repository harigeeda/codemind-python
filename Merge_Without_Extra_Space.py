for i in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=(b+c)
    e=sorted(d)
    k=[]
    for i in e:
        if i not in k:
            k.append(i)
    print(*(k))