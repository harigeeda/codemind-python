for i in range(int(input())):
    a=input()
    b=len(a)
    if a==a[::-1]:
        if b%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
        