for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range(a-1):
        if b[i+1]>=b[i]:
            c+=0
        else:
            c+=1
    if c==0:
        print("0")
    else:
        print(max(b)-min(b))