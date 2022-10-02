a=input()
s=0
for i in a:
    d=a.count(i)
    if d==1:
        s+=0
    else:
        s+=1
print(s==0)