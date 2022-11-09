a,b=map(int,input().split())
sa=0
k=[]
for i in range(a):
    k.append(list(map(int,input().split())))
for l in k:
    for j in l:
        sa+=j
print(sa)