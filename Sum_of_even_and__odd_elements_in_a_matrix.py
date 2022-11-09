a,b=map(int,input().split())
even=0
odd=0
k=[]
for i in range(a):
    k.append(list(map(int,input().split())))
for l in k:
    for z in l:
        if z%2==0:
            even+=z
        else:
            odd+=z
print(even,odd)