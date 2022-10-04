for i in range(int(input())):
    a=input()
    b="1234567890"
    c=0
    for i in a:
        if i not in b:
            c+=1
    print(c==0)