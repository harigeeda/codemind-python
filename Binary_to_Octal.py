for i in range(int(input())):
    x=int(input())
    a=str(x)
    b=len(a)
    y=0
    for i in range(1,b+1):
        y+=(int(a[-i]))*(2**(i-1))
    n=oct(y)
    print(n[2:])