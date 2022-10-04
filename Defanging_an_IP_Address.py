a=input()
b="1234567890"
c="."
s=""
for i in a:
    if i in b:
        s+=str(i)
    else:
        s+=str("[.]")
print(s)
