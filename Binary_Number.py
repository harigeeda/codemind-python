a=int(input())
b=2**a
for i in range(0,b):
    d=(bin(i)[2:])
    e=len(d)
    x=(a-e)*"0"
    print(x+d)
    