for i in range(int(input())):
    a=input()
    b=len(a)
    s=0
    for i in range(1,b+1):
        s+=int(a[-i])*8**(i-1)
    d=bin(s)
    print(d[2:])