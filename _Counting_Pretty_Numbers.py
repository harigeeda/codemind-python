for i in range(int(input())):
    a,b=map(int,input().split())
    s=0
    for i in range(a,b+1):
        b=str(i)
        if b[-1]=="2" or b[-1]=="3" or b[-1]=="9":
            s+=1
    print(s)