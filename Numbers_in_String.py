a=input()
s=[]
b="1234567890"
for i in a:
    if i in b:
        s.append(int(i))
print(sum(s))