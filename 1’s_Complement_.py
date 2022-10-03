a=int(input())
b=(bin(a))
c=b[2:]
d=""
for i in c:
    if i=="1":
        d+=("0")
    else:
        d+=("1")
print(int(d,2))