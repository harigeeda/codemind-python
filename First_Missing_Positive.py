a=int(input())
b=list(map(int,input().split()))
i=1
while True:
    if i not in b:
        print(i)
        break
    i+=1