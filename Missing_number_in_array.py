for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    for i in range(1,a+1):
        if i in b:
            continue
        else:
            print(i)
            break