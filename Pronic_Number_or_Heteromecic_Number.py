a=[]
b=int(input())
for i in range(1,b+1):
    a.append(i*(i+1))
c=str(b)
if b in a:
    print("YES")
else:
    print("NO")