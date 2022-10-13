for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=[]
    while len(b)>1:
        k=max(b)
        z=min(b)
        c.append(k)
        c.append(z)
        b.remove(z)
        b.remove(k)
    print(*(c+b))